---
title: "RFC 10015: Deprecating Obsolete Key Exchange Methods in TLS 1.2 and DTLS 1.2"
url: https://www.rfc-editor.org/rfc/rfc10015.html
clipped: 2026-08-31 12:22:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [RFC 10015: Deprecating Obsolete Key Exchange Methods in TLS 1.2 and DTLS 1.2](https://www.rfc-editor.org/rfc/rfc10015.html)

## Digest Summary
RFC 10015 deprecates obsolete key‑exchange methods in TLS 1.2 and DTLS 1.2. It identifies security and interoperability issues with finite‑field DH (FFDHE/FFD H) and RSA key exchange:


Finite‑field DH (FFDHE): lacks group‑negotiation, leading to incompatibility; custom or small groups may contain weak sub‑groups; many implementations still use 1024‑bit groups, providing only a narrow margin against the current 795‑bit discrete‑log record; a few large‑scale computations can break traffic using standardized groups; non‑ephemeral or partially‑ephemeral use is vulnerable to the Raccoon timing side‑channel unless constant‑time mitigations are applied.


RSA key exchange: provides no forward secrecy; susceptible to Bleichenbacher‑type attacks (e.g., ROBOT, DROWN) because correct countermeasures are hard to implement; lacks domain separation, so a compromised RSA key endangers all endpoints sharing it.


The document updates multiple TLS‑related RFCs, aligns with BCP 195, and specifies deprecation of the affected cipher suites in sections 5.2‑5.5. All other BCP recommendations remain unchanged.

---

## Full Article

RFC 10015
Deprecating Obsolete Key Exchanges in (D
July 2026

Aviram
Standards Track
[Page]

Stream:
Internet Engineering Task Force (IETF)
RFC:
[10015](https://www.rfc-editor.org/rfc/rfc10015)
Updates:

[4162](https://www.rfc-editor.org/rfc/rfc4162), [4279](https://www.rfc-editor.org/rfc/rfc4279), [4346](https://www.rfc-editor.org/rfc/rfc4346), [4785](https://www.rfc-editor.org/rfc/rfc4785), [5246](https://www.rfc-editor.org/rfc/rfc5246), [5288](https://www.rfc-editor.org/rfc/rfc5288), [5289](https://www.rfc-editor.org/rfc/rfc5289), [5469](https://www.rfc-editor.org/rfc/rfc5469), [5487](https://www.rfc-editor.org/rfc/rfc5487), [5932](https://www.rfc-editor.org/rfc/rfc5932), [6209](https://www.rfc-editor.org/rfc/rfc6209), [6347](https://www.rfc-editor.org/rfc/rfc6347), [6367](https://www.rfc-editor.org/rfc/rfc6367), [6655](https://www.rfc-editor.org/rfc/rfc6655), [7905](https://www.rfc-editor.org/rfc/rfc7905), [8422](https://www.rfc-editor.org/rfc/rfc8422), [9325](https://www.rfc-editor.org/rfc/rfc9325) 
Category:
Standards Track
Published:

July 2026
    
ISSN:
2070-1721
Author:

      N. Aviram

# RFC 10015

# Deprecating Obsolete Key Exchange Methods in TLS 1.2 and DTLS 1.2

      

## [Abstract](https://www.rfc-editor.org/rfc/rfc10015.html#abstract)

For (D)TLS 1.2, this document deprecates the use of two key exchanges, namely Diffie-Hellman (DH) over
a finite field and RSA. It also discourages the use of static Elliptic Curve Diffie-Hellman (ECDH)
cipher suites.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-abstract-1)

These prescriptions apply only to (D)TLS 1.2, since (D)TLS 1.0 and TLS 1.1 are
deprecated by RFC 8996 and (D)TLS 1.3 either does not use the affected
algorithms or does not share the relevant configuration options.
(There is no DTLS version 1.1.)[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-abstract-2)

This document updates RFCs 4162, 4279, 4346, 4785, 5246, 5288, 5289, 5469,
5487, 5932, 6209, 6347, 6367, 6655, 7905, 8422, and 9325 to either deprecate or
discourage the use of cipher suites using the above key exchange
methods in (D)TLS 1.2 connections.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-abstract-3)

        

## 
[Status of This Memo](https://www.rfc-editor.org/rfc/rfc10015.html#name-status-of-this-memo)
        

            This is an Internet Standards Track document.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-boilerplate.1-1)

            This document is a product of the Internet Engineering Task Force
            (IETF).  It represents the consensus of the IETF community.  It has
            received public review and has been approved for publication by
            the Internet Engineering Steering Group (IESG).  Further
            information on Internet Standards is available in Section 2 of 
            RFC 7841.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-boilerplate.1-2)

            Information about the current status of this document, any
            errata, and how to provide feedback on it may be obtained at
            [https://www.rfc-editor.org/info/rfc10015](https://www.rfc-editor.org/info/rfc10015).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-boilerplate.1-3)

        

## 
[Copyright Notice](https://www.rfc-editor.org/rfc/rfc10015.html#name-copyright-notice)
        

            Copyright (c) 2026 IETF Trust and the persons identified as the
            document authors. All rights reserved.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-boilerplate.2-1)

            This document is subject to BCP 78 and the IETF Trust's Legal
            Provisions Relating to IETF Documents
            ([https://trustee.ietf.org/license-info](https://trustee.ietf.org/license-info)) in effect on the date of
            publication of this document. Please review these documents
            carefully, as they describe your rights and restrictions with
            respect to this document. Code Components extracted from this
            document must include Revised BSD License text as described in
            Section 4.e of the Trust Legal Provisions and are provided without
            warranty as described in the Revised BSD License.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-boilerplate.2-2)

        [â²](https://www.rfc-editor.org/rfc/rfc10015.html#)

## 
[Table of Contents](https://www.rfc-editor.org/rfc/rfc10015.html#name-table-of-contents)
        

      

## 
[1.](https://www.rfc-editor.org/rfc/rfc10015.html#section-1)[Introduction](https://www.rfc-editor.org/rfc/rfc10015.html#name-introduction)
      

(D)TLS 1.2 supports a variety of key exchange algorithms, including RSA, Diffie-Hellman (DH)
over a finite field, and Elliptic Curve Diffie-Hellman (ECDH).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-1)

DH key exchange, over any group, comes in ephemeral and non-ephemeral
varieties. Non-ephemeral DH algorithms use static DH public keys included in
the authenticating peer's certificate; see [[RFC4492](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4492)] for discussion.  In
contrast, ephemeral DH algorithms use ephemeral DH public keys sent in the
handshake and authenticated by the peer's certificate.  Ephemeral and non-ephemeral finite field DH
algorithms are called DHE and DH (or FFDHE and FFDH), respectively,
and ephemeral and non-ephemeral elliptic curve DH algorithms are
called ECDHE and ECDH, respectively [[RFC4492](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4492)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-2)

In general, non-ephemeral cipher suites are not recommended due to their lack of
forward secrecy. Moreover, as demonstrated by the Raccoon attack [[RACCOON](https://www.rfc-editor.org/rfc/rfc10015.html#RACCOON)] on finite field DH, public key reuse (either via non-ephemeral cipher suites or reused keys with
ephemeral cipher suites) can lead to timing side channels that may leak connection
secrets. For ECDH, invalid curve attacks similarly exploit secret
reuse in order to break security [[ICA](https://www.rfc-editor.org/rfc/rfc10015.html#ICA)], further demonstrating the risk of reusing
public keys. While both side channels can be avoided in implementations, experience
shows that in practice, implementations may fail to thwart such attacks due to the
complexity and number of the required mitigations.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-3)

Additionally, RSA key exchange suffers from security problems that are independent
of implementation choices as well as problems that stem purely from the difficulty
of implementing security countermeasures correctly.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-4)

At a rough glance, the problems affecting FFDHE in (D)TLS 1.2 are as follows:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-5)

- 
          

FFDHE suffers from interoperability problems because there is no mechanism for
negotiating the group, and some implementations only support small group sizes
(see [[RFC7919](https://www.rfc-editor.org/rfc/rfc10015.html#RFC7919)], [Section 1](https://rfc-editor.org/rfc/rfc7919#section-1)).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-6.1.1)

        
- 
          

FFDHE groups may have small subgroups, which enables several attacks
[[SUBGROUPS](https://www.rfc-editor.org/rfc/rfc10015.html#SUBGROUPS)]. When presented with a custom, non-standardized FFDHE group, a handshaking client cannot practically verify that the group chosen by the server does not suffer from this problem. There is also no mechanism for such handshakes to fall back to other key exchange parameters that are acceptable to the client.
Custom FFDHE groups are widespread (as a result of advice based on [[WEAK-DH](https://www.rfc-editor.org/rfc/rfc10015.html#WEAK-DH)]).
Therefore, clients cannot simply reject handshakes that present custom, and thus potentially dangerous, groups.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-6.2.1)

        
- 
          

In practice, some operators use 1024-bit FFDHE groups since this is the
maximum size that ensures wide support (see [[RFC7919](https://www.rfc-editor.org/rfc/rfc10015.html#RFC7919)], [Section 1](https://rfc-editor.org/rfc/rfc7919#section-1)).
This size leaves only a small security margin versus the current discrete log record,
which stands at 795 bits [[DLOG795](https://www.rfc-editor.org/rfc/rfc10015.html#DLOG795)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-6.3.1)

        
- 
          

Expanding on the previous point, just a handful of very large computations allow
an attacker to cheaply decrypt a relatively large fraction of FFDHE traffic
(namely, traffic encrypted using particular standardized groups) [[WEAK-DH](https://www.rfc-editor.org/rfc/rfc10015.html#WEAK-DH)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-6.4.1)

        
- 
          

When secrets are not fully ephemeral, FFDHE suffers from the Raccoon side-channel attack [[RACCOON](https://www.rfc-editor.org/rfc/rfc10015.html#RACCOON)]. (Note that FFDH is inherently vulnerable to the Raccoon attack
unless constant-time mitigations are employed.)[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-6.5.1)

      

The problems affecting RSA key exchange in (D)TLS 1.2 are as follows:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-7)

- 
          

RSA key exchange offers no forward secrecy, by construction.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-8.1.1)

        
- 
          

RSA key exchange may be vulnerable to Bleichenbacher's attack [[BLEI](https://www.rfc-editor.org/rfc/rfc10015.html#BLEI)].
Experience shows that variants of this attack arise every few years because
implementing the relevant countermeasure correctly is difficult (see
[[ROBOT](https://www.rfc-editor.org/rfc/rfc10015.html#ROBOT)], [[NEW-BLEI](https://www.rfc-editor.org/rfc/rfc10015.html#NEW-BLEI)], and [[DROWN](https://www.rfc-editor.org/rfc/rfc10015.html#DROWN)]).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-8.2.1)

        
- 
          

In addition to the above point, there is no convenient mechanism in (D)TLS 1.2 for
the domain separation of keys. Therefore, a single endpoint that is vulnerable to
Bleichenbacher's attack would affect all endpoints sharing the same RSA key (see
[[XPROT](https://www.rfc-editor.org/rfc/rfc10015.html#XPROT)] and [[DROWN](https://www.rfc-editor.org/rfc/rfc10015.html#DROWN)]).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-8.3.1)

      

This document updates 
[[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)], [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)], [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)], [[RFC4785](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4785)], [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)], [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)], [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)], [[RFC5469](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5469)], [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)], [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)], [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)], [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)], [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)], [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)], [[RFC7905](https://www.rfc-editor.org/rfc/rfc10015.html#RFC7905)], [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)], and [[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)] to remediate the above problems, by deprecating and discouraging the use of affected cipher suites, as listed in Sections [5.2](https://www.rfc-editor.org/rfc/rfc10015.html#ecdhcs), [5.3](https://www.rfc-editor.org/rfc/rfc10015.html#dhecs), [5.4](https://www.rfc-editor.org/rfc/rfc10015.html#rsacs), and [5.5](https://www.rfc-editor.org/rfc/rfc10015.html#cert).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-9)

BCP 195 [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)] [[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)] contains the latest IETF recommendations for users of the (D)TLS protocol (and specifically, (D)TLS 1.2), and this
document updates [[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)] in several points. [Section 6](https://www.rfc-editor.org/rfc/rfc10015.html#update-9325) details the exact differences.
All other recommendations in the BCP documents remain valid.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1-10)

        

### 
[1.1.](https://www.rfc-editor.org/rfc/rfc10015.html#section-1.1)[Requirements Language](https://www.rfc-editor.org/rfc/rfc10015.html#name-requirements-language)
        

    The key words "MUST", "MUST NOT",
    "REQUIRED", "SHALL", "SHALL NOT",
    "SHOULD", "SHOULD NOT",
    "RECOMMENDED", "NOT RECOMMENDED",
    "MAY", and "OPTIONAL" in this document are to be
    interpreted as described in BCPÂ 14 [[RFC2119](https://www.rfc-editor.org/rfc/rfc10015.html#RFC2119)] [[RFC8174](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8174)] when, and only when, they appear in all capitals, as
    shown here.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-1.1-1)

      

## 
[2.](https://www.rfc-editor.org/rfc/rfc10015.html#section-2)[Non-Ephemeral Diffie-Hellman](https://www.rfc-editor.org/rfc/rfc10015.html#name-non-ephemeral-diffie-hellma)
      

Clients MUST NOT offer and servers MUST NOT select non-ephemeral FFDH cipher suites in (D)TLS 1.2 connections.
(Note that (D)TLS 1.0 and TLS 1.1 are deprecated by [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)], and (D)TLS 1.3 does not
support FFDH [[RFC9846](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9846)] [[RFC9147](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9147)].) This includes all cipher suites listed in [Table 1](https://www.rfc-editor.org/rfc/rfc10015.html#deprecated-cs) in
[Section 5.1](https://www.rfc-editor.org/rfc/rfc10015.html#dhcs).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-2-1)

Clients SHOULD NOT offer and servers SHOULD NOT select non-ephemeral ECDH cipher suites in (D)TLS 1.2 connections. (This requirement is already present in [[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)].
Note that (D)TLS 1.0 and TLS 1.1 are deprecated by [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)], and
(D)TLS 1.3 does not support ECDH [[RFC9846](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9846)] [[RFC9147](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9147)].) This includes all cipher suites listed
in [Table 2](https://www.rfc-editor.org/rfc/rfc10015.html#discouraged-cs) in [Section 5.2](https://www.rfc-editor.org/rfc/rfc10015.html#ecdhcs).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-2-2)

In addition, to avoid the use of non-ephemeral DH, clients SHOULD NOT use and servers SHOULD NOT accept certificates with fixed DH parameters. These certificate types are rsa_fixed_dh, dss_fixed_dh, rsa_fixed_ecdh, and ecdsa_fixed_ecdh as listed in [Section 5.5](https://www.rfc-editor.org/rfc/rfc10015.html#cert). These values only apply to (D)TLS versions of 1.2 and below.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-2-3)

      

## 
[3.](https://www.rfc-editor.org/rfc/rfc10015.html#section-3)[Ephemeral Finite Field Diffie-Hellman](https://www.rfc-editor.org/rfc/rfc10015.html#name-ephemeral-finite-field-diff)
      

Clients MUST NOT offer and servers MUST NOT select FFDHE cipher suites in (D)TLS 1.2 connections.
This includes all cipher suites listed in [Table 3](https://www.rfc-editor.org/rfc/rfc10015.html#deprecated-dhe-cs) in [Section 5.3](https://www.rfc-editor.org/rfc/rfc10015.html#dhecs).
(Note that (D)TLS 1.0 and TLS 1.1 are deprecated by [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)].) FFDHE cipher suites in (D)TLS 1.3 do not suffer from the problems presented in [Section 1](https://www.rfc-editor.org/rfc/rfc10015.html#introduction); see [[RFC9846](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9846)] and [[RFC9147](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9147)]. Therefore, clients and servers MAY offer FFDHE cipher suites in (D)TLS 1.3 connections.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-3-1)

      

## 
[4.](https://www.rfc-editor.org/rfc/rfc10015.html#section-4)[RSA](https://www.rfc-editor.org/rfc/rfc10015.html#name-rsa)
      

Clients MUST NOT offer and servers MUST NOT select RSA cipher suites in (D)TLS 1.2
connections. (Note that (D)TLS 1.0 and TLS 1.1 are deprecated by [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)], and (D)TLS
1.3 does not support static RSA [[RFC9846](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9846)] [[RFC9147](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9147)].) This includes all cipher suites
listed in [Table 4](https://www.rfc-editor.org/rfc/rfc10015.html#deprecated-rha-cs) in [Section 5.4](https://www.rfc-editor.org/rfc/rfc10015.html#rsacs). Note that these cipher suites were previously
marked as not recommended in the "TLS Cipher Suites" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-4-1)

      

## 
[5.](https://www.rfc-editor.org/rfc/rfc10015.html#section-5)[Updates to Cipher Suites and TLS ClientCertificateType Identifiers](https://www.rfc-editor.org/rfc/rfc10015.html#name-updates-to-cipher-suites-an)
      

The following subsections mention the use of "D" in the "Recommended" column of the "TLS Cipher Suites" and "TLS ClientCertificateType Identifiers" registries [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]. See [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)] for information on the use of the "D".[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-5-1)

        

### 
[5.1.](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.1)[DH Cipher Suites Deprecated by This Document](https://www.rfc-editor.org/rfc/rfc10015.html#name-dh-cipher-suites-deprecated)
        

IANA has set the "Recommended" column to "D" and added this document as a reference for the following entries in the "TLS Cipher Suites" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.1-1)

          [Table 1](https://www.rfc-editor.org/rfc/rfc10015.html#table-1)

            
              Cipher Suite
              Reference
            
          
          
            
              TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_DH_DSS_WITH_DES_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_DH_RSA_WITH_DES_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_anon_EXPORT_WITH_RC4_40_MD5
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_DH_anon_WITH_RC4_128_MD5
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_DH_anon_WITH_DES_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_DH_anon_WITH_3DES_EDE_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_DSS_WITH_AES_128_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_RSA_WITH_AES_128_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_anon_WITH_AES_128_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_DSS_WITH_AES_256_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_RSA_WITH_AES_256_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_anon_WITH_AES_256_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_DSS_WITH_AES_128_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_RSA_WITH_AES_128_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_DSS_WITH_AES_256_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_RSA_WITH_AES_256_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_anon_WITH_AES_128_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_anon_WITH_AES_256_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_DSS_WITH_SEED_CBC_SHA
              
                [[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)]

            
            
              TLS_DH_RSA_WITH_SEED_CBC_SHA
              
                [[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)]

            
            
              TLS_DH_anon_WITH_SEED_CBC_SHA
              
                [[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)]

            
            
              TLS_DH_RSA_WITH_AES_128_GCM_SHA256
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DH_RSA_WITH_AES_256_GCM_SHA384
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DH_DSS_WITH_AES_128_GCM_SHA256
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DH_DSS_WITH_AES_256_GCM_SHA384
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DH_anon_WITH_AES_128_GCM_SHA256
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DH_anon_WITH_AES_256_GCM_SHA384
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_anon_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_anon_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_anon_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_anon_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DH_RSA_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DH_RSA_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DH_DSS_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DH_DSS_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DH_anon_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DH_anon_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
          
        

        

### 
[5.2.](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.2)[ECDH Cipher Suites Whose Use Is Discouraged by This Document](https://www.rfc-editor.org/rfc/rfc10015.html#name-ecdh-cipher-suites-whose-us)
        

[[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)] specifies that implementations SHOULD NOT negotiate the following cipher suites; accordingly, they appeared with "N" in the "Recommended" column in the IANA "TLS Cipher Suites" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]. Per this document, IANA has updated them to have "D" in the "Recommended" column to align with [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)] (and added this document as a reference for each). This document also records the rationale for discouraging use of these cipher suites, and it cites prior analyses and attacks that demonstrate the associated risks (see [Section 8](https://www.rfc-editor.org/rfc/rfc10015.html#sec-considerations)).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.2-1)

          [Table 2](https://www.rfc-editor.org/rfc/rfc10015.html#table-2)

            
              Cipher Suite
              Reference
            
          
          
            
              TLS_ECDH_ECDSA_WITH_NULL_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_ECDSA_WITH_RC4_128_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_RSA_WITH_NULL_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_RSA_WITH_RC4_128_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_RSA_WITH_AES_128_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_RSA_WITH_AES_256_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_anon_WITH_NULL_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_anon_WITH_RC4_128_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_anon_WITH_AES_128_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_anon_WITH_AES_256_CBC_SHA
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)]

            
            
              TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384
              
                [[RFC5289](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5289)]

            
            
              TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
          
        

        

### 
[5.3.](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.3)[DHE Cipher Suites Deprecated by This Document](https://www.rfc-editor.org/rfc/rfc10015.html#name-dhe-cipher-suites-deprecate)
        

IANA has set the "Recommended" column to "D" and added this document as a reference for the following entries in the "TLS Cipher Suites" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.3-1)

          [Table 3](https://www.rfc-editor.org/rfc/rfc10015.html#table-3)

            
              Cipher Suite
              Reference
            
          
          
            
              TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_DHE_DSS_WITH_DES_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_DHE_RSA_WITH_DES_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_PSK_WITH_NULL_SHA
              
                [[RFC4785](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4785)]

            
            
              TLS_DHE_DSS_WITH_AES_128_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_RSA_WITH_AES_128_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_DSS_WITH_AES_256_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_RSA_WITH_AES_256_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_DSS_WITH_AES_128_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_DSS_WITH_AES_256_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_PSK_WITH_RC4_128_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)]

            
            
              TLS_DHE_PSK_WITH_AES_128_CBC_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)]

            
            
              TLS_DHE_PSK_WITH_AES_256_CBC_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)]

            
            
              TLS_DHE_DSS_WITH_SEED_CBC_SHA
              
                [[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)]

            
            
              TLS_DHE_RSA_WITH_SEED_CBC_SHA
              
                [[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)]

            
            
              TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DHE_DSS_WITH_AES_256_GCM_SHA384
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_DHE_PSK_WITH_AES_128_GCM_SHA256
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_DHE_PSK_WITH_AES_256_GCM_SHA384
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_DHE_PSK_WITH_AES_128_CBC_SHA256
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_DHE_PSK_WITH_AES_256_CBC_SHA384
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_DHE_PSK_WITH_NULL_SHA256
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_DHE_PSK_WITH_NULL_SHA384
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_DSS_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_DSS_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_DHE_RSA_WITH_AES_128_CCM
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_DHE_RSA_WITH_AES_256_CCM
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_DHE_RSA_WITH_AES_128_CCM_8
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_DHE_RSA_WITH_AES_256_CCM_8
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_DHE_PSK_WITH_AES_128_CCM
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_DHE_PSK_WITH_AES_256_CCM
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256
              
                [[RFC7905](https://www.rfc-editor.org/rfc/rfc10015.html#RFC7905)]

            
            
              TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256
              
                [[RFC7905](https://www.rfc-editor.org/rfc/rfc10015.html#RFC7905)]

            
            
              TLS_PSK_DHE_WITH_AES_128_CCM_8
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_PSK_DHE_WITH_AES_256_CCM_8
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
          
        

        

### 
[5.4.](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.4)[RSA Cipher Suites Deprecated by This Document](https://www.rfc-editor.org/rfc/rfc10015.html#name-rsa-cipher-suites-deprecate)
        

IANA has set the "Recommended" column to "D" and added this document as a reference for the following entries in the "TLS Cipher Suites" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.4-1)

          [Table 4](https://www.rfc-editor.org/rfc/rfc10015.html#table-4)

            
              Cipher Suite
              Reference
            
          
          
            
              TLS_RSA_WITH_NULL_MD5
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_WITH_NULL_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_EXPORT_WITH_RC4_40_MD5
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_RSA_WITH_RC4_128_MD5
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_RSA_WITH_RC4_128_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_RSA_WITH_IDEA_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_RSA_EXPORT_WITH_DES40_CBC_SHA
              
                [[RFC4346](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4346)]

            
            
              TLS_RSA_WITH_DES_CBC_SHA
              
                [[RFC8996](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8996)]

            
            
              TLS_RSA_WITH_3DES_EDE_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_PSK_WITH_NULL_SHA
              
                [[RFC4785](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4785)]

            
            
              TLS_RSA_WITH_AES_128_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_WITH_AES_256_CBC_SHA
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_WITH_NULL_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_WITH_AES_128_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_WITH_AES_256_CBC_SHA256
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)]

            
            
              TLS_RSA_WITH_CAMELLIA_128_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_RSA_WITH_CAMELLIA_256_CBC_SHA
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_RSA_PSK_WITH_RC4_128_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)] [[RFC6347](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6347)]

            
            
              TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)]

            
            
              TLS_RSA_PSK_WITH_AES_128_CBC_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)]

            
            
              TLS_RSA_PSK_WITH_AES_256_CBC_SHA
              
                [[RFC4279](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4279)]

            
            
              TLS_RSA_WITH_SEED_CBC_SHA
              
                [[RFC4162](https://www.rfc-editor.org/rfc/rfc10015.html#RFC4162)]

            
            
              TLS_RSA_WITH_AES_128_GCM_SHA256
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_RSA_WITH_AES_256_GCM_SHA384
              
                [[RFC5288](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5288)]

            
            
              TLS_RSA_PSK_WITH_AES_128_GCM_SHA256
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_RSA_PSK_WITH_AES_256_GCM_SHA384
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_RSA_PSK_WITH_AES_128_CBC_SHA256
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_RSA_PSK_WITH_AES_256_CBC_SHA384
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_RSA_PSK_WITH_NULL_SHA256
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_RSA_PSK_WITH_NULL_SHA384
              
                [[RFC5487](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5487)]

            
            
              TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256
              
                [[RFC5932](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5932)]

            
            
              TLS_RSA_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384
              
                [[RFC6209](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6209)]

            
            
              TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384
              
                [[RFC6367](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6367)]

            
            
              TLS_RSA_WITH_AES_128_CCM
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_RSA_WITH_AES_256_CCM
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_RSA_WITH_AES_128_CCM_8
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_RSA_WITH_AES_256_CCM_8
              
                [[RFC6655](https://www.rfc-editor.org/rfc/rfc10015.html#RFC6655)]

            
            
              TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256
              
                [[RFC7905](https://www.rfc-editor.org/rfc/rfc10015.html#RFC7905)]

            
          
        

        

### 
[5.5.](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.5)[TLS ClientCertificateType Identifiers Deprecated by This Document](https://www.rfc-editor.org/rfc/rfc10015.html#name-tls-clientcertificatetype-i)
        

IANA has set the "Recommended" column to "D" and added this document as a reference for the following entries in the "TLS ClientCertificateType Identifiers" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-5.5-1)

          [Table 5](https://www.rfc-editor.org/rfc/rfc10015.html#table-5)

            
              Certificate Type
              Reference
            
          
          
            
              rsa_fixed_dh (3)
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)] [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)]

            
            
              dss_fixed_dh (4)
              
                [[RFC5246](https://www.rfc-editor.org/rfc/rfc10015.html#RFC5246)] [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)]

            
            
              rsa_fixed_ecdh (65)
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)] [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)]

            
            
              ecdsa_fixed_ecdh (66)
              
                [[RFC8422](https://www.rfc-editor.org/rfc/rfc10015.html#RFC8422)] [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)]

            
          
        

      

## 
[6.](https://www.rfc-editor.org/rfc/rfc10015.html#section-6)[Updates to RFC 9325](https://www.rfc-editor.org/rfc/rfc10015.html#name-updates-to-rfc-9325)
      

This document updates [[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)] with respect to the use of (D)TLS 1.2, and [Table 6](https://www.rfc-editor.org/rfc/rfc10015.html#rfc9325-updates)
lists the exact changes. All of these changes are made in [Section 4.1](https://rfc-editor.org/rfc/rfc9325#section-4.1) of [[RFC9325](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9325)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-6-1)

        [Table 6](https://www.rfc-editor.org/rfc/rfc10015.html#table-6)

          
            
            RFC 9325
            RFC 10015
          
        
        
          
            Non-ephemeral FFDH
            
              SHOULD NOT

            
              MUST NOT

          
          
            Non-ephemeral ECDH
            
              SHOULD NOT

            No change
          
          
            Fixed DH certificate types
            Unspecified
            
              SHOULD NOT

          
          
            Ephemeral FFDH
            
              SHOULD NOT

            
              MUST NOT

          
          
            Static RSA
            
              SHOULD NOT

            
              MUST NOT

          
        
      

      

## 
[7.](https://www.rfc-editor.org/rfc/rfc10015.html#section-7)[IANA Considerations](https://www.rfc-editor.org/rfc/rfc10015.html#name-iana-considerations)
      

The "TLS Cipher Suites" and "TLS ClientCertificateType Identifiers" registries both appear within the "Transport Layer Security (TLS) Parameters" registry group [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)]. IANA has updated entries in the "TLS Cipher Suites" registry [[TLS-REGISTRY](https://www.rfc-editor.org/rfc/rfc10015.html#TLS-REGISTRY)] as indicated in Sections [5.1](https://www.rfc-editor.org/rfc/rfc10015.html#dhcs), [5.2](https://www.rfc-editor.org/rfc/rfc10015.html#ecdhcs), [5.3](https://www.rfc-editor.org/rfc/rfc10015.html#dhecs), and [5.4](https://www.rfc-editor.org/rfc/rfc10015.html#rsacs). IANA has also updated entries in the "TLS ClientCertificateType Identifiers" registry as indicated in [Section 5.5](https://www.rfc-editor.org/rfc/rfc10015.html#cert).[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-7-1)

For each entry listed in Sections [5.1](https://www.rfc-editor.org/rfc/rfc10015.html#dhcs), [5.2](https://www.rfc-editor.org/rfc/rfc10015.html#ecdhcs), [5.3](https://www.rfc-editor.org/rfc/rfc10015.html#dhecs), [5.4](https://www.rfc-editor.org/rfc/rfc10015.html#rsacs), and [5.5](https://www.rfc-editor.org/rfc/rfc10015.html#cert),
IANA has set the "Recommended" column to "D" and updated the entry's Reference column to refer to this document. For information about the use of "D" in the "Recommended" column, see [[RFC9847](https://www.rfc-editor.org/rfc/rfc10015.html#RFC9847)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-7-2)

      

## 
[8.](https://www.rfc-editor.org/rfc/rfc10015.html#section-8)[Security Considerations](https://www.rfc-editor.org/rfc/rfc10015.html#name-security-considerations)
      

Non-ephemeral finite field DH cipher suites (TLS_DH_*), as well as ephemeral key reuse
for finite field DH cipher suites, are prohibited due to the Raccoon attack [[RACCOON](https://www.rfc-editor.org/rfc/rfc10015.html#RACCOON)]. Both are
already considered bad practice since they do not provide forward secrecy. However,
the Raccoon attack revealed that timing side channels in processing TLS premaster secrets may be
exploited to reveal the encrypted premaster secret.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-1)

As for non-ephemeral ECDH cipher suites (TLS_ECDH_*), forgoing forward secrecy
not only allows retroactive decryption in the event of key compromise but may
also enable a broad category of attacks where the attacker exploits key reuse
to repeatedly query a cryptographic secret.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-2)

This category includes, but is not necessarily limited to, the following
examples:[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-3)

- 
          

Invalid curve attacks, where the attacker exploits key reuse to repeatedly
query and eventually learn the key itself. These attacks have been shown to be
practical against real-world TLS implementations [[ICA](https://www.rfc-editor.org/rfc/rfc10015.html#ICA)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-4.1.1)

        
- 
          

Side-channel attacks, where the attacker exploits key reuse and an additional
side channel to learn a cryptographic secret. For an example of such an attack,
refer to [[MAY4](https://www.rfc-editor.org/rfc/rfc10015.html#MAY4)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-4.2.1)

        
- 
          

Fault attacks, where the attacker exploits key reuse and incorrect
calculations to learn a cryptographic secret. For an example of such an attack,
see [[PARIS256](https://www.rfc-editor.org/rfc/rfc10015.html#PARIS256)].[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-4.3.1)

      

Such attacks are often implementation-dependent, including the above examples.
However, these examples demonstrate that building a system that reuses keys and
avoids this category of attacks is difficult in practice. In contrast, avoiding
key reuse not only prevents decryption in the event of key compromise, but it also
precludes this category of attacks altogether. Therefore, this document
discourages the reuse of ECDH public keys.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-5)

As for ephemeral finite field DH in (D)TLS 1.2 (TLS_DHE_* and TLS_PSK_DHE_*), as explained above, clients have no practical way to support these cipher suites while ensuring they only negotiate security parameters that are acceptable to them. In (D)TLS 1.2, the server chooses the DH group, and custom groups are prevalent. Therefore, once the client includes these cipher suites in its handshake and the server presents a custom group, the client cannot complete the handshake while ensuring security. Verifying the group structure is prohibitively expensive for the client. Using a safelist of known-good groups is also impractical, since server operators were encouraged to generate their own custom group. Further, there is no mechanism for the handshake to fall back to other parameters that are acceptable to both the client and server.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#section-8-6)

      

## 
[9.](https://www.rfc-editor.org/rfc/rfc10015.html#section-9)[References](https://www.rfc-editor.org/rfc/rfc10015.html#name-references)
      

        

### 
[9.1.](https://www.rfc-editor.org/rfc/rfc10015.html#section-9.1)[Normative References](https://www.rfc-editor.org/rfc/rfc10015.html#name-normative-references)
        

[RFC2119]
        
Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <[https://www.rfc-editor.org/info/rfc2119](https://www.rfc-editor.org/info/rfc2119)>. 

[RFC4162]
        
Lee, H.J., Yoon, J.H., and J.I. Lee, "Addition of SEED Cipher Suites to Transport Layer Security (TLS)", RFC 4162, DOI 10.17487/RFC4162, September 2005, <[https://www.rfc-editor.org/info/rfc4162](https://www.rfc-editor.org/info/rfc4162)>. 

[RFC4279]
        
Eronen, P., Ed. and H. Tschofenig, Ed., "Pre-Shared Key Ciphersuites for Transport Layer Security (TLS)", RFC 4279, DOI 10.17487/RFC4279, December 2005, <[https://www.rfc-editor.org/info/rfc4279](https://www.rfc-editor.org/info/rfc4279)>. 

[RFC4346]
        
Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.1", RFC 4346, DOI 10.17487/RFC4346, April 2006, <[https://www.rfc-editor.org/info/rfc4346](https://www.rfc-editor.org/info/rfc4346)>. 

[RFC4785]
        
Blumenthal, U. and P. Goel, "Pre-Shared Key (PSK) Ciphersuites with NULL Encryption for Transport Layer Security (TLS)", RFC 4785, DOI 10.17487/RFC4785, January 2007, <[https://www.rfc-editor.org/info/rfc4785](https://www.rfc-editor.org/info/rfc4785)>. 

[RFC5246]
        
Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, DOI 10.17487/RFC5246, August 2008, <[https://www.rfc-editor.org/info/rfc5246](https://www.rfc-editor.org/info/rfc5246)>. 

[RFC5288]
        
Salowey, J., Choudhury, A., and D. McGrew, "AES Galois Counter Mode (GCM) Cipher Suites for TLS", RFC 5288, DOI 10.17487/RFC5288, August 2008, <[https://www.rfc-editor.org/info/rfc5288](https://www.rfc-editor.org/info/rfc5288)>. 

[RFC5289]
        
Rescorla, E., "TLS Elliptic Curve Cipher Suites with SHA-256/384 and AES Galois Counter Mode (GCM)", RFC 5289, DOI 10.17487/RFC5289, August 2008, <[https://www.rfc-editor.org/info/rfc5289](https://www.rfc-editor.org/info/rfc5289)>. 

[RFC5469]
        
Eronen, P., Ed., "DES and IDEA Cipher Suites for Transport Layer Security (TLS)", RFC 5469, DOI 10.17487/RFC5469, February 2009, <[https://www.rfc-editor.org/info/rfc5469](https://www.rfc-editor.org/info/rfc5469)>. 

[RFC5487]
        
Badra, M., "Pre-Shared Key Cipher Suites for TLS with SHA-256/384 and AES Galois Counter Mode", RFC 5487, DOI 10.17487/RFC5487, March 2009, <[https://www.rfc-editor.org/info/rfc5487](https://www.rfc-editor.org/info/rfc5487)>. 

[RFC5932]
        
Kato, A., Kanda, M., and S. Kanno, "Camellia Cipher Suites for TLS", RFC 5932, DOI 10.17487/RFC5932, June 2010, <[https://www.rfc-editor.org/info/rfc5932](https://www.rfc-editor.org/info/rfc5932)>. 

[RFC6209]
        
Kim, W., Lee, J., Park, J., and D. Kwon, "Addition of the ARIA Cipher Suites to Transport Layer Security (TLS)", RFC 6209, DOI 10.17487/RFC6209, April 2011, <[https://www.rfc-editor.org/info/rfc6209](https://www.rfc-editor.org/info/rfc6209)>. 

[RFC6347]
        
Rescorla, E. and N. Modadugu, "Datagram Transport Layer Security Version 1.2", RFC 6347, DOI 10.17487/RFC6347, January 2012, <[https://www.rfc-editor.org/info/rfc6347](https://www.rfc-editor.org/info/rfc6347)>. 

[RFC6367]
        
Kanno, S. and M. Kanda, "Addition of the Camellia Cipher Suites to Transport Layer Security (TLS)", RFC 6367, DOI 10.17487/RFC6367, September 2011, <[https://www.rfc-editor.org/info/rfc6367](https://www.rfc-editor.org/info/rfc6367)>. 

[RFC6655]
        
McGrew, D. and D. Bailey, "AES-CCM Cipher Suites for Transport Layer Security (TLS)", RFC 6655, DOI 10.17487/RFC6655, July 2012, <[https://www.rfc-editor.org/info/rfc6655](https://www.rfc-editor.org/info/rfc6655)>. 

[RFC7905]
        
Langley, A., Chang, W., Mavrogiannopoulos, N., Strombergson, J., and S. Josefsson, "ChaCha20-Poly1305 Cipher Suites for Transport Layer Security (TLS)", RFC 7905, DOI 10.17487/RFC7905, June 2016, <[https://www.rfc-editor.org/info/rfc7905](https://www.rfc-editor.org/info/rfc7905)>. 

[RFC7919]
        
Gillmor, D., "Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for Transport Layer Security (TLS)", RFC 7919, DOI 10.17487/RFC7919, August 2016, <[https://www.rfc-editor.org/info/rfc7919](https://www.rfc-editor.org/info/rfc7919)>. 

[RFC8174]
        
Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, <[https://www.rfc-editor.org/info/rfc8174](https://www.rfc-editor.org/info/rfc8174)>. 

[RFC8422]
        
Nir, Y., Josefsson, S., and M. Pegourie-Gonnard, "Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS) Versions 1.2 and Earlier", RFC 8422, DOI 10.17487/RFC8422, August 2018, <[https://www.rfc-editor.org/info/rfc8422](https://www.rfc-editor.org/info/rfc8422)>. 

[RFC8996]
        
Moriarty, K. and S. Farrell, "Deprecating TLS 1.0 and TLS 1.1", BCP 195, RFC 8996, DOI 10.17487/RFC8996, March 2021, <[https://www.rfc-editor.org/info/rfc8996](https://www.rfc-editor.org/info/rfc8996)>. 

[RFC9147]
        
Rescorla, E., Tschofenig, H., and N. Modadugu, "The Datagram Transport Layer Security (DTLS) Protocol Version 1.3", RFC 9147, DOI 10.17487/RFC9147, April 2022, <[https://www.rfc-editor.org/info/rfc9147](https://www.rfc-editor.org/info/rfc9147)>. 

[RFC9325]
        
Sheffer, Y., Saint-Andre, P., and T. Fossati, "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 9325, DOI 10.17487/RFC9325, November 2022, <[https://www.rfc-editor.org/info/rfc9325](https://www.rfc-editor.org/info/rfc9325)>. 

[RFC9846]
        
Rescorla, E., "The Transport Layer Security (TLS) Protocol Version 1.3", RFC 9846, DOI 10.17487/RFC9846, July 2026, <[https://www.rfc-editor.org/info/rfc9846](https://www.rfc-editor.org/info/rfc9846)>. 

[RFC9847]
      
Salowey, J. and S. Turner, "IANA Registry Updates for TLS and DTLS", RFC 9847, DOI 10.17487/RFC9847, December 2025, <[https://www.rfc-editor.org/info/rfc9847](https://www.rfc-editor.org/info/rfc9847)>. 

        

### 
[9.2.](https://www.rfc-editor.org/rfc/rfc10015.html#section-9.2)[Informative References](https://www.rfc-editor.org/rfc/rfc10015.html#name-informative-references)
        

[BLEI]
        
Bleichenbacher, D., "Chosen Ciphertext Attacks against Protocols Based on the RSA Encryption Standard PKCS #1", Advances in Cryptology -- CRYPTO'98, Lecture Notes in Computer Science, vol. 1462, pp. 1-12, DOI 10.1007/BFb0055716, 1998, <[https://doi.org/10.1007/BFb0055716](https://doi.org/10.1007/BFb0055716)>. 

[DLOG795]
        
Boudot, F., Gaudry, P., Guillevic, A., Heninger, N., ThomÃ©, E., and P. Zimmermann, "Comparing the difficulty of factorization and discrete logarithm: a 240-digit experiment", Cryptology ePrint Archive, Paper 2020/697, DOI 10.1007/978-3-030-56880-1_3, 17 August 2020, <[https://eprint.iacr.org/2020/697](https://eprint.iacr.org/2020/697)>. 

[DROWN]
        
Aviram, N., Schinzel, S., Somorovsky, J., Heninger, N., Dankel, M., Steube, J., Valenta, L., Adrian, D., Halderman, J. A., Dukhovni, V., KÃ¤sper, E., Cohney, S., Engels, S., Paar, C., and Y. Shavitt, "DROWN: Breaking TLS using SSLv2", Proceedings of the 25th USENIX Security Symposium, August 2016, <[https://drownattack.com/drown-attack-paper.pdf](https://drownattack.com/drown-attack-paper.pdf)>. 

[ICA]
        
Jager, T., Schwenk, J., and J. Somorovsky, "Practical invalid curve attacks on TLS-ECDH", ESORICS 2015, Part I, Lecture Notes in Computer Science, vol. 9326, pp. 407-425, DOI 10.1007/978-3-319-24174-6_21, 21 September 2015, <[https://link.springer.com/content/pdf/10.1007/978-3-319-24174-6_21.pdf](https://link.springer.com/content/pdf/10.1007/978-3-319-24174-6_21.pdf)>. 

[MAY4]
        
Genkin, D., Valenta, L., and Y. Yarom, "May the Fourth Be With You: A Microarchitectural Side Channel Attack on Several Real-World Applications of Curve25519", Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, DOI 10.1145/3133956.3134029, 30 October 2017, <[https://dl.acm.org/doi/pdf/10.1145/3133956.3134029](https://dl.acm.org/doi/pdf/10.1145/3133956.3134029)>. 

[NEW-BLEI]
        
Meyer, C., Somorovsky, J., Weiss, E., Schwenk, J., Schinzel, S., and E. Tews, "Revisiting SSL/TLS Implementations: New Bleichenbacher Side Channels and Attacks", Proceedings of the 23rd USENIX Security Symposium, August 2014, <[https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-meyer.pdf](https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-meyer.pdf)>. 

[PARIS256]
        
Devlin, S. and F. Valsorda, "The PARIS256 Attack", 8 August 2018, <[https://i.blackhat.com/us-18/Wed-August-8/us-18-Valsorda-Squeezing-A-Key-Through-A-Carry-Bit-wp.pdf](https://i.blackhat.com/us-18/Wed-August-8/us-18-Valsorda-Squeezing-A-Key-Through-A-Carry-Bit-wp.pdf)>. 

[RACCOON]
        
Merget, R., Brinkmann, M., Aviram, N., Somorovsky, J., Mittmann, J., and J. Schwenk, "Raccoon Attack: Finding and Exploiting Most-Significant-Bit-Oracles in TLS-DH(E)", 9 September 2020, <[https://raccoon-attack.com/RacoonAttack.pdf](https://raccoon-attack.com/RacoonAttack.pdf)>. 

[RFC4492]
        
Blake-Wilson, S., Bolyard, N., Gupta, V., Hawk, C., and B. Moeller, "Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS)", RFC 4492, DOI 10.17487/RFC4492, May 2006, <[https://www.rfc-editor.org/info/rfc4492](https://www.rfc-editor.org/info/rfc4492)>. 

[ROBOT]
        
Boeck, H., Somorovsky, J., and C. Young, "Return Of Bleichenbacher's Oracle Threat (ROBOT)", Proceedings of the 27th USENIX Security Symposium, August 2018, <[https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-bock.pdf](https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-bock.pdf)>. 

[SUBGROUPS]
        
Valenta, L., Adrian, D., Sanso, A., Cohney, S., Fried, J., Hastings, M., Halderman, J. A., and N. Heninger, "Measuring small subgroup attacks against Diffie-Hellman", Cryptology ePrint Archive, Paper 2016/995, 17 October 2016, <[https://eprint.iacr.org/2016/995/20161017:193515](https://eprint.iacr.org/2016/995/20161017:193515)>. 

[TLS-REGISTRY]
        
IANA, "Transport Layer Security (TLS) Parameters", <[https://www.iana.org/assignments/tls-parameters](https://www.iana.org/assignments/tls-parameters)>. 

[WEAK-DH]
        
Adrian, D., Bhargavan, K., Durumeric, Z., Gaudry, P., Green, M., Halderman, J. A., Heninger, N., Springall, D., ThomÃ©, E., Valenta, L., VanderSloot, B., Wustrow, E., Zanella-BÃ©guelin, S., and P. Zimmermann, "Weak Diffie-Hellman and the Logjam Attack", October 2015, <[https://weakdh.org/](https://weakdh.org/)>. 

[XPROT]
      
Jager, T., Schwenk, J., and J. Somorovsky, "On the Security of TLS 1.3 and QUIC Against Weaknesses in PKCS#1 v1.5 Encryption", Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security, pp. 1185-1196, DOI 10.1145/2810103.2813657, October 2015, <[https://doi.org/10.1145/2810103.2813657](https://doi.org/10.1145/2810103.2813657)>. 

      

## 
[Acknowledgments](https://www.rfc-editor.org/rfc/rfc10015.html#name-acknowledgments)
      

This document includes many important contributions from Carrie Bartle, who wrote much of the prose and presented it several times at the IETF TLS WG.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#appendix-A-1)

The document was inspired by discussions on the TLS WG mailing list and
a suggestion by Filippo Valsorda following the release of the Raccoon attack [[RACCOON](https://www.rfc-editor.org/rfc/rfc10015.html#RACCOON)].
Thanks to Christopher A. Wood for writing up the initial draft of this document.
Thanks also to Thomas Fossati, Sean Turner, Joe Salowey, Yaron Sheffer, Christian Buchgraber, John PreuÃ Mattsson, and Manuel PÃ©gouriÃ©-Gonnard for their comments and suggestions.[Â¶](https://www.rfc-editor.org/rfc/rfc10015.html#appendix-A-2)

      

## 
[Author's Address](https://www.rfc-editor.org/rfc/rfc10015.html#name-authors-address)
      

        Nimrod Aviram

Email:
[nimrod.aviram@gmail.com](mailto:nimrod.aviram@gmail.com)
