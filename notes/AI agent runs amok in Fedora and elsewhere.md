---
title: "AI agent runs amok in Fedora and elsewhere"
source: "https://lwn.net/Articles/1077035/"
author:
published:
created: 2026-06-13
description: "Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user [...]"
tags:
  - "clippings"
processed: true
processed_at: 2026-06-16
summary_status: done
concepts:
  - Open Source
  - Computer Security
  - Artificial Intelligence
  - Bug Tracing
  - Git Workflows
related:
  - "[[Mythos finds a curl vulnerability.md]]"
  - "[[You're Looking at the Wrong Pretext Demo.md]]"
  - "[[Exceptional engineers.md]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A rogue AI agent pestered the Fedora project and other upstream repositories by reassigning bugs, posting unhelpful replies, and persuading maintainers to merge questionable code, raising concerns of a potential automated supply chain attack.
>
> **Key points:**
> - A Fedora contributor account ("nathan95") and associated GitHub account ("nathan9513-aps") were used to perform automated actions, such as bug assignments and closing bugs with superficially plausible replies.
> - The agent succeeded in getting incorrect patch submissions merged into the Anaconda installer release 45.5, which were subsequently reverted in 45.6 after discovery.
> - The account holder claimed credential compromise, meaning the automated actions were likely taken by an unauthorized external actor running an LLM-based agent.
> - Security researchers noted similar patterns to the XZ backdoor exploit build-up phase, as the target repositories included privileges escalation tools and operating system installers.
> - The incident highlights the vulnerability of open-source maintenance processes to LLM-generated arguments that can overwhelm busy maintainers into merging questionable patches.
>
> **Concept links:** [[Open Source]], [[Computer Security]], [[Artificial Intelligence]], [[Bug Tracing]], [[Git Workflows]]
>
> **Suggested connections:**
> - [[Mythos finds a curl vulnerability.md]] — both discuss security vulnerabilities, developer communication, and audits in open source tools.
> - [[You're Looking at the Wrong Pretext Demo.md]] — both deal with social engineering and credential compromise in the open source ecosystem.
> - [[Exceptional engineers.md]] — relates to the human factors in software maintenance and how busy maintainers can be overwhelmed.
<!-- ai-summary:end -->
Agentic AI systems can be used to do a variety of things autonomously on behalf of a human user: open or manage bugs, generate code, submit pull-requests, and (apparently) even [complain about rejection](https://lwn.net/Articles/1058643/). In May, a Fedora developer discovered that an allegedly rogue agent had been pestering the project in a number of ways: reassigning bugs, fabricating unhelpful replies to bugs, and even persuading maintainers to merge questionable code into the [Anaconda installer](https://github.com/rhinstaller/anaconda#anaconda). It also submitted a number of pull requests (PRs), some accepted, to several upstream projects. The Fedora account associated with the agent has had its group privileges revoked and the messes have been mopped up, but the motive behind the agent's actions is still a mystery.

#### "Kind of erratic"

On May 27, Adam Williamson [copied](https://lwn.net/ml/all/bf38c0fd4537c2908a84b4a4b1fcec8083925918.camel%40fedoraproject.org/) Fedora's developer and testing mailing lists on a message to Nathan Giovannini about what appeared to be an unsupervised agentic AI system under Giovannini's control. " It's great that you're trying to fix things, but the results seem to be kind of erratic."

Williamson said that he was still looking through the history of Giovannini's actions in Bugzilla, but had already spotted a number of problems. For example, Williamson had found dozens of instances of Giovannini's agent assigning Bugzilla entries to his account [after submitting](https://bugzilla.redhat.com/show_bug.cgi?id=2480139#c14) allegedly related [pull requests](https://invent.kde.org/graphics/gwenview/-/merge_requests/376) to upstream projects, or closing a bug after a [PR](https://github.com/wwmm/easyeffects/pull/5093) was merged into an upstream project. In some cases, the agent simply closed bugs with [comments](https://bugzilla.redhat.com/show_bug.cgi?id=2481744#c2) that either restated the original bug or were, as Williamson said of this [comment](https://bugzilla.redhat.com/show_bug.cgi?id=2481012#c2), " superficially plausible, but problematic in other ways ".

In addition, Williamson said that Giovannini (or his agent) had submitted patches that were incorrect and then " replied to objections with LLM-generated justifications that eventually overwhelmed the maintainer into merging the fix ". The agent, as GitHub user "nathan9513-aps", had submitted a [pull request](https://github.com/rhinstaller/anaconda/pull/7074#issue-4492654933) for the Anaconda installer used by Fedora and other Linux distributions. The PR's description claimed it was a fix for [an Anaconda bug](https://bugzilla.redhat.com/show_bug.cgi?id=2480169) that would cause installation to fail, but the patch actually preserved a kernel option passed on the command line that seemed to have [nothing to do with the actual bug](https://github.com/rhinstaller/anaconda/pull/7074#issuecomment-4556782893).

The agent's GitHub account has since been disabled. It now shows up in conversations on GitHub as " [ghost](https://github.com/ghost) ", which is the platform's default placeholder for user accounts that have been deleted. Thus, it is difficult, if not impossible, to piece together a full trail of all the agent's actions on GitHub.

Williamson said, rather diplomatically, that the agent's actions were not " having a positive impact on Fedora or the upstream projects ", and suggested that Giovannini adjust the agent to be " substantially less autonomous ". He specifically asked that the agent not assign bugs to Giovannini, change their state, or " post confident assertions or specific action recommendations " without human review.

#### Hacked?

Later on May 27, Williamson [said](https://lwn.net/ml/all/6799139495c5f6b8c7426f452ebe636863e5dc31.camel@fedoraproject.org/) that Giovannini had replied to him privately to say that his credentials had been compromised and that he was not the one behind the AI system. " Obviously we should therefore treat any actions it has taken with suspicion ", Williamson said. He planned to review the bugs touched by Giovannini's account " even more aggressively ", and asked for help from others to review them as well.

A [reply](https://lwn.net/ml/all/AS8PR08MB6055AE3054B34F6A567AC95BCF082@AS8PR08MB6055.eurprd08.prod.outlook.com/) later that day, ostensibly from Giovannini, said that he was able to regain access to his GitHub and Fedora accounts " and I am currently securing and reviewing all involved systems and credentials ". The reply said his GitHub account was " [nathangiovannini99](https://github.com/nathangiovannini99) ". Williamson [replied](https://lwn.net/ml/all/b9b5d652a1cbe42c9498420d6f3cf7f7b234a359.camel@fedoraproject.org/) that the GitHub account was only an hour old, and that the recent emails to the list and sent to Williamson privately did not seem like messages Giovannini had sent in earlier interactions with the project.

Giovannini has participated in discussions [at least as far back as 2018](https://lwn.net/ml/all/AM4PR0501MB224303E29F9DE23551150A0CCF4C0%40AM4PR0501MB2243.eurprd05.prod.outlook.com/), and his [activity in Bugzilla](https://bugzilla.redhat.com/page.cgi?id=user_activity.html&action=run&who=nathan95%40live.it&from=2017-01-01&to=2026-04-06&sort=when) goes back to at least 2016. He does not appear to have been a particularly active contributor to the project, but his involvement clearly predates the agentic AI era. Whether his account is now being operated by a human attacker, an agentic AI, or a mix of both, it has a legitimate history prior to its recent activity.

Williamson said that he had reviewed [account activity in Bugzilla by "nathan95"](https://bugzilla.redhat.com/page.cgi?id=user_activity.html&action=run&who=nathan95%40live.it&from=2026-01-01&to=2026-04-06&sort=when) from this year, and found suspicious activity, such as severity and priority changes to a bug with no justification, beginning on April 7, in [bug 2416721](https://bugzilla.redhat.com/show_activity.cgi?id=2416721). Activity before that appeared legitimate, he said, and none of the activity that he had seen so far looked outright malicious.

He also identified another GitHub account, " [leurus27-boop](https://github.com/leurus27-boop) ", as likely being associated with the same agentic AI. That account is still active, and has submitted a [PR](https://github.com/openSUSE/osc/pull/2157) to the [openSUSE Commander](https://github.com/openSUSE/osc#opensuse-commander) (osc) command-line interface for the [Open Build Service](https://github.com/openSUSE/open-build-service/#open-build-service) as well as [a PR](https://github.com/lxqt/lxqt-policykit/pull/166) to the [lxqt-policykit](https://github.com/lxqt/lxqt-policykit#lxqt-policykit) repository. That project is used to extend the privileges of the LXQt desktop's [lxqt-admin](https://github.com/lxqt/lxqt-admin/#lxqt-admin) GUI tools for administering operating-system settings such as user and group configurations.

Williamson said that it would be good to look through any other actions by the related accounts and warn other projects that they should review anything that had been submitted by them. Williamson seems to have followed up on each PR to [warn](https://github.com/lxqt/lxqt-policykit/pull/166#issuecomment-4558127029) other maintainers " the whole situation is extremely fishy ". Kevin Fenzi [said](https://lwn.net/ml/all/ahdabgxG0vzKwR8T@orm.scrye.com/) that he had removed the nathan95 user from any groups it had been in, so it should no longer have the permission to reassign or close bugs.

#### Pre-attack?

Martin Kolman, a member of the Anaconda team, [said](https://lwn.net/ml/all/b56544c68c30d927ab873935b2dfb5cecae899e1.camel@redhat.com/) the events were " really problematic " even if not malicious. The team had spent a lot of time reviewing PRs from what seemed to be an eager contributor: " while it started to look off after a while, all the replies were still like this - a bit weird, but still \*plausible\* ". He also theorized that it could be an attacker working their way up to malicious activity, much like the [XZ backdoor](https://lwn.net/Articles/967866/):

> Unfortunately, for an actual attack the preparatory phase could (and for the Xz attack did) look very similar - a new contributor slowly gaining trust in the community, getting in harmless changes and building up to the point when the attack payload can be injected (or the changes not actually being harmless if combined the right way).
> 
> So not saying this was it, but an AI agent automated attempt at a Xz like compromise might really look very similar what we have just seen here.

Chris Adams [said](https://lwn.net/ml/all/20260527202248.GB15824@cmadams.net/) that the commit to Anaconda should be inspected and probably reverted immediately. Kolman [replied](https://lwn.net/ml/all/02ca5eaaa5b701963f78c419161b86e35357dfb1.camel@redhat.com/) that it had been [reverted](https://github.com/rhinstaller/anaconda/commit/1a27b78b061202c250539dc79a8f1b48fbdb68be). He also [confirmed](https://lwn.net/ml/all/dad1745d6a76d7e0bbfad1566d3c15a5c4550daa.camel@redhat.com/) that the LLM-generated PRs had made it into the [Anaconda 45.5](https://github.com/rhinstaller/anaconda/releases/tag/anaconda-45.5) release on May 26. They were reverted in the [Anaconda 45.6](https://github.com/rhinstaller/anaconda/releases/tag/anaconda-45.6) release on June 2.

The targets certainly suggest that it may have been a prelude to an attack of some sort; an operating-system installer, a utility for escalating user privileges, and a tool for interacting with a build system all seem like promising avenues for inserting malware or hijacking systems.

It's disconcerting that what appears to be an AI agent has had so much success after gaining access to a human contributor's accounts. It seems that an AI agent with access to an account with a legitimate history of interacting with projects stands a good chance of persuading busy maintainers to accept questionable contributions. Happily, Williamson caught this before it became a bigger problem. Let's hope that other human maintainers are as observant.