---
title: "Algorithmic Monocultures in Hiring"
url: https://algorithmichiring.github.io/
clipped: 2026-06-17 00:50:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hiring algorithms
  - algorithmic bias
  - vendor concentration
  - labor market economics
  - systemic discrimination
related:
  - "[[Algorithmic Bias]]"
  - "[[Systemic Discrimination]]"
  - "[[Vendor Concentration]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A study of 3.4 million job applicants shows that the widespread adoption of a single hiring algorithm vendor creates systemic racial disparities and homogeneous rejection rates.
>
> **Key points:**
> - Vendor concentration (e.g., HireVue) results in an algorithmic monoculture where many employers screen applicants using identical models.
> - Black applicants experience significant adverse impact, while Asian applicants experience the largest aggregate shortfall in recommendations.
> - Candidates rejected by one employer face a disproportionately high rate of systemic rejection across all employers using the same vendor.
>
> **Concept links:** [[Hiring Algorithms]], [[Algorithmic Bias]], [[Vendor Concentration]], [[Labor Market Economics]], [[Systemic Discrimination]]
>
> **Suggested connections:**
> - [[Algorithmic Bias]] — how automated models amplify human and historical biases.
> - [[Systemic Discrimination]] — institutional barriers reinforced by standardized technology.
> - [[Vendor Concentration]] — market dominance risks in critical infrastructure and services.
<!-- ai-summary:end -->

# [Algorithmic Monocultures in Hiring](https://algorithmichiring.github.io/)

## Digest Summary
The study analyzes 3.4 million applicants (4 million applications) screened by a single hiring‑algorithm vendor across 156 U.S. employers in 11 sectors, exposing the effects of an algorithmic monoculture. Key results:

- Over 60 % of Fortune 100 firms use the same vendor (e.g., HireVue), creating shared decision pipelines.
- Racial disparity: 30 % of Black applicants encounter at least one position with adverse impact; Asian applicants experience the largest aggregate shortfall—≈29 000 additional recommendations would be needed to match the most‑selected group’s rate.
- Systemic rejection: among candidates submitting four applications, 10 % are rejected by every employer, a rate significantly above the independent‑decision baseline (χ² = 18 481, p < 0.001).
- Counterfactual simulation shows that, under realistic application behavior, 25 submissions are required for a 99.9 % chance of at least one recommendation, versus 10 submissions under independent decisions.

Policy suggestions include position‑level adverse‑impact measurement, enhanced market surveillance of homogeneous outcomes, monitoring of vendor concentration, and expanded data access for independent research.

## Discussion Summary
The commentary critiques algorithmic hiring systems, arguing they impose a uniform disparate‑impact standard despite evaluating applications rather than people, and may perpetuate bias through applicant pools and cached scoring. It questions the relevance of such measures to actual job performance and highlights the risk of creating hiring monocultures. The author advocates for legal scrutiny of these practices, noting parallels to anticompetitive behavior, and contrasts them with a personal hiring approach that relies on behavioral interviewing, long‑term potential, and continuous development, which is presented as more effective and equitable.

---

## Full Article

Algorithmic Monocultures in Hiring
==================================

