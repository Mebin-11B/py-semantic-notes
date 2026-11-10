---
title: "Stop Doom Scrolling, Start Doom Coding: Build via the terminal from your phone"
url: https://github.com/rberg27/doom-coding
clipped: 2026-06-17 02:02:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - mobile development
  - remote access
  - tailscale vpn
  - ssh terminal
  - ai-assisted coding
related:
  - "[[Mobile Development]]"
  - "[[Remote Access]]"
  - "[[Tailscale VPN]]"
  - "[[AI-Assisted Coding]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A step-by-step DIY guide to setting up mobile terminal coding using Tailscale VPN, Termius SSH, and Claude Code.
>
> **Key points:**
> - Establishes a remote coding workspace on a phone using a 24/7 home server connection.
> - Uses Tailscale VPN for secure networking and Termius for SSH terminal access from a mobile phone.
> - Integrates LLM-assisted coding directly through terminal interfaces (e.g., Claude Code) to build prototypes on the go.
> - Identifies common mobile coding failure modes, including VPN drops, locked computers, and closed laptop sleep behaviors.
>
> **Concept links:** [[Mobile Development]], [[Remote Access]], [[Tailscale Vpn]], [[Ssh Terminal]], [[Ai-Assisted Coding]]
>
> **Suggested connections:**
> - [[Mobile Development]] — transforming mobile downtime into productive coding sessions using phone terminals.
> - [[AI-Assisted Coding]] — using LLM agents like Claude Code inside remote shells.
<!-- ai-summary:end -->


# [Stop Doom Scrolling, Start Doom Coding: Build via the terminal from your phone](https://github.com/rberg27/doom-coding)

## Digest Summary
The page for the GitHub repository “rberg27/doom-coding” is unavailable, displaying the message “You can’t perform that action at this time.” No additional textual content or description of the guide is provided, aside from a placeholder for an image with alt text “image.”

## Discussion Summary
Comments reflect a split view on remote phone‑based coding with Claude. Many describe functional setups using Termux, SSH, tmux, Tailscale, Docker containers or email‑based workflows, emphasizing flexibility, low cost and occasional convenience when away from a laptop. Others criticize the added complexity of VPNs or layered remote access, cite poor typing and UI experiences on phones, and argue that established tools (local terminals, GitHub Copilot, web IDEs) already meet most needs. Security, session persistence and integration with diff/preview tools are repeatedly mentioned as concerns, while enthusiasm varies between those who see practical value and those who view the approach as unnecessary or cumbersome.

---

## Full Article

A DIY approach to coding on-the-go!

As an aspiring builder, I sought out a way to keep coding while not at home. Thanks to some Claude-assisted research and troubleshooting, I can now code via the terminal on my phone anywhere at anytime via "Doom Coding" (think *Doom Scrolling* but more productive).

After this 5-minute setup guide, you'll be able to "doom code" anywhere you have Internet connection.

Code in the air!  
  
