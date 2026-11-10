---
title: "A Botnet Accidentally Destroyed I2P"
url: https://www.sambent.com/a-botnet-accidentally-destroyed-i2p-the-full-story/
clipped: 2026-06-17 01:41:54
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A Botnet Accidentally Destroyed I2P](https://www.sambent.com/a-botnet-accidentally-destroyed-i2p-the-full-story/)

## Digest Summary
On 3 Feb 2026 the I2P anonymity network suffered a massive Sybil attack: ≈700 000 hostile nodes were introduced, overwhelming its normal 15‑20 k active participants (≈39 : 1 ratio). Similar attacks occurred each February in 2023 and 2024 via malicious floodfill routers, but those remained unattributed. Investigation linked the 2026 surge to the Kimwolf IoT botnet, which had infected millions of devices (streaming boxes, consumer routers) after a record‑setting 31.4 Tbps DDoS in Dec 2025. Botnet operators disclosed on Discord that the disruption was accidental; they were repurposing I2P as a backup command‑and‑control layer after researchers dismantled >550 of their primary C2 servers. I2P’s developers released version 2.11.0 six days later, adding hybrid ML‑KEM + X25519 post‑quantum encryption (enabled by default), SAMv3 API upgrades, and additional Sybil‑mitigation and infrastructure improvements.

## Discussion Summary
The discussion reflects uncertainty and a demand for clearer context surrounding the I2P botnet incident, with participants questioning the completeness of the headline coverage and seeking more in‑depth reporting. Common concerns include the reported pattern of state‑sponsored attacks, the mechanisms enabling large botnets to communicate through platforms like Discord, and why such servers remain permissible, indicating overall confusion and a desire for additional technical and policy explanations.

---

## Full Article

VIDEO

On February 3, 2026, the I2P anonymity network was flooded with 700,000 hostile nodes in what became one of the most devastating Sybil attacks an anonymity network has ever experienced. The network normally operates with 15,000 to 20,000 active devices. The attackers overwhelmed it by a factor of 39 to 1.  
  
For three consecutive years, I2P has been hit with Sybil attacks every February. The 2023 and 2024 attacks used malicious floodfill routers and remain unattributed. When the 2026 attack began, most assumed it was the same state-sponsored operation continuing its annual disruption campaign. The assumption was wrong.  
  
The attacker was identified as the Kimwolf botnet, an IoT botnet that infected millions of devices including streaming boxes and consumer routers throughout late 2025. Kimwolf is the same operation behind the record-setting 31.4 terabit per second DDoS attack in December 2025. The operators admitted on Discord they accidentally disrupted I2P while attempting to use the network as backup command-and-control infrastructure after security researchers destroyed over 550 of their primary C2 servers.  
  
The I2P development team responded by shipping version 2.11.0 just six days after the attack began. The release includes hybrid ML-KEM plus X25519 post-quantum encryption enabled by default, making I2P one of the first production anonymity networks to ship post-quantum cryptography to all users. Additional Sybil mitigations, SAMv3 API upgrades, and infrastructure improvements were included.