Over 90% of U.S. employers [rely](https://www.weforum.org/stories/2025/03/ai-hiring-human-touch-recruitment/) on hiring algorithms to screen job applicants. Many different employers use algorithms from the same few vendors. We conduct the largest empirical study of algorithmic hiring with data for 3.4 million real job applicants submitting 4 million applications to 156 employers across 11 market sectors. Every application was assessed by algorithms from a single vendor: we test whether this *algorithmic monoculture* bottlenecks job opportunities. We are the first to demonstrate large-scale evidence of racial disparities and homogeneous outcomes in high-stakes hiring decisions.

---

Key Findings
------------

1
**Large-scale adverse impact for Asians and Blacks.** We are the first to demonstrate adverse impact in deployed algorithmic hiring as one of the largest demonstrations of unfair outcomes in real high-stakes AI decisions. **25.87% of applications** submitted by Black applicants and **14.74%** of applications submitted by Asian applicants are directed to positions that adversely impact them based on the standards of the relevant [U.S. employment law (Title VII)](https://www.eeoc.gov/statutes/title-vii-civil-rights-act-1964).

2
**Adverse impact only revealed by disaggregated position-by-position analysis.** While empirical studies of algorithmic hiring are very constrained due to data access limitations, prior studies [showed](https://dl.acm.org/doi/10.1145/3442188.3445928) minimal adverse impact due studying all of the vendor's data as a whole. By studying each position separately, in accordance with the standards of Title VII, we identify positions that demonstrate adverse impact that gets washed out in aggregate.

3
**Algorithmic monocultures in hiring yield systemic rejections.** We are the first to demonstrate systemic rejections in deployed algorithmic hiring as posited in [prior](https://arxiv.org/abs/2211.13972) [theoretical](https://www.cambridge.org/core/journals/canadian-journal-of-philosophy/article/algorithmic-leviathan-arbitrariness-fairness-and-opportunity-in-algorithmic-decisionmaking-systems/3AA0ECA77F8622488E9DB0834287215B) [research](https://scholarship.law.unc.edu/aidr_collection/11/) about algorithmic monoculture. The observed systemic rejection rate significantly exceeds that of the baseline of statistically independent decisions, even though the baseline accurately predicted observed systemic rejection rates in other hiring data in the absence of centralized algorithmic monocultures.

4
**Data access inhibits independent research into hiring algorithms.** We are the first and only group to independently conduct empirical research deployed hiring algorithms at scale, even though hiring algorithms mediate high-stakes decisions and are pervasively adopted. Given the data barriers, policy intervention may be necessary to enable scientific inquiry and increase accountability into this high-impact application of AI.

---

Algorithmic Hiring Pipeline
---------------------------

Many employers procure hiring algorithms from the same third-party vendors. Over 60% of the Fortune 100 use HireVue's algorithms. When hiring algorithms from a single vendor mediate hiring decisions at multiple employers, they constitute an **algorithmic monoculture**.

![Diagram of the AI-mediated hiring pipeline showing how applicants are screened by shared algorithms across multiple employers](https://algorithmichiring.github.io/figures/fig1_pipeline.png)


**Figure 1.** Job applications are assessed by hiring AI to be recommended or not recommended. If an applicant is not recommended by the algorithm, they are likely to be rejected without further consideration by a human.

---

Revealing Adverse Impact
------------------------

Title VII of the US Civil Rights Act governs discrimination in hiring. [Prior](https://dl.acm.org/doi/10.1145/3442188.3445928) [studies](https://link.springer.com/article/10.1007/s43681-022-00208-x) found very limited adverse impact in algorithmic hiring data as a whole. We surface previously-overlooked adverse impact by studying positions separately. Black applicants are the most likely to be adversely impacted: 30% of Black applicants apply to at least one position that demonstrates adverse impact against Black applicants. In terms of total effect, Asian applicants experience the largest shortfall: if Asians were selected at the same rate as the most selected racial group for each position, then 29000 additional Asian applications would be recommended.

![Adverse impact across applicant groups](https://algorithmichiring.github.io/figures/adverse_impact.png)


**Figure 2.** Adverse impact according to the Title VII four-fifths rule measured at the level of positions (left) and applications/applicants (center). The shortfall (right) is the number of applications that would have been selected if the adversely impacted racial group was selected at the same rate as the most selected group.

---

Identifying Systemic Rejection
------------------------------

When applicants apply to multiple positions, they can receive the same outcomes. Algorithmic monoculture could make this most likely. If so, the systemic rejections where applicants are rejected everywhere would be especially concerning. Of applicants that submit 4 applications, 10% are systemically rejected. The observed systemic rejection rate significantly exceeds the baseline rate expected under independent decisions (χ2 = 18,481, *p* < 0.001).

![Chart showing systemic rejection rates exceed baseline predictions](https://algorithmichiring.github.io/figures/pymetrics_homogeneity.png)


**Figure 3.** Systemic rejection rates in hiring AI data. The observed rates always exceed the baseline: shared dependence on one vendor yields homogeneous outcomes.

To contextualize the observed systemic rejection rates, we introduce the baseline of independent decisions ([Toups et al., 2023](https://arxiv.org/abs/2307.05862)). To test the predictivity of this baseline, we use data from the largest prior study of hiring ([Kline et al., 2022](https://www.nber.org/papers/w29053)), which sent 83,000 applications to 108 Fortune 500 firms. The baseline accurately predicts the observed rates (χ2 = 20.05, *p* = 0.69). Therefore, excess homogeneity is distinctive of centralized algorithmic assessment.

![Kline et al. systemic rejection rates matching baseline predictions](https://algorithmichiring.github.io/figures/kline.png)


**Figure 4.** Systemic rejection rates for data from [Kline et al. (2022)](https://www.nber.org/papers/w29053). Unlike the algorithmic hiring data, the baseline accurately predicted the observed rates.

---

Simulating Counterfactual Outcomes
----------------------------------

What would happen if applicants applied more broadly than they did in reality? Would this lessen their chances of systemc rejection? When applicants apply everywhere, we find that at least one model recommends them. But under more realistic behavior, applicants need to submit 25 applications to ensure at least one recommendation with 99.9% probability — compared to just 10 applications for independent decisions.

![Simulation showing systemic rejection rates under broader application behavior](https://algorithmichiring.github.io/figures/simulation.png)


**Figure 5.** Simulated systemic rejection rates if applicants applied where they applied in reality, as well as to neighboring models that share applicants.

---

Policy Recommendations
----------------------

Hiring AI is governed by employment discrimination law, general AI regulation, and specific rules for algorithmic hiring. In the U.S., Title VII already evaluates adverse impact at the level of [specific jobs](https://www.ecfr.gov/current/title-41/subtitle-B/chapter-60/part-60-3/subject-group-ECFR34f59e83ab36f01/section-60-3.15) rather than blended aggregates. More broadly, hiring systems are increasingly treated as [high-risk AI](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689), including under the EU AI Act. At the municipal level, New York City Local Law 144 established an early framework for regulating automated employment decision tools, but [current guidance](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-138393) does not adequately address the position-level effects we document.

1

**Measure adverse impact per position.** Regulators and auditors should evaluate adverse impact ratios at the level of individual positions. Aggregate-only analyses can conceal disparate impact.

2

**Strengthen market surveillance.** Federal agencies should quantify the rate of homogeneous outcomes. Without cross-employer links, existing reporting won't capture systemic rejection.

3

**Monitor algorithmic monoculture.** Policymakers should surveil shared dependencies in the hiring supply chain. Concentrated reliance on the same systems can yield correlated failures, systemic rejection, and reduced competition in hiring.

4

**Expand researcher access.** Legislators should stimulate independent research, including underlying data access, into major hiring platforms. Issues will be difficult to diagnose, let alone rectify, without the foundation of empirically-grounded externally-conducted inquiry.

---

Citation
--------

Copy

@article{bommasani2026algorithmic,
title={Algorithmic Monocultures in Hiring},
author={Bommasani, Rishi and Bana, Sarah H. and Creel, Kathleen A. and Jurafsky, Dan and Liang, Percy},
booktitle={Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency},
year={2026}
}

© 2026 Bommasani, Bana, Creel, Jurafsky, Liang