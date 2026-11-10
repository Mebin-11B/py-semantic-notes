---
title: "The Resolv hack: How one compromised key printed $23M"
url: https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/
clipped: 2026-06-17 01:28:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - defi security
  - private key compromise
  - stablecoins
  - smart contract design
  - aws kms
  - on-chain monitoring
related:
  - "[[DeFi Security]]"
  - "[[Private Key Compromise]]"
  - "[[Stablecoins]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A compromised AWS KMS signing key allowed an attacker to bypass Resolv's off-chain validation, minting $25 million in unbacked USR stablecoins and collapsing its peg.
>
> **Key points:**
> - Resolv, a DeFi stablecoin protocol, was exploited on March 22, 2026, for approximately $23-25 million.
> - The breach occurred when an attacker gained access to Resolv's AWS Key Management Service (KMS) environment, obtaining the `SERVICE_ROLE` key.
> - The smart contract lacked an on-chain maximum minting limit, trusting whatever swap ratio was signed by the privileged key.
> - The attacker deposited $100K-200K USDC, minted 80 million USR, wrapped it into wstUSR, and swapped it into 11,400 ETH, causing an 80% de-peg of USR.
>
> **Concept links:** [[Defi Security]], [[Private Key Compromise]], [[Stablecoins]], [[Smart Contract Design]], [[Aws Kms]], [[On-Chain Monitoring]]
>
> **Suggested connections:**
> - [[DeFi Security]] — vulnerabilities and mitigations in decentralized financial protocols.
> - [[Private Key Compromise]] — the risk of cloud-based key management systems in blockchain applications.
> - [[Stablecoins]] — related concept or discussion in this area.
<!-- ai-summary:end -->
# [The Resolv hack: How one compromised key printed $23M](https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/)

## Digest Summary
The Resolv DeFi protocol was exploited on March 22 2026 when an attacker compromised the protocol’s AWS KMS environment and obtained the privileged private key used by the off‑chain SERVICE_ROLE to sign mint‑approval transactions. The minting design required only a valid signature, without any on‑chain cap or collateral‑to‑mint ratio check. Using the stolen key, the attacker deposited roughly $100‑200 k USDC and called the `completeSwap` function to mint about 80 million USR (≈ $25 M) far exceeding the collateral. The USR was then wrapped into wstUSR, swapped through stablecoins, and converted to ETH, resulting in an estimated 11,400 ETH (≈ $24 M) extracted. The sudden influx of unbacked USR caused the token’s peg to collapse by ~80 % before partially recovering. Resolv halted operations and began investigation. Post‑mortem analysis highlights that the vulnerability stemmed from reliance on off‑chain key management rather than smart‑contract logic, and that real‑time on‑chain monitoring (e.g., anomalous mint‑to‑deposit ratios) could have generated early alerts or automated pauses to limit loss.

## Discussion Summary
The comments focus on a recent hack in which an attacker compromised a platform’s AWS account, stole a signing key, and minted large amounts of tokens before the protocol was halted, emphasizing that the breach stemmed from traditional credential theft rather than a pure smart‑contract flaw. The discussion repeatedly questions the usefulness and stability of stablecoins, critiques the industry’s vulnerability and regulatory gaps, and speculates about an insider’s involvement, while expressing overall skepticism toward crypto’s security and practical value.

---

## Full Article

