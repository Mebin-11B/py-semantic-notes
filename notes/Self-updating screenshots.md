---
title: "Self-updating screenshots"
url: https://interblah.net/self-updating-screenshots
clipped: 2026-06-17 01:11:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Self-updating screenshots](https://interblah.net/self-updating-screenshots)

## Digest Summary
The author built an automated screenshot system for the Jelly help centre. Documentation pages are written in Markdown, processed by Redcarpet into HTML and rendered as ERB views in Rails. Within the Markdown, HTML comments of the form `` serve as instructions for the screenshot generator. A Rake task launches headless Chrome via Capybara + Cuprite, scans all Markdown files for these comments, groups them by team to reuse logins, navigates to each URL, performs optional actions (click, wait), and captures screenshots in one of three modes: **element** (specific CSS selector), **full_page** (entire page with optional cropping), or **viewport** (visible area). Additional options include `click`, `wait`, `crop`, `torn` (CSS clip‑path edge effect), and `hide` (temporarily hide elements). The task outputs PNGs referenced by the image tags, then builds the help pages, placing source Markdown in `public/manual/` and generated ERB views in `app/views/help/`. Running the single build command updates all screenshots whenever the UI changes, eliminating manual capture and keeping documentation in sync with code.

## Discussion Summary
The comments collectively praise automated screenshot generation as a valuable, low‑maintenance approach that enhances documentation, app store submissions, and CI/CD pipelines. Users note its applicability to mobile and game projects, its compatibility with tools like Fastlane, and the convenience of embedding capture instructions directly in markdown. Several contributors share related implementations and extensions, while occasional technical issues are mentioned without detracting from the overall endorsement. The consensus is that integrating screenshot automation into the build process is widely regarded as beneficial and worth adopting.

---

## Full Article

I think this might be the neatest thing Iâve built in
[Jelly](https://letsjelly.com) that nobody will ever notice.

If youâve ever maintained a help centre or documentation site for a web
application, youâll know the particular misery of screenshots. You write a
lovely help article, carefully capture a screenshot of the feature youâre
documenting, crop it, maybe add a border and a shadow, upload it, and it looks
great. Then you change the UI slightly â tweak a colour, move a button,
update some copy â and suddenly every screenshot that includes that element
is stale. You know theyâre stale. Your users might not notice, but *you*
know, and it gnaws at you.

Or maybe thatâs just me.

Either way, I decided to fix it. The help centre in Jelly has a build system
where **screenshots are captured automatically from the running application**,
and they update themselves whenever you rebuild.

Markdown with a twist
---------------------

The help articles are written in Markdown, which gets processed into HTML via
Redcarpet and then rendered as ERB views in the Rails app. So far, so
ordinary. But scattered through the Markdown are comments like this:

```
<!-- SCREENSHOT: acme-tools/inbox | element | selector=#inbox-brand-new-section -->
![The "Brand New" section](images/basics-brand-new-section.png ':screenshot')
```

That HTML comment is an instruction to the screenshot system. It says: âgo to
the inbox page for the Acme Tools demo team, find the element matching
`#inbox-brand-new-section`, and capture a screenshot of it.â The image tag
below it is where the result ends up.

How it works
------------

Under the hood, itâs a Rake task that fires up a headless Chrome browser via
Capybara and Cuprite. It scans every Markdown file for those `SCREENSHOT`
comments, groups them by team (so it only needs to log in once per team),
navigates to each URL, and captures the screenshot.

The capture modes are:

* **element** â screenshot a specific DOM element by CSS selector
* **full\_page** â capture the whole page, optionally cropped to a height
* **viewport** â just whatâs visible in the browser window

And there are a handful of options that handle the fiddly cases:

```
<!-- SCREENSHOT: nectar-studio/manage/rules | full_page | click=".rule-create-button" wait=200 crop=0,800 -->
```

That one navigates to the rules page, *clicks a button* to open a form, waits
200 milliseconds for the animation, then captures a full-page screenshot
cropped to a specific region. The `click` option is the one that really makes
it sing â so many features live behind a button press or a popover, and being
able to capture those states automatically is wonderful.

Thereâs also `torn` â which applies a torn-paper edge effect via a CSS
clip-path â and `hide`, which temporarily hides elements you donât want in
the shot (dev toolbars, cookie banners, that sort of thing).

The satisfying bit
------------------

The whole pipeline runs with just this:

That captures every screenshot and then builds all the help pages. When I
change the UI, I run that command and every screenshot updates to match. No
manual cropping, no âoh I forgot to update that oneâ, no slowly-diverging
screenshots that make the help centre look abandoned.

The markdown files live in `public/manual/`, organised by section â basics,
setup, advanced â and the build step processes them into ERB views in
`app/views/help/`, complete with breadcrumbs and section navigation, all generated
from the source markdown files.

This also makes it easy to update the help centre at the same time Iâm working
on the feature; the code and the documentation live together and can be kept in
sync within the same PR or even commit.

One of those âwhy didnât I do this soonerâ things
-------------------------------------------------------

I put off building this for ages because it seemed like a lot of work for a
ânice to haveâ. It *was* a fair bit of work, honestly. Handling the edge cases
â elements that need scrolling into view, popovers that need clicking,
images that need cropping to avoid showing irrelevant content â took longer
than the happy path.

But now that it exists, I update the help centre far more often than I used to,
because the friction is almost gone. Change the UI, run the build,
commit the results. The screenshots are always current, and I never have to
open a browser and fumble around with the macOS screenshot tool.