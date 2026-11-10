---

title: "The Showa Hundred Year Problem"
url: https://www.dampfkraft.com/showa-100.html
clipped: 2026-06-17 02:03:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - legacy systems
  - date format overflow
  - japanese calendar
  - software engineering history
  - y2k bug
related:
  - "[[Legacy Systems]]"
  - "[[Date Format Overflow]]"
  - "[[Japanese Calendar]]"
  - "[[Software Engineering History]]"
  - "[[Y2K Bug]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article discusses the 'Showa Hundred Year Problem,' a Japanese calendar-equivalent of Y2K that ended up passing without major computer system failures in 2025.
>
> **Key points:**
> - The Japanese imperial year system (Wareki) is widely used in official, legal, and medical documents alongside the Gregorian calendar.
> - The Showa era (1926-1989) spanned 62 years, overlapping with the early history of computing when years were frequently stored as two digits.
> - Legacy software patched to convert Showa years to Heisei could trigger overflows when Showa reached year 100 in 2025.
> - No major system crashes were reported because legacy systems had been retired, but a subtle off-by-one error (eras start at year 1) could shift potential issues to 2026.
>
> **Concept links:** [[Legacy Systems]], [[Date Format Overflow]], [[Japanese Calendar]], [[Software Engineering History]], [[Y2K Bug]]
>
> **Suggested connections:**
> - [[Legacy Systems]] — on the longevity and retirement of early computing architectures.
> - [[Software Engineering History]] — on early design trade-offs such as storing dates in two digits.
> - [[Japanese Calendar]] — how imperial era transitions are represented in date systems.
<!-- ai-summary:end -->

# [The Showa Hundred Year Problem](https://www.dampfkraft.com/showa-100.html)

## Digest Summary
The article explains Japan’s “Showa Hundred Year Problem,” a potential Y2K‑type overflow arising from the long Showa era (1926‑1989). Japanese dates can be expressed in imperial years, which are still used in legal, fiscal, medical, and other records. Because Showa lasted 62 years—the longest era—early computer systems that stored only two‑digit imperial years could misinterpret dates once the internal value wrapped from “99” to “00”. A hypothetical patch might have added a conditional offset to convert Showa‑based values to Heisei, but the underlying two‑digit storage would still overflow, causing dates after 2025 to be interpreted as 1925‑type values. The article notes that no major failures were reported in 2025, likely because legacy systems had been retired. It also highlights a subtle off‑by‑one issue: imperial eras start at year 1, not 0, so a system that treats the first year as zero would encounter overflow at Showa 101 (2026) rather than Showa 100.

## Discussion Summary
The comment draws a parallel between Japan’s continued use of the imperial year system and the United States’ persistence with imperial measurement units, suggesting neither is likely to shift soon. It notes that era changes create overlapping year designations, such as 1989 being both Showa 64 and Heisei 1, and compares this to the dual labeling of school years (e.g., 2023‑2024 and 2024‑2025). The broader observation is that many cultures employ timelines that do not align with the Gregorian New Year, a widespread and enduring practice.

---

## Full Article

