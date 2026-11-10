---
title: "Wander – A tiny, decentralised tool to explore the small web"
url: https://susam.net/wander/
clipped: 2026-06-17 01:30:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Wander – A tiny, decentralised tool to explore the small web](https://susam.net/wander/)

## Digest Summary
A Wander console enables users to browse random sites and pages contributed by the Wander community, a network of personal websites. While a user can switch to another console on a different domain, the current console can also retrieve recommendations recursively from linked consoles without leaving the page. To host a personal Wander console, one must download the provided ZIP file, extract `index.html` and `wander.js`, place them in a `/wander/` directory on the web server, and edit `wander.js` according to the instructions on codeberg.org/susam/wander. After deployment, the console’s URL can be shared in the community thread; other users may add it to their consoles, integrating it into the broader Wander network. Additional documentation and source code are available at codeberg.org/susam/wander.

## Discussion Summary
The comments are largely positive, praising the project’s decentralized, webring‑like approach and its potential to revive exploratory browsing similar to StumbleUpon. Users appreciate its simplicity, low hosting requirements, and alignment with grassroots web values, while many express hope that it reaches non‑tech creators and diverse content areas. Repeated constructive feedback includes requests for better curation tools, broader protocol support (e.g., Gemini, Gopher), improved navigation (open‑in‑new‑tab options, compatibility with older browsers), and resolution of occasional loading loops. Overall sentiment is supportive with practical suggestions for refinement.

---

## Full Article

JavaScript is required to use this application.







Base Console
------------

Your base console is:

This is the console you have loaded on your browser. The
base console fetches website recommendations from itself as
well as other remote consoles and shows them to you.

Remote Console
--------------

The last web page recommendation to you was:

This recommendation was fetched from the following remote
console:

Console Neighbours
------------------

This console lists the following consoles as its neighbours:

You can wander to a neighbouring console by clicking one of
the links above. Note that you do not really need to change
console to browse the Wander network. The host console can
fetch recommendations from other consoles, then from the
consoles they link to and so on recursively. However, if
you want to explore other consoles, you may click one of the
links above.

Pages
-----

This console recommends the following websites and pages to
the Wander community:

If you click on any link above, it will open in a new tab.

Ignore List
-----------

This console ignores URLs matching the following patterns:

You might find the reasons for these ignore patterns in this
console's  file.

A URL that matches an ignore pattern is never recommended in
this console, even if it appears in the recommendation lists
of this console or other remote consoles.

Ignore patterns are normalised before matching. The URL
scheme, query parameters and fragments are ignored, matching
is case-insensitive and the patterns act like prefixes. A
pattern such as https://example.com/foo/ matches both HTTP
and HTTPS URLs for the same site, as well as all pages under
that path.

Wandering History
-----------------

Your wandering history from the current session, in reverse
chronological order
(up to  pages):

Each item above includes three links: the console that
recommended a page, the wander.js file of that console and
the page that was recommended.

Discovered Consoles
-------------------

Consoles discovered in the current session, in reverse
chronological order (up to ):

Each item above includes four links: the recommending
console and its wander.js file, followed by the recommended
console and its wander.js file.

Console Crawler
---------------

This dialog is now running a crawler to find consoles
reachable from this console. The list below updates
automatically as new consoles are found.



Version  

Wander Console lets you discover random personal websites from
the Wander community.

To learn more about Wander or set up your own console, see
[codeberg.org/susam/wander](https://codeberg.org/susam/wander#readme).

Wander Console is free and open source software. You can use,
copy, modify, merge, publish, distribute, sublicence and/or
sell copies of it, under the terms of the
[MIT Licence](https://codeberg.org/susam/wander/src/branch/main/LICENCE.md).

This software is provided "AS IS", WITHOUT WARRANTY OF ANY
KIND, express or implied. See the
[licence](https://codeberg.org/susam/wander/src/branch/main/LICENCE.md)
for details.