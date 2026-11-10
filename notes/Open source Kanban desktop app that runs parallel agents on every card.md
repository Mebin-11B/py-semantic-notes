---
title: "Open source Kanban desktop app that runs parallel agents on every card"
url: https://www.kanbots.dev/
clipped: 2026-06-17 00:58:55
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Open source Kanban desktop app that runs parallel agents on every card](https://www.kanbots.dev/)

## Digest Summary
The document outlines three candidate designs for a password‑reset mechanism:

- **Single‑use JWT**: Uses an HS256‑signed JSON Web Token, valid for 15 minutes and intended for one‑time use.  
- **Database‑stored opaque token**: A random token persisted in a database, expires after 1 hour, and can be revoked manually.  
- **Magic‑link only**: No explicit token; the reset link itself is sent to the user’s verified email and serves as the authentication step.

The author notes that trade‑offs among these options will be explained subsequently, and seeks clarification on which design aligns with the target security requirements.

## Discussion Summary
Comments show strong interest in kanban‑style orchestration of AI agents, especially features like remote support, IDE integration, and local‑first operation, with several users noting similar internal tools and open‑source projects. However, many express frustration over buggy implementations, broken links, poor mobile performance, and the need for supervision, citing Vibe Kanban’s stalled development and pricing concerns. There is a recurring call for better conflict handling, clearer documentation, and more stable, self‑hosted solutions, while overall sentiment remains cautiously optimistic about the concept’s potential.

---

## Full Article

I've drafted three approaches for the password reset token. Which one fits your security requirements?

1Single-use JWT signed with HS256, 15 min expiry2DB-stored opaque token, 1 hour expiry, revocable3Magic link only — no token, email-verified login4I'll explain the tradeoffs firstDismiss