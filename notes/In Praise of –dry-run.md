---
title: "In Praise of –dry-run"
url: https://henrikwarne.com/2026/01/31/in-praise-of-dry-run/
clipped: 2026-06-17 01:50:27
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [In Praise of –dry-run](https://henrikwarne.com/2026/01/31/in-praise-of-dry-run/)

## Digest Summary
The author describes adding a ‑dry‑run option to a reporting application that generates daily reports, zips them, uploads them via SFTP, processes server responses, and sends notification emails. The ‑dry‑run mode logs each step—identifying which reports would be created, which files would be zipped or moved, and what would be uploaded or downloaded—without performing any actions. This feature proved valuable for daily development, allowing quick sanity checks of configuration, data accessibility, and state consistency, and for testing changes (e.g., modifying report state dates) without incurring the time cost of full execution. The primary drawback is modest code duplication: each major phase must conditionally skip actual work when the flag is set, though core report‑generation logic remains unchanged. The author concludes that ‑dry‑run is well‑suited to command‑driven, state‑changing utilities but less applicable to reactive, message‑driven programs, and that early implementation maximized its benefits.

## Discussion Summary
Comments generally view dry‑run flags as useful safeguards that enable safe testing and verification before destructive actions, especially in CLI tools and migration scripts. Many favor a default‑safe mode requiring an explicit commit or ‑‑wet‑run flag, while others propose three‑state designs with prompts or ‑‑yes options. Implementations that separate side‑effects via injectable strategies or logging are praised for reducing code clutter. Some note increased complexity for multi‑step operations and suggest alternative approaches such as overlay filesystems. Overall sentiment is supportive of dry‑run functionality, emphasizing clear, explicit activation.

---

## Full Article

For the last few months, I have been developing a new reporting application. Early on, I decided to add a *–dry-run* option to the run command. This turned out to be quite useful – I have used it many times a day while developing and testing the application.

[![](https://henrikwarne.com/wp-content/uploads/2026/01/snow.jpg?w=1024)](https://henrikwarne.com/wp-content/uploads/2026/01/snow.jpg)


Background
----------

The application will generate a set of reports every weekday. It has a loop that checks periodically if it is time to generate new reports. If so, it will read data from a database, apply some logic to create the reports, zip the reports, upload them to an sftp server, check for error responses on the sftp server, parse the error responses, and send out notification mails. The files (the generated reports, and the downloaded feedback files) are moved to different directories depending on the step in the process. A simple and straightforward application.

Early in the development process, when testing the incomplete application, I remembered that Subversion (the version control system after CVS, before Git) had a *–dry-run* option. Other linux commands have this option too. If a command is run with the argument *–dry-run*, the output will print what will happen when the command is run, but no changes will be made. This lets the user see what will happen if the command is run without the *–dry-run* argument.

I remembered how helpful that was, so I decided to add it to my command as well. When I run the command with *–dry-run*, it prints out the steps that will be taken in each phase: which reports that will be generated (and which will not be), which files will be zipped and moved, which files will be uploaded to the sftp server, and which files will be downloaded from it (it logs on and lists the files).

Looking back at the project, I realized that I ended up using the *–dry-run* option pretty much every day.

Benefits
--------

I am surprised how useful I found it to be. I often used it as a check before getting started. Since I know *–dry-run* will not change anything, it is safe to run without thinking. I can immediately see that everything is accessible, that the configuration is correct, and that the state is as expected. It is a quick and easy sanity check.

I also used it quite a bit when testing the complete system. For example, if I changed a date in the report state file (the date for the last successful report of a given type), I could immediately see from the output whether it would now be generated or not. Without *–dry-run*, the actual report would also be generated, which takes some time. So I can test the behavior, and receive very quick feedback.

Downside
--------

The downside is that the *dryRun*-flag pollutes the code a bit. In all the major phases, I need to check if the flag is set, and only print the action that will be taken, but not actually doing it. However, this doesn’t go very deep. For example, none of the code that actually generates the report needs to check it. I only need to check if that code should be invoked in the first place.

Conclusion
----------

The type of application I have been writing is ideal for *–dry-run*. It is invoked by a command, and it may create some changes, for example generating new reports. More reactive applications (that wait for messages before acting) don’t seem to be a good fit.

I added *–dry-run* on a whim early on in the project. I was surprised at how useful I found it to be. Adding it early was also good, since I got the benefit of it while developing more functionality.

The *–dry-run* flag is not for every situation, but when it fits, it can be quite useful.