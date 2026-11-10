---
title: "Cloudflare Turnstile requiring fingerprintable WebGL"
url: https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting
clipped: 2026-06-17 00:54:23
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cloudflare Turnstile requiring fingerprintable WebGL](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting)

## Digest Summary
Cloudflare Turnstile now requires a readable WebGL fingerprint to verify human users. WebKit‑GTK browsers block or randomize such fingerprinting, causing the Turnstile challenge to loop indefinitely and deny access to sites that use it. Cloudflare’s documentation claims the fingerprint is needed for bot detection and that allowing fingerprinting will resolve the issue. The policy appears to exempt Safari, while other WebKit implementations remain blocked. Firefox’s recent changes (Bug 1916271) expose sanitized GPU characteristics, but its “privacy.resistFingerprinting” setting does not fully disable WebGL fingerprinting even under strict privacy modes, potentially preventing Firefox users from passing Turnstile in the future. The author notes that Mozilla’s privacy controls are insufficient for this specific test, and that both WebKit and Blink browsers return hard‑coded strings for GPU data, whereas Firefox now provides more detailed information. Consequently, users of WebKitGTK and privacy‑focused Firefox configurations encounter persistent verification failures on Cloudflare‑protected sites.

## Discussion Summary
Comments express widespread frustration with Cloudflare’s reliance on browser fingerprinting, particularly in Turnstile challenges, which many see as invasive and detrimental to privacy‑focused browsers. Users report broken functionality, increased barriers for non‑Chrome agents, and describe the approach as a gatekeeping measure that forces trade‑offs between security and usability. Several suggest alternative mitigations such as proof‑of‑work or less aggressive fingerprinting, while acknowledging that spoofing techniques exist but are not universally effective. Overall sentiment is negative, calling for more transparent or less restrictive bot‑defense methods.

---

## Full Article

Since about a week, Cloudflare Turnstile (their "Verify you're human"
device verification) has been looping indefinitely in my
[webkit-gtk based browser](https://hacktivis.me/projects/badwolf).
Preventing access to quite few websites ([previously](https://hacktivis.me/articles/blocking%20cloudflare%20IP-range%20be%20like), but it even went worse lately).
  
Turns out it's because Cloudflare wants to have a fingerprint of your
device via WebGL, the only reason for doing this would be tracking.

![](https://hacktivis.me/images/cloudflare-webgl-fingerprinting.png?serial=2026053100)


Screenshot of [Turnstile test page](https://browser-compat.turnstile.workers.dev/), "WebGL renderer info is spoofed"

Their pro-tracking non-justification copied here just in case:

> Turnstile uses browser fingerprinting to verify you're human.
> Privacy tools that block or randomize fingerprinting make
> your browser look like a bot trying to hide its identity.
> Temporarily allowing fingerprinting for this site will fix the issue.

Such things are blocked in WebKit, and have been for years.
Meaning it's tracking so awful that even Apple would block it,
and as far as I can tell it's not the kind of privacy protection
you can easily disable in it.  
So Cloudflare just **banned all WebKitGTK browsers** as I guess they
put an exception for Safari.

As an aside, if you're wondering, Mozilla Firefox screwed up their
WebGL fingerprinting protection:
[Bugzilla#1916271: Gecko reveals sanitized GPU Characteristics; webkit and blink return hardcoded strings for all users](https://bugzilla.mozilla.org/show_bug.cgi?id=1916271)

![](https://hacktivis.me/images/cloudflare-webgl-fingerprinting-firefox-default.png?serial=2026053100)


Screenshot of Turnstile test page on Firefox 145.0 passing with no issues.

Plus `privacy.resistfingerprinting` isn't enabled even
when selecting "Strict" "Enhanced Privacy Protection" in the settings,
great job there Mozilla.  
But I guess with it enabled, privacy-conscious Firefox users might
not be able to pass Cloudflare's device verification in the future.

![](https://hacktivis.me/images/cloudflare-webgl-fingerprinting-firefox-much-resist.png?serial=2026053100)


Screenshot of Turnstile test page on Firefox 145.0 passing with just "Canvas Randomization Detected"; after enabling `privacy.resistfingerprinting` manually.