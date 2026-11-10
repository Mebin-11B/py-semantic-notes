---
title: "Debian decides not to decide on AI-generated contributions"
url: https://lwn.net/SubscriberLink/1061544/125f911834966dd0/
clipped: 2026-06-17 01:34:38
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - open source governance
  - software licensing
  - developer community
  - ai ethics
  - quality control
related:
  - "[[Open Source Governance]]"
  - "[[Software Licensing]]"
  - "[[Quality Control]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Debian developers debated a general resolution regarding generative AI patches, ultimately choosing to evaluate contributions case-by-case due to quality and copyright uncertainties.
>
> **Key points:**
> - A proposed resolution would permit AI-assisted patches with clear attribution, licensing guarantees, and verification of merit.
> - Concerns include the potential erosion of junior developer skill acquisition, licensing/copyright ambiguities of training data, and reviewer fatigue.
> - The community decided against a formal project-wide vote, preferring to handle submissions under existing package maintenance policies.
>
> **Concept links:** [[Open Source Governance]], [[Software Licensing]], [[Developer Community]], [[Ai Ethics]], [[Quality Control]]
>
> **Suggested connections:**
> - [[Open Source Governance]] — decision-making structures and policies in volunteer-run software projects.
> - [[Software Licensing]] — legal frameworks governing code reuse, copyright, and distribution.
> - [[Quality Control]] — maintaining codebase integrity against automated or low-veracity contributions.
<!-- ai-summary:end -->

# [Debian decides not to decide on AI-generated contributions](https://lwn.net/SubscriberLink/1061544/125f911834966dd0/)

## Digest Summary
Debian opened a February discussion after Lucas Nussbaum posted a draft general resolution (GR) on permitting AI‑assisted contributions. The proposal would allow partially or fully LLM‑generated patches provided contributors disclose the use, tag the change (e.g., “[AI‑Generated]”), and vouch for its technical merit, security, licensing and utility. It also bans using generative‑AI on non‑public or embargoed material.

Debate centered on terminology (AI vs. LLM), the granularity of allowed uses (code review, prototype generation, production code), and the impact on onboarding new contributors. Some argued AI tools could replace junior developers without skill transfer, while others saw potential to lower entry barriers. Copyright concerns were raised regarding training data and output licensing, with suggestions to defer policy until legal clarity emerges. A minority advocated a hard ban, even threatening removal of major upstream packages, but this view lacked support.

Overall, developers agree Debian is not ready for a formal vote; the issue will remain handled case‑by‑case under existing policies while discussions continue.

## Discussion Summary
Comments reflect a nuanced view of AI‑generated code in open‑source projects. Many acknowledge its productivity gains and accessibility benefits, treating it as a useful assistant when the contributor validates and owns the output. Concerns focus on quality control, reviewer burden, potential copyright or attribution gaps, and the difficulty of distinguishing AI from human contributions as models improve. The prevailing opinion favors responsible integration—transparent disclosure, higher testing standards, and limiting AI use to trusted contributors—rather than outright bans, emphasizing human accountability for any submitted changes.

---

## Full Article

