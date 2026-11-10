---
title: "6-Day and IP Address Certificates Are Generally Available"
url: https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability
clipped: 2026-06-17 01:57:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [6-Day and IP Address Certificates Are Generally Available](https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability)

## Digest Summary
Let’s Encrypt now offers two new certificate types that are generally available:

- **Short‑lived certificates**: valid for 160 hours (≈6 days). They are obtained by selecting the “shortlived” profile in an ACME client. The reduced lifespan forces more frequent domain validation, limiting the impact of compromised private keys and mitigating the unreliability of revocation, which previously left certificates vulnerable for up to 90 days. These certificates are optional; they are not the default, and adoption depends on fully automated renewal processes.

- **IP‑address certificates**: enable TLS authentication for servers accessed via IPv4 or IPv6 addresses rather than hostnames. They are required to be short‑lived because IP addresses tend to be more transient, necessitating more frequent validation.

The default certificate lifetime will be lowered from 90 days to 45 days over the coming years. Development was supported by the Open Technology Fund, Sovereign Tech Agency, and other sponsors.

## Discussion Summary
The discussion highlights strong interest in IP‑address certificates for self‑hosted services, noting that tools like lego and acme.sh can obtain them while certbot lacks support. Contributors appreciate the ability to avoid bootstrap domains and see potential for iOS DoH setups, yet many question the six‑day validity, deeming it overly short for static VPS IPs and raising concerns about renewal reliability and possible denial‑of‑service risks. Additional points include calls for .onion support, skepticism about broader usefulness, and worries about security implications such as BGP hijacking.

---

## Full Article

> **Update: March 11, 2026**
>
> If you use Certbot, see [Six-Day and IP Address Certificates Available in Certbot](https://letsencrypt.org/2026/03/11/shorter-certs-certbot) for details on requesting these certificates.

Short-lived and IP address certificates are now generally available from Let’s Encrypt. These certificates are valid for 160 hours, just over six days. In order to get a short-lived certificate subscribers simply need to select the ‘shortlived’ [certificate profile](https://letsencrypt.org/docs/profiles/) in their ACME client.

Short-lived certificates improve security by requiring more frequent validation and reducing reliance on unreliable revocation mechanisms. If a certificate’s private key is exposed or compromised, revocation has historically been the way to mitigate damage prior to the certificate’s expiration. Unfortunately, revocation is an unreliable system so many relying parties continue to be vulnerable until the certificate expires, a period as long as 90 days. With short-lived certificates that vulnerability window is greatly reduced.

Short-lived certificates are opt-in and we have no plan to make them the default at this time. Subscribers that have fully automated their renewal process should be able to switch to short-lived certificates easily if they wish, but we understand that not everyone is in that position and generally comfortable with this significantly shorter lifetime. We hope that over time everyone moves to automated solutions and we can demonstrate that short-lived certificates work well.

Our default certificate lifetimes will be going from 90 days down to 45 days over the next few years, [as previously announced](https://letsencrypt.org/2025/12/02/from-90-to-45).

IP address certificates allow server operators to authenticate TLS connections to IP addresses rather than domain names. Let’s Encrypt supports both IPv4 and IPv6. IP address certificates must be short-lived certificates, a decision we made because IP addresses are more transient than domain names, so validating more frequently is important. You can learn more about our IP address certificates and the use cases for them from our [post announcing our first IP Certificate](https://letsencrypt.org/2025/07/01/issuing-our-first-ip-address-certificate).

We’d like to thank the Open Technology Fund and Sovereign Tech Agency, along with our [Sponsors](https://www.abetterinternet.org/sponsors/) and Donors, for supporting the development of this work.