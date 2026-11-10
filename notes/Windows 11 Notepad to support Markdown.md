---
title: "Windows 11 Notepad to support Markdown"
url: https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/
clipped: 2026-06-17 01:40:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Windows 11 Notepad to support Markdown](https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/)

## Digest Summary
Notepad (v 11.2512.10.0) receives several enhancements for Windows 11 Insiders in the Canary and Dev channels. Markdown support is expanded to include strikethrough and nested‑list syntax, accessible via the formatting toolbar, shortcuts, or direct markup. A new welcome dialog introduces core features and can be reopened via a megaphone icon. AI‑assisted “Write,” “Rewrite,” and “Summarize” functions now stream results, showing partial output sooner; these features require a Microsoft‑account sign‑in. Feedback should be filed in Feedback Hub under Apps → Notepad.  

Paint (v 11.2512.191.0) adds two features. “Coloring book,” an AI‑driven tool in the Copilot menu, generates custom coloring‑page images from text prompts; it is limited to Copilot+ devices and also requires a Microsoft‑account sign‑in. A fill‑tolerance slider for the Fill tool lets users adjust precision, enabling cleaner fills or artistic effects. Feedback for Paint is to be submitted via Feedback Hub under Apps → Paint.

## Discussion Summary
The comments show a largely critical response to the new Notepad features, with many users emphasizing that the program’s core value is its simplicity and plain‑text handling, and warning that markdown, AI integration, and account requirements threaten that purpose. Several participants note recent security concerns and prefer to keep Notepad unchanged or use existing alternatives such as Notepad++ or edit.exe, while a minority acknowledge potential usefulness of markdown support if it does not compromise basic functionality. Overall, the sentiment leans toward preserving Notepad’s minimalism and avoiding feature creep.

---

## Full Article

Hello Windows Insiders, today we are beginning to roll out updates for Notepad and Paint apps to Windows Insiders in the Canary and Dev Channels on Windows 11.

**Notepad (version 11.2512.10.0)**
----------------------------------

In this update, we’re introducing multiple improvements to Notepad.

First, we are expanding support of lightweight formatting to include additional Markdown syntax features. This includes strikethrough formatting and nested lists. To get started, explore these new options in the formatting toolbar, keyboard shortcuts, or by editing the Markdown syntax directly.

[![Notepad app screenshot of a nested list and strikethrough formatted created using the Increase indent command.](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/1-Notepad-Strikethrough_Nested-list.png)](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/1-Notepad-Strikethrough_Nested-list.png)

Notepad app screenshot of a nested list and strikethrough formatted created using the Increase indent command.

We are also introducing a new welcome experience in Notepad designed to help users discover and learn about the app’s latest and most useful features. This dialog provides a quick overview of what’s possible in Notepad and serves as a helpful starting point for both new and returning users. You can close it anytime and revisit it later by clicking the megaphone icon in the top-right corner of the toolbar.

[![Notepad app screenshot of the updated “What’s New” first run experience.](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/2-Notepad-Whats-New-1024x897.png)](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/2-Notepad-Whats-New.png)

Notepad app screenshot of the updated “What’s New” first run experience.

Finally, we are expanding support for streaming results for AI text features. Whether generated locally or in the cloud, results for Write, Rewrite, and Summarize will start to appear quicker without the need to wait for the full response, providing a preview sooner that you can interact with. To use Write, Rewrite, and Summarize in Notepad, you will need to sign in with your Microsoft account.

**FEEDBACK: Please file feedback in Feedback Hub (WIN + F)**[**under Apps > Notepad**](https://aka.ms/notepadfeedback)**.**

**Paint (version 11.2512.191.0)**
---------------------------------

In this update, we’re introducing two new features to Paint, Coloring book and fill tolerance slider.

**Coloring book**, an AI-powered feature that lets you create unique coloring book pages from a text prompt. To get started, open Paint and select the **Coloring book** option from the Copilot menu. Once the side panel is open, type in a description of the coloring book you want to create, like “a cute fluffy cat on a donut” or “a house with a garden and fence” and hit the **Generate** button. Paint will then generate a set of unique coloring book pages based on your prompt. Once the coloring book pages are generated, you can click on any one of them to Add to canvas, copy, or save it for later use.

[![Paint app showing a cat on a donut coloring book page.](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/3-Paint_Coloring_book-1-1024x676.png)](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/3-Paint_Coloring_book-1.png)

Paint app showing a cat on a donut coloring book page.

*Coloring book will be available only on Copilot+ PCs. To use Coloring book, you will need to sign in with your Microsoft account.*

We’re also adding a fill tolerance slider, giving you control over how precisely the Fill tool applies color. To get started, select the **Fill** tool and use the slider on the left side of the canvas to adjust the tolerance to your desired level. Experiment with different tolerance settings to achieve clean fills or creative effects.

[![Paint app showing Fill tool with tolerance set to 8% versus 18%. ](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/Fill_Tolerance-1.gif)](https://winblogs.thesourcemediaassets.com/sites/44/2026/01/Fill_Tolerance-1.gif)

Paint app showing Fill tool with tolerance set to 8% versus 18%.

**FEEDBACK: Please file feedback in Feedback Hub (WIN + F)**[**under Apps > Paint**](https://aka.ms/paintfeedback)**.**

As always, we love getting feedback from the community and we will be looking out for your thoughts and suggestions on these updates!

Thanks,  
Dave Grochocki, Principal Group Product Manager – Windows Inbox Apps