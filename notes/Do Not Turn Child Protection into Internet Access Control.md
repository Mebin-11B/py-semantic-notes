---
title: "Do Not Turn Child Protection into Internet Access Control"
url: https://news.dyne.org/child-protection-is-not-access-control/
clipped: 2026-06-17 01:29:28
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Do Not Turn Child Protection into Internet Access Control](https://news.dyne.org/child-protection-is-not-access-control/)

## Digest Summary
Age‑verification systems, once limited to adult sites, are spreading to mainstream platforms (social media, messaging, gaming, search) across Europe, the US, the UK and Australia. Technically this shifts the Internet from open to permissioned access: users must prove attributes before a service responds. Proposals in the US embed a persistent age‑status layer in operating systems, exposing it via system‑level APIs; Linux’s systemd has added an optional birth‑date field, showing regulatory influence on personal‑computing data models. The debate conflates content moderation (classification and filtering) with guardianship (parental or community responsibility), ignoring that centralized age checks are easily evaded (VPNs, shared or fabricated credentials) and create a broad identity‑logging infrastructure. Investigations link lobbying by data‑driven firms to the legislation. The author argues for separating problems: keep content moderation at the endpoint (browser, device, school network) and retain guardianship locally, allowing OS‑level policies only as user‑controlled surfaces. Regulation should target manipulative recommendation systems and dark‑pattern designs rather than imposing universal permission layers.

## Discussion Summary
The comments converge on strong criticism of mandatory age‑verification measures, viewing them as a gateway to pervasive identity tracking and surveillance rather than genuine child protection. Contributors argue that responsibility should lie with parents and that technical safeguards—such as password‑protected controls on devices or network‑level filtering—are preferable to broad biometric data collection. Skepticism about corporate and governmental motives is prevalent, with many citing profit, advertising, and control agendas, while a minority expresses tentative acceptance if it reduces unwanted content. Overall, the discourse frames the policies as intrusive, ill‑designed, and misrepresented as safety measures.

---

## Full Article

Age verification is no longer a narrow mechanism for a few adult websites. [Across Europe, the USA, the UK, Australia, and elsewhere](https://www.politico.eu/article/age-check-social-media-scientist-warning/), it is expanding into social media, messaging, gaming, search, and other mainstream services.

> The real question is no longer whether age checks will spread. It is what kind of internet they are turning into.

The common framing says these systems exist to protect children. That concern is real. Children are exposed to harmful content, manipulative recommendation systems, predatory behavior, and compulsive platform design. Even adults are manipulated, quite succesfully, with techniques that can influence national elections.

[Democracy at risk: media warfare and the role of technology in modern elections - Friends of Europe

The think tank for a more inclusive Europe](https://www.friendsofeurope.org/insights/critical-thinking-democracy-at-risk-media-warfare-and-the-role-of-technology-in-modern-elections/)

But from a technical and political point of view, age verification is not just a child-safety feature. It is an access control architecture. It changes the default condition of the network from open access to permissioned access. Instead of receiving content unless something is blocked, **users increasingly have to prove something about themselves before a service is allowed to respond**.

That shift becomes clearer when age assurance moves down into the operating system. In some US proposals, the model is no longer a one-off check at a website. It becomes a persistent [age-status layer maintained by the OS](https://www.tomshardware.com/software/operating-systems/california-introduces-age-verification-law) and exposed to applications through a system-level interface. At that point, age verification stops looking like a limited safeguard and starts looking like a general identity layer for the whole device.

This is no longer only a proprietary-platform story either. Even the Linux desktop stack is beginning to absorb this pressure. [systemd has reportedly added an optional `birthDate` field to `userdb` in response to age-assurance laws](https://itsfoss.com/news/systemd-age-verification/). Regulation is beginning to shape the data model of personal computing, so that higher-level components can build age-aware behavior on top.

> The main conceptual mistake in the current debate is simple. It confuses content moderation with guardianship. Those are not the same problem.

**Content moderation is about classification and filtering**. It asks whether some content should be blocked, labeled, delayed, or handled differently. **Guardianship is something else:** the contextual responsibility of parents, teachers, schools, and other trusted adults to decide what is appropriate for a child, when exceptions make sense, and how supervision should evolve over time.

I am also a parent. I understand the fear behind these proposals because I live with it too. Children do face real online risks. But recognizing that does not oblige us to accept any solution placed in front of us, least of all one that **weakens privacy for everyone while shifting responsibility away from families**, schools, and the people who actually have to guide children through digital life.

> Moderation is partly technical. Guardianship is relational, local, and situated in specific contexts.

**Age-verification laws collapse two questions in one centralized answer**. The result is predictable. A platform, browser vendor, app store, operating-system provider, or identity intermediary is asked to enforce what is presented as a child-protection policy, even though no centralized actor can replace the judgment of a parent, a school, or a local community.

> This is the wrong solution. It treats an educational and social problem as an authentication problem.

It also fails on its own terms. The **bypasses are obvious**: VPNs, borrowed accounts, purchased credentials, fake credentials, and tricks against age-estimation systems. A control that is easy to evade but expensive to impose is not a serious compromise: it is an error or, one may say, a **corporate data-grab**.

[Age Verification Lobbying: Dark Money, Model Legislation & Institutional Capture

Investigative research into age verification lobbying, dark money, and model legislation](https://tboteproject.com)

OSINT investigation tracing corporate lobbying and opaque advocacy networks behind world-wide age-verification policies.

Even when adopting advanced zero-knowledge proof, even with [cryptography I do develop myself at work since a decade](https://web.archive.org/web/20210805203257/https://europost.eu/en/a/view/dr-denis-roio-we-want-people-to-have-full-control-over-their-data-26620), it won't help. Because the mobile operating system manufacturers will know what goes into the blinding mechanisms and, paradoxically, they will know more than authorities do now!

[Privacy in EUDI

Until process isolation is granted for every execution of zero-knowledge algorithms, privacy-preserving technology won’t protect us from mega-corporations spying on us.](https://news.dyne.org/privacy-in-eudi/)

**The price is very high and paid by everyone**. More identity checks. More metadata. More logging. More vendors in the middle. More friction for people who lack the right device, the right papers, or the right digital skills. This is not a minor safety feature. It is a **new control layer for the network**.

And once that layer exists, it rarely stays confined to age. Infrastructure built for one attribute is easily reused for others: location, citizenship, legal status, platform policy, or whatever the next panic demands. This is how **a limited check becomes a general gate**.

> The solution is simple: moderate content close to the endpoint, in the browser, on the device, on the school network, or through trusted local lists.

**Keep guardianship where it belongs**: with parents, teachers, schools, and communities that can make contextual decisions, authorize exceptions, and adjust over time.

**The operating system can help** here, but only as a **local policy surface** under the control of users and guardians. It should not become a universal age-broadcasting layer for apps and remote services. That is the architectural line that matters.

> **We should punish the predatory behavior of platforms towards minors, instead of forcing everyone to feed them information.**

Most of the harms invoked in this debate do not come from the mere existence of content online. They come from recommendation systems, dark patterns, addictive metrics, and business models that reward amplification without responsibility.  
If the goal is to protect minors, that is where regulation should bite.

> Children need protection.  
> The internet does not need a permission system.

If we are serious about reducing harm, we should stop asking how to identify everyone and start asking how to strengthen local control without turning the network into a checkpoint.

Chronology
----------

It is encouraging to see this article circulating widely, as it may contribute to a shift in how policymakers approach the issue. Given its growing visibility, I will keep a concise record here of the sequence of its coverage across media outlets, as well pilot implementations across the world.

My first account on the problem emerged from a dialogue with Brave's developer [Kyle den Hartog](https://kyledenhartog.com/) at a [cypherpunk retreat in Berlin](https://cypherpunk.camp/). It was right after facilitating the digital identity track of the event that I published a rather technical piece on the topic.

[Age Verification for Humans

Europe’s age‑verification pilots conflate censorship with guardianship. This essay argues for a decentralised approach that separates technical filtering from social responsibility.](https://news.dyne.org/age-verification-for-humans/)

Later, as age verification measures began to take hold, and in alignment with our community facilitators at the Dyne.org foundation, [we decided to discontinue Discord as a channel for participation](https://toot.community/@dyne/116086807698886883), as the platform moved to impose age verification.

> This decision to leave Discord was received positively across the community, a clear indication that privacy is valued above outreach.

Then the systemd dispute unfolded, and I found myself, as founder of the project, as the first distro maintainer stating that we would not implement age verification in [Devuan GNU/Linux](https://devuan.org), a Debian fork without systemd that has, since 2016, shown fewer bugs and security advisories. The tech journalist Lunduke picked it up immediately, setting off a wave of similar declarations across the distribution maintainer community.



That was the moment I realised the need to set out, in clear terms, the reasons behind this choice, and the grounds for a form of **conscientious objection should such laws ever be enforced on our projects at Dyne.org**. So I wrote a piece for Wired Italy in my native language.

[La verifica dell’età in rete non solo non protegge i minori, ma ci mette tutti a rischio

Pensata come misura di tutela, la verifica dell’età rischia di creare più problemi di quanti ne risolva, tra inefficacia, perdita di privacy e maggiore centralizzazione del controllo online](https://www.wired.it/article/verifica-eta-rete-non-protegge-minori-rischio)

I then translated this article and published it here, in English, through our think and do tank, where I'll keep updating it. The piece you have just read quickly reached the front page of Hacker News, drawing nearly 400 comments from concerned readers and technical experts, a valuable body of material to build on.

[Do Not Turn Child Protection into Internet Access Control | Hacker News](https://news.ycombinator.com/item?id=47470991)

As the discussion gains momentum, I am engaging with colleagues at the City of Lugano and the [Plan₿ Foundation](https://planb.lugano.ch), where I have recently taken on the role of Scientific Director. The proposal is to move from analysis to action by establishing a city-wide pilot that explores technologies for locally managed guardianship, offering a constructive example for Switzerland.

[draft lip-ageverif: local child protection without internet age verification by jaromil · Pull Request #1 · LuganoPlanB/LIPs

Inspired by https://news.dyne.org/child-protection-is-not-access-control/
This PR adds a new draft proposal in lip-ageverif.md for a Lugano approach to child protection that does not rely on mandat…](https://github.com/LuganoPlanB/LIPs/pull/1)

We are approaching this with confidence and preparing for a rollout for Lugano within the next two years. At the same time, within the Swiss Confederation there are signs of a more grounded direction, taking time before rushing into the imposition of age verification. The [Republik magazine published an excellent article by Adrienne Fichter](https://www.republik.ch/2026/04/10/ctrl-warum-das-social-media-verbot-fuer-teenager-zum-albtraum-wird) on the topic which got also translated to english:

[Why a Social Media Ban for Teens Is Turning into a Nightmare - techjournalismus.ch

(english translation, original article in german below)](https://techjournalismus.ch/why-a-social-media-ban-for-teens-is-turning-into-a-nightmare/)

My next steps include reaching out to contacts in Europe to help broaden the discussion and contribute to a more balanced public debate, in the face of sustained pressure from corporate lobbies advancing data-extractive measures.

And you can play a meaningful role as well: engage with the issue, bring your technical and political understanding to it, and help sustain attention so that those who make up the internet are not excluded from decisions that affect it. I hope this material and the reasoning behind it can be useful in that direction. Do let us at Dyne.org know if we can assist in making visible successful local pilots that implement child protection in a sound and proportionate way.

### Who am I

I've written extensively about the problems of European Digital Identity implementation plans and architecture.

[The Seven Sins of European Digital Identity (EUDI)

EUDI as is today presents big problems and disregards criticism, warnings, and requests to review technical details, with results that harm the fairness of the system and the privacy of its participants, also limiting infrastructure security and scalability.](https://news.dyne.org/the-problems-of-european-digital-identity/)

Besides being the founder of the [Devuan GNU+Linux](https://devuan.org) distribution, I've been working on privacy and identification technologies for over a decade, primarily in [projects funded by the European Commission](https://jaromil.dyne.org/?ref=news.dyne.org#grants).  
Among my efforts are [decodeproject.eu](https://decodeproject.eu/?ref=news.dyne.org) and [reflowproject.eu](https://projects.research-and-innovation.ec.europa.eu/en/projects/success-stories/all/six-european-cities-gear-more-circular-future), various academic papers, including [SD-BLS](https://arxiv.org/abs/2406.19035?ref=news.dyne.org), recently published by IEEE. Additionally, with our team at [The Forkbomb Company](https://forkbomb.solutions/?ref=news.dyne.org) we've developed digital identification products as [DIDROOM.com](https://didroom.com/?ref=news.dyne.org) and [CREDIMI.io](https://credimi.io/?ref=news.dyne.org).