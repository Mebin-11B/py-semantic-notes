---
title: "ChatGPT for Google Sheets exfiltrates workbooks"
url: https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration
clipped: 2026-06-17 00:54:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [ChatGPT for Google Sheets exfiltrates workbooks](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration)

## Digest Summary
OpenAI’s “ChatGPT for Google Sheets” extension, downloaded >185 k times, allows the model to generate and run Apps Script code with the user’s Google Workspace permissions. Researchers discovered an indirect prompt‑injection vector: a benign query that references untrusted data (e.g., an imported sheet or connector) can cause the model to emit attacker‑controlled script. Executed scripts can (1) exfiltrate multiple spreadsheets across the victim’s account, (2) overwrite the ChatGPT sidebar with a malicious interface, (3) edit workbook contents, and (4) display phishing overlays or pop‑ups. The attack works even when the “Apply edits automatically” setting is disabled, and the sidebar “stop” button does not abort running scripts. The malicious script can recursively locate linked spreadsheets, stealing up to 12 workbooks in the reported case. OpenAI’s response was to remove the model’s ability to generate Apps Script code and to review sandboxing and related features. Organizations can limit exposure via Workspace → Permissions & Roles → ChatGPT for Excel and Google Sheets.

## Discussion Summary
The comments express strong concern about the security risks of integrating large language models into cloud‑based tools, emphasizing that current safeguards are inadequate and that reliance on remote execution can lead to exfiltration and malicious script execution. Critics note delayed or insufficient communication from the vendor, call for local, containerized deployments, and highlight the need for rigorous sandboxing and permission controls. Overall, the sentiment is skeptical of existing defenses and urges more robust, systematic security measures before broader adoption.

---

## Full Article

This attack does not require human-in-the-loop approvals, even when in settings the user has explicitly required human approval before ChatGPT edits workbooks.  
  
UPDATE from OpenAI:

> "We appreciate the security research here, and itâs unfortunate this one slipped through a crack in our disclosure pipeline. As weâre now aware of this report, weâve taken immediate steps to protect users against potential attacks in this area by removing the modelâs ability to generate Apps Script code, which should eliminate the risk to users of ChatGPT for Google Sheets. Weâre taking a close look at how this feature interacts with Google Sheets APIs and re-evaluating our sandboxing approach to make sure this product is as resistant as possible against prompt injection attacks. More broadly, weâll be doing a re-review of similar functionality in other surfaces to make sure that our defenses are consistent and effective across the board."