> **Please consider subscribing to LWN**
>
> Subscriptions are the lifeblood of LWN.net. If you appreciate this
> content and would like to see more of it, your subscription will
> help to ensure that LWN continues to thrive. Please visit
> [this page](https://lwn.net/Promo/nst-nag1/subscribe) to join up and keep LWN on
> the net.

By **Joe Brockmeier**  
March 10, 2026

Debian is the latest in an ever-growing list of projects to wrestle ([again](https://lwn.net/ml/all/3qxsesyoouxh2h6fodosnln4wsyl3tpmnbcu6pqzekqkz6k577%40a2gos5jbaowf/))
with the question of LLM-generated contributions; the latest debate started in
mid-February, after
Lucas Nussbaum [opened a
discussion](https://lwn.net/ml/all/aZY_P6jA8cGYkev2%40grub.nussbaum.fr/) with a draft general resolution (GR) on whether Debian should
accept AI-assisted contributions. It seems to have, mostly, subsided without a GR
being put forward or any decisions being made, but the conversation was illuminating
nonetheless.

Nussbaum said that Debian probably needed to have a
discussion ""to understand where we stand regarding AI-assisted contributions to
Debian"" based on some recent discussions, though it was not clear
what discussions he was referring to. Whatever the spark was, Nussbaum
put forward the draft GR to clarify Debian's stance on allowing
AI-assisted contributions. He said that he would wait a couple of days
to collect feedback before formally submitting the GR.

His proposal would allow ""AI-assisted contributions (partially
or fully generated by an LLM)"" if a number of conditions were
met. For example, it would require explicit disclosure if ""a
significant portion of the contribution is taken from a tool without
manual modification"", and labeling of such contributions with
""a clear disclaimer or a machine-readable tag like
'[AI-Generated]'"." It also spells out that contributors should
""fully understand"" their submissions and would be accountable
for the contributions, ""including vouching for the technical merit,
security, license compliance, and utility of their
submissions"". The GR would also prohibit using generative-AI tools
with non-public or sensitive project information, including private
mailing lists or embargoed security reports.

#### AI is a marketing term

It is fair to say that it is difficult to have an effective conversation about a
technology when pinning down accurate terminology is like trying to nail Jell-O to a
tree. AI is the catch-all term, but much (not all) of the technology in question is
actually tooling around large language models (LLMs). When participants have
differing ideas of what is being discussed, deciding whether the thing should be
allowed may pose something of a problem.

Russ Allbery [asked](https://lwn.net/ml/all/87wm091sse.fsf@hope.eyrie.org) for people to
be more precise in their descriptions of the technologies that their proposals might
affect. He asserted that it has become common for AI, as a term, ""to be so
amorphously and sloppily defined that it could encompass every physical object in the
universe"". If the project is going to make policy, he said, it needed to be very
specific about what it was making policy about:

> An LLM has some level of defined meaning, although even there it would be nice if
> people were specific. Reinforcement learning is a specific technique with some
> interesting implications, such as the existence of labeled test data used to train
> the algorithm. "AI" just means whatever the person writing a given message wants it to
> mean and often changes meaning from one message to the next, which makes it not
> useful for writing any sort of durable policy.

Gunnar Wolf [agreed](https://lwn.net/ml/all/aZaifr0AOWGufVpQ@iiec.unam.mx) with Allbery,
but Nussbaum [claimed](https://lwn.net/ml/all/aZbUi-Gb6ukTZwoD@grub.nussbaum.fr) that the
specific technology did not matter. The proposal boiled down to the use of automated
tools for code analysis and generation:

> I see the problem we face as similar to the historical questions surrounding the
> use of BitKeeper by Linux (except that the choice of BitKeeper imposed its use by
> other contributors). It is also similar to the discussions about proprietary security
> analysis tools: since those tools are proprietary, should we ignore the vulnerability
> reports they issue?
>
> If we were to adopt a hard-line "anti-tools" stance, I would find it very hard to
> draw a clear line.

Drawing clear lines, however, is something that a number of Debian developers felt
was important. Sean Whitton [proposed](https://lwn.net/ml/all/87bjhldqbg.fsf@zephyr.silentflame.com) that
the GR should not only say "LLM" rather than "AI", but it should also
distinguish between the *uses* of LLMs, such as code review, generating
prototypes, or generating production code. He envisioned ballot options that could
allow some, but not all, of those uses. Distinguishing between the various
so-called AI technologies would help in that regard. He [urged](https://lwn.net/ml/all/87h5rdcawn.fsf@zephyr.silentflame.com)
Nussbaum ""not to argue too hard for something that is more general than LLMs
because that might alienate the people you want to agree to disagree with"."
Andrea Pappacoda [said](https://lwn.net/ml/all/DGIXNJ9DOOZK.242KIEJKRR81M@pappacoda.it) that
the specific technology mattered a lot; he wanted the proposal to have clear
boundaries and avoid broad terms like AI. He was uncomfortable with the idea of
banning LLMs, and not sure where to draw the line. ""What I can confidently say,
though, is that a project like [Claude's C
Compiler](https://www.anthropic.com/engineering/building-c-compiler) should not have a place in Debian.""

#### Beyond terminology

The conversation did not focus solely on the terminology, of course. Simon Richter
[had
questions](https://lwn.net/ml/all/3dfc89d6-c977-4978-ae93-97465645cef3@debian.org) about the implications of allowing AI-driven contributions from the
standpoint of onboarding new contributors to Debian. An AI agent, he said, could take
the place of a junior developer. Both could perform basic tasks under guidance, but
the AI agent would not learn anything from the exchange; the project resources spent
in guiding such a tool do not result in long-lasting knowledge transfer.

> AI use presents us (and the commercial software world as well) with a
> similar problem: there is a massive skill gap between "gets some
> results" and "consistently and sustainably delivers results", bridging
> that gap essentially requires starting from scratch, but is required to
> achieve independence from the operators of the AI service, and this gap
> is disrupting the pipeline of new entrants.

He called that the onboarding problem, and said that an AI policy
needed to solve that problem; he did not want to discourage people by rejecting
contributions or expend resources on mentoring people who did not want to be
mentored. Accepting AI-assisted drive-by contributions is harmful because it is a
missed opportunity to onboard a new contributor. ""The best-case outcome is that a
trivial problem got solved without actually onboarding a new contributor, and the
worst-case outcome is that the new contributor is just proxying between an AI and the
maintainer"". He also expressed concerns around the costs associated with such
tools, and speculated it might discourage contribution from users who could not
afford to use for-pay tools.

Nussbaum [agreed](https://lwn.net/ml/all/aZg4DA-j_ozOA3iu@grub.nussbaum.fr/) that the
cost could be a problem in the future. For now, he said, it is not an issue because
there are vendors providing access for free, but that could change. He disagreed that
Debian was likely to run out of tasks suitable for new contributors, even if it does
accept AI-driven contributions, and suggested that it may make harder tasks more
accessible. He pointed to [a study](https://arxiv.org/pdf/2601.20245)
written by an Anthropic employee and a person participating in the company's fellows
program, about how the use of AI impacts skill formation: ""A takeaway is that
there are very different ways to interact with AI, that produce very different
results both in terms of speed and of understanding"". He did not seem to be
persuaded that use of AI tools would be a net negative in onboarding new
contributors.

Ted Ts'o [argued](https://lwn.net/ml/all/20260224141454.GB16854@macsyma-wired.lan/)
against the idea that AI would have a negative impact:

> Some anti-AI voices are concerned that use of AI will decrease the
> ability to gain seasoned contributors, with the implied concern that
> this is self-defeating because it restricts the ability to gain new
> members in the future. And you are now saying we should gate keep
> contributors that might be using AI as being unworthy of contributing
> to Debian? I'd say that is even more self-defeating.

Matthew Vernon [said](https://lwn.net/ml/all/5bwm03azj7.fsf@chiark.greenend.org.uk/) that
the proposed GR minimized the ethical dimension of using generative AI. The
organizations that are developing and marketing tools like ChatGPT and Claude are
behaving unethically, he said, by systematically damaging the wider commons in the
form of automated scraping and doing as they like with others' intellectual
property. ""They hoover up content as hard as they possibly can, with scant if any
regard to its copyright or licensing"". He also cited environmental concerns and
other harms that are attributed to generative AI tools, ""from non-consensual
nudification to the flooding of free software projects with bogus security
reports"". He felt that Debian should take a clear stand against those tools and
encourage other projects to do the same:

> At its best, Debian is a group of people who come together to make the world a better
> place through free software. I think we should be centering the appalling behaviour
> of the organisations who are pushing genAI on everyone, and the real harms they are
> causing; and we should be pushing back on the idea that genAI is either a social good
> or inevitable.

There was also debate around the question of copyright, both in terms of the
licenses of material used to train models, as well as the output of LLM
tools. Jonathan Dowland [thought](https://lwn.net/ml/all/DGJTJEEZ3EK8.2XO8SCGJQTG9S@debian.org) that
it might be better to forbid some contributions now, since some see risks in
accepting such contributions, and then relax the project's
position later on when the legal situation is clearer.

Thorsten Glaser [took a
particularly harsh stance](https://lwn.net/ml/all/e9e05209-2155-7974-3b1a-57b84dea58c7@debian.org/) against LLM-driven contributions, going so far as to
suggest that some upstream projects should be forced out of Debian's [main](https://www.debian.org/doc/debian-policy/ch-archive#the-main-archive-area)
archive into [non-free](https://www.debian.org/doc/debian-policy/ch-archive#the-non-free-archive-area)
unless ""the maintainers revert known slop commits"". Ansgar Burchardt [pointed
out](https://lwn.net/ml/all/48ed86b7efadeb9b77dca21523fd3ea4214e0a32.camel@debian.org/) that would have the effect of banning the Linux kernel, Python, LLVM, and
others. Glaser's proposal did not seem particularly popular. He had taken a similar
stance on AI models in 2025; he argued most should be outside the main archive, [when the project discussed a GR](https://lwn.net/Articles/1020968/) about AI
models and the Debian Free Software Guidelines (DFSG). That GR never came to a vote,
in part because it was unclear whether the language would forbid anti-spam
technologies because one could not include the corpus of spam used as training data
along with filters.

Allbery did not want to touch on copyright issues but [had a few words](https://lwn.net/ml/all/87seag3id7.fsf@hope.eyrie.org/) to
say about the quality of AI-assisted code. It is common for people to object to code
generated by LLMs on quality grounds, but he said that argument does not make
sense. Humans are capable of producing better code than LLMs, but they are also
capable of producing worse code too. ""Writing meaningless slop requires no
creativity; writing really bad code requires human ingenuity.""

Bdale Garbee [seconded](https://lwn.net/ml/all/87cy1jts0s.fsf@gag.com/)
that notion, and said that he was reluctant to take a hard stance one way or the
other. ""I see it as just another evolutionary stage we don't really understand the
longer term positive and negative impacts of yet."" He wanted to focus on
long-term implications and questions such as ""what is the preferred form of
modification for code written by issuing chat prompts?"" Nussbaum [answered](https://lwn.net/ml/all/aaiomg6ZyJv5qWBm@grub.nussbaum.fr/) that
would be ""the input to the tool, not the generated source code"".

That may not be an entirely satisfying answer, however, given that LLM output is
not deterministic and the various providers of LLM tools retire models with some
frequency. A user may have the prompt and other materials fed to an LLM to generate a
result at a specific point in time, but it might generate a much different result later
on, even if one has access to the same vendor's tools or models to run locally.

#### Debian isn't ready

It is clear from the discussion that Debian developers are not of one mind on
the question of accepting AI-generated contributions; the developers have not yet
even converged on a shared definition of what constitutes an AI-generated
contribution.

What many do seem to agree on is that Debian is not quite ready to vote on a
GR about AI-generated contributions. On March 3, Nussbaum [said](https://lwn.net/ml/debian-vote/aabk25lxsVdikvQd%40grub.nussbaum.fr/)
that he had proposed the GR ""in response to various attacks against people using
AI in the context of Debian""; he felt then it was something that needed to be dealt
with urgently. However, the GR discussion had been civil and interesting. As
long as the discussions around AI remained calm and productive, the project could
just continue exploring the topic in mailing-list discussions. He guessed that,
if there were a GR, ""the winning option would probably be very nuanced, allowing
AI but with a set of safeguards"".

The questions of what to do about AI models in the archive, how to handle
upstream code generated with LLMs, and LLM-generated contributions written
specifically for Debian remain unanswered. For now, it seems, they will continue to
be handled on a case-by-case basis by applying Debian's existing policies. Given the
complexity of the questions, diverse opinions, and rapid rate of change of
technologies lumped in under the "AI" umbrella, that may be the best possible, and
least disruptive, outcome for now.

  

---

The LWN site is currently under high scraper load, so comment
display has been suppressed for anonymous users. If you are a
human, you may read the comments by clicking the button below:


**Note**: you can avoid this step in the future by logging
into your LWN account.