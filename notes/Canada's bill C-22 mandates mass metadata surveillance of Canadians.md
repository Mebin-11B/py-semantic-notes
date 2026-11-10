---
title: "Canada's bill C-22 mandates mass metadata surveillance of Canadians"
url: https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/
clipped: 2026-06-17 01:32:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Canada's bill C-22 mandates mass metadata surveillance of Canadians](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/)

## Digest Summary
Bill C‑22, the Lawful Access Act, revises Canada’s lawful‑access framework in two parts. The first section replaces the broad, warrant‑less “information demand” power of Bill C‑2 with a limited “confirmation of service” request that lets police ask telecoms only whether they serve a specific person; any further subscriber data requires a production order signed by a judge, applying a “reasonable grounds to suspect” standard. The bill also codifies rules on voluntary disclosure, challenges, exigent circumstances and foreign requests.

The second part, the Supporting Authorized Access to Information Act (SAAIA), largely retains Bill C‑2’s obligations for electronic service providers (ESPs). Core providers must assist law‑enforcement testing of access capabilities, keep related requests secret, and retain categories of metadata (including transmission data) for up to one year, while being prohibited from retaining content, browsing history, or social‑media activity. An exemption permits non‑compliance when compliance would create systemic vulnerabilities. Oversight is shifted to the Intelligence Commissioner, but concerns remain about security risks, secrecy, and alignment with international regimes such as the Budapest Convention and the CLOUD Act.

## Discussion Summary
The discussion is dominated by concern that Bill C‑22 expands state surveillance by allowing warrant‑free data access and obligating service providers, which many view as a serious erosion of privacy and democratic safeguards. Critics highlight a subjective loophole, potential foreign influence, and risk of abuse, while a minority argue that broader police powers could improve investigations and recover stolen property. Overall the consensus leans toward opposition, citing insufficient safeguards and the threat of a permanent surveillance infrastructure.

---

## Full Article

