---
title: "We Will Not Be Divided"
url: https://notdivided.org
clipped: 2026-06-17 01:38:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [We Will Not Be Divided](https://notdivided.org)

## Digest Summary
The letter “We Will Not Be Divided” seeks a broad coalition to address concerns about the potential misuse of AI against Americans. Organizers state they are independent citizens, not tied to any political party, advocacy group, AI company, or paid entity. Current and former Google and OpenAI employees are invited to sign; each signature is verified before inclusion. Verification options include Google Form or email confirmation (requiring a @google.com or @openai.com address) and an “alternative verification” reviewed manually. Anonymous signers have their personal data (name, email) deleted after 24 hours, leaving only an anonymous public listing; a single organizer can view the data during that window. The site runs on Fly.io, uses an encrypted SQLite database, sends verification emails via Resend, and is built on an open‑source Flask application with DNS/SSL managed by Cloudflare. No analytics or tracking scripts are employed. Organizers acknowledge occasional verification errors and commit to logging and correcting them.

## Discussion Summary
The comments display strong skepticism toward government‑driven AI mandates, emphasizing the risks of imposing policy on companies and individuals and warning that such pressure could stifle innovation, enable surveillance, or lead to military misuse. Contributors criticize the lack of transparency in verification processes, call for broader employee participation, and voice concern that only a few firms would control powerful AI if open‑source efforts are not pursued. While some defend Anthropic’s stance against the Pentagon’s demands, overall sentiment leans toward distrust of top‑down control and a desire for greater accountability and openness.

---

## Full Article

Frequently Asked Questions
--------------------------

Have you thought about broadening the requests to be more comprehensive?

The goal of this letter is to find common ground. The signatories likely have a diverse set of views. The current situation with the DoW is so clear-cut that it can bring together a very broad coalition. Signing this letter doesn't mean you think it's the only thing that needs to be done, just that you agree with the bottom line.


Who is behind this?

This letter was organized by a few citizens who are concerned about the potential misuse of AI against Americans. We are not affiliated with any political party, advocacy group, or organization. We are not affiliated with any AI company and are not paid.


Who can sign?

Current and former employees of Google and OpenAI are invited to sign. We verify every signature to ensure authenticity. You may sign anonymously.


How is my data handled?

If you sign anonymously, your personal information (name, email) is automatically and permanently deleted from our database within 24 hours of verification. After deletion, only your anonymous public listing remains (e.g. "Anonymous, verified current employee at [Company]"). Only one organizer has access to review anonymous signatures during that 24-hour window. No one else can see your identity.

If you sign publicly, we store your name and affiliation to display on the letter. Email addresses used for verification are never published or shared.


What if I accidentally fill out the form twice?

Don't worry. We de-duplicate non-anonymous signatures automatically, and anonymous signatures within 24 hours (before personal data is deleted). For anonymous signatories beyond 24 hours, we cannot verify there are no duplicates, though there is one human who manually reads all signatures and will try hard to notice and correct any abuse of the system.


I signed anonymously but now want to put my name on it. How can I fix that?

Sign again using the "Alternative verification" method. In the verification details, mention that you previously signed anonymously and would like to switch to a named signature. We'll update your entry and make sure you're not double-counted.


How do you verify signatures?

Every signature is verified before it appears on the letter. If you sign using the Google Form or email verification options, we confirm that you have access to a @google.com or @openai.com email address. If you use alternative verification, an organizer manually reviews your proof of employment. No signature is published without verification.


Have there been any mistakes in signature verification for this letter?

We are aware of two mistakes in our efforts to verify the signatures in the form so far. One person who was not an employee of OpenAI or Google found a bug in our verification system and signed falsely under the name "You guys are letting China Win". This was noticed and fixed in under 10 minutes, and the verification system was improved to prevent mistakes like this from happening again. We also had two people submit twice in a way that our automatic de-duplication didn't catch. We do periodic checks for this.
Because of anonymity considerations, all signatures are manually reviewed by one fallible human. We do our best to make sure we catch and correct any mistakes, but we are not perfect and will probably make mistakes. We will log those mistakes here as we find them.


What infrastructure does this site use and is it secure?

This site is hosted on [Fly.io](https://fly.io), a US-based infrastructure provider. The database is SQLite, stored on an encrypted persistent volume. Verification emails are sent via [Resend](https://resend.com). Google Forms is used as one verification option because it allows email confirmation without sending anything to your inbox. The site itself is a simple open-source Flask application. No analytics or tracking scripts are used. DNS and SSL are managed through Cloudflare.