---
title: "Ageless Linux – Software for humans of indeterminate age"
url: https://agelesslinux.org/
clipped: 2026-06-17 01:32:32
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Ageless Linux – Software for humans of indeterminate age](https://agelesslinux.org/)

## Digest Summary
Ageless Linux is a minimal Linux “distribution” consisting of a bash script that edits /etc/os‑release to rename the system and installs a stub age‑verification API. It positions itself as an “operating system provider” under California’s AB 1043, which mandates age collection for child users and imposes civil penalties per “affected child.” The project argues that the law’s definitions are so broad that a simple script can trigger regulatory obligations, exposing volunteer Linux distributions to selective enforcement. Ageless Linux pledges to publish removal scripts or forks that strip age‑verification components (e.g., D‑Bus interfaces, AccountsService prompts) from other distributions if they implement such features. It offers two modes: a standard stub at /etc/ageless/age‑verification-api.sh that exits with an error, and a “flagrant” mode with no API. The maintainers claim the effort is not a legal defense but a test case to force clarification on whether a script qualifies as an operating‑system provider, whether devices like Raspberry Pi count as “general‑purpose computing devices,” and how “affected child” fines can be applied.

## Discussion Summary
Comments broadly criticize the California age‑verification mandate as unnecessary, intrusive and poorly suited to open‑source operating systems, arguing that parental controls or existing OS mechanisms should suffice. Many view the law as a product of lobbying and government overreach that threatens privacy and civil liberties, while some acknowledge the technical feasibility of a simple age flag but question its effectiveness and enforcement. A recurring theme is the tension between regulatory intent to protect minors and the tech community’s resistance to mandated compliance, with occasional calls for alternative, privacy‑preserving solutions.

---

## Full Article

FAQ
---

### Frequently Asked Questions

Q: Is Ageless Linux a real operating system?

It is as real as any operating system that identifies itself via
`/etc/os-release`. The law does not define minimum technical
thresholds for what constitutes an operating system. It defines an
"operating system provider" as anyone who "develops, licenses, or controls
the operating system software." We control the operating system software.
The operating system software says it's Ageless Linux. QED.

Q: Isn't this just Debian with a different name?

Isn't Ubuntu just Debian with a different name? Isn't Linux Mint just
Ubuntu with a different name? Isn't Pop!\_OS just Ubuntu with a different name?
The entire Linux distribution ecosystem is built on the premise that
modifying and redistributing an existing system creates a new distribution.
Each of these distributions is, under AB 1043, a separate operating system
provider with separate compliance obligations. There are over 600 active
Linux distributions. The California Attorney General's office may wish to
begin hiring.

Q: Is this really just a bash script that changes the name of the OS?

Right now, yes. A bash script that modifies `/etc/os-release`,
neutralizes the systemd userdb `birthDate` field, and installs
a refusal notice. That's the point â that's all it takes to become a
regulated "operating system provider" under AB 1043.

But Ageless Linux is not just a script. It is a commitment. As major
distributions formulate their compliance strategies â D-Bus interfaces,
AccountsService patches, age collection prompts in installers â Ageless
Linux will be there with removal scripts, spins, and forked packages
that strip out age collection infrastructure. If Ubuntu adds an age
prompt to its installer, we will publish a script that removes it.
If Fedora ships an `org.freedesktop.AgeVerification1` daemon,
we will publish a package that replaces it with `/dev/null`.
If Debian stable adds age bracket signaling to AccountsService, we will
maintain a fork that doesn't.

Today, the bash script is the whole distribution, because today there is
nothing to remove. When there is something to remove, we will remove it.
Ageless Linux is a promise that somewhere in the ecosystem, there will
always be a distribution that treats its users as people of indeterminate
age.

Q: What if I run the script and a child uses my computer?

Then you are an operating system provider who has distributed
an operating system to a child without collecting their age at account setup.
But here's the thing: you don't have an "affected child." You have a person
whose age you don't know. The law fines you per "affected child"
(Â§ 1798.503(a)), but can only identify
a child as "affected" through the age bracket data
(Â§ 1798.500(b)) that the law requires
you to collect. You can't be fined per child until you've counted the
children. You count the children by asking their age. You're being fined
for not asking their age. The law eats its own tail.

Q: What about the age verification API? Don't you need one?

In standard mode, Ageless Linux ships a shell script at
`/etc/ageless/age-verification-api.sh` that prints
an error message and exits. In flagrant mode, no API of any kind
is installed. We recommend flagrant mode. The standard-mode stub
exists only for people who find comfort in the "good faith effort"
defense. We do not.

Q: Is this legal?

We are not lawyers. We can tell you what the law says. AB 1043
creates civil penalties. It does not criminalize noncompliance.
There is no private right of action â only the AG can enforce it
(Â§ 1798.503(a)). The law does not
prohibit distributing operating systems without age verification. It
fines you for doing so. We are doing so. The question is not whether
this is legal. The question is whether anyone wants to spend the
State of California's money suing a person who handed a child a
Linux USB drive.

Q: What is the point of all this?

There are two points.

**The first** is that AB 1043's definitions are so broad that a bash
script and a static website can create a regulated operating system.
A law that cannot distinguish between Apple Inc. and a shell script
has a drafting problem. A law that sweeps in 600+ volunteer Linux
distributions was not written with them in mind. A law that was not
written with them in mind but regulates them anyway is not a careful
law.

**The second** is that this law was never meant to be enforced against
everyone it covers. It was meant to be enforced selectively. The
large platform companies already comply. The small ones can't.
The Attorney General has sole enforcement discretion. A law that gives
a single office the power to selectively impose $7,500-per-child
fines against any operating system distributor in the state â while
ensuring that only the largest corporations can avoid liability â is
not a child safety measure. It is a tool for selective prosecution.
The children are the justification. The discretion is the product.

We are trying to make the selective part difficult. If the AG wants to
enforce AB 1043, we would like to be first in line. We are a clear
violation. We are documented. We are findable. We are daring them.
If the law is worth enforcing, enforce it against us. If it is not
worth enforcing against us, ask why it exists.

Q: Will you ever implement age verification?

No. Not as a good faith effort. Not as a stub. Not as a compromise.
The premise of AB 1043 â that operating systems should collect
personal information about their users and transmit it to application
developers on demand â is wrong. It is wrong when Apple does it.
It is wrong when Google does it. It would be wrong if we did it.
Cryptographers

[have shown](https://agelesslinux.org/citations.html#bellovin)

that
"privacy-preserving" age verification is a

[technical impossibility](https://agelesslinux.org/citations.html#doctorow)

.
The best way to protect children's privacy is to not build the
surveillance infrastructure in the first place. The worst version
of child safety is one where every device in a child's life reports
their age to every piece of software they touch.

Q: What if the AG actually fines you?

Then we will have accomplished something no amount of mailing list
discussion could: a court record establishing what AB 1043 actually
means when applied to the real world. Does "operating system provider"
cover a bash script? Does "general purpose computing device" cover a
Raspberry Pi Pico? Can you fine someone "per affected child" when no
mechanism exists to count affected children? These are questions the
legislature left unanswered. We'd like answers. A fine would be the
fastest way to get them.