The decades-long battle over lawful access entered a new phase yesterday with the introduction of [Bill C-22, the Lawful Access Act](https://www.parl.ca/legisinfo/en/bill/45-1/c-22). This bill follows the attempt last spring to bury [lawful access provisions in Bill C-2](https://www.michaelgeist.ca/2025/06/privacy-at-risk-government-buries-lawful-access-provisions-in-new-border-bill/), a border measures bill that was the new government’s first piece of substantive legislation. The lawful access elements of the bill faced an immediate backlash given the inclusion of unprecedented rules permitting widespread warrantless access to personal information. Those rules were on very shaky constitutional ground and the government ultimately decided to [hit the reset button](https://www.michaelgeist.ca/2025/10/government-reverses-on-bill-c-2-removes-lawful-access-warrantless-demand-powers-in-new-border-bill/) on lawful access by proceeding with the border measures in a different bill.

Lawful access never dies, however. Bill C-22 cover the two main aspects of lawful access: law enforcement access to personal information held by communication service providers such as ISPs and wireless providers and the development of surveillance and monitoring capabilities within Canadian networks. In fact, the bill is separated into two with the first half dealing with “timely access to data and information” and the second establishing the Supporting Authorized Access to Information Act (SAAIA).

I anticipate providing extensive coverage of the bill on both this blog and my podcast. My initial take is that the access to data and information piece of the bill is much improved. The earlier Bill C-2 iteration of a new information demand power was astonishing in its breadth (covering far more than just communications providers by targeting anyone who provides a service in Canada including physicians and lawyers) and demands for warrantless disclosure of personal information in direct contradiction to recent Supreme Court of Canada jurisprudence.

The government has scrapped that approach by shifting to a new “confirmation of service” demand power. This would allow law enforcement to demand that telecom providers (not any service provider) confirm whether they provide service to a particular person. The other subscriber information would be subject to a new production order reviewed and approved by a judge. This would address the longstanding police complaint that they may do considerable work seeking information about a subscriber at a provider only to learn that the person isn’t a customer and they start over with someone else.

These new rules contain other orders and rules on voluntary disclosure, challenging the requests, exigent circumstances, and foreign orders for the same information. I plan to unpack these rules in the coming weeks. For example, there are concerns about the thresholds that the production orders envision, namely the low “reasonable grounds to suspect” standard. However, the main takeaway here is that the government has significantly limited the scope of warrantless information demand powers, now focusing solely on telecommunications providers and whether they provide service to a particular individual. Access to more personal information will require oversight. That’s a major concession and highlights how Bill C-2 was too broad, dangerous from a privacy perspective, and unlikely to pass constitutional muster.

If that is the good news, the bad news is very bad. The SAAIA, which establishes new requirements for communications providers to actively work with law enforcement on their surveillance and monitoring capabilities are largely unchanged from Bill C-2. In fact, there are elements involving data retention that are even worse. The government will point to increased oversight – ministerial orders must now be approved by the Intelligence Commissioner – but the concerns regarding surveillance capabilities, security vulnerabilities, secrecy, and cross-border data sharing remain.

The SAAIA has huge implications for network providers as they envision providing law enforcement with direct access to provider networks to test capabilities for data access and interception. The bill introduces a new term – “electronic service provider” – that is presumably designed to extend beyond telecom and Internet providers by scoping in Internet platforms (Google, Meta, etc.). Those international services are now key players in electronic communications (think Gmail or WhatsApp), though some may be beyond this form of regulation (eg. Signal if you don’t inadvertently add people to chat groups).

The definition of an ESP is:

> *a person that, individually or as part of a group, provides an electronic service, including for the purpose of enabling communications, and that (a) provides the service to persons in Canada; or  (b) carries on all or part of its business activities in Canada.‍*

An electronic service includes:

> *“a service, or a feature of a service, that involves the creation, recording, storage, processing, transmission, reception, emission or making available of information in electronic, digital or any other intangible form by an electronic, digital, magnetic, optical, biometric, acoustic or other technological means, or a combination of any such means.”*

All electronic service providers are subject to obligations to “provide all reasonable assistance, in any prescribed time and manner, to permit the assessment or testing of any device, equipment or other thing that may enable an authorized person to access information.” Moreover, all are required to keep such requests secret.

But beyond the basic obligations, the government will identify “core providers” who will be subject to additional regulations. These may include:

> *(a) the development, implementation, assessment, testing and maintenance of operational and technical capabilities, including capabilities related to extracting and organizing information that is authorized to be accessed and to providing access to such information to authorized persons;*  
> *(b) the installation, use, operation, management, assessment, testing and maintenance of any device, equipment or other thing that may enable an authorized person to access information;*  
> *(c) notices to be given to the Minister or other persons, including with respect to any capability referred to in paragraph (a) and any device, equipment or other thing referred to in paragraph (b); and*  
> *(d) the retention of categories of metadata — including transmission data, as defined in section 487.‍011 of the Criminal Code — for reasonable periods of time not exceeding one year.*

Note that the retention of metadata found in (d) is new. It was not in Bill C-2, so this bill actually expands the scope of obligations. The new bill contains some limits on data retention:

> *4) Paragraph (2)‍(d) does not authorize the making of regulations that require core providers to retain information that would reveal*  
> *(a) the content — that is to say the substance, meaning or purpose — of information transmitted in the course of an electronic service;*  
> *(b) a person’s web browsing history; or*  
> *(c) a person’s social media activities.*

The bill also retains an exception for systemic vulnerabilities, which states:

> *A core provider is not required to comply with a provision of a regulation made under subsection (2), with respect to an electronic service, if compliance with that provision would require the provider to introduce a systemic vulnerability related to that service or prevent the provider from rectifying such a vulnerability.*

There remain concerns that is insufficient and that there are real risks that networks may be [made less secure](https://ccla.org/privacy/ccla-joins-calls-for-withdrawal-of-bill-c-2/?utm_source=chatgpt.com) by virtue of these rules with the changes kept secret from the public. Moreover, as [Kate Robertson of the Citizen Lab has discussed](https://citizenlab.ca/research/a-preliminary-analysis-of-bill-c-2/) (including on the [Law Bytes podcast](https://www.michaelgeist.ca/2025/10/law-bytes-podcast-episode-245/)), many of these rules appear geared toward global information sharing, including compliance with the Second Additional Protocol to the Budapest Convention (2AP) and the CLOUD Act.

There is much to unpack with this section including the ability to challenge orders, the secrecy associated with the system, oversight, and costs. I plan to cover these as well but for the moment it is sufficient to conclude that Bill C-22’s SAAIA envisions a significant change to how government agencies interact with Canadian communications networks and network providers raising enormous privacy and civil liberties concerns. The government may have taken warrantless access to subscriber information off the table, but there remains serious privacy concerns associated with its lawful access plans.

***Enjoyed this post? Get every post plus the Law Bytes podcast delivered to your inbox – [subscribe on Substack](https://mgeist.substack.com/).***