On March 22, 2026, the Resolv DeFi protocol became the latest example of how quickly things can unravel in DeFi when security assumptions fail. In a matter of minutes, **an attacker was able to mint tens of millions of Resolv’s unbacked stablecoins (USR) and extract roughly $23 million in value,** triggering a sharp de-peg and forcing the protocol to [halt operations](https://x.com/ResolvLabs/status/2035581976514609437).

At first glance, this might look like another smart contract exploit. But it wasn’t. The code worked exactly as intended.

Instead, **it was a case of overly trusting off-chain infrastructure.** As DeFi systems become more complex and use more external services, privileged keys, and cloud infrastructure, the attack surface expands far beyond the blockchain itself.

In this post, we’ll look at what happened and what the impact was. We’ll also explore how when off-chain components are compromised, only real-time, on-chain threat detection and response mechanisms can act as the critical final line of defence and make the difference between a contained incident and a multi-million dollar exploit.

What happened, in a nutshell
----------------------------

The attacker started by depositing a relatively small amount (around $100K–$200K in USDC) and used it to interact with Resolv’s USR stablecoin minting system. Normally, users deposit USDC and receive an equivalent amount of USR in return. However, in this case, the attacker was able to mint around 80 million USR tokens, far beyond what their deposit should have allowed.

This was possible because minting approvals depended on an off-chain service that used a privileged private key to sign off on how much USR could be created. Unfortunately, the smart contract itself did not enforce any maximum limit on minting – it only checked that a valid signature existed.

After minting the unbacked USR, the attacker quickly converted it into a staked version (wstUSR), then gradually swapped it into other stablecoins and eventually into ETH. By the end of the attack, they had extracted approximately $25 million in ETH. The sudden flood of unbacked USR into the market also caused the token’s price to drop by around 80%.

With the outcome known, let’s take a quick look at how the minting design made this hack possible.

How Resolv’s token minting is supposed to work
----------------------------------------------

Understanding how this attack happened requires first understanding Resolv’s minting design.

When a user wants to mint Resolv’s native token, USR, they don’t interact with an autonomous on-chain mechanism. Instead, they go through a two-step off-chain process:

1. **requestSwap** – The user deposits USDC into the USR Counter contract and submits a minting request.
2. **completeSwap** – An off-chain service, controlled by **a privileged private key** called the SERVICE\_ROLE, reviews the request and calls back to the contract to finalize how much USR to mint.

The contract enforces a **minimum** USR output – **but critically, no maximum**. There is no on-chain ratio check between the collateral deposited and the USR to be minted. No price oracle. No cap. No maximum mint ratio. So, whatever the key holder signs will get minted.

A step by step breakdown of the attack
--------------------------------------

**Step 1. Gaining Access to Resolv’s AWS KMS Environment**

The attacker compromised Resolv’s cloud infrastructure to gain access to Resolv’s **AWS Key Management Service (KMS) environment** where the protocol’s privileged signing key was stored. With control over the KMS environment, the attacker could use Resolv’s own minting key to authorize any minting operation they chose.

**Step 2. Minting the USR Tokens**

Armed with the signing key, the attacker made two swap requests, each funded with a modest USDC deposit totaling approximately $100K – $200K across a handful of transactions. The SERVICE\_ROLE key was then used to call completeSwap with inflated output amounts, **authorizing tens of millions of USR in exchange for the USDC deposits**.

Two primary transactions have been identified on-chain:

In total, **80 million USR tokens were minted,** approximately **$25 million.**

**Step 3. Bypassing Liquidity with wstUSR**

The attacker then **converted USR into wstUSR** (wrapped staked USR), a derivative token that represents a share of the staking pool rather than a fixed number of USR. By staking into wstUSR, the attacker moved their position out of a form that would immediately tank the market and into a less liquid but more fungible derivative.

**Step 4. Cashing Out**

From wstUSR, the attacker swapped into stablecoins, then into ETH, rotating through multiple DEX pools and bridges to maximize their extraction and obscure the trail.

At the time of writing, the [attacker’s wallet](https://etherscan.io/address/0x8ed8cf0c1c531c1b20848e78f1cb32fa5b99b81c) holds:

* **~11,400 ETH** (~$24 million)
* **~20 million wstUSR** (~$1.3 million at depressed prices)

The consequences for USR holders were immediate and severe.

The 80 million newly minted, unbacked tokens began hitting DEX liquidity pools. As the supply flooded the markets, USR’s dollar peg collapsed. The token dropped as low as **$0.20** (an 80% collapse) before recovering partially to around [$0.56](https://www.coingecko.com/en/coins/resolv-usr) in the hours that followed.

Following the attack, Resolv Labs [issued a statement](https://x.com/ResolvLabs/status/2035581976514609437) and **suspended all protocol functions** to prevent further damage and began investigating the breach. The urgency to prevent further damage couldn’t have been stronger either, especially as the attacker was [trying to mint](https://etherscan.io/address/0xa27a69ae180e202fde5d38189a3f24fe24e55861) even more, hence the importance of having as an immediate response as possible to such an attack.

[![Resolv hack timeline](https://www.chainalysis.com/wp-content/uploads/2026/03/image2-800x356.png)](https://www.chainalysis.com/wp-content/uploads/2026/03/image2.png)

How Hexagate could have protected Resolv
----------------------------------------

The hack on Resolv is a good example of what real-time on-chain monitoring is designed to catch. With Chainalysis Hexagate, two concrete detection approaches would have been available:

### **Option 1: Monitor for anomalous minting events**

A monitoring system like Hexagate could have been configured to watch for any completeSwap function call where the minted USR output was disproportionate to the deposited collateral input.

A $100K USDC deposit authorizing 50 million USR is an anomaly that no legitimate user would ever generate. An alert on this function call pattern with a threshold that flags ratios above, say, 1.5x the normal range, would have flagged both primary transactions instantly.

[![Hexagate screen](https://www.chainalysis.com/wp-content/uploads/2026/03/image1-800x334.png)](https://www.chainalysis.com/wp-content/uploads/2026/03/image1.png)

Hexagate’s customized monitor that would have triggered an automated response upon detecting the minting anomaly that exploited Resolv’s minting mechanism.

### **Option 2: Gatesigner with custom functionality for this critical contract event**

The attacker had to go through the requestSwap → completeSwap flow, and this flow generates on-chain events at every stage. Hexagate’s [GateSigner](https://www.chainalysis.com/product/gatesigner/) combined with contract event monitoring could have been configured to detect the anomalous Mint event and **automatically trigger a contract pause** before a single dollar of the 80 million USR reached the open market.

Good security means assuming something will go wrong
----------------------------------------------------

While Resolv had undergone all the classic security measures, and had undergone as many as [18 audits](https://docs.resolv.xyz/litepaper/resources/security), the hack on Resolv is, in one sense, a simple story: an attacker got a key, used it to print money, and sold the fake money before anyone noticed.

But in a deeper sense, it’s a story about how DeFi protocols inherit the security assumptions, and the vulnerabilities, of the off-chain infrastructure they depend on. The on-chain smart contract worked perfectly. The broader system design and off-chain infrastructure of the compromised key apparently did not.

Real-time monitoring and automated response mechanisms are now a necessity, not a luxury, as exploits unfold in minutes, leaving no time for reactive measures once the damage is visible.

***Learn more about how** [**Hexagate’s real-time on-chain threat detection**](https://www.chainalysis.com/product/hexagate/) **monitors and automated response can prevent you from being a victim of the next big heist, or** [**request a demo**](https://www.chainalysis.com/request-a-demo/) **today.***