---
title: "In Edison’s Revenge, Data Centers Are Transitioning From AC to DC"
url: https://spectrum.ieee.org/data-center-dc
clipped: 2026-06-17 01:27:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [In Edison’s Revenge, Data Centers Are Transitioning From AC to DC](https://spectrum.ieee.org/data-center-dc)

## Digest Summary
Data centers are shifting from traditional AC‑to‑DC power chains to high‑voltage DC (≈800 V) to meet AI workloads that can demand up to 1 MW per rack. The conventional path—medium‑voltage AC → low‑voltage AC → UPS‑DC → AC → low‑voltage DC at the server—incurs multiple conversion losses and massive copper busbars (≈200 kg per 1 MW rack). Directly converting 13.8 kV AC to 800 V DC at the perimeter eliminates most intermediate stages, cutting resistive losses, reducing conductor size by ~45 %, improving efficiency by ~5 %, and lowering total cost of ownership by ~30 % for gigawatt‑scale facilities. Vendors such as Vertiv, Eaton, Delta and SolarEdge are introducing 800 V DC ecosystems, solid‑state transformers, in‑row 660 kW racks, and 99 % efficient SST‑UPS combos, with commercial releases slated for late 2026. Industry adoption remains limited; most innovation centers on 400 V DC, and broader rollout depends on coordinated standards, safety frameworks, and a mature supply chain for DC‑specific power electronics, connectors, and protection components.

## Discussion Summary
The comments converge on the view that high‑voltage DC is technically viable and already employed in specialized contexts such as data‑center power distribution and telecom equipment, but widespread adoption remains limited by entrenched AC‑centric infrastructure and market hesitation. Historical references to Tesla and Edison are used to argue that transformers make AC preferable for long‑distance transmission, while noting that modern power semiconductors now enable efficient DC conversion. Frustration appears regarding the persistence of AC‑to‑DC conversion in consumer devices and a desire for broader, standardized DC solutions.

---

## Full Article

Last week’s [Nvidia GTC](https://www.nvidia.com/gtc/) conference highlighted new [chip](https://spectrum.ieee.org/nvidia-groq-3) architectures to power AI. But as the chips become faster and more powerful, the remainder of data center [infrastructure](https://spectrum.ieee.org/data-center-liquid-cooling) is playing catch-up. The power-delivery community is responding: Announcements from [Delta](https://www.prnewswire.com/news-releases/delta-exhibits-energy-saving-solutions-for-800-vdc-in-next-gen-ai-factories-and-digital-twin-applications-built-on-omniverse-at-nvidia-gtc-2026-302715850.html), [Eaton](https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-collaborates-with-nvidia-to-unveil-its-beam-rubin-dsx-platform.html), [Schneider Electric](https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-teams-with-NVIDIA-to-develop-validated-blueprints-to-design-simulate-build-operate-and-maintain-gigawattscale-AI-Factories-69b82f61aa1027e04205d273/), and [Vertiv](https://www.vertiv.com/en-us/about/news-and-insights/corporate-news/2026/vertiv-brings-converged-physical-infrastructure-to-nvidia-vera-rubin-dsx-ai-factories/) showcased new designs for the AI era. Complex and inefficient AC-to-DC power conversions are gradually being replaced by DC configurations, at least in hyperscale [data centers](https://spectrum.ieee.org/tag/data-centers).

“While AC distribution remains deeply entrenched, advances in [power electronics](https://spectrum.ieee.org/tag/power-electronics) and the rising demands of AI infrastructure are accelerating interest in DC architectures,” says [Chris Thompson](https://www.linkedin.com/in/solarchris/), vice president of advanced technology and global [microgrids](https://spectrum.ieee.org/tag/microgrids) at Vertiv.

AC-to-DC Conversion Challenges
------------------------------

Today, nearly all data centers are designed around AC utility power. The electrical path includes multiple conversions before power reaches the compute load. Power typically enters the data center as medium-voltage AC (1 to 35 kilovolts), is stepped down to low-voltage AC (480 or 415 volts) using a transformer, converted to DC inside an uninterruptible power supply (UPS) for battery storage, converted back to AC, and converted again to low-voltage DC (typically 54 V DC) at the server, supplying the DC power computing chips actually require.

“The double conversion process ensures the output AC is clean, stable, and suitable for data center servers,” says [Luiz Fernando Huet de Bacellar,](https://www.linkedin.com/in/luiz-fernando-huet-de-bacellar-b2112117/) vice president of engineering and technology at Eaton.

That setup worked well enough for the amounts of power required by traditional data centers. Traditional data center computational racks draw on the order of 10 kW each. For AI, that is starting to approach 1 megawatt. At that scale, the energy losses, current levels, and copper requirements of AC-to-DC conversions become increasingly difficult to justify. Every conversion incurs some power loss. On top of that, as the amount of power that needs to be delivered grows, the sheer size of the convertors, as well as the connector requirements of copper busbars, becomes untenable. According to an [Nvidia](https://spectrum.ieee.org/tag/nvidia) [blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/), a 1-MW rack could require as much as 200 kilograms of copper busbar. For a 1-gigawatt data center, it could amount to 200,000 kg of copper.

Benefits of High-Voltage DC Power
---------------------------------

By converting 13.8-kV AC grid power directly to 800 V DC at the data center perimeter, most intermediate conversion steps are eliminated. This reduces the number of fans and power-supply units, and leads to higher system reliability, lower heat dissipation, improved [energy efficiency](https://spectrum.ieee.org/tag/energy-efficiency), and a smaller equipment footprint.

“Each power conversion between the [electric grid](https://spectrum.ieee.org/tag/electric-grid) or power source and the silicon chips inside the [servers](https://spectrum.ieee.org/tag/servers) causes some energy loss,” says Bacellar.

Switching from 415-V AC to 800-V DC in electrical distribution enables 85 percent more power to be transmitted through the same conductor size. This happens because higher voltage reduces current demand, lowering resistive losses and making power transfer more efficient. Thinner conductors can handle the same load, reducing copper requirements by 45 percent, a 5 percent improvement in efficiency, and 30 percent lower total cost of ownership for gigawatt-scale facilities.

“In a high-voltage DC architecture, power from the grid is converted from medium-voltage AC to roughly 800-V DC and then distributed throughout the facility on a DC bus,” said Vertiv’s Thompson. “At the rack, compact DC-to-DC converters step that voltage down for [GPUs](https://spectrum.ieee.org/tag/gpus) and CPUs.”

A [report](https://www.datacenter-asia.com/wp-content/uploads/2025/08/Omdia-Analysts-Summit-Omdia%E5%88%86%E6%9E%90%E5%B8%88%E5%B3%B0%E4%BC%9A.pdf) from technology advisory group [Omdia](https://omdia.tech.informa.com/) claims that higher voltage DC data centers have already appeared in [China](https://spectrum.ieee.org/tag/china). In the Americas, the [Mt. Diablo Initiative](https://www.linkedin.com/posts/sharada-yeluri_microsoft-meta-google-activity-7367974455052017666-nXV5/) (a collaboration among [Meta](https://www.meta.com/about/?srsltid=AfmBOoq7uBjCU2oG3oI6Ti8VQaMdaxhAcxXmXD-twy9OTi0cbmTqGKVQ), [Microsoft](https://www.microsoft.com/en-us), and the [Open Compute Project](https://www.opencompute.org/)) is a 400-V DC rack power distribution experiment.

A handful of vendors are trying to get ahead of the game. Vertiv’s 800-V DC ecosystem that integrates with [Nvidia Vera Rubin Ultra Kyber platforms](https://www.vertiv.com/en-us/about/news-and-insights/corporate-news/vertiv-develops-energy-efficient-cooling-and-power-reference-architecture-for-the-nvidia-gb300-nvl72/) will be commercially available in the second half of 2026. Eaton, too, is well advanced in its 800-V DC systems innovation courtesy of a medium-voltage solid-state transformer (SST) that will sit at the heart of DC power distribution system. Meanwhile Delta, has released 800-V DC in-row 660-kW power racks with a total of 480 kW of embedded battery backup units. And, [SolarEdge](https://www.solaredge.com/us/) is hard at work on a 99%-efficient SST that will be paired with a native DC UPS and a DC power distribution layer.

But much of the industry is far behind. [Patrick Hughes](https://www.linkedin.com/in/pehughes/), senior vice president of strategy, technical, and industry affairs for the [National Electrical Manufacturers Association](https://www.makeitelectric.org/), says most innovation is happening at the 400-V DC level, though some are preparing 800-V DC. He believes the industry needs a complete, coordinated ecosystem, including power electronics, protection, connectors, sensing, and service‑safe components that scale together rather than in isolation. That, in turn, requires retooling manufacturing capacity for DC‑specific equipment, expanding semiconductor and materials supply, and clear, long‑term demand commitments that justify major capital investment across the value chain.

“Many are taking a cautious approach, offering limited or adapted solutions while waiting for clearer standards, safety frameworks, and customer commitments,” said Hughes. “Building the [supply chain](https://spectrum.ieee.org/tag/supply-chain) will hinge on stabilizing standards and safety frameworks so suppliers can design, certify, manufacture, and install equipment with confidence.”

From Your Site Articles

Related Articles Around the Web