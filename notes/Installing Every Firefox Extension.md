---
title: "Installing Every* Firefox Extension"
url: https://jack.cab/blog/every-firefox-extension
clipped: 2026-06-17 01:19:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - web browsers
  - browser extensions
  - performance testing
  - dataset scraping
  - malware & phishing
related:
  - "[[Web Browsers]]"
  - "[[Browser Extensions]]"
  - "[[Performance Testing]]"
  - "[[Dataset Scraping]]"
  - "[[Malware & Phishing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The author documents a humorous and chaotic experiment scraping and installing over 84,000 Firefox extensions simultaneously, exploring the limits of browser performance, storage, and memory.
>
> **Key points:**
> - Scrapes the Mozilla Add-ons API to download 84,235 unique extensions, creating a 49 GB dataset published on Hugging Face.
> - Documents browser performance degradation across progressive attempts, highlighting how Firefox struggles to serialize `extensions.json` at scale.
> - Successfully stabilizes the browser running all 84,194 user extensions on a high-spec VM using over 30 GB of RAM.
> - Explores the landscape of AMO add-ons, identifying phishing campaigns, SEO spam, potentially unwanted applications (PUAs), and extreme permission requests.
> - Details humorous outcomes of loading Firefox preferences, which broke page renders, crashed telemetry, and loaded context menus too large to display.
>
> **Concept links:** [[Web Browsers]], [[Browser Extensions]], [[Performance Testing]], [[Dataset Scraping]], [[Malware & Phishing]]
>
> **Suggested connections:**
> - [[Web Browsers]] — the internals of Firefox database serialization (`extensions.json`) and tab management limits.
> - [[Browser Extensions]] — security risks of add-ons, including permissions, homoglyph phishing, and affiliate search hijackers.
> - [[Performance Testing]] — pushing software boundaries to absolute failure points (memory consumption and GUI thread locking).
<!-- ai-summary:end -->

# [Installing Every* Firefox Extension](https://jack.cab/blog/every-firefox-extension)

## Digest Summary
The author scraped the entire Mozilla Add‑ons API to collect every public Firefox extension. Using the `/api/v5/addons/search/` endpoint with various sort parameters (recommended, users, created, updated, downloads) and the `exclude_addons` filter, they fetched all pages in parallel, ultimately obtaining 84 235 unique extensions—about 99.94 % of the ~84 000 listed. The dataset (≈49 GB, avg 585 kB per extension) is hosted on Hugging Face as `all_extensions.json`. Analysis shows the largest extensions range from 115 MB to 196 MB (e.g., dmitlichess, ReactBot Web, AI‑based tools) while the smallest is a 7.5 kB tab‑saver. The lowest‑rated extension (≥10 ratings) is “Tab Stack for Firefox.” The earliest extension is “Web Developer.” The most‑screenshot‑rich add‑on is RDS Bar (54 screenshots). The most prolific developer, “Dr. Bis,” has 84 published extensions. The author identified phishing extensions (homoglyph attacks, clipboard theft) and SEO‑spam extensions with fabricated homepage links, as well as a large group of “Custom Web Search” PUAs linked to Innover Online Group Ltd, collectively accounting for >700 k users.

## Discussion Summary
Comments express strong amusement at the chaotic overload of Firefox extensions, describing the presentation as funny and entertaining. Reviewers note the absurd scale of thousands of extensions causing page failures and highlight a discovered performance bug linked to the extensions.json handling. Some compare the situation to outdated browser toolbar overloads and suggest similar behavior in Chrome. While a few lament the inability to load pages, the predominant tone is light‑hearted appreciation of the writing and the comedic illustration of extension bloat.

---

## Full Article

