---
title: "AI agent runs amok in Fedora and elsewhere [LWN.net]"
url: https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/
clipped: 2026-08-31 12:26:30
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [AI agent runs amok in Fedora and elsewhere [LWN.net]](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

## Full Article

[LWN.net
            News from the source](https://lwn.net/)
            
           
        
- [Content](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/#t)
- [Weekly Edition](https://lwn.net/current/)
- [Archives](https://lwn.net/Archives/)
- [Search](https://lwn.net/Search/)
- [Kernel](https://lwn.net/Kernel/)
- [Security](https://lwn.net/Security/)
- [Events calendar](https://lwn.net/Calendar/)
- [Unread comments](https://lwn.net/Comments/unread)
- 
- [LWN FAQ](https://lwn.net/op/FAQ.lwn)
- [Write for us](https://lwn.net/op/AuthorGuide.lwn)

- [Edition](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/#t)
- [Return to the Front page](https://lwn.net/Articles/1076255/)

 

        User:  
		Password:    |
           
           
            |
           
           
           
        
               
               [Log in](https://lwn.net/Login/) /
               [Subscribe](https://lwn.net/subscribe/) /
               [Register](https://lwn.net/Login/newaccount)
               
               

# AI agent runs amok in Fedora and elsewhere

Did you know...?

LWN.net is a subscriber-supported publication; we rely on subscribers
       to keep the entire operation going.  Please help out by [buying a subscription](https://lwn.net/Promo/nst-nag4/subscribe) and keeping LWN on the
       net.

           By Joe BrockmeierJune 10, 2026
           

Agentic AI systems can be used to do a variety of things
autonomously on behalf of a human user: open or manage bugs, generate
code, submit pull-requests, and (apparently) even [complain about
rejection](https://lwn.net/Articles/1058643/). In May, a Fedora developer discovered that an allegedly
rogue agent had been pestering the project in a number of ways:
reassigning bugs, fabricating unhelpful replies to bugs, and even
persuading maintainers to merge questionable code into the [Anaconda
installer](https://github.com/rhinstaller/anaconda#anaconda). It also submitted a number of pull requests (PRs),
some accepted, to several upstream projects. The Fedora account
associated with the agent has had its group privileges revoked and the
messes have been mopped up, but the motive behind the agent's actions is still
a mystery.

#### "Kind of erratic"

On May 27, Adam Williamson [copied](https://lwn.net/ml/all/bf38c0fd4537c2908a84b4a4b1fcec8083925918.camel%40fedoraproject.org/)
Fedora's developer and testing mailing lists on a message to Nathan
Giovannini about what appeared to be an unsupervised agentic AI system
under Giovannini's control. "It's great that you're trying to fix
things, but the results seem to be kind of erratic."

Williamson said that he was still looking through the history of
Giovannini's actions in Bugzilla, but had already spotted a number of
problems. For example, Williamson had found dozens of instances of
Giovannini's agent assigning Bugzilla entries to his account [after submitting](https://bugzilla.redhat.com/show_bug.cgi?id=2480139#c14) allegedly related
[pull
requests](https://invent.kde.org/graphics/gwenview/-/merge_requests/376) to upstream projects, or closing
a bug after a [PR](https://github.com/wwmm/easyeffects/pull/5093) was merged
into an upstream project. In some cases, the agent simply closed bugs
with [comments](https://bugzilla.redhat.com/show_bug.cgi?id=2481744#c2)
that either restated the original bug or were, as Williamson said of
this [comment](https://bugzilla.redhat.com/show_bug.cgi?id=2481012#c2),
"superficially plausible, but problematic in other ways".

In addition, Williamson said that Giovannini (or his agent) had
submitted patches that were incorrect and then "replied to
objections with LLM-generated justifications that eventually
overwhelmed the maintainer into merging the fix". The agent, as
GitHub user "nathan9513-aps", had
submitted a [pull
request](https://github.com/rhinstaller/anaconda/pull/7074#issue-4492654933) for the Anaconda
installer used by Fedora and other Linux distributions. The PR's
description claimed it was a fix for [an Anaconda
bug](https://bugzilla.redhat.com/show_bug.cgi?id=2480169) that would cause installation to fail, but the patch actually
preserved a kernel option passed on the command line that seemed to
have [nothing
to do with the actual bug](https://github.com/rhinstaller/anaconda/pull/7074#issuecomment-4556782893).

The agent's GitHub account has since been disabled. It now shows up in
conversations on GitHub as "[ghost](https://github.com/ghost)", which is the platform's
default placeholder for user accounts that have been deleted. Thus, it
is difficult, if not impossible, to piece together a full trail of all
the agent's actions on GitHub.

Williamson said, rather diplomatically, that the agent's actions were not
"having a positive impact on Fedora or the upstream projects",
and suggested that Giovannini adjust the agent to be "substantially
less autonomous". He specifically asked that the agent not assign
bugs to Giovannini, change their state, or "post confident
assertions or specific action recommendations" without human
review.

#### Hacked?

Later on May 27, Williamson [said](https://lwn.net/ml/all/6799139495c5f6b8c7426f452ebe636863e5dc31.camel@fedoraproject.org/)
that Giovannini had replied to him privately to say that his
credentials had been compromised and that he was not the one behind
the AI system. "Obviously we should therefore treat any actions it
has taken with suspicion", Williamson said. He planned to review
the bugs touched by Giovannini's account "even more
aggressively", and asked for help from others to review them as
well.

A [reply](https://lwn.net/ml/all/AS8PR08MB6055AE3054B34F6A567AC95BCF082@AS8PR08MB6055.eurprd08.prod.outlook.com/)
later that day, ostensibly from Giovannini, said that he was able to
regain access to his GitHub and Fedora accounts "and I am currently
securing and reviewing all involved systems and credentials". The reply 
said his GitHub account was "[nathangiovannini99](https://github.com/nathangiovannini99)". Williamson
[replied](https://lwn.net/ml/all/b9b5d652a1cbe42c9498420d6f3cf7f7b234a359.camel@fedoraproject.org/)
that the GitHub account was only an hour old, and that the recent
emails to the list and sent to Williamson privately did not seem like
messages Giovannini had sent in earlier interactions with the
project.

Giovannini has participated in discussions [at
least as far back as 2018](https://lwn.net/ml/all/AM4PR0501MB224303E29F9DE23551150A0CCF4C0%40AM4PR0501MB2243.eurprd05.prod.outlook.com/), and his [activity
in Bugzilla](https://bugzilla.redhat.com/page.cgi?id=user_activity.html&action=run&who=nathan95%40live.it&from=2017-01-01&to=2026-04-06&sort=when) goes back to at least 2016. He does not appear to
have been a particularly active contributor to the project, but his
involvement clearly predates the agentic AI era. Whether his account
is now being operated by a human attacker, an agentic AI, or a mix of
both, it has a legitimate history prior to its recent activity.

Williamson said that he had reviewed [account
activity in Bugzilla by "nathan95"](https://bugzilla.redhat.com/page.cgi?id=user_activity.html&action=run&who=nathan95%40live.it&from=2026-01-01&to=2026-04-06&sort=when) from this year, and found
suspicious activity, such as severity and priority changes to a bug with no
justification, beginning on April 7, in [bug
2416721](https://bugzilla.redhat.com/show_activity.cgi?id=2416721). Activity before that appeared legitimate, he said, and
none of the activity that he had seen so far looked outright
malicious.

He also identified another GitHub account, "[leurus27-boop](https://github.com/leurus27-boop)", as likely
being associated with the same agentic AI. That account is still
active, and has submitted a [PR](https://github.com/openSUSE/osc/pull/2157) to the [openSUSE
Commander](https://github.com/openSUSE/osc#opensuse-commander) (osc) command-line interface for the [Open
Build Service](https://github.com/openSUSE/open-build-service/#open-build-service) as well as [a PR](https://github.com/lxqt/lxqt-policykit/pull/166) to the
[lxqt-policykit](https://github.com/lxqt/lxqt-policykit#lxqt-policykit)
repository. That project is used to extend the privileges of the LXQt
desktop's [lxqt-admin](https://github.com/lxqt/lxqt-admin/#lxqt-admin)
GUI tools for administering operating-system settings such as user and
group configurations.

Williamson said that it would be good to look
through any other actions by the related accounts and warn other
projects that they should review anything that had been submitted by
them. Williamson seems to have followed up on each PR to [warn](https://github.com/lxqt/lxqt-policykit/pull/166#issuecomment-4558127029)
other maintainers "the whole situation is extremely
fishy". Kevin Fenzi [said](https://lwn.net/ml/all/ahdabgxG0vzKwR8T@orm.scrye.com/)
that he had removed the nathan95 user from any groups it had been in,
so it should no longer have the permission to reassign or close
bugs.

#### Pre-attack?

Martin Kolman, a member of the Anaconda team, [said](https://lwn.net/ml/all/b56544c68c30d927ab873935b2dfb5cecae899e1.camel@redhat.com/)
the events were "really problematic" even if not malicious. The
team had spent a lot of time reviewing PRs from what seemed to be an
eager contributor: "while it started to look off after a while, all
the replies were still like this - a bit weird, but still
*plausible*". He also theorized that it could be an attacker
working their way up to malicious activity, much like the [XZ backdoor](https://lwn.net/Articles/967866/):

Unfortunately, for an actual attack the preparatory phase could (and
for the Xz attack did) look very similar - a new contributor slowly
gaining trust in the community, getting in harmless changes and
building up to the point when the attack payload can be injected (or
the changes not actually being harmless if combined the right way).

So not saying this was it, but an AI agent automated attempt at a Xz
like compromise might really look very similar what we have just seen
here.

Chris Adams [said](https://lwn.net/ml/all/20260527202248.GB15824@cmadams.net/)
that the commit to Anaconda should be inspected and probably reverted
immediately. Kolman [replied](https://lwn.net/ml/all/02ca5eaaa5b701963f78c419161b86e35357dfb1.camel@redhat.com/)
that it had been [reverted](https://github.com/rhinstaller/anaconda/commit/1a27b78b061202c250539dc79a8f1b48fbdb68be). He
also [confirmed](https://lwn.net/ml/all/dad1745d6a76d7e0bbfad1566d3c15a5c4550daa.camel@redhat.com/)
that the LLM-generated PRs had made it into the [Anaconda 45.5](https://github.com/rhinstaller/anaconda/releases/tag/anaconda-45.5)
release on May 26. They were reverted in the [Anaconda 45.6](https://github.com/rhinstaller/anaconda/releases/tag/anaconda-45.6)
release on June 2.

The targets certainly suggest that it may have been a prelude to an
attack of some sort; an operating-system installer, a utility for escalating
user privileges, and a tool for interacting with a build system all
seem like promising avenues for inserting malware or hijacking
systems.

It's disconcerting that what appears to be an AI agent has had so
much success after gaining access to a human contributor's accounts.
It seems that an AI agent with access to an account with a legitimate
history of interacting with projects stands a good chance of
persuading busy maintainers to accept questionable
contributions. Happily, Williamson caught this before it became a
bigger problem. Let's hope that other human maintainers are as
observant.

            
            
             to post comments
            

        

    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 16:06 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077407/)] (17 responses)
      
      
      
      
      
> It also submitted a number of pull requests (PRs), some accepted, to several upstream projects.

It would be very interesting to see a link to at least some of those PRs, especially the accepted ones.

Do we need to worry?

      
          
            
            
            
          
        
     

     
    
    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 16:13 UTC (Wed)
                               by jzb (editor, #7867)
                              [[Link](https://lwn.net/Articles/1077408/)] (15 responses)
      
      
      
      
      

I did link to the PRs for OSC and LXQt.

 Do we need to worry?

Well... I am. But I might be a bit paranoid.

      
          
            
            
            
          
        
     

     
    
    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 16:20 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077410/)] (14 responses)
      
      
      
      
      
> I did link to the PRs for OSC and LXQt.

Yup; sorry.  I didn't find any in the text near that, nor with a search of keywords like "merged" and "accepted".  But I've found some after carefully reading.

>> Do we need to worry?

> Well... I am. But I might be a bit paranoid.

Yup; me too.  I'm kind of between being worried, and thinking this was obviously predictable and thus negligence.  That's why I plan moving to vim-classic as soon as possible, and similar stuff, and also why I don't accept any LLM-poisoned contributions.

      
          
            
            
            
          
        
     

     
    
    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 16:28 UTC (Wed)
                               by jzb (editor, #7867)
                              [[Link](https://lwn.net/Articles/1077411/)] (1 responses)
      
      
      
      
      
That's helpful feedback; I'll work on being extra-extra-clear on those kinds of links next time around... 

      
          
            
            
            
          
        
     

     
    
    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 16:32 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077412/)] 
      
      
      
      
      
Nice!  :-)

      
          
            
            
            
          
        
     

     
    

    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 18:43 UTC (Wed)
                               by Wol (subscriber, #4433)
                              [[Link](https://lwn.net/Articles/1077415/)] (11 responses)
      
      
      
      
      
> and also why I don't accept any LLM-poisoned contributions.

Just because you're paranoid, doesn't mean they're not out to get you.

And how, anyway, do you plan to avoid - "LLM-poisoned" as you call them - contributions? I get the impression these "slipped through the net" because they came from hijacked accounts (or from human accounts with dodgy motives) and didn't ring alarm bells.

What we *need* is a human "in the loop" at all times. What we're getting is - as the title puts it - "agents running amok" and overwhelming the humans. Who's to say *you* won't be taken in?

Cheers,
Wol

      
          
            
            
            
          
        
     

     
    
    
      

### Triaging LLM-poisoned or other malicious activity

      
      

 Posted Jun 10, 2026 19:46 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077426/)] (10 responses)
      
      
      
      
      
> Just because you're paranoid, doesn't mean they're not out to get you.

I remain alerted.

> And how, anyway, do you plan to avoid - "LLM-poisoned" as you call them - contributions?

The first measure is to disallow anything that has touched an LLM in the slightest way.  The actual specification is:

|	It is expressly forbidden to contribute to this project any
|	content that has been created or derived with the assistance of
|	AI tools.
|
|	This includes AI assistive tools used in the contributing
|	process, even if such tools do not directly generate the
|	contributed code but are used to derive the contribution.  For
|	example, AI linters, AI static analyzers, and AI tools that
|	summarize input are forbidden.

This already removes a large amount of LLM-poisoned contributions.  That keeps the amount of contributions to reasonable levels.

Then, we can group contributors in 4 categories:

-  Those that are unaware of the policy, and publicly disclose use of LLMs.
-  Those that are unaware of the policy, and don't say anything about using AI.
-  Those that are aware of the policy, and comply with it.
-  Those that are aware of the policy, and don't comply with it.

Most fall under the 3rd category.  Between 1st and 2nd category, usually, more competent programmers tend to be on the 1st category, and the least competent/experienced ones might be on the 2nd category.

This is nice, because it's easy to spot inexperienced programmers after a few emails; once I suspect that they're inexperienced and that they might have violated it or if they've done something else wrong, I point them to the contributing guidelines (not the AI policy, but the entire contributing policy, so that they don't feel offended), just asking them to check them for a revision of their contribution.  If they are benevolent, they'll easily find the AI guidelines and tell me they used AI, and then we figure out how to proceed (e.g., discard the patch, and start from scratch).

That leaves us with the 4th category.

Because the amount of contributions are at reasonable levels, I have the time and energy to actually interact with contributors enough to have them talk quite a bit.  Once you talk for a while with contributors, you can get a sense of whether they talk like humans, and whether they understand and can defend their contributions in discussion.

Common suspicious things are:

-  The contributor suddenly changes little details from one version of a patch to the next, without being able to justify them (and often being completely silent about it).
-  The patch contained more code than necessary for the change, and can't justify the extra code.
-  Entirely ignoring some important feedback.

The more alarms ring in my head, the more picky I'm with a contributor.  After all, they are the ones to prove that the contribution is correct; I should not be reviewing their code, but rather help them review it for me.

At the moment, I don't think an LLM can pass this without triggering alarms; maybe in the future they improve enough, but we'll see.

Maybe for small contributions (one-liners), LLMs may have larger success rate with this filter, but those are less important.  I don't expect significant contributions that are LLM-poisoned (in a significant amount) to pass it.  It's not a matter of being perfectly clean of LLM-poisoned contributions (and it's mostly impossible, just like low-background steel); it's a matter of filtering enough to be safe.

> I get the impression these "slipped through the net" because they came from hijacked accounts (or from human accounts with dodgy motives) and didn't ring alarm bells.

I think a benefit of email-based patches is that the hijacked account will often receive a copy of the email even if they have been hijacked, while accounts in pages might be more difficult to spot.  If I send an email to Respected Developer replying to a patch that it sent, it will probably receive a copy of my response, and if it didn't write to me, it will probably suspect something's wrong.  And if they don't receive any emails at all, they'll also suspect.

Anyway, I keep the mental filter from above enabled for old programmers too, because these days many old programmers also use LLMs.

If there's an old programmer that is a frequent trusted contributor, I will actually disable my mental filter.  However, I expect I would be able to distinguish the way they talk (precisely because I talk to them frequently), and if they're hijacked, I expect I'd at least suspect something.

Not perfect, but it works for me.

      
          
            
            
            
          
        
     

     
    
    
      

### LLMs can find real bugs

      
      

 Posted Jun 10, 2026 20:02 UTC (Wed)
                               by DemiMarie (subscriber, #164188)
                              [[Link](https://lwn.net/Articles/1077430/)] (6 responses)
      
      
      
      
      
LLMs can and have found real bugs, including security vulnerabilities.  The human reporter needs to filter out hallucinations, but a substantial fraction of the findings are often genuine.

      
          
            
            
            
          
        
     

     
    
    
      

### LLMs can find real bugs

      
      

 Posted Jun 10, 2026 20:59 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077432/)] (5 responses)
      
      
      
      
      
> LLMs can and have found real bugs, including security vulnerabilities. The human reporter needs to filter out hallucinations, but a substantial fraction of the findings are often genuine.

I guess it depends on several factors:

-  Age of the project.
-  Quality of the source code.
-  Number of users of the project.
-  Frequency of feature additions.

As co-maintainer of a project that is very old (and thus, most bugs have been vetted), has very simple and robust C code, is used almost everywhere, and has few new features, I'm seeing a very low number of LLM-based reports, and only one has been useful so far (it reports a yet-unreleased bug we introduced while adding a new feature recently).

Since this is not law, but rather guidelines, we could of course make an exception if we see a report that is useful enough.  I've made this one exception so far, because it was trivial.  However, I expect that if we didn't have that report, we'd have caught the bug within hours or a few days from users trying the release candidates or even from users of the release in bleeding-edge distros if it wasn't caught in the -rc, as has happened usually with previous releases.

Interestingly, we haven't seen the flood of reports that have affected many projects (and I suspect we're a juicy target for people to find vulnerabilities, so it's probably not a lack of interest).

      
          
            
            
            
          
        
     

     
    
    
      

### LLMs can find real bugs

      
      

 Posted Jun 10, 2026 21:34 UTC (Wed)
                               by NYKevin (subscriber, #129325)
                              [[Link](https://lwn.net/Articles/1077435/)] (1 responses)
      
      
      
      
      
> I'm seeing a very low number of LLM-based reports, and only one has been useful so far (it reports a yet-unreleased bug we introduced while adding a new feature recently).

Couldn't that be a result of people respecting your contribution policy (that you quoted upthread), which explicitly prohibits contributing such reports to the project? If so, I'm not sure it provides any useful data on whether LLMs in general are capable of finding security vulnerabilities (or other problems) in your code.

      
          
            
            
            
          
        
     

     
    
    
      

### LLMs can find real bugs

      
      

 Posted Jun 10, 2026 21:44 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077436/)] 
      
      
      
      
      
I've published that policy in one project, but on the other one we haven't merged it yet (it's waiting for review of one co-maintainer).  While regular contributors are aware of it (since we've discussed it at length), passing-by contributors have certainly not read it.

      
          
            
            
            
          
        
     

     
    

    
      

### LLMs can find real bugs

      
      

 Posted Jun 11, 2026 13:46 UTC (Thu)
                               by DemiMarie (subscriber, #164188)
                              [[Link](https://lwn.net/Articles/1077458/)] (2 responses)
      
      
      
      
      
I think you can filter out the false positives by requiring a complete reproducer.   LLMs are pretty good at that nowadays, and since the reproducer won’t become part of the codebase there are no copyright concerns.  This is especially true if the reproducer triggers a crash or sanitizer error.

Reproducing a race condition reliably can require a source code patch to add delays.  Those are more common in projects like the Linux kernel, though.  A man page viewer probably won’t have those.

      
          
            
            
            
          
        
     

     
    
    
      

### LLMs can find real bugs

      
      

 Posted Jun 11, 2026 14:48 UTC (Thu)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077590/)] 
      
      
      
      
      
That doesn't do anything to address the ethical concerns.

Also, my filter is easier to implement, requires less work from the maintainers, and moves the burden to the contributor, which also means that if a malicious actor wants to attack us, it will have to do more work for it to work, possibly deciding to attack a different project.

I just don't see why I'd want to do that.

      
          
            
            
            
          
        
     

     
    

    
      

### LLMs can find real bugs

      
      

 Posted Jun 11, 2026 14:52 UTC (Thu)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077591/)] 
      
      
      
      
      
> A man page viewer probably won’t have those.

I also co-maintain other projects, such as shadow-utils.  But even there, I haven't seen LLMs report useful stuff (except for the one exception I mentioned above, and which I expect would have been found by a human anyway once we do the -rc pre-release).  It's true that it's a set of single-threaded programs, which makes them inherently simpler than the kernel, though.

      
          
            
            
            
          
        
     

     
    

    
      

### Triaging LLM-poisoned or other malicious activity

      
      

 Posted Jun 11, 2026 6:49 UTC (Thu)
                               by NAR (subscriber, #1313)
                              [[Link](https://lwn.net/Articles/1077445/)] (2 responses)
      
      
      
      
      
I guess it works until you have maybe a dozen regular and a few drive-by contributors. Neither is true for a project like Fedora. Also, a malicious actor (which might be behind this activity) won't care about the no-LLM policy, so it doesn't really matter.

      
          
            
            
            
          
        
     

     
    
    
      

### Triaging LLM-poisoned or other malicious activity

      
      

 Posted Jun 11, 2026 13:30 UTC (Thu)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1077571/)] 
      
      
      
      
      
More importantly a malicious actor narrowly targeting a specific project doesn't need an LLM to achieve the same result. An LLM might make it a bit simpler to scale this up to many projects but on an individual project level posing as a minor contributor for a while is quite feasible manually too.

      
          
            
            
            
          
        
     

     
    

    
      

### Triaging LLM-poisoned or other malicious activity

      
      

 Posted Jun 11, 2026 14:28 UTC (Thu)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077589/)] 
      
      
      
      
      
If malicious actors use LLMs, I'm thankful to them, because that makes them easier to identify.  I haven't yet seen an LLM that could not be detected after consistent engagement.

An LLM-using contributor I can always trust to be dishonest.  Honestly, it's the humans that I am worried about, because you can never predict when they're going to do something incredibly... malicious.  :)

      
          
            
            
            
          
        
     

     
    

    
      

### Merged PR in upstream projects

      
      

 Posted Jun 10, 2026 16:14 UTC (Wed)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1077409/)] 
      
      
      
      
      
Oh, here's one: <[https://github.com/rhinstaller/anaconda/pull/7074#issue-4...](https://github.com/rhinstaller/anaconda/pull/7074#issue-4492654933)> (linked under "Kind of erratic").

      
          
            
            
            
          
        
     

     
    

    
      

### Fighting fire with fire

      
      

 Posted Jun 10, 2026 20:08 UTC (Wed)
                               by capn (subscriber, #183548)
                              [[Link](https://lwn.net/Articles/1077429/)] (1 responses)
      
      
      
      
      
Interesting that AI has doubled the number of CVEs detected in human written code in the past year, but when an AI causes a problem itself, people cry bloody murder.

Now, naive enthusiasts using AI tools are a legitimate problem right now. In defense of the overeager minority, people are still in the early days of learning these new tools, and the first taste of them leaves many engineers a bit... overenthusiastic, perhaps. It's also important to remember that tools like Copilot are kept significantly behind in terms of model generations. And, in the general case as well, many cash-starved engineers turn to the much lower end, and older, models to automate things (which is obviously a rude thing to do when contributing code or other activity to an org that doesn't have them on their payroll, or hire list, and has no meaningful recourse).

But, just as the landscape of the tools used to write and participate in coding projects are changing, the projects themselves must adapt to the times and embrace the new tools available for triage and code review. They can (and will) drastically reduce the load that the increased amount of activity has put on maintainers. (And, no, some briefly-considered top-of-the-head flaw in this concept of significant automation of triage and review is not fatal. We're engineers, and solving problems in such processes is basically the profession.)

There is far too much seeing the glass a quarter empty, rather than seeing it three quarters full.

This is the kind of fire that we can fight with the exact same type of fire. And I'm greatly looking forward to seeing just how hot the progress of open source software can get.

      
          
            
            
            
          
        
     

     
    
    
      

### Fighting fire with fire

      
      

 Posted Jun 11, 2026 12:31 UTC (Thu)
                               by Wol (subscriber, #4433)
                              [[Link](https://lwn.net/Articles/1077434/)] 
      
      
      
      
      
> Interesting that AI has doubled the number of CVEs detected in human written code in the past year, but when an AI causes a problem itself, people cry bloody murder.

The difference is that a human makes maybe a couple of mistakes a month (that actually make it into released code). What was that incident recently where Claude was filing PRs at the rate of a couple every second, creating serious security problems!?

When a human makes a mistake, it's fairly easy to clean up. When an AI makes a mistake it's a nightmare to clean up, it's everywhere!

> There is far too much seeing the glass a quarter empty, rather than seeing it three quarters full.

The trouble with Agentic AI, it's three-quarters full of the brown stuff you need a paddle to deal with.

> And I'm greatly looking forward to seeing just how hot the progress of open source software can get.

If we use AI as a servant, I would agree with you. But there are too many people bowing down to AI as their master. Therein lies disaster ...

Cheers,
Wol

      
          
            
            
            
          
        
     

     
    

    
      

### Credit where it's due

      
      

 Posted Jun 10, 2026 21:49 UTC (Wed)
                               by AdamW (subscriber, #48457)
                              [[Link](https://lwn.net/Articles/1077437/)] 
      
      
      
      
      
Ooh, I'm famous again.

"Happily, Williamson caught this before it became a bigger problem. Let's hope that other human maintainers are as observant."

To give credit where it's due: it was in fact Yanko Kaneti who first spotted this - he posted "[https://bugzilla.redhat.com/show_bug.cgi?id=2481872#c1](https://bugzilla.redhat.com/show_bug.cgi?id=2481872#c1)    ....wtf.. " in the fedora-devel room on Matrix. Kevin Fenzi flagged me (because Nathan is in the qa group) and I then took it from there and found all the other bugzilla posts, and pull requests.

To answer Joe's concerns to some extent - I did look through every PR I could find from the nathan9513-aps account before reporting it to GitHub, and didn't see any that looked outright malicious, just...incompetent. As you noticed, I commented on them all to try and alert the project maintainers to the situation. I think I checked all the leurus27-boop PRs at that time too (there aren't as many, the account was only created recently).

      
          
            
            
            
          
        
     

     
    

 
 

 

            
            
            

            
            Copyright © 2026, Eklektix, Inc.
            This article may be redistributed under the terms of the
              [Creative
              Commons CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/) license
            Comments and public postings are copyrighted by their creators.
            Linux  is a registered trademark of Linus Torvalds
