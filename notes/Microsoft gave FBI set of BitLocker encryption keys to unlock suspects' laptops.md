---
title: "Microsoft gave FBI set of BitLocker encryption keys to unlock suspects' laptops"
url: https://techcrunch.com/2026/01/23/microsoft-gave-fbi-a-set-of-bitlocker-encryption-keys-to-unlock-suspects-laptops-reports/
clipped: 2026-06-17 01:54:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Microsoft gave FBI set of BitLocker encryption keys to unlock suspects' laptops](https://techcrunch.com/2026/01/23/microsoft-gave-fbi-a-set-of-bitlocker-encryption-keys-to-unlock-suspects-laptops-reports/)

## Digest Summary
Microsoft supplied FBI agents with BitLocker recovery keys for three laptops seized in a fraud investigation tied to Guam’s Pandemic Unemployment Assistance program. BitLocker, Windows’ default full‑disk encryption, automatically uploads recovery keys to Microsoft’s cloud, allowing the company—and, by legal process, law‑enforcement—to retrieve them. Microsoft has indicated it receives roughly 20 such government requests annually. The FBI obtained a warrant six months after seizing the devices, after which Microsoft provided the keys. Security experts, including Johns Hopkins cryptographer Matthew Green, highlighted privacy risks: a breach of Microsoft’s cloud could expose recovery keys, though attackers would still need physical access to the drives. Microsoft did not comment further on the specific request.

## Discussion Summary
Comments show a split between acceptance of Windows 11’s default BitLocker encryption as a practical safeguard for average users and criticism of its automatic key escrow to Microsoft accounts, which enables law‑enforcement access under warrants. Many view the feature as a reasonable trade‑off against theft, while privacy‑focused contributors warn of government overreach, potential cloud breaches, and advocate alternative systems like Linux with self‑managed keys. The discussion also touches on the inconvenience of key loss, the broader issue of corporate‑government collusion, and the desire for clearer user choice in encryption settings.

---

## Full Article

Microsoft provided the FBI with the recovery keys to unlock encrypted data on the hard drives of three laptops as part of a federal investigation, [Forbes reported on Friday](https://www.forbes.com/sites/thomasbrewster/2026/01/22/microsoft-gave-fbi-keys-to-unlock-bitlocker-encrypted-data/).

Many modern Windows computers rely on full-disk encryption, called BitLocker, which is [enabled by default](https://www.theverge.com/2024/8/14/24220138/microsoft-bitlocker-device-encryption-windows-11-default). This type of technology should prevent anyone except the device owner from accessing the data if the computer is locked and powered off.

But, by default, BitLocker recovery keys are uploaded to Microsoft’s cloud, allowing the tech giant — and by extension law enforcement — to access them and use them to decrypt drives encrypted with BitLocker, as with the case reported by Forbes.

The case involved several people suspected of fraud related to the Pandemic Unemployment Assistance program in Guam, a U.S. island in the Pacific. Local news outlet Pacific Daily News [covered](https://www.guampdn.com/news/another-unsealed-warrant-encrypted-data-seized-in-pua-fraud-investigation/article_1b98b770-daf5-436a-97f9-3a11f57accf5.html) the case last year, reporting that a warrant had been served to Microsoft in relation to the suspects’ hard drives. Kandit News, another local Guam news outlet, [also reported](https://kanditnews.com/3rd-warrant-against-tenorio-unsealed-encrypted-computer-files-seized/) in October that the FBI requested the warrant six months after seizing the three laptops encrypted with BitLocker.

A spokesperson for Microsoft did not immediately respond to a request for comment by TechCrunch. Microsoft told Forbes that the company sometimes provides BitLocker recovery keys to authorities, having received an average of 20 such requests per year.

Apart from the privacy risks of handing recovery keys to a company, Johns Hopkins professor and cryptography expert Matthew Green [raised the potential scenario](https://bsky.app/profile/matthewdgreen.bsky.social/post/3md3vciumvk2s) where malicious hackers compromise Microsoft’s cloud infrastructure — something that [has happened](https://techcrunch.com/2023/07/17/microsoft-lost-keys-government-hacked/) [several times](https://techcrunch.com/2024/01/19/hackers-breached-microsoft-to-find-out-what-microsoft-knows-about-them/) in recent years — and get access to these recovery keys. The hackers would still need physical access to the hard drives to use the stolen recovery keys.

“It’s 2026 and these concerns have been known for years,” Green wrote in a [post on Bluesky](https://bsky.app/profile/matthewdgreen.bsky.social/post/3md3vnprijk2s). “Microsoft’s inability to secure critical customer keys is starting to make it an outlier from the rest of the industry.”