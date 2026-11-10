---
title: "Take potentially dangerous PDFs, and convert them to safe PDFs"
url: https://github.com/freedomofpress/dangerzone
clipped: 2026-06-17 01:55:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Take potentially dangerous PDFs, and convert them to safe PDFs](https://github.com/freedomofpress/dangerzone)

## Digest Summary
GitHub repository freedomofpress/dangerzone is a tool designed to mitigate security risks in file handling by converting potentially malicious PDFs, Office documents, and image files into safe, sanitized PDFs. The project’s interface includes settings and conversion functions, as indicated by associated UI screenshots. The repository lists contributions from multiple users (e.g., @apyrgio, @micahflee, @deeplow, @almet, @jkarasti, @dependabot[bot], @gmarmstrong, @naglis, @OctopusET, @garrettr, @EtiennePerot, @keywordnew, @rocodes, @sudwhiwdh). Access to the repository’s main content is currently restricted, shown by the message “You can’t perform that action at this time.” No additional documentation or code details are present in the provided text.

## Discussion Summary
The comments express caution about leaking documents, emphasizing the need for strong warnings and acknowledging that personal exposure to source files makes safety verification difficult. Watermarking and text paraphrasing are noted as partial mitigations, while sandboxed Docker execution and limited‑function PDF viewers are suggested as safer alternatives. Users criticize the current interface for lacking command‑line integration, appreciate the compression benefits of OCR‑based processing, and highlight the high cost of commercial CDR tools, promoting a free, multi‑format preview service and questioning its relevance for image files.

---

## Full Article

Take potentially dangerous PDFs, office documents, or images and convert them to a safe PDF.

Dangerzone works like this: You give it a document that you don't know if you can trust (for example, an email attachment). Inside of a sandbox, Dangerzone converts the document to a PDF (if it isn't already one), and then converts the PDF into raw pixel data: a huge list of RGB color values for each page. Then, outside of the sandbox, Dangerzone takes this pixel data and converts it back into a PDF.

*Read more about Dangerzone in the [official site](https://dangerzone.rocks/about/).*

Follow the instructions for each platform:

You can read more about our operating system support [here](https://github.com/freedomofpress/dangerzone/blob/v0.10.0/INSTALL.md#operating-system-support).

* Sandboxes don't have network access, so if a malicious document can compromise one, it can't phone home
* Sandboxes use [gVisor](https://gvisor.dev/), an application kernel written in Go, that implements a substantial portion of the Linux system call interface.
* Dangerzone can optionally OCR the safe PDFs it creates, so it will have a text layer again
* Dangerzone compresses the safe PDF to reduce file size
* After converting, Dangerzone lets you open the safe PDF in the PDF viewer of your choice, which allows you to open PDFs and office docs in Dangerzone by default so you never accidentally open a dangerous document

Dangerzone can convert these types of document into safe PDFs:

* PDF (`.pdf`)
* Microsoft Word (`.docx`, `.doc`)
* Microsoft Excel (`.xlsx`, `.xls`)
* Microsoft PowerPoint (`.pptx`, `.ppt`)
* ODF Text (`.odt`)
* ODF Spreadsheet (`.ods`)
* ODF Presentation (`.odp`)
* ODF Graphics (`.odg`)
* Hancom HWP (Hangul Word Processor) (`.hwp`, `.hwpx`)
* EPUB (`.epub`)
* Jpeg (`.jpg`, `.jpeg`)
* GIF (`.gif`)
* PNG (`.png`)
* SVG (`.svg`)
* other image formats (`.bmp`, `.pnm`, `.pbm`, `.ppm`, `.tif`, `.tiff`)

Dangerzone was inspired by [Qubes trusted PDF](https://blog.invisiblethings.org/2013/02/21/converting-untrusted-pdfs-into-trusted.html), but it works in non-Qubes operating systems. It uses containers as sandboxes instead of virtual machines (using Docker for macOS and Windows, and [podman](https://podman.io/) on Linux).

Set up a development environment by following [these instructions](https://github.com/freedomofpress/dangerzone/blob/main/BUILD.md).

Licensed under the AGPLv3: <https://opensource.org/licenses/agpl-3.0>

```
Copyright © 2022–2024 Freedom of the Press Foundation and Dangerzone contributors
Copyright © 2020–2021 First Look Media
```

See also [THIRD\_PARTY\_NOTICE.md](https://github.com/freedomofpress/dangerzone/blob/main/THIRD_PARTY_NOTICE.md) for more information regarding the third-party software that Dangerzone depends on.

### Has Dangerzone received a security audit?

Yes, Dangerzone received its [first security audit](https://freedom.press/news/dangerzone-receives-favorable-audit/) by [Include Security](https://includesecurity.com/) in December 2023. The audit was generally favorable, as it didn't identify any high-risk findings, except for 3 low-risk and 7 informational findings.

### "I'm experiencing an issue while using Dangerzone."

Dangerzone gets updates to improve its features *and* to fix problems. So, updating may be the simplest path to resolving the issue which brought you here. Here is how to update:

1. Check which version of Dangerzone you are currently using: run Dangerzone, then look for a series of numbers to the right of the logo within the app. The format of the numbers will look similar to `0.4.1`
2. Now find the latest available version of Dangerzone: go to the [download page](https://dangerzone.rocks/#downloads). Look for the version number displayed. The number will be using the same format as in Step 1.
3. Is the version on the Dangerzone download page higher than the version of your installed app? Go ahead and update.

### Can I run Dangerzone in an airgapped environment?

Yes, Dangerzone is designed to run in airgapped environments without any
configuration. If you want to update its container image, follow
[our instructions](https://github.com/freedomofpress/dangerzone/blob/main/docs/developer/independent-container-updates.md#Installing-image-updates-to-airgapped-environments).

### Can I use a custom runtime, such as Podman Desktop?

On Windows and macOS, Dangerzone embeds Podman, so there is no need to.

To use a different podman version, such as Podman Desktop, [follow our documentation](https://github.com/freedomofpress/dangerzone/blob/main/docs/podman-desktop.md).