\*All but 8 we didnât scrape (or got deleted between me checking the website and me scraping) and 42 missing from extensions.json.[1](https://jack.cab/blog/every-firefox-extension#user-content-fn-undownloaded) Technically we only installed 99.94% of the extensions.

It turns out thereâs only [84 thousand](https://addons.mozilla.org/en-US/firefox/search/?type=extension) Firefox extensions.
That sounds [feasibly](https://unnamed.website/posts/installing-every-arch-package/) small. That even sounds like itâs less than 50 gigabytes. Letâs install them all!

Scraping every Firefox extension
--------------------------------

Thereâs a [public API](https://mozilla.github.io/addons-server/topics/api/index.html) for the add-ons store.
No authentication required, and seemingly no rate limits. This should be easy.

The [search endpoint](https://mozilla.github.io/addons-server/topics/api/addons.html#search) can take an empty query. Letâs read every page:

```
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&appversion=150.0"



let res = await fetch(url)



let data = await res.json()



console.log(`PAGE ${page++}: ${data.results.length} EXTENSIONS`)



extensions.push(...data.results)



Bun.write("extensions-default.json", JSON.stringify(extensions))
```

The search API only gives me 600 pages, meaning I can only see 30 thousand extensions, less than half of them.

A solution I found is to use different sorts. The default sort is `sort=recommended,users`: first recommended extensions, then sorted by users, descending. Changing to just `sort=created` gave me some of the long tail:

```
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&appversion=150.0"



"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&appversion=150.0&sort=created"
```

```
Bun.write("extensions-default.json", JSON.stringify(extensions))



Bun.write("extensions-newest.json", JSON.stringify(extensions))
```

```
import extensions_default from "../extensions-default.json"



import extensions_newest from "../extensions-newest.json"



// Yes, somehow I got the same slug twice



for (const ext of extensions_default) {



extensions[ext.slug] = ext



for (const ext of extensions_newest) {



extensions[ext.slug] = ext



console.log(`TOTAL UNIQUE EXTENSIONS: ${Object.keys(extensions).length}`)
```

```
~/Developer/every-addon> bun count



TOTAL UNIQUE EXTENSIONS: 54218
```

Iâm still missing 30,025[2](https://jack.cab/blog/every-firefox-extension#user-content-fn-upd) extensions, so I added `rating` and `hotness` too.

```
~/Developer/every-addon> bun count



TOTAL UNIQUE EXTENSIONS: 67458
```

Thatâs still 16,785[2](https://jack.cab/blog/every-firefox-extension#user-content-fn-upd) missing. Adding `updated`â¦

```
~/Developer/every-addon> bun count



TOTAL UNIQUE EXTENSIONS: 67945
```

Starting to hit diminishing returns. While I was waiting 7 minutes for that last list to get scraped because my code didnât fetch in parallel, I had an epiphany: use `exclude_addons`. I can just fetch page 600 and exclude all its addons to get page 601.

```
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&page=600&type=extension&app=firefox&appversion=150.0&sort=updated"



const page_600 = await fetch(url).then(res => res.json())



const page_601 = await fetch(



`${url}&exclude_addons=${page_600.results.map(ext => ext.id).join(",")}`,



).then(res => res.json())
```

It works! There is a URL length limit, sadly, so I can only fetch an extra 20 pages.

```
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&page=600&type=extension&app=firefox&appversion=150.0&sort=created&exclude_addons="



let res = await fetch(url)



let data = await res.json()



console.log(`PAGE ${page++}: ${data.results.length} EXTENSIONS`)



if (data.results.at(-1).id === extensions.at(-1)?.id) break // IDK



extensions.push(...data.results)



url += data.results.map(ext => ext.id).join(",")



Bun.write("created-2.json", JSON.stringify(extensions))
```

TAke a look, yâall:

```
~/Developer/every-addon> bun count



TOTAL UNIQUE EXTENSIONS: 68035
```

A lot less than I expected, especially considering what happens when I add the `downloads` sort:

```
~/Developer/every-addon> bun count



TOTAL UNIQUE EXTENSIONS: 68901
```

Reading the docs again, I notice I can filter by category as well.
Iâm tired of waiting 7 minutes so Iâll just fetch every page in parallel.

```
function get(url: string, path: string) {



Array.from({ length: 600 }, (_, i) => fetch(`${url}&page=${i + 1}`).then(res => res.json())),



let extensions = pages.flatMap(page => page.results)



Bun.write(path, JSON.stringify(extensions))



const categories = await fetch("https://addons.mozilla.org/api/v5/addons/categories/").then(res =>



.filter(category => category.type === "extension")



`https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&sort=created&category=${category.slug}&appversion=150.0`,



`./newest-${category.slug}.json`,
```

I got basically all the extensions with this, making everything I did before this look really stupid.

```
~/Developer/every-addon> bun analyze



Found 84235 unique extensions



That would be 49.3 GB, an average of 584.9 kB per extension
```

Thatâs 8 less extensions than what it says on the website.
When I ran this in September 2025, it found 21 *more* extensions than what was mentioned on the website, so I think this is enough.

So that nobody has to do this again, Iâve uploaded this dataset to [Hugging Face](https://huggingface.co/datasets/jack5079/extensions).

Alternatively, `addons-server` has CORS enabled, so click this funny button to get
your very own `all_extensions.json`:

Download all\_extensions.json This requires JavaScript!

 

### April 11 update

The search API supports date filters: `created__gte` and `created__lte`.
The API also returns the full number of extensions that match your search.

You can start with a filter that includes all extensions, then keep splitting the ranges in half until it is less than 30 thousand, then
fetch all of them.

Iâve updated the downloader: it is faster, wastes fewer requests, and seems to scrape exactly all the extensions, too.

This wonât work if over 30 thousand extensions get created in a single second, which I canât imagine will ever happen.

Analyzing every Firefox extension
---------------------------------

I have a copy of Bun and `all_extensions.json`, so I will torment you with my unmatched script power.

### Biggest extensions

The biggest Firefox extension is [dmitlichess](https://addons.mozilla.org/en-US/firefox/addon/dmitlichess/) at 196.3â¯MB, which contains 2000+ audio files.

Hereâs the rest of the top ten:

* [(Unoffical) ReactBot Web](https://addons.mozilla.org/en-US/firefox/addon/unoffical-reactbot-web/), 184.9â¯MB: I thought this was a direct port of jacksfilms ReactBot, but no, itâs just a bunch of .webms.
* [Ericâs Thumbnail Seasoning!](https://addons.mozilla.org/en-US/firefox/addon/eric-s-thumbnail-seasoning/), 146.6â¯MB: Someoneâs personal fork of YouTube MrBeastify. Contains 900 .pngs.
* [Animal Forest:PG BGM](https://addons.mozilla.org/en-US/firefox/addon/animal-forest-pg-bgm/), 137.4â¯MB: Evil version of <https://tane.us/ac>.
* [YouTube OCR](https://addons.mozilla.org/en-US/firefox/addon/youtube-ocr/), 128.3â¯MB: [Tesseract.js](https://tesseract.projectnaptha.com/).
* [Image to Text for ChatGPT](https://addons.mozilla.org/en-US/firefox/addon/image-to-text-chatgpt/), 128.3â¯MB: Also [Tesseract.js](https://tesseract.projectnaptha.com/).
* [qwip AI Detection BETA](https://addons.mozilla.org/en-US/firefox/addon/qwip-ai-detection-beta/), 126.0â¯MB: AI models (not Tesseract.js).
* [Kumo Study](https://addons.mozilla.org/en-US/firefox/addon/kumo-study/), 117.0â¯MB: 50 royalty free lo-fi study beats.
* [YouTube Jakkify](https://addons.mozilla.org/en-US/firefox/addon/youtube-jakkify/), 114.0â¯MB: Another YouTube MrBeastify fork. 500 soyjaks.
* [True Paper](https://addons.mozilla.org/en-US/firefox/addon/true-paper/), 111.6â¯MB: Also AI models that arenât Tesseract.js.

The first time I ran this analysis, in September, â[Cute doggy - Dog puppies](https://addons.mozilla.org/en-US/firefox/addon/cute-doggy-dog-puppies/)â was the 10th largest extension. Iâm still mentioning it here, because I was so fucking confused:

![Cute doggy - Dog puppies by cutypal dotcom: Cute AI dog wallpapers with live clock & messages. Click âTalk with Meâ to chat and enjoy cozy dog vibes anytime!](https://jack.cab/_astro/dog.4zlazN5-_Z2tyfVx.webp)

The smallest extension is [theTabs-saver](https://addons.mozilla.org/en-US/firefox/addon/thetabs-saver/), which is 7518 bytes and has no code.

### Worst extension

Subjectively itâs Cute doggy - Dog puppies, but objectively:

```
import extensions from "../all_extensions.json"



.filter(ext => ext.ratings.count > 10)



.sort((a, b) => a.ratings.bayesian_average - b.ratings.bayesian_average)[0],
```

itâs [Tab Stack for Firefox](https://addons.mozilla.org/en-US/firefox/addon/tab-stack-for-firefox/), by lolicon (?!?!?!?!?!).

### First extension

[Web Developer](https://addons.mozilla.org/en-US/firefox/addon/web-developer/).

### Most screenshots

[RDS Bar](https://addons.mozilla.org/en-US/firefox/addon/rds-bar/) has 54.

[FalscheLaden](https://addons.mozilla.org/en-US/firefox/addon/falscheladen/), with no users, requests 3,695 permissions.
The author has posted [a writeup](https://www.arnevogel.com/firefox-permissions/).

Second place is [Google Dark Theme](https://addons.mozilla.org/en-US/firefox/addon/dark-theme-for-google-searches/), which requests 2,675 permissions but has 1,687 users.

### Most prolific developer

```
import extensions from "../all_extensions.json"



extensions.flatMap(e => e.authors),



).sort((a, b) => b.length - a.length)[0][0],
```

[Dr. B](https://addons.mozilla.org/en-US/firefox/user/18672722/) is the king of slop, with 84 extensions published, all of them vibe coded.

How do I know? Most of their extensions have a README.md in them describing their process of getting these through addon review, and mention Grok 3.
Also, not a single one of them have icons or screenshots.

Personally, Iâm shocked this number is this low. I expected to see some developers with hundreds!

### Phishing

I reviewed the source of a couple homoglyph attacks on crypto wallets discovered in the dataset
and was disappointed to find out they just pop up a form asking for your seed phrase and send it off to their server.
Itâs an extension!!! You can steal their `coinbase.com` token! You can monitor the clipboard and swap out their address for yours!
You can [crash their browser and claim your real malware is the fix](https://www.microsoft.com/en-us/security/blog/2026/02/05/clickfix-variant-crashfix-deploying-python-rat-trojan/)!

Why would you make a fake MetaMask extension and bot 1-star reviews?

![A phishing extension has 1,672 1-star reviews, which all use the same template](https://jack.cab/_astro/1-star.CXwdwkkq_14u9G1.webp)

Is this the doing of their cybercrime competitors, who bot 4-star reviews on extensions of their own?

![A phishing extension has two 5-star reviews, 1,113 4-star reviews and a single 3-star review](https://jack.cab/_astro/4-stars.BDHbjOWR_20DAWY.webp)

Either way, these extensions are clearly phishing. I reported some to Mozilla, and the next day they were all gone, even the ones I was too lazy to report. I forgot to archive them, so I guess they live on in Mayâs VM!

In terms of implementation, the most interesting one is âÐron WÐ°llÐµtâ (the I, a, and e are Cyrillic).
Three seconds after install, it fetches the phishing pageâs URL from the first record of a NocoDB spreadsheet and opens it:

```
chrome.runtime.onInstalled.addListener(async () => {



await new Promise(e => setTimeout(e, 3e3))



let e = await (0, r.fetchUrlFromNocoRest)()



? await chrome.tabs.create({



: console.warn("No valid URL from NocoDB.")



console.error("Install flow failed:", e)
```

I think the extensionâs âno accounts or remote codeâ description is really funny, like putting âno copyright infringement intendedâ in your videoâs description in case YouTube is watching.
The API key had write access, so I wiped the spreadsheet.

### SEO spam

You get a âHomepageâ link in your extensionâs page and your own page.
[Itâs been `nofollow` for two years](https://github.com/mozilla/addons/issues/14753),
but that hasnât stopped grifters from trying anyway.

On [Attempt 1](https://jack.cab/blog/every-firefox-extension#attempt-1-1000), I encountered [Typo Sniper](https://addons.mozilla.org/en-US/firefox/addon/typo-sniper/) and [Tab Fortune Teller](https://addons.mozilla.org/en-US/firefox/addon/tab-fortune-teller-kk/),
AI generated extensions with casinos in their authorâs Homepage links.

In the dataset, thereâs [many âCode Injectorâ extensions](https://addons.mozilla.org/en-US/firefox/search/?q=code%20injector), which are all virtually identical
and also have random websites in their authorâs Homepage link.

All of these extensions are from 2025. Is an ancient SEO guide circulating?
Is there some evil AMO frontend theyâre still getting a backlink from?
I have no idea whatâs happening here.

### PUAs

Do you notice a pattern?

* [Maps Assist & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/mapsassistcustomwebsearch): 138,082 users
* [Package Tracking Tab & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/packagetrackingtabcustomsearch): 83,506 users
* [Converter Suite & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/convertersuitecustomwebsearch): 82,502 users
* [Manuals Explorer & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/manualsexplorercustomwebsearch): 66,835 users
* [Ezy Photo Tab & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/ezyphototabcustomwebsearch): 54,347 users
* [Easy Games Tab & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/easygamestabcustomwebsearch): 34,918 users
* [Task Manager Tab & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/task-manager-custom-web-search): 34,585 users
* [Turbo Converter & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/turboconverter-customwebsearch): 32,236 users
* [Quick Live News & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/quicklivenewscustomwebsearch): 31,542 users
* [Ezy Speed Test & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/ezy-speed-test-customwebsearch): 30,853 users
* [Quick Recipe Hub & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/quickrecipehubcustomwebsearch): 29,556 users
* [Flight Tab Pro & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/flighttabprocustomwebsearch): 28,633 users
* [Weather Authority & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/weatherauthoritycustomsearch): 13,658 users
* [Video Converter World & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/videoconvertercustomweb-search): 13,191 users
* [Daily Top Coupons & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/dailytopcouponscustomwebsearch): 9,385 users
* [Password Generator Pro & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/passwordgeneratorcustomsearch): 5,289 users
* [Calculator Whiz & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/calculatorwhizcustomweb-search): 4,563 users
* [Calendar Planner & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/calendarplannercustomwebsearch): 4,223 users
* [Ezy Alarm Clock & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/ezy-alarmclock-customwebsearch): 4,051 users
* [Zip-Unzip Files & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/zipunzipfiles-customweb-search): 3,298 users
* [Latest Wallpapers & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/latest-wallpaperscustomsearch): 2,648 users
* [Ezy Screenshot & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/ezyscreenshotcustom-web-search): 2,231 users
* [Precious Bible & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/preciousbiblecustomwebsearch): 1,946 users
* [Grammar Wise & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/grammar-wise-custom-web-search): 1,115 users
* [Stream Live Radio & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/streamliveradiocustomwebsearch): 725 users
* [Astrology Craft & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/astrologycraftcustomweb-search): 185 users
* [AI Chat Pro & Custom Web Search](https://addons.mozilla.org/en-US/firefox/addon/ai-chat-pro-custom-web-search): 1 poor user

Over 700 thousand users in total.

All of these extensions are their authorâs only uploads and they have their own domains. Most of them are on both Chrome and Firefox, their websites look the same, and they all have a terms of service referencing âInnover Online Group Ltdâ, which is a .png for some reason.

Because I scraped every Firefox extension twice, I can see what got removed in between the runs.
Three of Innover Groupâs extensionsâEarth View 360Â°, View Manuals, and View Recipes, totaling 115 thousand usersâhave been disabled by Mozilla.

Innover Group runs [Google ads](https://adstransparency.google.com/advertiser/AR09906877289868558337) for their extensions, a lot of them [simply saying âContinueâ](https://adstransparency.google.com/advertiser/AR09906877289868558337/creative/CR18374283903797035009).

The âCustom Web Searchâ is Yahoo but with their affiliate code.
That code being `safeplexsearch`, which has a website of its own which of course mentions Innover Online Group Ltd, and links to [an addon](https://addons.mozilla.org/en-US/firefox/addon/safeplex-search/) with 3,892 users, which is actually a Firefox exclusive.
Actually, âCustom Web Searchâ is a Firefox exclusive on all of these extensions. Why did they even make a Chrome version, to sell them to the NSA??

One user claimed Ezy Speed Test â[disables Ublock [sic] Origin once installed](https://addons.mozilla.org/en-US/firefox/addon/ezy-speed-test-customwebsearch/reviews/1986723/)â, which I did not find in its code.

Thereâs a million companies like this, though.
I just went to Download.com with my ad-blocker off and discovered the company Atom Apps in an ad,
which *also* uploads extensions for both Chrome and Firefox,
with a new account for each extension,
only includes Yahoo in the Firefox version,
with names that end in either âand Searchâ or â& Searchâ,
and has their company name as a .png in their terms of service.
They have 220 thousand daily users total across 12 extensions, and none of theirs have been disabled.

### Some percentages

* 34.3% of extensions have no daily users
  + 25.1% of extensions have more than 10 daily users
  + 10.6% of extensions have more than 100 daily users
  + 3.2% of extensions have more than 1000 daily users
  + 0.7% of extensions have more than 10000 daily users
* 76.7% of extensions are open source (SPDX license that isnât All Rights Reserved)
* 23% of extensions were created after I started writing this article
  + 19% of extensions have no users, no reviews, no screenshots, no downloads, and no icon
* 2.4% of extensions require payment
  + 38.1% of those are open source???

Installing every Firefox extension
----------------------------------

Obviously Iâm not going to [open each of these in a new tab](https://jack.cab/blog/every-firefox-extension) and [go through those prompts](https://jack.cab/blog/every-firefox-extension). Not for lack of trying:

![The "select add-on to install" dialog is Not Responding as I try to select all](https://jack.cab/_astro/xpi-select.Doz-Ecll_Zak7FD.webp)

Each extension has the `current_version.file.url` property which is a direct download for the extension.
I download them to my profileâs extensions folder with the `guid` property as the base name and the .xpi file extension, because [anything else will not be installed](https://support.mozilla.org/en-US/kb/deploying-firefox-with-extensions#w_step-2-add-extensions).

Then, I delete the `addonStartup.json.lz4` and `extensions.json` files.
When I reopen Firefox, each extension is disabled. Tampering with `extensions.json` is common enough that you can ask any chatbot to do it for you:

```
const fs = require("fs") // WHY IS THIS COMMONJS



const path = require("path")



// Path to extensions.json (adjust this to your Firefox profile directory)



// WHY IS THIS IN CAMELCASE



const extensionsJsonPath =



"/Users/user/Library/Application Support/Firefox/Profiles/1avegyqd.default-release/extensions.json"



// Read the extensions.json file



const data = fs.readFileSync(extensionsJsonPath, "utf-8") // WHY IS THIS NOT NODE:FS/PROMISES



const extensionsData = JSON.parse(data)



if (Array.isArray(extensionsData.addons)) {



extensionsData.addons.forEach(addon => {



addon.userDisabled = false



// WHY IS THIS NOT A GUARD



console.error("Unexpected format: addons property is missing or not an array.")



// Write the updated data back to extensions.json



fs.writeFileSync(extensionsJsonPath, JSON.stringify(extensionsData, null, 2))



console.log("All extensions enabled successfully!")



console.error("Error processing extensions.json:", error)
```

### Attempt 0: 65,335

My first attempt was in a [tiny11 core](https://github.com/ntdevlabs/tiny11builder) VM on my desktop.

At first, instead of downloading all of them with a script, I tried using enterprise policies, but this copies all the extensions into the folder.
I quickly ran out of memory, and the pagefile took up the rest of the storage allocated to the VM.
I had also expected Firefox to open immediately and the extensions to install themselves as the browser is being used, but that also did not happen: it just froze.

![Firefox skeleton UI inside a VM](https://jack.cab/_astro/frozen.CllhqcKu_2wCdlq.webp)

### Attempt 1: ~1,000

After that, I tried downloading them myself.

```
import extensions from "./all_extensions.json"



import { exists } from "node:fs/promises"



let count = extensions.length



const PATH_TO_EXTENSIONS_FOLDER =



"C:\\Users\\user\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\mkrso47f.default-release\\"



extensions.map(async ext => {



if (await exists(PATH_TO_EXTENSIONS_FOLDER + ext.guid + ".xpi")) {



console.log("Downloading", ext.current_version.file.url)



const file = await fetch(ext.current_version.file.url)



await Bun.write(PATH_TO_EXTENSIONS_FOLDER + ext.guid + ".xpi", file)



console.log("Downloaded", ext.slug, `${(++progress / count) * 100}% done`)
```

![File explorer with the extensions folder open in the foreground, and the download script open in the background. All visible extensions were last modified on 9/27/2025 at 1:12 AM.](https://jack.cab/_astro/attempt-1-downloading.ChmLisZs_138GAG.webp)

To make sure I was installing extensions correctly, I moved the extensions folder elsewhere and then moved about a thousand extensions back in. It worked.

![Jack.cab open on Attempt 1. The color scheme is strange, all text is "Se ni vaÅ¾n", there's a low resolution Goku background, and there's a sticky note](https://jack.cab/_astro/jackcab.DsjudTCQ_ZE9kwx.webp)

There were multiple extensions that changed all text to a certain string. [bruh-ifier](https://addons.mozilla.org/en-US/firefox/addon/bruh-ifier) lost to [Se ni vaÅ¾n](https://addons.mozilla.org/en-US/firefox/addon/se-ni-va%C5%BEn/).
Goku is in the background.

My context menu is so long that [Iâm showing it sideways](https://unsung.aresluna.org/so-long-im-showing-it-sideways/):

![Context menu bloated with a lot of extensions](https://jack.cab/_astro/context-menu.D0MVKa2F_nDT8a.webp)

I had installed lots of protection extensions. One [blocks traffic to .zip and .mov domains](https://addons.mozilla.org/en-US/firefox/addon/zip-and-mov-domain-blocker/), presumably because they are file extensions.
This is [.cab](https://en.wikipedia.org/wiki/Cabinet_(file_format)) erasure!
Then, I realized that there were likely multiple people viewing my browsing history, so I went to send them a message.

![Scam warning popups from both "Anti-Phishing Alert" and Fraudulent Detector on a DuckDuckGo search for "IF YOU SEE THIS MESSAGE CONTACT ME JACK.CAB"](https://jack.cab/_astro/scam-warning.qijFx36f_Z1TvIkI.webp)

That ââ ï¸ SCAM WARNING!â popup is from [Anti-Phishing Alert](https://addons.mozilla.org/en-US/firefox/addon/anti-phishing-alert). As you may have inferred, it seems to only exist for its Homepage link. How does it work?

```
function isPhishingURL(url) {



const suspiciousPatterns = [



/[a-z0-9\-]{1,}\.com\.xyz/i,



/https?:\/\/(?!www\.)[a-z0-9\-]+\.([a-z]{2,}){2,}/i,



return suspiciousPatterns.some(pattern => pattern.test(url))
```

[Vasavi Fraudulent Detector](https://addons.mozilla.org/en-US/firefox/addon/vasavi-fraudulent-detector/) also has a popup for when a site is safe:

```
title: "Vasavi Fraudulent Detector",



content: "Safe Webpage !!",



icon: $.sweetModal.ICON_SUCCESS,
```

### Attempt 2: 65,335

Only the addons from Attempt 1 were actually loaded, because I didnât know I needed to delete `addonStartup.json.lz4` yet.
I scrolled through the addons page, then I opened DevTools to verify it was the full 65,335, at which point Firefox froze and I was unable to reopen it.

[![](https://video.bsky.app/watch/did:plc:rl7veq6ixcxbvxskltypdcpa/bafkreiesifnzyjbkonnfjrryrks6g4b6iowvttggsl7q4zldhrxuvhsq6u/thumbnail.jpg)](https://pds.synth.download/xrpc/com.atproto.sync.getBlob?did=did:plc:rl7veq6ixcxbvxskltypdcpa&cid=bafkreiesifnzyjbkonnfjrryrks6g4b6iowvttggsl7q4zldhrxuvhsq6u)

### Attempt 3: 65,335 (Mac edition)

After that, [I made a new (non-admin) user on my Mac](https://bsky.app/profile/jack.cab/post/3lztchhxdss25) to
try again on a more powerful device.

Every time I glanced at my script downloading extensions one at a time for six hours, I kept recognizing names.
Oops, Iâm the AMO subject-matter expert now!
Parallelizing was making it *slower* by the last 4000 extensions, which didnât happen on my Windows VM.

When that finished, I found out my hardware couldnât run 65,335 extensions at once, sadly.
The window [does open](https://bsky.app/profile/jack.cab/post/3lzubyinjv22x) after some time I didnât measure, but the window [never starts responding](https://bsky.app/profile/jack.cab/post/3lzuerhj3gk2c).
I donât have the balls to run my laptop overnight.[3](https://jack.cab/blog/every-firefox-extension#user-content-fn-foreshadowing)

Firefox *did* make [over 400â¯GB of disk writes](https://bsky.app/profile/jack.cab/post/3lztusyism22z).
Because I forgot swap existed, I checked the profile trying to find the culprit, which is when I learned I needed to delete `addonStartup.json.lz4` and modify `extensions.json`.
The `extensions.json` was 144â¯MB. For comparison, my PCâs `extensions.json` is 336â¯KB.

[](/_astro/none.BkkHVogm.mov)

### Attempts 4-10: 1000-6000

My solution: add 1000 extensions at a time until Firefox took too long to open. I got to 6000.

3000 extensions was the last point where I was at least able to load webpages.

![Hacker News but most of the page is just gray where Hacker News itself is really small and to the left and its links have a dark bg with bright text. There is also an auth popup from "w7.mul.ir".](https://jack.cab/_astro/hn.B_pMG-c9_Z1kTULE.webp)

After 4000 or more extensions, the experience is basically identical. Hereâs a video of mine (**epilepsy warning**):

[![](https://video.bsky.app/watch/did:plc:rl7veq6ixcxbvxskltypdcpa/bafkreicjmxzcsatofua2k6rcpsjlg6wq3ch2o6mvylv3vkpebdjkbs3xmy/thumbnail.jpg)](https://pds.synth.download/xrpc/com.atproto.sync.getBlob?did=did:plc:rl7veq6ixcxbvxskltypdcpa&cid=bafkreicjmxzcsatofua2k6rcpsjlg6wq3ch2o6mvylv3vkpebdjkbs3xmy)

5000 was the same as 4000 but every website was blocked by some extension I know starts with an S and ends with Blocker and has a logo with CJK characters.
At 6000 extensions, the only page that I could load was `about:addons`.

### Attempt 11: 84,194 (six months later)

My desktop has 16â¯GB of RAM, and my laptop has 24â¯GB of unified memory.
You might notice that 49.3â¯GB is more than twice that.

I asked a friend to help.

What youâre about to see was recorded in [Mayâs](https://split.pet) virtual machine.
Do not try this on your main profile.

#### Downloading

My download script started in parallel, then we switched it to serial when it slowed down.
In total, downloading took about 1 hour and 43 minutes.

I was on a call the entire time, and we spotted a lot of strange extensions in the logs.
What kind of chud would use â[KiwiFarms Math Renderer](https://addons.mozilla.org/en-US/firefox/addon/kiwifarms-math-renderer/)â?
Are they drafting the theory of soytivity?

Turning on Mullvad VPN and routing to Tel Aviv appeared to [speed up the process](https://x.com/itsauroraeeeee/status/2031389838251852019).
This was not because of Big Yahu, but because May restarted the script, so she repeated that a couple times.
Whether thatâs a Bun bug, I donât know and I donât care.
May joked about a âversion 2â that I dread thinking about.

Defender marked one extension, [HackTools](https://addons.mozilla.org/en-US/firefox/addon/hacktools/), as malware.
May excluded the folder after that, so it may not be the only one.

![Defender triggered: HackTools is marked as Trojan:Win32/Vigorf.A.](https://jack.cab/_astro/defender.CCfUhElO_Z18rvT5.webp)

#### Launch 1

Firefox took its sweet time remaking extensions.json, and it kept climbing.
About 39 minutes of Firefox displaying a skeleton (hence â[it has yet to render a second frame](https://bsky.app/profile/jack.cab/post/3misgrravfs2q)â) later, it was 189â¯MB large: a new record! May killed Firefox and ran `enable.js`.

![Firefox skeleton. Only 10 GiB of memory is being used.](https://jack.cab/_astro/first-frame.Be4JSnGL_Z1eob2g.webp)

I did some research to find why this took so long.
[13 years ago, extensions.json used to be extensions.sqlite](https://bugzilla.mozilla.org/show_bug.cgi?id=853388).
Nowadays, extensions.json [is](https://searchfox.org/firefox-main/source/toolkit/mozapps/extensions/internal/XPIDatabase.sys.mjs) serialized and rewritten in full on every write debounced to 20 ms, which works fine for 15 extensions but not 84,194.

#### Launch 2

Finally, we see the browser.
The onboarding tabs trickled in, never loading.

![Firefox with "Emoji Sidebar Keyboard" open in a sidebar. The sidebar and toolbar are covered in extensions.](https://jack.cab/_astro/launch.fuIAiunJ_Z1EvHhB.webp)

3 minutes later, Firefox crashed.

#### Launch 3

May reopened it, took a shower, and came back to this:

![Firefox open, 24 minutes elapsed on a stopwatch, and "Ariba Automator" open in a sidebar](https://jack.cab/_astro/relaunch.BaYmJpna_2oOHc8.webp)

**IT STABILIZED**. YOU CAN (barely) RUN FIREFOX WITH ALL 84 THOUSAND EXTENSIONS.

![Firefox is not responding and using 32,335 MiB of memory](https://jack.cab/_astro/not-responding.CNXpo3t1_Z1gpui2.webp)

Well, we were pretty sure it had 84 thousand extensions.
It had [Tab Counter](https://addons.mozilla.org/en-US/firefox/addon/tab-counter-webext), at least, and the scrollbar in the extensions panel was absolutely massive.

Using every Firefox extension
-----------------------------

It works.

![Quite underwhelming search dropdown](https://jack.cab/_astro/search-dropdown.LVYlJNau_ZvJ8Oe.webp)

### about:addons

#### Addon page

She loaded the configure pages of two extensions. The options iframe never loaded.

![Firefox open to the options page for "The ABC of Faith"](https://jack.cab/_astro/configure-addon-2.0PDOi0qc_ZNC98B.webp)

#### Index page

I realized we need to disable auto update before Firefox sends another 84 thousand requests. This one took a while to load.

The list loaded but with no icons and stopped responding, and **6 hours later** it had loaded fully.

![Firefox using 31329 MiB of memory as about:addons is displayed. There's a shit ton of extensions, example.com and example.org are open in the background still loading, and Tab Counter has a badge of "wait"](https://jack.cab/_astro/aboutaddons.BwnHDmc1_14U25n.webp)

We recorded the entire process; the memory usage fluctuated between 27 and 37 GiB the entire time.

We did have basically every extension, including Mayâs own [mt-rpc](https://addons.mozilla.org/en-US/firefox/addon/5a60cdd881144ce48844/).

![mt-rpc: Discord RPC for Monkeytype](https://jack.cab/_astro/mt-rpc.Dyzdk25i_Z2csvP2.webp)

I *still* have no idea why `about:addons` took 6 hours to load.

I tested my first theory, the extension icons not [loading lazily](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/loading)âironically, sending another 84 thousand requestsâwith
a [one-line patch to Firefox](https://github.com/mozilla-firefox/firefox/blob/190ff4d6d43141ada74f505e77428def2a6748f6/toolkit/mozapps/extensions/content/aboutaddons.html#L381) and installed 3 thousand (disabled) extensions on my Mac.
To compile Firefox, I had to delete the extensions from Attempt 3 to free up storage.

![Moving 63,357 items to Trash](https://jack.cab/_astro/trash.J-vd-I0V_aYRhM.webp)

I donât think it reduced the amount of time Firefox was frozen for.
To be fair, I tested with 28 times less extensions than Attempt 11, so perhaps the issue only manifests at that scale.

### about:support

Wow, thatâs a lot of extensions. You canât be sure, though.

I asked May to open DevTools and check `$$("#addons-tbody tr").length` so we could be sure what we thought was 84,205 extensions were running.

![There are 84204 addons listed on about:support](https://jack.cab/_astro/support.Bwtw6AEg_Z1GIn7o.webp)

Reading `about:support` closer, I realized my fear was correct, but not for the reason I expected: that 84,205 included the built-in addons like Web Compatibility Interventions.
Excluding those, it was a total of 84,194 extensions we had installed.

Previously, I had written that DevTools had loaded no extensions because it was an `about:` page, but I just installed webhint and went to `about:support` and sure enough itâs there, so I donât know what caused that.

### about:preferences

We wanted to see how many New Tab options we can choose from.

![Preferences page. Homepage is set to "Visual Bookmark Tree manifest". The New Tab dropdown is enormous, and is currently set to "New New Tab Page".](https://jack.cab/_astro/preferences.Btbm0aAJ_Z25QYMT.webp)

We turned on crash reporting on the way.

### New Tab

Which extension wins? The answer is none of them.
The New Tab page never loaded, no matter which extension we selected for it, except for Firefox Home which opened instantly.

### moz-extension

A page from the [buyPal](https://addons.mozilla.org/en-US/firefox/addon/buypal/) (1 user) extension opened without action on our end and replaced the other tabs open at the time. It loaded: the only non-`about:` page to do so.

![](https://jack.cab/_astro/buypal.CspufbnP_1dbEAK.webp)

Then Firefox crashed again.

### example.com

This is the first page where content scripts can run.

Like in Attempt 9, there had to have been multiple extensions that block every website.
They didnât matter, though, because we kept the tab open for **24 hours** and it never loaded.

### about:telemetry

It loaded, then she clicked on Environment Data and the browser crashed.

![Crash report being sent with the description "i just tried to look at telemetry after customizing my computer and it just crashed out of nowhere"](https://jack.cab/_astro/crash-report.DaeFkuuS_Z20V4Tz.webp)

Is this usable?
---------------

No.

Further potential explorations
------------------------------

* Find out why `about:addons` took 6 hours to load and why `example.com` never loaded.
* Firefox isnât the only browser that supports `.xpi`s: so do [Kagi Orion](https://kagi.com/orion/) and [GNOME Web](https://apps.gnome.org/en/Epiphany/), both WebKit. Orion doesnât have bulk install, so I didnât try it, and Web is [slow enough with 0 extensions](https://bsky.app/profile/jack.cab/post/3lu2cx7ox222m).
* We intentionally installed every *extension*, not every addon. Itâs pretty obvious what happens when you install a lot of themes, thereâs 500 thousand of them, and they are bigger than extensions on average.
* Install every user script and user style? There isnât really a central database for these.
* Install every Chrome extension? No, just kidding, thereâs too many to do that, and no easy way to scrape them all.