There are many notable hundredth anniversaries in 2025. This year marks the origin of [Hey Song](https://www.heysong.com.tw/), Taiwan's singular sarsaparilla; [Kewpie Mayonnaise](https://www.kewpie.co.jp/mayonnaise/100th/), known for its tang and naked dolls; [Bontan Ame](https://www.seikafoods.jp/100year/), a railway kiosk staple with gentle pomelo flavor; and even the [naming of the Miura Daikon](https://jimoto-ryohin.com/miura/article/2fmua7mlyx9g/), which is [much too big to be called a mere vegetable](https://knowyourmeme.com/memes/it-was-too-big-to-be-called-a-sword-guts-copypasta). But one particular event turned out to be happily unremarkable. 2025 was the hundredth year of the Showa imperial era, and, thankfully, at one minute past midnight on January 1, 2025, nothing happened.

[![](https://www.dampfkraft.com/by-id/7ffc3f3a/img/anniversary-items.l.jpg)](https://www.dampfkraft.com/by-id/7ffc3f3a/anniversary-items.jpg)

Some things celebrating their hundredth anniversary in 2025.

The Showa era actually ended in 1989 with the emperor's death and was no longer used for dates, but the unusual length of the period and its overlap with the rise of personal computing meant that the hundredth anniversary was long feared as a peculiarly Japanese version of the [Y2K problem](https://en.wikipedia.org/wiki/Year_2000_problem). In practice the date change appears to have passed without issue, but before the number goes up one more let's take a look about what all the fuss was about.

First, a quick refresh on the Japanese imperial year system. Briefly, besides the Gregorian calendar year, every year belongs to an imperial era. So 2025 is also the 7th year of the Reiwa Era, typically simply referred to as Reiwa 7. While daily life in Japan usually uses Gregorian calendar years, imperial eras are not merely symbolic, and imperial year numbering is widely used in laws, taxes, finance, religion, and medical records, to give just a few examples.

Until the Meiji era began in 1868, imperial eras changed mostly arbitrarily and frequently, with average length around five years, with [the shortest era](https://ja.wikipedia.org/wiki/%E6%9A%A6%E4%BB%81) lasting less than three months. Following the introduction of constitutional government the imperial era was tied to the reigning emperor, and simply begins as he takes the throne and ends when he dies or (in the most recent case) retires. Additionally, years increment with Gregorian calendar years, so they don't all last 365 days. (This also means that, when an era changes, the Gregorian year will have two imperial year designations, for example 1989 is both Showa 64 and Heisei 1, depending whether the day of the year is before or after the imperial transition.) In the modern period Japan has had five eras - Meiji, Taisho, Showa, Heisei, and the current Reiwa.

The Showa period is a bit exceptional from a calendar perspective, particularly as it relates to computers. The Taisho period was brief, just around fifteen years, meaning the Showa emperor took the throne at a young age and had a long reign. In total the period lasted 62 years, making it the longest era by an almost twenty year margin. (If you noticed a contradiction, don't worry, we'll get to it.) This long period also had another feature that's of interest: since it lasted from 1926 to 1989, it happened to cover the entire early history of computing.

Given all the above, you may have already figured out what the Showa Hundred Year Problem is - it's essentially the same problem as Y2K, just shifted to the start of the Showa era rather than the 20th century. Suppose that somewhere a programmer had to display dates according to Japanese imperial years. Suppose that, since their entire career (and probably entire life) the only era in use had been Showa, they used the Showa year to store the date in the program. And since they weren't thinking about thirty years in the future, they only stored it as two digits.

It's unlikely this program would be around over thirty years later. But perhaps part of the program survived into the Heisei era, and someone just wrote a little patch that checked if the number was greater than 63, and subtracted that to show the Heisei year - a formatting trick to avoid rewriting old but functional code. But if that happened, then actually the internal representation of the year could still be just a two digit decimal number.

So what happens when the year wraps around from 99 to 00? Things that should happen in 2025 instead somehow belong to 1925, cats and dogs live together, and hell breaks loose, or something like that. [Mu](https://web-mu.jp/), Japan's monthly magazine of the strange, featured an article about the problem on the cover of its [November 2024 special issue](https://www.amazon.co.jp/%E3%83%A0%E3%83%BC11%E6%9C%88%E5%8F%B7%E5%88%A5%E5%86%8A-2025%E5%B9%B4%E4%BA%BA%E9%A1%9E%E6%BB%85%E4%BA%A1%E5%A4%A7%E4%BA%88%E8%A8%80-%E5%B5%A9%E5%A4%9C%E3%82%86%E3%81%86/dp/B0DHW9N2F2), issue describing the potential downfall of the financial system and the Internet, though the piece only rated a small mention on the cover. The article was light on technical details, and also curiously described Unix as a programming language.

While a number of articles cropped up explaining what the Showa Hundred Year Problem was leading up to 2025, they passed mostly unnoticed, mere curiosities compared to the major media attention showered on Y2K a quarter century ago. And, in fact, as 2025 comes to a close, I can't find any reports of actual issues stemming from the date change. There are a few records of preparations for any issues, but even those are from the past, and it seems that any system old enough to be a source of problems had already outlived its natural usefulness.

That said, while reviewing documents about the problem there is one little detail that struck me. Centuries in the Gregorian calendar start from 00 with their last two digits - 1800, 1900, and 2000. But that isn't the case for imperial eras, which don't have a zero year, and start from year one. That means that for anything started in the first year of an imperial era, like [Cafe Lion](https://www.dampfkraft.com/tokyo-spots/cafe-lion.html), the hundredth anniversary is not year 100, but year 101. (This is also why the last Showa year was 64 even though the era only lasted 62 *full* years - it started on December 25, 1926, and ended just a week into 1989.)

What if a system somewhere stored the first year as zero, and just added one for output and formatting? If there is a system like that, it wouldn't run into overflow issues in Showa 100, but in Showa 101... or 2026.

But I'm sure it'll be fine. Ψ