[![image](https://private-user-images.githubusercontent.com/114448747/530833069-bda532b6-3963-4ace-907b-ebbf9460032c.jpeg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwODMzMDY5LWJkYTUzMmI2LTM5NjMtNGFjZS05MDdiLWViYmY5NDYwMDMyYy5qcGVnP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDYxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MTZUMjAzMjM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmYxMDdjY2Q4ZjRjNWNlZjM4NTZkYWUwMzU0ZGQ2Y2MzM2FmMTI3Zjg3NDVmYWQzMjcyN2IyNGExNTg4ZTMyZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGanBlZyJ9.toFRYuZ742gYEHdyk9Dc79llRVf1X2RDc8YH5NPRd6g)](https://private-user-images.githubusercontent.com/114448747/530833069-bda532b6-3963-4ace-907b-ebbf9460032c.jpeg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwODMzMDY5LWJkYTUzMmI2LTM5NjMtNGFjZS05MDdiLWViYmY5NDYwMDMyYy5qcGVnP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDYxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MTZUMjAzMjM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmYxMDdjY2Q4ZjRjNWNlZjM4NTZkYWUwMzU0ZGQ2Y2MzM2FmMTI3Zjg3NDVmYWQzMjcyN2IyNGExNTg4ZTMyZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGanBlZyJ9.toFRYuZ742gYEHdyk9Dc79llRVf1X2RDc8YH5NPRd6g)

Code on a run!   
[![image](https://private-user-images.githubusercontent.com/114448747/530367038-f5449004-0a76-44ee-9922-a5cce1423f93.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzY3MDM4LWY1NDQ5MDA0LTBhNzYtNDRlZS05OTIyLWE1Y2NlMTQyM2Y5My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMTU2NGFkN2ZjNjRjNGJjM2M5N2Y3MTM1Mzk2MzZhNDhmMjNlN2YzYTY2MmVlOGJjYjcwNDAxMWI4YTg0ZTE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.EM9CielGZ1C_DoRR0qZTIJhMDNQqZXwRSrNmTusbUpM)](https://private-user-images.githubusercontent.com/114448747/530367038-f5449004-0a76-44ee-9922-a5cce1423f93.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzY3MDM4LWY1NDQ5MDA0LTBhNzYtNDRlZS05OTIyLWE1Y2NlMTQyM2Y5My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMTU2NGFkN2ZjNjRjNGJjM2M5N2Y3MTM1Mzk2MzZhNDhmMjNlN2YzYTY2MmVlOGJjYjcwNDAxMWI4YTg0ZTE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.EM9CielGZ1C_DoRR0qZTIJhMDNQqZXwRSrNmTusbUpM)

Even code at the club!   
[![image](https://private-user-images.githubusercontent.com/114448747/530365787-f3d05c00-a47a-4ebe-8db3-1795a6a0798c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzY1Nzg3LWYzZDA1YzAwLWE0N2EtNGViZS04ZGIzLTE3OTVhNmEwNzk4Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NmNlMjg5OWEzZjJmZjg5MGJmMGI2ZjQ1M2Y1MTE2MTQyMTllZmMxMGI5ZWVjM2VhM2JiN2ZkM2UzNmM0MmYzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.BXWgPPPnQQ1dhLwtK6aJgzNWoiXTIPSZcVxG7a0mYCY)](https://private-user-images.githubusercontent.com/114448747/530365787-f3d05c00-a47a-4ebe-8db3-1795a6a0798c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzY1Nzg3LWYzZDA1YzAwLWE0N2EtNGViZS04ZGIzLTE3OTVhNmEwNzk4Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NmNlMjg5OWEzZjJmZjg5MGJmMGI2ZjQ1M2Y1MTE2MTQyMTllZmMxMGI5ZWVjM2VhM2JiN2ZkM2UzNmM0MmYzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.BXWgPPPnQQ1dhLwtK6aJgzNWoiXTIPSZcVxG7a0mYCY)

I've been amazed by how much I can get done while being so far away from home. In Taiwan, I could access my computer in Philadelphia and coded a prototype in my downtime.

*Shameless plug: check out [www.friendlyr.ai](http://www.friendlyr.ai) to help shape the future of connection!*

Make sure to "Watch" this repo for future updates to this doom coding guide. As I tryout the latest mobile coding tools (e.g. Claude Code on the Web), I'll update this repository with comparisons.

Happy doom coding my friends!

1. A Computer running 24/7 with Internet Connection
2. A Smartphone
3. A Claude Pro subscription

Use Tailscale, Termius, Claude Code, and a computer running 24/7 to continue building anywhere you have Internet connection.

* Turn on Tailscale VPN on your phone  
  [![image](https://private-user-images.githubusercontent.com/114448747/530203492-03646788-619b-427e-8e47-5bf8219c1c36.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMjAzNDkyLTAzNjQ2Nzg4LTYxOWItNDI3ZS04ZTQ3LTViZjgyMTljMWMzNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NzRmMDU2MWViODU3MmEwNGM3ZWE4YmIzMThkNTJlNTQ5NDhiMjI5ODdlODE0NDA0NDg5NmQ5MTE5ODg3NGIxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Ci4BQpQJ48L8NrusapJWmEV9gO96CyVtVXw7jfn5iis)](https://private-user-images.githubusercontent.com/114448747/530203492-03646788-619b-427e-8e47-5bf8219c1c36.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMjAzNDkyLTAzNjQ2Nzg4LTYxOWItNDI3ZS04ZTQ3LTViZjgyMTljMWMzNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NzRmMDU2MWViODU3MmEwNGM3ZWE4YmIzMThkNTJlNTQ5NDhiMjI5ODdlODE0NDA0NDg5NmQ5MTE5ODg3NGIxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Ci4BQpQJ48L8NrusapJWmEV9gO96CyVtVXw7jfn5iis)
* Select your host in Termius  
  [![image](https://private-user-images.githubusercontent.com/114448747/530203710-18d5a03e-acf7-4069-93c2-c67d45a25183.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMjAzNzEwLTE4ZDVhMDNlLWFjZjctNDA2OS05M2MyLWM2N2Q0NWEyNTE4My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNWZhYmVjYjZjZGU2MTE2MzE3MzYxNDVkNWUxY2Y4MDI1ZDFjODJkZGVjOGY2ZDIyNjg1ZWJlOWU5Zjk1NjhhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.hKpQlDWkG6Q3qOcKCIM2Io40Uuy691CkxXA25BlVCGQ)](https://private-user-images.githubusercontent.com/114448747/530203710-18d5a03e-acf7-4069-93c2-c67d45a25183.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMjAzNzEwLTE4ZDVhMDNlLWFjZjctNDA2OS05M2MyLWM2N2Q0NWEyNTE4My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNWZhYmVjYjZjZGU2MTE2MzE3MzYxNDVkNWUxY2Y4MDI1ZDFjODJkZGVjOGY2ZDIyNjg1ZWJlOWU5Zjk1NjhhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.hKpQlDWkG6Q3qOcKCIM2Io40Uuy691CkxXA25BlVCGQ)
* Run `claude` and start coding!

[![image](https://private-user-images.githubusercontent.com/114448747/530205087-d92df1cd-570b-49b0-96f7-a5ce31644a6f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMjA1MDg3LWQ5MmRmMWNkLTU3MGItNDliMC05NmY3LWE1Y2UzMTY0NGE2Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yY2E4YmU0MzhlNGU0YThkMmI3ODc5MmNjZWQxZjQwMDZjNTlhNjViZTBmODA4MTdmZjE1ZGQ3ZDkwMzY5ZTg4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ._H2fTKWMvbgeGIZmS8W7ouhvTp5r54yj8qCKFR3b7Yk)](https://private-user-images.githubusercontent.com/114448747/530205087-d92df1cd-570b-49b0-96f7-a5ce31644a6f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMjA1MDg3LWQ5MmRmMWNkLTU3MGItNDliMC05NmY3LWE1Y2UzMTY0NGE2Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yY2E4YmU0MzhlNGU0YThkMmI3ODc5MmNjZWQxZjQwMDZjNTlhNjViZTBmODA4MTdmZjE1ZGQ3ZDkwMzY5ZTg4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ._H2fTKWMvbgeGIZmS8W7ouhvTp5r54yj8qCKFR3b7Yk)

* If you're not able to establish a connection from your phone via Termius to your computer:

1. Reset your Tailscale VPN
---------------------------

* Check your phone settings to make sure you are connected to the Tailscale VPN.   
  [![image](https://private-user-images.githubusercontent.com/114448747/530353567-1b041eff-9001-4e41-8922-c7f3bcb368da.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzUzNTY3LTFiMDQxZWZmLTkwMDEtNGU0MS04OTIyLWM3ZjNiY2IzNjhkYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hN2NmN2YxYjM2ZDA1Zjk2YmRlNTE2YzIxNjU1NmMwNmQ0MmI3ZmFhZTE4ODA3YzkwMzVjY2VhMTY0Y2RkMjVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.JqfnBWL4_vuEyGngEc7c4eBKVr98heHr-M8fD9lBCtE)](https://private-user-images.githubusercontent.com/114448747/530353567-1b041eff-9001-4e41-8922-c7f3bcb368da.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzUzNTY3LTFiMDQxZWZmLTkwMDEtNGU0MS04OTIyLWM3ZjNiY2IzNjhkYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hN2NmN2YxYjM2ZDA1Zjk2YmRlNTE2YzIxNjU1NmMwNmQ0MmI3ZmFhZTE4ODA3YzkwMzVjY2VhMTY0Y2RkMjVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.JqfnBWL4_vuEyGngEc7c4eBKVr98heHr-M8fD9lBCtE)
* Check the Tailscale app to make sure the Tailscale VPN is on. If your phone and doom coding computer do not have a green circle next to their labels, there is an issue with your Tailscale/Internet connection.

[![image](https://private-user-images.githubusercontent.com/114448747/530364232-e5da61ab-828d-4f40-920d-840306c284ed.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzY0MjMyLWU1ZGE2MWFiLTgyOGQtNGY0MC05MjBkLTg0MDMwNmMyODRlZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xODFhZTlkMGY4ZDY4ZmFiNmU4NGRmY2EzYTk1YWRlNjA4M2RhNGEyZWNmODc4YmI1NzkxODNkODA1NWZiNjBjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Iz7qma83TljyWsV0S7EzWxtHHcjq2-H--hEUhw6Eopc)](https://private-user-images.githubusercontent.com/114448747/530364232-e5da61ab-828d-4f40-920d-840306c284ed.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIyNTUsIm5iZiI6MTc4MTY0MTk1NSwicGF0aCI6Ii8xMTQ0NDg3NDcvNTMwMzY0MjMyLWU1ZGE2MWFiLTgyOGQtNGY0MC05MjBkLTg0MDMwNmMyODRlZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDMyMzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xODFhZTlkMGY4ZDY4ZmFiNmU4NGRmY2EzYTk1YWRlNjA4M2RhNGEyZWNmODc4YmI1NzkxODNkODA1NWZiNjBjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Iz7qma83TljyWsV0S7EzWxtHHcjq2-H--hEUhw6Eopc)

2. Make sure your computer is ON and UNLOCKED
---------------------------------------------

* When disconnecting/reconnecting power, make sure you unlock the computer. I've ran into this issue one too many times.
* New niche bug: If you're using a closed laptop to doom code, do not connect that laptop to a monitor. I've recently changed my setup from displaying my doom coding laptop 24/7 to connecting the doom code laptop display to a backup HDMI port I can switch too. Despite setting the doom code laptop to never sleep, it would still disconnect from tailscale after 10 minutes. Issue was resolved by disconnecting the doom code laptop from the monitor. Go figure.

3. Check your Access control settings on the web
------------------------------------------------

* Refer to the screenshots in "1. Set Up Your Computer" above. I reset my doom-coding setup to test out the guide and forgot this critical step. You need to disable IPv4 so that Termius connects via MagicDNS. I don't know why, but that's the beauty of hours of AI-Enabled troubleshooting.

End sessions by asking Claude to update CLAUDE.md with where you left off.

Go to your desired directory and start an HTTP server  
`python -m http.server 3005`
then visit <http://your-machine.tailnet-name.ts.net:3005/your-html-file.html> in a browser on your phone.

*Wherever you would use localhost:PORT to view an app on your computer, replace localhost with the computer's MagicDNS from the Tailscale app (e.g. your-computer.tailnet-name.ts.net)*

Use the PostgreSQL app to view databases for your projects <https://apps.apple.com/us/app/postgresql-client/id1233662353>

On your computer, bookmark the sites you refer to during development (e.g. Google OAuth, GitHub) to make it easier to reference from your phone. I use the Chrome app to seamlessly access the sites I need.

Please contibute your best practices! I am looking forward to seeing all the places you will code!

I'm new to the world of hacking - so please share your ideas, feedback, and questions - you will help me learn! Please connect at [rmb1@wharton.upenn.edu](mailto:rmb1@wharton.upenn.edu) or <https://www.linkedin.com/in/ryan-bergamini-223606107/>