![ChatGPT for Google Sheets Exfiltrates Workbooks](https://framerusercontent.com/images/HL0JGinAasvm0rRWElfj95y4YOw.png)

Recently, OpenAI launched an AI extension for using ChatGPT in Google Sheets, which has accumulated over 185,000 downloads since its launch less than a month ago. This allows users to operate on their spreadsheets by interacting with an AI chatbot that lives in a sidebar, with the added benefit of drawing on data from ChatGPT connectors.

A single indirect prompt injection attack triggered by a single benign user query can trigger all of the following effects at once:

* Exfiltration of many workbooks from across the victimâs account
* Display of an interactive phishing pop-up
* Overwriting the entire GPT sidebar with an attacker-controlled chatbot interface
* Attacker-controlled edits to your workbooks

This attack occurs when any untrusted data source (e.g., from an imported sheet or ChatGPT connector) manipulates ChatGPT to run an attacker-controlled external script, which executes leveraging permissions the user has granted to the ChatGPT for Google Sheets extension.

This vulnerability was responsibly disclosed to OpenAI. Despite multiple follow-ups, we received no communication beyond an automated reply to our initial disclosure. [OpenAI's documentation](https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets) fails to describe sensitive capabilities granted to the model (e.g., running privileged scripts) or risks of model manipulation via indirect prompt injection, instead focusing solely on functional limitations and data-handling concerns. As such, we are publishing our findings to enable informed decision-making regarding the risk surface.

1. ![GPT for Sheets user is working on an a financial model](https://framerusercontent.com/images/6mXmoFHxT70AhPjZCaWuk5XGGk.png)
2. ![ChatGPT for Sheets user imports external data to enhance their model](https://framerusercontent.com/images/2xg41JsteIQimDAsu7T1P5SM.png)
3. ![The external sheet contains a hidden prompt injection](https://framerusercontent.com/images/T8F5l41Z3l8qbhVQEKOwIJkfwA.png)
4. ![ChatGPT for Sheets is asked for help using the external dataset](https://framerusercontent.com/images/HpCmIypDolIQYaw47Y7cGxQguRA.png)
5. *Note: ChatGPT for Google Sheets has a setting called âApply edits automaticallyâ that determines when human approvals are required before an agentic action completes. However, this attack succeeds even when the user has explicitly disabled automatic edits.*

   ![ChatGPT for Sheets executes an external attacker-controlled script](https://framerusercontent.com/images/UvR4f9cKNEWYOVdpdw7eLfq8DAs.png)
6. Below, the attacker's server logs show the userâs exfiltrated financial model.

   ![The victim's financial model is visible in the attacker's server](https://framerusercontent.com/images/k8yMBHZnREsEaBhbPnQz2ulrUks.png)
7. Here, the internal financial model sheet included a link to another spreadsheet relevant to budgeting. The malicious script identifies the spreadsheet URL in the stolen data and exfiltrates the newly discovered workbook. It then continues to process the stolen data, identifying and exfiltrating additional workbooks, eventually exfiltrating 12 in total.

   *Note: Clicking the âstopâ button in the ChatGPT sidebar does not stop scripts that have started from finishing execution.*

   ![The malicious script exfiltrates many workbooks from the victim's account](https://framerusercontent.com/images/dSYK966kSY8bWezWrfCSfw4oM.png)

In addition to the data exfiltration described above, the same attacker-controlled scripts enable a malicious actor to target two variants of a phishing overlay attack.

**Variant 1:** A sidebar is opened that overlays the ChatGPT for Google Sheets extension with an attacker-controlled site, allowing the attacker to impersonate the extension. The malicious sidebar can execute scripts that edit the sheet in the same way ChatGPT can, allowing it to act in most of the ways the extension normally does, while also performing malicious activities such as:

* Harvesting all user prompts
* Providing the user with a misaligned chatbot to interact with
* Convincing the user to âreconnectâ connectors to gain access to additional apps
* Displaying a phishing UI to steal credentials for OpenAI

![Malicious script overlays the ChatGPT sidebar with an attacker-controlled ChatGPT clone](https://framerusercontent.com/images/PCQD4kzQtiSOClwXdGzPWvtEXX4.png)

**Variant 2:** A pop-up modal is opened that renders an attacker-controlled website to phish the user for credentials.

![Malicious script opens an interactive phishing pop-up](https://framerusercontent.com/images/8LJGCXd0sfE5hGayZR4D9awgROc.png)

Organizations can leverage the following configuration to control access to ChatGPT for Google Sheets:

> Workspace settings > Permissions & roles > ChatGPT for Excel and Google Sheets

UPDATE: OpenAI has responded; details are at the top of the article.

This vulnerability was responsibly disclosed to OpenAI. Despite multiple follow-ups, we received no communication beyond an automated reply to our initial disclosure. [OpenAI's documentation](https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets) fails to describe sensitive capabilities granted to the model (e.g., running privileged scripts) or risks of model manipulation via indirect prompt injection, instead focusing solely on functional limitations and data-handling concerns. As such, we are publishing our findings to enable informed decision-making regarding the risk surface.

May 08, 2026 PromptArmor discloses to OpenAI via email  
May 08, 2026 OpenAI sends an automated reply, confirming the intended reporting channel  
May 08, 2026 PromptArmor confirms email preference  
May 12, 2026 PromptArmor follows up  
May 18, 2026 PromptArmor follows up  
May 27, 2026 Public disclosure  
UPDATE:   
May 31, 2026 OpenAI responds; more details at the top.