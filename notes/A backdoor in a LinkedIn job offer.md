---
title: "A backdoor in a LinkedIn job offer"
url: https://roman.pt/posts/linkedin-backdoor/
clipped: 2026-06-17 00:42:32
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A backdoor in a LinkedIn job offer](https://roman.pt/posts/linkedin-backdoor/)

## Digest Summary
A recruiter on LinkedIn sent a public GitHub repository, claiming a “deprecated Node modules” issue needed a lead engineer. The repo contains a React frontend and Node backend, but the backdoor resides in `app/test/index.js` (~250 lines). It builds the URL `https://rest‑icon‑handler.store/icons/77` from string fragments and executes any code returned by that server on line 225, hidden among commented‑out tests. The backdoor is triggered automatically because `package.json` defines a `prepare` script that runs `node app/index.js`; `npm install` runs `prepare`, loading `app/index.js`, which requires `./test` and thus executes the malicious test file. The commit history is falsified: all 39 commits are attributed to a real full‑stack developer who never touched the repo, and the recruiter’s LinkedIn profile belongs to an unrelated arts journalist who pretended technical expertise. The author avoided execution by using a read‑only analysis agent, reported the repo to GitHub and the recruiter to LinkedIn, and warned that similar supply‑chain attacks can arise from unsolicited code‑review requests.

## Discussion Summary
Comments converge on strong concern about increasingly sophisticated recruiter scams that distribute malicious npm packages via LinkedIn and GitHub, exploiting job‑seeker desperation and supply‑chain vulnerabilities. Contributors criticize the platforms’ inadequate reporting channels and slow remediation, noting repeated exposure and limited impact of reports. Advice emphasizes isolating any untrusted code, using virtual environments, and treating unsolicited installation requests as high‑risk. Several remarks suggest possible state‑backed actors and call for coordinated defensive measures, while overall sentiment remains wary and critical of current safeguards.

---

## Full Article

![A backdoor in a LinkedIn job offer](/posts/linkedin-backdoor/splash_hu_6f6d450d0d33e225.png)

Last week, I got a LinkedIn message from a recruiter at a small crypto startup. We exchanged a few messages over a couple of days, she described a broken proof-of-concept they needed a lead engineer for, and then sent me a public GitHub repo to review. Specifically, she asked me to “check out the deprecated Node modules issue.”

It’s not uncommon to ask for a review of an existing codebase, but something felt off and raised an alarm in my head, so I decided to get a bit extra paranoid.

Instead of cloning and installing dependencies, I spun up a throwaway VPS on Hetzner, cloned the repo there, and pointed [Pi](https://pi.dev) at it in read-only mode, with only file-reading tools enabled:

```
pi --tools read,grep,find,ls
```

I asked the agent to review the codebase and flag anything suspicious. It stopped almost immediately at `app/test/index.js`.

The backdoor
------------

The repo felt like a React frontend with a Node backend. The trap was in `app/test/index.js`, about 250 lines disguised as a test suite. Inside, a URL is assembled from fragments:

```
const protocol = "https",
  domain = "store",
  separator = "://",
  path = "/icons/",
  token = "77",
  subdomain = "rest-icon-handler",
  bearrtoken = "logo";
```

These combine into `https://rest-icon-handler.store/icons/77`.

Then, buried between walls of commented-out tests, the payload runs anything the server sends back to your machine.

![The payload on a single minified line in app/test/index.js, surrounded by commented-out test code](/posts/linkedin-backdoor/payload-in-test-file.png)

The payload on line 225, hiding in plain sight between commented-out tests.

How it triggers
---------------

The file doesn’t wait for the tests to run. `app/index.js` itself executes `const test = require('./test')`, which loads and runs `app/test/index.js`.

`package.json` wires `app/index.js` into startup:

![package.json scripts section with prepare and app:pre highlighted; app:pre runs node app/index.js](/posts/linkedin-backdoor/package-json-scripts.png)

`prepare` runs `app:pre`, which is `node app/index.js`.

The `prepare` script is the important one. npm runs [`prepare`](https://docs.npmjs.com/cli/v8/using-npm/scripts#life-cycle-scripts) automatically after `npm install`, so just installing dependencies executes the backdoor.

The instruction to “check out the deprecated Node modules issue” was bait to get me to run `npm install`.

I could have let the payload run in the sandbox and watched what the server sent back as the second stage, but I stopped there. A repo that runs whatever a server hands it was enough evidence.

A borrowed identity
-------------------

The commits in the repo were authored under the name and email of a real developer, a full-stack engineer with an ordinary LinkedIn profile, a personal website, and a GitHub account with a long history. I messaged him, pretending I’d inherited the codebase and had a few implementation questions, to see how he’d react.

He told me he’d never worked for them. He’d been impersonated on GitHub before and had a repo taken down over it, and he had nothing to do with this one. He was reporting these repos too.

![GitHub contributors graph showing a single contributor with 39 commits and 4,470 additions, name and avatar redacted](/posts/linkedin-backdoor/contributor-graph.png)

The whole commit history, 39 commits, attributed to one developer who’d never touched the repo.

A second borrowed identity
--------------------------

The recruiter’s profile belonged to a real arts journalist, a well-known one I looked up later, with a long cultural background and nothing technical on it. When I played along and told her I couldn’t get the project to install, the journalist instantly turned into an expert on npm and Node versions. It was quite amusing, I’d say.

![LinkedIn chat where the recruiter insists the project runs fine on Node.js v24 and asks whether I ran npm install](/posts/linkedin-backdoor/npm-install-bait.png)

The non-technical recruiter, suddenly debating Node versions and pushing me to run npm install.

This can happen to anyone
-------------------------

I’ve heard of these attacks and read about them on HN, but when one came after me it still caught me a bit off guard. I suspected something from the first few messages, but on a more tired or rushed day, I could easily have run `npm install` before thinking it through. So, if you get a LinkedIn message asking you to review a repo, a bit of paranoia and good security hygiene never hurts.

Another takeaway is that reviewing the code with a read-only agent turned out more productive than reading it myself. The backdoor was dressed up as sloppy beginner code, but the agent flagged it in seconds.

I reported the repo to GitHub and the recruiter to LinkedIn. So far nothing has changed and the code is still up.