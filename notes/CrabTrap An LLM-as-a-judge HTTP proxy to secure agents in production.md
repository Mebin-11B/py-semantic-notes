---
title: "CrabTrap: An LLM-as-a-judge HTTP proxy to secure agents in production"
url: https://www.brex.com/crabtrap
clipped: 2026-06-17 01:14:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [CrabTrap: An LLM-as-a-judge HTTP proxy to secure agents in production](https://www.brex.com/crabtrap)

## Digest Summary
Brex LLC, a Capital One subsidiary, offers a business account comprising a checking service through Column N.A. (FDIC‑insured) and cash‑management services (Treasury and Vault) via Brex Treasury LLC, a FINRA‑registered Capital One company. Treasury funds lack FDIC coverage; Vault funds become insured only after transfer to program banks. Securities provided by Brex Treasury LLC involve investment risk, variable yields, and are not FDIC‑insured or guaranteed; past performance does not assure future results. The Brex Mastercard® Corporate Credit Card is issued by Emigrant Bank, Fifth Third Bank N.A., or Airwallex (Netherlands) B.V., while the Brex Commercial Card is issued by Sutton Bank under a Visa license; both are unaffiliated with Brex and have no ATM access. Loans require standard underwriting, credit, and collateral approvals. Brex Payments LLC, a licensed money transmitter (NMLS #2035354), handles certain payment services. Product fees vary, with plans starting at $0 per user per month and advanced features at $12 per user per month.

## Discussion Summary
The comments express cautious interest in the LLM‑as‑judge approach, noting potential security benefits but also highlighting significant risks such as shared‑model vulnerabilities, prompt‑injection, and limited visibility of request context. Reviewers question the latency‑vs‑safety trade‑off, the choice of HTTP framing, and the need for deterministic safeguards like ACLs rather than probabilistic guards. While several contributors are building similar open‑source solutions and appreciate the focus on agent security, many stress that adding extra LLM layers may not fundamentally improve safety.

---

## Full Article

Brex LLC is a wholly owned subsidiary of Capital One, N.A.

Brex LLC | 650 S 500W Suite 300 | Salt Lake City, UT 84101

The Brex business account consists of Checking, a commercial checking account provided by Column N.A., Member [FDIC](https://www.fdic.gov/about/what-we-do) (an unaffiliated institution), and Treasury and Vault, cash management services provided by Brex Treasury LLC, Member [FINRA](https://brokercheck.finra.org/)/[SIPC](https://www.sipc.org/) and a Capital One company.

Securities are offered through Brex Treasury LLC. Funds in Treasury are not FDIC-insured. Funds in Vault at [program banks](https://www.brex.com/legal/brex-cash-partner-banks) are eligible for [FDIC](https://www.fdic.gov/about/what-we-do) insurance. Funds are not FDIC-insured until they arrive at program banks. Conditions apply.

Investing in securities involves risk and loss of money. Yield and return are variable and fluctuate. Past performance is not a guarantee of future results. This is not an offer to, or implied offer, or a solicitation to, buy or sell any securities. Brex Treasury LLC does not provide legal, tax, or investment advice. The latest statement of financial condition for Brex Treasury LLC is available [here](https://www.brex.com/statement-of-financial-condition). You could lose money by investing in the Fund. Although the Fund seeks to preserve the value of your investment at $1.00 per share, it cannot guarantee it will do so. An investment in the Fund is not insured or guaranteed by the FDIC or any other government agency.

The Brex Mastercard® Corporate Credit Card is issued by Emigrant Bank, Fifth Third Bank N.A., or Airwallex (Netherlands) B.V. (all unaffiliated institutions), pursuant to licenses by Mastercard International Inc. Mastercard is a registered trademark, and the circles design is a trademark of Mastercard International Inc. The Brex Commercial Card is issued by Sutton Bank (an unaffiliated institution), pursuant to a license from Visa® U.S.A. Inc. Can be used where Visa® cards are accepted. No ATM access. All loans are subject to approval, including underwriting, credit, and collateral approval, as well as availability restrictions. Nothing herein should be construed as a commitment to lend.

Certain payment services are provided by Brex Payments LLC, a [licensed money transmitter](https://www.brex.com/legal/state-disclosures) (NMLS #2035354) and a Capital One company.

Some Brex products have associated fees. Plans start at $0 per user, per month, and more advanced features are available for $12 per user, per month.