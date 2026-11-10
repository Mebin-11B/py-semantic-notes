---
title: "Meta's Un-Stable Signature"
url: https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html
clipped: 2026-08-31 12:22:27
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Meta's Un-Stable Signature](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html)

## Digest Summary
Meta’s “Stable Signature” claims a 48‑bit watermark with a false‑positive rate below 1 in 10⁶, but empirical testing on 10 000 uncurated images shows massive deviations. The bits are not independent; a single neural network generates them, creating attractor clusters and a strong bias toward 1s (≈56 % ones). Chi‑square tests (χ² ≈ 7 632 and 12 205) reject randomness with p ≈ 0. Clusters of 25 identical codes and dozens of groups >10 images occur at Hamming distances ≤6, yielding an effective false‑positive rate of ~1 in 4 for Meta. Similar independence assumptions underlie Google’s SynthID and Adobe’s TrustMark, which also exhibit inflated true‑positive claims and false‑positive rates around 1 in 20 (Google) and 1 in 5 (Adobe). All three systems thus cannot reliably attribute images in legal or regulatory contexts, despite being promoted for AI‑generated content detection. The fundamental error is treating correlated neural‑network outputs as independent Bernoulli trials.

---

## Full Article

[The Hacker Factor Blog](https://hackerfactor.com/blog/)

    Home of the Angry Sheep

[Home](https://hackerfactor.com/)
[Blog](https://hackerfactor.com/blog/)
[Swag](https://www.zazzle.com/hackerfactor/?rf=238307745558769988)

    
        

### About

        [Dr. Neal Krawetz](https://hackerfactor.com/about.php) writes The Hacker Factor Blog. Follow him on [Mastodon](https://noc.social/@hackerfactor).
    
    
        

### Tools

        • [FotoForensics](https://fotoforensics.com/): Test your own photos.
• [Hintfo](https://hintfo.com/): View metadata.
• [Gender Guesser](https://hackerfactor.com/GenderGuesser.php): Use your words.
    
    
        

### Links

        Security
[Internet Storm Center](http://isc.sans.org/)
[Krebs on Security](http://krebsonsecurity.com/)
[Bruce Schneier](http://www.schneier.com/)

Images
[Photo Stealers](http://stopstealingphotos.com/)
[Awkward Family Photos](http://awkwardfamilyphotos.com/)
[Unsplash](https://unsplash.com/)

Debunking News
[iMediaEthics](http://www.imediaethics.org/)
[Poynter](http://www.poynter.org/)

Debunking Politics
[FactCheck](http://www.factcheck.org/)
[PolitiFact](http://www.politifact.com/)

Debunking Other
[Snopes](http://www.snopes.com/)
[Math with Bad Drawings](http://mathwithbaddrawings.com/)
    
    
        

### Calendar

        
  
      [«](https://hackerfactor.com/blog/index.php?/archives/2026/07.html)
      August '26
      [»](https://hackerfactor.com/blog/index.php?/archives/2026/09.html)
  

  
    S
    M
    T
    W
    T
    F
    S
  

          
                     
                     
                     
                     
                     
                     
                    1
              
          
                    2
                    3
                    4
                    5
                    6
                    7
                    8
              
          
                    9
                    10
                    11
                    12
                    13
                    [14](https://hackerfactor.com/blog/index.php?/archives/2026/08/14.html)
                    15
              
          
                    16
                    17
                    18
                    19
                    20
                    21
                    22
              
          
                    23
                    24
                    [25](https://hackerfactor.com/blog/index.php?/archives/2026/08/25.html)
                    26
                    27
                    28
                    29
              
          
                    30
                    31
                     
                     
                     
                     
                     
              
    

    
    
        

### Archives

        

- [August 2026](https://hackerfactor.com/blog/index.php?/archives/2026/08.html)

- [July 2026](https://hackerfactor.com/blog/index.php?/archives/2026/07.html)

- [June 2026](https://hackerfactor.com/blog/index.php?/archives/2026/06.html)

- [Recent...](https://hackerfactor.com/blog/index.php?frontpage)

- [Older...](https://hackerfactor.com/blog/index.php?/archive)

    
    
        

### Feeds

                
- 
            
            [RSS 1.0 feed](https://hackerfactor.com/blog/index.php?/feeds/index.rss1)
        
        
- 
            
            [RSS 2.0 feed](https://hackerfactor.com/blog/index.php?/feeds/index.rss2)
        

    
    
        

### Categories

        
- [Conferences](https://hackerfactor.com/blog/index.php?/categories/7-Conferences)

- [Copyright](https://hackerfactor.com/blog/index.php?/categories/16-Copyright)

- [Financial](https://hackerfactor.com/blog/index.php?/categories/8-Financial)

- [Forensics](https://hackerfactor.com/blog/index.php?/categories/14-Forensics)

- [Authentication](https://hackerfactor.com/blog/index.php?/categories/23-Authentication)

- [FotoForensics](https://hackerfactor.com/blog/index.php?/categories/17-FotoForensics)

- [Image Analysis](https://hackerfactor.com/blog/index.php?/categories/1-Image-Analysis)

- [IoT](https://hackerfactor.com/blog/index.php?/categories/22-IoT)

- [Mass Media](https://hackerfactor.com/blog/index.php?/categories/6-Mass-Media)

- [Music](https://hackerfactor.com/blog/index.php?/categories/24-Music)

- [Network](https://hackerfactor.com/blog/index.php?/categories/3-Network)

- [Honeypot](https://hackerfactor.com/blog/index.php?/categories/21-Honeypot)

- [Tor](https://hackerfactor.com/blog/index.php?/categories/19-Tor)

- [PTSD](https://hackerfactor.com/blog/index.php?/categories/25-PTSD)

- [Phones](https://hackerfactor.com/blog/index.php?/categories/18-Phones)

- [Politics](https://hackerfactor.com/blog/index.php?/categories/13-Politics)

- [Privacy](https://hackerfactor.com/blog/index.php?/categories/9-Privacy)

- [Programming](https://hackerfactor.com/blog/index.php?/categories/5-Programming)

- [AI](https://hackerfactor.com/blog/index.php?/categories/20-AI)

- [Security](https://hackerfactor.com/blog/index.php?/categories/4-Security)

- [Terrorists](https://hackerfactor.com/blog/index.php?/categories/2-Terrorists)

- [Travel](https://hackerfactor.com/blog/index.php?/categories/15-Travel)

- [Unfiction](https://hackerfactor.com/blog/index.php?/categories/12-Unfiction)

- [[Other]](https://hackerfactor.com/blog/index.php?/categories/11-Other)
[All categories](https://hackerfactor.com/blog/index.php?frontpage)
    

	

    

        

			

# [Meta's Un-Stable Signature](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html)

	

## 
	
		Tuesday, 30 June 2026
		

	
	    
	    
	    
		I'm wrapping up my investigation into invisible watermark algorithms and I am extremely disappointed. Not only do none of the modern AI-based algorithms work as they claim, it turns out that they are all making the same fundamental mistake.

I previously evaluated [Google's SynthID](https://hackerfactor.com/blog/index.php?/archives/1092-Reversing-SynthID.html) and [Adobe's TrustMark](https://hackerfactor.com/blog/index.php?/archives/1097-TrustMarks-False-Positive-Problem.html) algorithms. Both of them claim to have incredibly accurate results.

- According to Google's peer-reviewed and published [paper](https://arxiv.org/abs/2510.09263), they claim to have a true positive rate (TPR) above 99.97% -- meaning that they will miss their own watermarks no more than 3 in 10,000 times. However, my own [empirical testing](https://hackerfactor.com/blog/index.php?/archives/1092-Reversing-SynthID.html) found that is it much closer to 1 in 20. Moreover, SynthID is proprietary and only accessible through Google's "Gemini" AI system. Gemini has been observed [hallucinating results](https://hackerfactor.com/blog/index.php?/archives/1092-Reversing-SynthID.html) and providing contradictory conclusions depending on how the question is phrased.

- [According to Adobe's Content Authenticity Initiative](https://opensource.contentauthenticity.org/docs/trustmark/faq/), their TrustMark "can exceed 96% bit accuracy at around 42-45dB PSNR quality under severe noise degradations". However, that [statistic](https://arxiv.org/abs/2311.18297) focuses on resilience and not accuracy. In my [empirical tests](https://hackerfactor.com/blog/index.php?/archives/1097-TrustMarks-False-Positive-Problem.html), I found that TrustMark has a 10%-20% false positive rate, effectively making it useless. (If you see a TrustMark signature, then it is very likely random noise and not an actual signature.)
This time, I evaluated Meta's "Stable Signature" algorithm. (Their paper and code are in [GitHub](https://github.com/facebookresearch/stable_signature).) This system encodes a 48-bit sequence into the picture's visual content. The idea is that you can encode a unique 48-bit sequence as your watermark. If your decoder finds the same 48-bit sequence, then it can identify your own watermark.

WARNING: This blog entry leans heavily into math and statistics to prove that Stable Signature, TrustMark, and SynthID are nowhere near as reliable as their developers claim.

### The Basic Algorithm

Traditional (non-AI) invisible watermarks typically hide in subtle locations, such as the least significant bits, changes in brightness (e.g., Digimarc) or the frequency spectrum (DCT or FFT). There is always the risk that image encoding could corrupt the hidden data, so these algorithms typically rely on repetition over the image to help identify the true signal. In addition, they may include error correction code (extra bits in the data) to fix any minor data errors.

However, there is a problem with the traditional approaches: injecting hidden data in the image could create visible distortions. The modern approach uses an AI system to better hide the data with less added distortion.

As with SynthID and TrustMark, Stable Signature encodes binary data and uses an AI-model to decide where to hide it in the image. The AI is tuned to minimize visible distortions when embedding the data. Later, an AI-based decoder looks at the image and identifies the likely location where bits are stored, then it extracts the data.

There is always the case that the data may be mixed with noise. Different AI-based watermarking systems rely on different techniques for reducing the noise. For example:

- Google's SynthID only stores a few bits of data (effectively a flag or version number). This allows them to use a lot of data as repetition and to increase the accuracy rate.

- Adobe's TrustMark uses the [Bose-Chaudhuri-Hocquenghem](https://en.wikipedia.org/wiki/BCH_code) (BCH) algorithm. This acts as a combination of checksum and error correcting code that should reduce the number of errors.
Meta's Stable Signature uses a simple [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance).

 

The Hamming distance measures the number of bits that need to be swapped in order to correct the code. In effect, it defines a set of stable states (e.g., 10110 and 11000) and places a ring around each state that represents the single bit changes. If you change enough bits, then you will reach a different stable state.

According to Meta's [Stable Signature research paper](https://arxiv.org/abs/2303.15435), the 48-bits should be uniformly distributed and cites a "false positive rate below 10-6", or 1 in one million. This means you can choose a 48-bit sequence to use as your signature. Every picture will generate a 48-bit sequence, and the sequence can vary a little based on noise in the picture. However, if you find a code that is within a short Hamming distance of your code (e.g., within 6 bits difference), then you can determine that it is the same code with a high reliability.

At least, that's the theory.

### Empirical Testing

I went into this experiment assuming that everything works like they claim. I want to be able to reliably identify invisible watermarks associated with Meta. What I don't know is what sequence they use, or whether they use multiple codes depending on whether it comes from Meta's AI system, Facebook, Instagram, WhatsApp, etc.

Fortunately, this is something I can test! I grabbed an uncurated sample of pictures from FotoForensics: the first 10,000 unique images uploaded last month (May 2026). If the bit sequences are uniformly distributed with a "1 in 1 million" collision rate, then I should see a huge number of unique bit sequences and a few small clusters around pictures from Meta (Meta AI, Facebook, Instagram, etc.). Those clusters will represent the invisible watermarks used by Meta.

The results from my empirical test were definitely not what I expected. I found:

- No clusters associated with any Meta images. This suggests that Meta does not use their own Stable Signature watermarking software found on GitHub.

- With a random distribution, there should be no clusters. However, I had 25 different pictures that had the exact same bit sequence: 110110100111111011101001111000100111011000011101. With a 1 in a million collision rate, this should not happen! These pictures came from very different sources. Here's four of the 25 pictures (ranging from planets to light bulbs to text with a transparent (black) background):

    

All of these pictures have dark/black backgrounds and something bright in the middle. This suggests that Stable Signature operates more like a [perceptual hash](https://hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html) than an invisible watermark.

- Stable Signature uses a Hamming distance to identify a cluster. If I assume the 25 pictures are the center (centroid) of the cluster and use a 6-bit Hamming distance, then there are 356 pictures that are similar. And if I assume that the 25 pictures are not the center but part of a cluster, then a Hamming distance of 6 has a cluster of 450 pictures centered 3 bits away, at 110110000111111011101011111000100111001000011101. This cluster represents 4.5% of the uncurated image data set! Here are a few samples from this larger cluster:

   

(I'm explicitly not sharing pictures with personal information, like invoices, recognizable people, and GPS information.)
It's not just one random cluster that is massively large (450 pictures out of 10,000). There's a cluster of 184 pictures at 110101001011001011001011111000100111001000011101, 58 pictures at 110100000011111010001001111000100111011000011101, etc. I found over 60 clusters with more than 10 pictures each at a Hamming distance of 6. That should not happen with a "1 in 1 million" collision rate.

### Independent Analysis

I went back to Meta's research paper to see if I could find the discrepancy. And there it was, in section 3.1: They tested their system against the hypothesis that the 48-bits are each independent and uniformly distributed. The problem is, they use one neural network to generate the bits. That explicitly means that the bits are dependent, not independent.

Their paper assumes a binomial distribution. That is, given an arbitrary image, the 48-bits represent a random coin flip. The math becomes:
 

This computes the probability of 48 random bits being within a Hamming distance (T). The probabilities table becomes:

Hamming Distance Threshold (T)Bit Error Rate (BER)Probability of a Random Image Matching by Chance14 bits or fewer≤ 29.17%1 in 362.6313 bits or fewer≤ 27.08%1 in 957.8112 bits or fewer≤ 25.00%1 in 2,788.3511 bits or fewer≤ 22.92%1 in 8,999.0810 bits or fewer≤ 20.83%1 in 32,416.809 bits or fewer≤ 18.75%1 in 131,390.288 bits or fewer≤ 16.67%1 in 605,094.897 bits or fewer≤ 14.58%1 in 3.20 Million6 bits or fewer≤ 12.50%1 in 19.83 Million5 bits or fewer≤ 10.42%1 in 146.19 Million4 bits or fewer≤ 8.33%1 in 1.32 Billion3 bits or fewer≤ 6.25%1 in 15.24 Billion2 bits or fewer≤ 4.17%1 in 239.15 Billion1 bit or fewer≤ 2.08%1 in 5.74 Trillion0 bits (perfect match)= 0.00%1 in 281.47 Trillion

Meta's paper says that they use a Hamming distance of 7 bits (requiring 41 of 48 bits), which matches their claim of a "false positive rate below 10−6". However, I'm seeing problems at a Hamming distance of 6 (should be 1 in 20 million) and even collisions at 0 (1 in 281 trillion)!

### The Core Problem

There is clearly a discrepancy between the theoretical probabilities and the empirical testing. When I looked back over [Meta's research paper](https://arxiv.org/abs/2303.15435), I saw the problem:

According to Meta's paper, each of the 48-bits are independent. In a perfectly independent 48-bit hypercube, un-watermarked images should scatter uniformly across all 248 possible values. However, neural networks map a [non-linear manifold](https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction) (a multi-dimensional wavy surface) through this hypercube. This mathematical landscape is warped with its own peaks, ravines, and valleys. It has attractors that form clusters, and repulsers that form voids where stable values can never exist; this is a feature of a neural network. And most importantly, the output bits are explicitly not independent.

 

The left diagram illustrates an expected uniform distribution if all of the bits were independent. The right diagram are the types of theoretical clusters that form when the bits are dependent. There should be clusters around attractors and voids (areas with no dots) from the repelling regions.

Moving from theoretical to empirical, I graphed the data. The 48 bits can be represented as bytes. I took the first 24 bits and converted them into 8-bit red, green, and blue pixel colors. If the data is truly random, then the colored dots should be distributed across the RGB cube. However, if the bits are dependent, then there should be very clear clusters, structures, and voids. Here's the graph:

 

Yes, there are very clear structures that look like planes and lines. Within the planes are clusters, and outside the planes are very large voids -- areas where there are no dots at all. The data generated by Meta's Stable Signature implementation fails this basic test for independence.

The biggest cluster that I found represents a Zero Signal Bias (ZSB). When their neural network doesn't find a watermark, it moves the 48 bits toward a strong attractor, like a massive gravitational well. At 6 bits error, it should have a collision of around 1 in 20 Million. But in reality, my 10,000 pictures had a cluster of 450 images within 6 bits due to the ZSB. That's an error rate of around 1 in 22 with the ZSB alone. If we add in all of the other clusters that contain at least 10 pictures, then 2327 pictures are in various clusters; we're looking at an error rate around 1 in 4 -- and that's at a Hamming distance of 6, which is more conservative than their paper's Hamming distance of 7. (In AI terms, this is a representation collapse or structural bias that is typical for deep neural networks.)

(As an aside: Given their "1 in 1 million" claim, I could look for any clusters of 2 or more pictures. At clusters of 2 or larger, 5,237 of the 10,000 test images were in clusters, or 52%. If you show their algorithm 10,000 pictures, then there is a better-than 50% chance of a false positive match.)

### Less Than Random

It's one thing for me to claim that there are visible clusters and to show pictures of clusters, but another to prove it mathematically. (Time to dust off my college textbooks from "Introduction to Statistics"...)

I fed Meta's code the first 10,000 images from May 2026. A few of the images were in unsupported formats (HEIC, WebP, and a few corrupted JPEG files), resulting in 9,847 viable pictures. I evaluated this data with elements from the [NIST Statistical Test Suite](https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final) (SP 800-22) for randomness, including a monobit test and Chi-Squared (χ2) test for independence.

The monobit test determines if the baseline frequency of adjacent bits seems independent.

- Total Bits Processed: 9,847 pictures × 48 bits per signature = 472,656 bits

- Observed Count of Ones ('1'): 266,419

- Observed Count of Zeros ('0'): 206,237

- Expected Count (E): 236,328 for each.
Running a simple standard Chi-Square Goodness-of-Fit test for this bit balance:

- In mathemat-ese: with 1 degree of freedom, a χ2 statistic of 7,662.81 yields a p-value infinitely close to 0.0 (p ⋘ 10-100). (As an aside, most Chi-square [tables](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm) usually evaluate the 1 degree of freedom up to around χ2=10. This χ2 value is so astronomically high that the probability p effectively becomes zero.)

- In English: That's definitely not random or independent.
The watermark extraction is strongly biased toward producing 1s over 0s across global arbitrary images (roughly 56% ones to 44% zeros). This immediately violates the uniform distribution assumption.

The second test is the Chi-Square (χ2) Test for Serial Independence. If the bits were independent, the transition probability between adjacent bits would just be the product of their individual probabilities. This table shows the occurrence rate of the transition pairs across all of the observed 10,000 (well, 9,847) pictures:

Transition PairObserved Count (O)Expected Count under Independence (E)0 to 0106,75090,0510 to 195,296116,1861 to 095,302116,1861 to 1165,461149,976

- In mathemat-ese: With 1 degree of freedom for the transition contingency table (accounting for fixed margins), a χ2 value of 12,205.9 gives a p-value of 0.0.

- In English: Ain't no way this is random or independent.
And as if this wasn't conclusive enough, there are other tests we could apply:

- Static Tail Patterns: Looking closely at the end of the 48-bit sequences, a massive cluster of strings end explicitly in ...111101 or ...00111101. Additionally, bit position 46 is nearly always "1" (228 zeros vs 9619 ones, or 97.7% of the time it is "1"), position 47 is "0" (8958 of 9847 images, or 90.97%), and position 48 is "1" (found with 9696 images, or 98.5%) across thousands of uncurated, real-world images.

- Structural Clustering: Certain bit columns share an extraordinarily high Mutual Information score (I(X;Y)). For example, knowing the output of bit position 12 gives you better than an 80% accuracy in predicting bit position 28.
The assumption of a "uniform distribution over arbitrary pictures" relies on the idealistic premise that random natural image features project uniformly across the decision boundaries of a network. However, because the extraction network maps inputs to a constrained, highly continuous hyper-dimensional manifold, the network's latent layers natively enforce structural smoothness.

For the TL;DR crowd: 
Meta's researchers made a fundamental mistake when computing their accuracy rates. It's not a "1 in 1 million" chance of a false match, it's closer to 1 in 4 -- because the 48 bit values per signature are not independent.

As I re-read Meta's research paper, I realized that the statistical error wasn't an oversight; Meta's researchers explicitly acknowledged the problem. In [their paper](https://arxiv.org/pdf/2303.15435) (Section 4.1), they wrote:
Second, we observed that W’s output bits for vanilla images are correlated and highly biased, which violates the assumptions of Sec. 3.1 [the section about independent statistical test methods].
In other words, they recognized that the extracted bits are not independent. Despite this, their published false-positive analysis still relies on the assumption that the bits are independent.

### Widespread Problems

Knowing that Meta's accuracy rate is grossly inflated due to assuming bit-wise independence when there is none, I looked back over Google's and Adobe's papers for their own watermarks. Did Google's and Adobe's researchers make this same mistake?

- Google's SynthID [research paper](https://arxiv.org/abs/2510.09263) talks in terms of True Positive Rates (TPR). They do make this same "bit-wise independent" mistake, but it's obfuscated in the paper. You can see the error in their Equation 3 ([PDF](https://arxiv.org/pdf/2510.09263) page 8), where they assume there is a uniform (independent) distribution. Their paper hyperfocuses on the true positive rate and never addresses the false positive distribution. (Either they didn't know to look, or they knew and decided to not report it because it would expose a serious weakness in their solution.)

- Adobe's TrustMark [research paper](https://arxiv.org/abs/2311.18297) also makes assumptions of independence. You can see this in their [PDF](https://arxiv.org/pdf/2311.18297) with the binary cross-entropy loss in Section 3.1.4. This mathematically treats each bit position as an independent Bernoulli trial. (By definition, a [Bernoulli process](https://en.wikipedia.org/wiki/Bernoulli_process) strictly requires independence.) In their experiments (Section 4.1), they wrote "At test time, every image is associated with a random watermark", but they never tested if the random watermarks were similar to each other.
This introduction-to-statistics mistake is found in all three of these invisible watermarking technologies. The detections produced by these systems are so unreliable that an analyst cannot determine whether a reported detection is real or a false positive, or whether a reported non-detection is genuine or a false negative.

It's also worth noting that, shortly after releasing Stable Signature, Meta developed another algorithm: [Pixel Seal](https://arxiv.org/abs/2512.16874). (Not to be confused with my own Secure Evidence Attribution Label / SEAL technology.) Pixel Seal moves to a 256-bit payload to increase the capacity, and their related model, [Chunky Seal](https://arxiv.org/abs/2510.12812), pushes up to 1024 bits. While [Meta's approach](https://github.com/facebookresearch/videoseal) focuses heavily on addressing the invisibility side using an adversarial-only discriminator, the underlying approach still uses a neural network mapping. Using more bits only exacerbates this flaw.

### Potential Uses

Algorithms can have uses. For example, Meta, Google, and Adobe are training their own AI models on images that they encounter. To prevent poisoning their training sets, they want to exclude images generated by their own systems. In this regard, watermarking does help them. For example, if Meta excludes an extra 25% of images (from false positives), then they still have a lot of images that they can train on.

However, that same usage does not work with legal cases. For example, consider an insurance company. Most insurance claims today include photographic evidence. The company wants camera-original photos, but have to use whatever the customer submits. The problem is that there is a lot of insurance fraud. In theory, seeing a watermark from an AI system like Meta, Google, or Adobe, should be great for identifying and ruling out fraud. Unfortunately, Stable Signature, SynthID, and TrustMark are so inaccurate that none of them can be trusted; it's not even worth testing to see if customer photos contain these invisible watermarks.

For these watermarking systems, I'm talking about very high error rates: roughly 1-in-4 for Meta, 1-in-5 for Adobe, and 1-in-20 for Google. But let's pretend that they work much better, like a 1-in-20,000 false positive rate. An insurer processing 100,000 claims per month would expect to accuse around 5 completely honest customers of fraud each month. Falsely denying 5 out of 100,000 claims? That creates a toxic customer service nightmare, severe legal liability, and fines from regulatory bodies for bad-faith claim denials. This could even become a class-action lawsuit that they couldn't win.

As bad as it is for insurance and financial institutions, there are much higher stakes at play. The EU AI Act ([Article 50(2)](https://artificialintelligenceact.eu/wp-content/uploads/2024/04/TA-9-2024-0138_EN.pdf)), China's [GB 45438-2025](https://www.congress.gov/crs-product/R48555), [California SB 942](https://legiscan.com/CA/text/SB942/id/3013546), and similar legislation are moving toward mandating AI content watermarking.

The failure of these three leading systems, from three Fortune-500 companies, to meet their own claimed accuracy rates is not just an academic curiosity. Regulators and courts will employ these systems for attribution and fraud detection. Reliable AI-based watermarking technology is not ready.

Three companies. Three algorithms. Three different research teams. The same fundamental error. The false positives won't go on trial. People will.
	    

	    
	    
	    
	    
				    
						   Read more about [AI](https://hackerfactor.com/blog/index.php?/categories/20-AI), [Authentication](https://hackerfactor.com/blog/index.php?/categories/23-Authentication), [Forensics](https://hackerfactor.com/blog/index.php?/categories/14-Forensics), [FotoForensics](https://hackerfactor.com/blog/index.php?/categories/17-FotoForensics), [Image Analysis](https://hackerfactor.com/blog/index.php?/categories/1-Image-Analysis), [Programming](https://hackerfactor.com/blog/index.php?/categories/5-Programming), [Security](https://hackerfactor.com/blog/index.php?/categories/4-Security)		
				    			| [Comments (6)](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#comments)
		    		
		| [Direct Link](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html)

		
	    
	
	

		    
	    
	    	
		    
		
		Comments
		
		        
    
        
            [#1](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#c5673)
            
                            H4x0R
                        
                        on
            2026-06-30 14:26

                                        ([Reply](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#serendipity_CommentForm))
                
                    
	
        Nice work! Finding the AI image watermarks from Meta, Adobe, and Google are criticized as statistically unreliable. Their false-positive claims assume independent bits, but tests show biased, clustered outputs. They may help internal filtering, but are unsafe for legal, fraud, or regulatory evidence.
    
    
    
        
            [#2](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#c5674)
            
                            Pierre Fernandez
                        
                        on
            2026-07-01 02:27

                                        ([Reply](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#serendipity_CommentForm))
                
                    
	
        Hi! author of Stable Signature here. 

"""
Second, we observed that W’s output bits for vanilla images are correlated and highly biased, which violates the assumptions of Sec. 3.1 [the section about independent statistical test methods].

In other words, they recognized that the extracted bits are not independent. Despite this, their published false-positive analysis still relies on the assumption that the bits are independent.
"""

You're explicitly removing the next sentence of the article! which is
"Therefore we remove the bias and
decorrelate the outputs of W by applying a PCA whitening transformation (more details in App. A.1)."

It might not be perfect, but on the distribution of the images we operated on (COCO), we were quite close to this assumption. 

If you are feeling ok sharing code/ chatting via email, I'd be happy to improve the independence for the next models. What you're suggesting is to group image by perceptual clusters and check the independence there?
    
    
    
        
            [#2.1](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#c5675)
            
                            Dr. Neal Krawetz
                        
                            ([Homepage](https://hackerfactor.com/))
                        on
            2026-07-01 07:56

                                        ([Reply](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#serendipity_CommentForm))
                
                    
	
        Hello Pierre Fernandez,

Thank you for the feedback. You're right that the paper applies PCA whitening to decorrelate the outputs before the statistical evaluation.

However, PCA whitening only removes linear correlations. The dependency I'm identifying is nonlinear and arises from the geometry of the high-dimensional manifold that the neural network implicitly defines over the image distribution. No linear transformation can remove that structure. My empirical tests, run on images outside the COCO distribution, show that the clustering and bit-position biases persist after whatever normalization the model applies internally.

The deeper issue is architectural: a single neural network with shared weights (the weight matricies) will produce all 48 output bits from common intermediary representations. Unless you use 48 fully independent AI networks, the outputs will share the same structure. PCA whitening measured on COCO may look close to independent on COCO, but that's a property of that particular distribution, and not a guarantee that holds across arbitrary inputs. A watermarking system deployed in the real world cannot limit its guarantees to the COCO distribution.
    
    
    
        
            [#3](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#c5676)
            
                            Dodo
                        
                        on
            2026-07-04 16:32

                                        ([Reply](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#serendipity_CommentForm))
                
                    
	
        I wonder why you even need AI for this.
It's not that hard to create a watermark.

Just do some minimal pixel nudging and you have something that is imperceptible but adds up over the entire image.
You don't even need to do frequency transformations or anything, just plain statistical analysis is enough.
Align the image according to the hidden markers and then read the vectors for all bits.
Then you can reconstruct the original data using probability and error correction.

It should be able to survive quite a bit of abuse.
Or am i too naïve?
    
    
    
        
            [#3.1](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#c5677)
            
                            Dr. Neal Krawetz
                        
                            ([Homepage](https://hackerfactor.com/))
                        on
            2026-07-04 18:44

                                        ([Reply](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#serendipity_CommentForm))
                
                    
	
        Hi Dodo,

There are two driving forces: data and shiny.

Force #1: Data
With non-AI watermarking (FFT, DCT, intensity, etc.), there is a low limit to the amount of data that can be stored before causing visual distortions. ("Visual" meaning "a human might see it".)

This low data limit is fine if you're competing with something like Google SynthID (which only stores a few bytes of data). However, TrustMark, Stable Signal, Pixel Seal, Chunky Seal, etc. try to store a lot more data (100 bytes with TrustMark up to 1024 bytes with Chunky Seal).

AI helps hide the data better, reducing visual distortions. However, there is a tradeoff: you can have independent bits and low data without AI, or dependent bits and higher data with AI.

Force #2: Shiny
There are some people who strongly believe that "AI can solve everything". In effect, it's the latest round of shiny, hype-based technology. "IoT everything" (remember the Juicero and networked coffee makers?), "Flash" web sites (from Macromedia to Adobe to historical footnote), Blockchain, NFTs, and now "AI". This is just another instance of developers forcing a technology into an ill-suited problem space.

Wait a year or two and some new shiny tech will replace AI. "Post Quantum Invisible Watermarking!"  (I wish I was kidding: https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1750515/full)
    
    
    
        
            [#4](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#c5678)
            
                            Cat
                        
                        on
            2026-07-04 23:29

                                        ([Reply](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html#serendipity_CommentForm))
                
                    
	
        Is there a significant false positive rate for a random image's (non-uniform) hash matching a cryptographically random string of bits, rather than another image's (non-uniform) hash?
    

				

		
		
		
		
			Add Comment

[ Top level ]#1: H4x0R on 2026-06-30 14:26
#2: Pierre Fernandez on 2026-07-01 02:27
  #2.1: Dr. Neal Krawetz on 2026-07-01 07:56
#3: Dodo on 2026-07-04 16:32
  #3.1: Dr. Neal Krawetz on 2026-07-04 18:44
#4: Cat on 2026-07-04 23:29

Enclosing asterisks marks text as bold (*word*), underscore are made via _word_.Standard emoticons like :-) and ;-) are converted to images.E-Mail addresses will not be displayed and will only be used for E-Mail notifications.

		

			    
	
	
	    
    
    
    
    
    
    
    

    
    

Copyright 2002-2026 Hacker Factor. All rights reserved.
