---
title: "AMD acquires Taalas to boost inference performance by etching models in silicon"
url: https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344
clipped: 2026-08-31 12:22:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [AMD acquires Taalas to boost inference performance by etching models in silicon](https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344)

## Digest Summary
AMD has acquired Toronto‑based AI chip startup Taalas, whose chips embed model weights directly into silicon (model‑specific integrated circuits, MSICs) rather than using HBM. The first test chip, HC1, fabricated on TSMC’s 6 nm process, demonstrated 16,960 tokens / s for Meta’s Llama 3.1 8B—approximately 48× faster than Nvidia GPUs and 8.5× faster than Cerebras accelerators. Taalas chips comprise a mask‑ROM region for etched weights and an SRAM region for KV caches and fine‑tuning adapters. A second‑generation HC2, slated for release this summer, will support up to 20 billion parameters per chip, implying that 50 such accelerators could handle a trillion‑parameter model, offering greater space‑ and power‑efficiency than Nvidia’s LPX systems. AMD plans to pair Taalas accelerators with its Instinct‑based Helios racks in a disaggregated architecture, offloading token generation to the etched‑weight chips. The approach trades flexibility for performance: model changes beyond lightweight adapters require a chip re‑spin, though Taalas claims only two metal layers need alteration, reducing cost and lead time. The acquisition is expected to close in Q4 pending regulatory approval.

---

## Full Article

[Jump to main content](https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344#main)

        

        

        
                

        
            

        REG AD
        
        

            
                

                    

                            

                        

    

        

AI and ML

    
                
    

        

# AMD acquires AI chip startup Taalas to boost inference performance by etching models into silicon

        

Early tech demos show model-specific integrated circuits churning out up to 17,000 tokens a second

        
    

    
        
    
    
            
    
        
    

        
        Tobias Mann
                [Tobias
                Mann](https://www.theregister.com/author/tobias-mann)

                SYSTEMS EDITOR
        
    

        
    

    
    
        
            Published
            thu 6 Aug 2026 // 21:05 UTC
        
    

    
            
            
            
            
            
            
    

                        

                        
                        

                        

                        
    
    

    

In AMD’s latest bid to upset Nvidia's dominance in AI hardware, the House of Zen has acquired AI chip company Taalas, which bakes model weights directly into silicon in a process that promises to boost inference performance by an order of magnitude or more.

The deal, announced at market close on Thursday, appears to be framed in much the same context as Nvidia’s $20 billion [licensing deal](https://www.theregister.com/on-prem/2025/12/31/why-did-nvidia-really-drop-20b-on-groq/2018042)with Groq last December: make high-performance “premium” inference services prized for AI agents, like code assistants, faster and cheaper to run. AMD didn’t disclose the terms of the deal, but from what we understand, this is an actual acquisition rather than an acquihire.

Founded in 2023 and based in Toronto, Taalas’ approach to inference is radically different from conventional GPUs or the dataflow architectures that underpin Groq LPUs or Cerebras' waferscale accelerators. 

        REG AD
        
        

### A model-specific integrated circuit

        REG AD
        
        

The startup’s chips don’t rely on HBM to store the model weights but rather etch them directly into the silicon. In a sense, Taalas’ chips are really model-specific integrated circuits or MSICs.

Perhaps more importantly, Taalas’ tech isn’t just conceptual. In February, the startup [revealed](https://www.nextplatform.com/compute/2026/02/19/taalas-etches-ai-models-onto-transistors-to-rocket-boost-inference/4092140) its first test chip fabbed on TSMC’s 6nm process tech, which it called the HC1. Initial benchmarks saw the chip serve Meta’s Llama 3.1 8B at a blistering 16,960 tokens a second — when announced last February, that was 48x faster than Nvidia's GPUs and 8.5x faster than Cerebras' accelerators. 

While Llama 3.1 is ancient by today’s standards, having made its debut all the way back in mid 2024, the reticle-sized chip was really intended to prove the concept. 

Taalas has been incredibly secretive about how its chips actually work, but we know its processors are comprised of two main regions: the mask-ROM recall fabric where model weights are etched, and the SRAM recall fabric where KV caches and fine-tuning adapters are stored.

For its second-gen HC2 chip due out this summer, Taalas aims to boost parameter count to 20 billion parameters. That might not sound like much, but just like with GPUs for larger models, weights are simply distributed across multiple accelerators using pipeline parallelism.

At 20 billion parameters per chip, you’d need just 50 accelerators to support a trillion-parameter model, and AMD just so happens to have a rack-scale compute platform and in-house system design team that can comfortably accommodate that.

That’s quite a bit more space and power efficient than Nvidia’s recently unveiled LPX systems, which would need a few dozen GPUs and at least [2,000 Groq LPUs](https://www.theregister.com/special-features/2026/03/19/a-closer-look-at-nvidias-groq-powered-lpx-rack-systems/5223364) to serve the same model.

From what we understand, AMD intends to pair its Instinct-based [Helios racks](https://www.theregister.com/systems/2026/07/23/amd-attacks-the-rack-with-helios-systems-that-rival-nvidias/5277246) with chips based on Taalas’ tech, which implies a disaggregated architecture where compute-heavy prompt processing is done on GPUs while token generation is offloaded to Taalas-based accelerators.

        REG AD
        
        

It’s also possible that AMD could adopt a sort of tick-tock cadence in which customers initially deploy and validate models on Instinct accelerators and, once they’re satisfied with them, transition to Taalas accelerators. We can only speculate at this point, but here’s what AMD’s SVP of AI, Vamsi Boppana, had to say about it in a canned statement:

“AMD is building a full-stack AI platform that gives customers the flexibility to deploy the right compute solutions for every AI workload."

### You better really love that model

While the tech is blazing fast, if you hadn’t already figured it out, it comes with a pretty substantial downside. Once the chips are deployed you’re stuck with that model. Any change bigger than something like a LoRA adapter is going to require a re-spin of the chips, which is not only expensive but time-consuming.

Nearly four years into the AI boom, new models are rolling out on a nearly monthly basis. In order to benefit from Taalas’ tech, AMD’s customers are going to have to be really sure about their choice of models, which will be easier for some than others.

However, if the startup is to be believed, the situation isn’t quite as bad as it sounds. While new models will require a re-spin, it doesn’t require starting over from scratch. Instead, just two layers of metal need to be changed, which is a lot cheaper and less time-consuming.
    
    
        

## MORE CONTEXT

        
- 
    

### 

[Elon pledges to give Nvidia a virtual monopoly over the stars](https://www.theregister.com/systems/2026/08/05/elon-pledges-to-give-nvidia-a-virtual-monopoly-over-the-stars/5283605)

- 
    

### 

[AMD's AI eggs are in too few baskets, Wall Street worries](https://www.theregister.com/systems/2026/08/05/amds-ai-eggs-are-in-too-few-baskets-wall-street-worries/5283142)

- 
    

### 

[China turns up the heat with open model blitz as US model makers panic](https://www.theregister.com/ai-and-ml/2026/08/03/china-turns-up-the-heat-with-open-model-blitz-as-us-model-makers-panic/5282526)

- 
    

### 

[A deep dive into Nvidia's Vera CPU and the Olympus cores that power it](https://www.theregister.com/systems/2026/08/01/nvidias-vera-cpu-and-the-olympus-cores-that-power-it-deep-dive/5282056)

    

With that said, we strongly suspect this tech will largely be deployed by AI model devs, their infrastructure providers, and a handful of inference providers. In an interview with our sibling site [The Next Platform](https://www.nextplatform.com/compute/2026/02/19/taalas-etches-ai-models-onto-transistors-to-rocket-boost-inference/4092140) in February, the company suggested that etching a model's weights into silicon is 100x less expensive than training a frontier model.

AMD is certainly in a position to negotiate those deals. OpenAI, Anthropic, and Meta are all major Instinct customers. Given the close working relationship between the model houses and the chip designer, it wouldn't be surprising to see a GPT or Claude deployed on a combination of Taalas and instinct accelerators.

        REG AD
        
        

The tech also has implications for model development. One of the ways developers have cut down on hallucinations is by trading time for accuracy. The technique, called test-time scaling, is quite simple in practice, and involves allowing a model to “think” for longer before responding.

One drawback of test-time scaling is that it consumes substantially more tokens, which makes it expensive, and means users have to wait longer for the chatbot, code assistant, or agent to respond. If AMD’s Taalas buy can drive down the cost per token and boost output speeds by 10x or 20x, model devs may opt to extend the reasoning time even further.

In any case, we may not have to wait long to see just how Taalas fits into AMD’s broader vision. Subject to regulatory approval, the deal is expected to close in the fourth quarter. ®

    

    

                        

                        
        
                    [gpu](https://www.theregister.com/tag/gpu)
                    [nvidia](https://www.theregister.com/tag/nvidia)
                    [amd](https://www.theregister.com/tag/amd)
                    [ai](https://www.theregister.com/tag/ai)
                    [semiconductor](https://www.theregister.com/tag/semiconductor)
                    [systems](https://www.theregister.com/tag/systems)
                    [cloud infrastructure month 2026](https://www.theregister.com/tag/cloud%20infrastructure%20month%202026)
        
    

                        
                            
                                    
                                    
                                    
                                    
                                    
                                    
                            
                        

                    
                    
                
                
                
	

        REG AD
        
        

	

    
    
            
            
	
    
    

        

        

            

        
        
    

	
	
    
    
        
            

## 

[AI AND ML

                
                
            
            

        

        
                Debian votes to let contributors code with AI 

                
    Disclosure optional, quality mandatory](https://www.theregister.com/ai-and-ml/2026/08/30/debian-votes-to-let-contributors-code-with-ai/5293421)

        
    

    
    
        
            

## 

[security

                Turns out Brits would quite like their private messages to stay private

                
    Polling finds two-thirds don't trust this government, or any future one, with access to their encrypted chats](https://www.theregister.com/security/2026/08/30/turns-out-brits-would-quite-like-their-private-messages-to-stay-private/5292994)

        
    

    
    
        
            

## 

[devops

                Platform Engineering 2.0: your platform was built for a different era. AI just exposed it

                
    PARTNER CONTENT: Platform engineering won the argument. Now it has to grow up fast and evolve for the AI era.](https://www.theregister.com/devops/2026/08/06/partner-content-platform-engineering-20-your-platform-was-built-for-a-different-era-ai-just-exposed-it/5283237)

        
    

	
    
    
        
            

## 

[NETWORKS

                AWS mumbles about its cost-busting networking tech when it should be shouting

                
    A lot of datacenter networks are run by absolute clowns. Not Amazon's](https://www.theregister.com/networks/2026/08/29/aws-mumbles-about-its-cost-busting-networking-tech-when-it-should-be-shouting/5293379)

        
    

    
    
        
            

## 

[COLUMNISTS

                
                
            
            

        

        
                Unsafe at any speed: AI optimists are turning cautious as safety concerns mount

                
    And as for getting US government to help – uncontrolled AI is not as dangerous as AI under the control of the technically clueless](https://www.theregister.com/columnists/2026/08/28/unsafe-at-any-speed-ai-optimists-are-turning-cautious-as-safety-concerns-mount/5292853)

        
    

    
    
        
            

## 

[offbeat

                Startup bags $7M to build drone-interceptor-in-a-backpack systems

                
    Spike drone defense system is designed to be carried in a rucksack or mounted on top of a vehicle](https://www.theregister.com/offbeat/2026/08/29/startup-bags-7m-to-build-drone-interceptor-in-a-backpack-systems/5293176)

        
    

    
    

                

### 
                    TOP STORIES
                

        
                
- 
                    
                        
                    
                    
                        

#### 

[security
                            
                            Researcher shows how Claude Code can be tricked simply by asking it to summarize a website](https://www.theregister.com/research/2026/08/28/researcher-shows-how-claude-code-can-be-tricked-simply-by-asking-it-to-summarize-a-website/5293372)
                    
                
                
- 
                    
                        
                    
                    
                        

#### 

[security
                            
                            Security vets rally around $4 paper password books for sale in Australia](https://www.theregister.com/security/2026/08/24/security-vets-rally-around-4-paper-password-books-for-sale-in-australia/5291234)
                    
                
                
- 
                    
                        
                    
                    
                        

#### 

[science
                            
                            German-Japanese researchers invent electricity-free tech that could cool datacenters](https://www.theregister.com/science/2026/08/28/german-japanese-researchers-invent-electricity-free-tech-that-could-cool-datacenters/5293364)
                    
                
                
- 
                    
                        
                    
                    
                        

#### 

[Legal
                            
                            Nuisance-call blocker fined £190k for being a nuisance caller](https://www.theregister.com/security/2026/08/27/nuisance-call-blocker-fined-190k-for-being-a-nuisance-caller/5292888)
                    
                
                
- 
                    
                        
                    
                    
                        

#### 

[AI and ml
                            
                            Apple defies memory shortage with new Mac minis](https://www.theregister.com/ai-and-ml/2026/08/25/apple-defies-memory-shortage-with-new-mac-minis/5292406)
                    
                
                
- 
                    
                        
                    
                    
                        

#### 

[Security
                            
                            AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones](https://www.theregister.com/security/2026/08/24/aliexpress-accused-of-fingerprinting-shoppers-with-silent-audio-trick-that-also-muted-a-devs-headphones/5291662)
                    
                
        
    

	

    
    
                

### [AI](https://beta.theregister.com/tag/ai)

            
                    
- 
                        

#### 

[security
                                    Industry that built the problem offers to sell you the solution
                                    100+ tech giants warn AI attacks are coming, skip the part where they pay for defenses](https://www.theregister.com/security/2026/08/28/industry-that-built-the-problem-offers-to-sell-you-the-solution/5293207)
                    
                    
- 
                        

#### 

[SYSTEMS
                                    Nvidia and Cerebras are selling performance their customers will (probably) never see
                                    Touting batch 1 token generation is a bit like boasting about the top speed of your car](https://www.theregister.com/systems/2026/08/27/nvidia-and-cerebras-are-selling-performance-their-customers-will-probably-never-see/5293117)
                    
                    
- 
                        

#### 

[software
                                    Google forces Android apps to use memory more wisely as RAMpocalypse rages
                                    No one can afford RAM anymore, so we're requiring devs to mind memory usage](https://www.theregister.com/software/2026/08/27/google-forces-android-apps-to-use-memory-more-wisely-as-rampocalypse-rages/5293071)
                    
                    
- 
                        

#### 

[personal tech
                                    HP has a solution to expensive AI tokens: Buy a more expensive PC
                                    Rising cloud AI costs are pushing workloads onto pricier PCs – which just happen to be better for PC maker's margins](https://www.theregister.com/personal-tech/2026/08/27/hp-has-a-solution-to-expensive-ai-tokens-buy-a-more-expensive-pc/5292922)
                    
                    
- 
                        

#### 

[SYSTEMS
                                    Meta's new MTIA 400 chip has a split personality: Training AI and serving ads
                                    Faster than Blackwell, but still no replacement for AMD or Nvidia ... yet](https://www.theregister.com/systems/2026/08/26/metas-new-mtia-400-chip-has-a-split-personality-training-ai-and-serving-ads/5292727)
                    
            
    

    
    
                

### [Infosec](https://beta.theregister.com/security)

            
                    
- 
                        

#### 

[Security
                                    Russians are posing as Signal support to launch phishing attacks
                                    PLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!](https://www.theregister.com/security/2026/03/22/russians-posing-as-signal-support-to-launch-phishing-raids/5221189)
                    
                    
- 
                        

#### 

[Security
                                    Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attack
                                    PLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more](https://www.theregister.com/security/2025/07/21/microsoft-warns-on-prem-sharepoint-users-of-a-zero-day/550805)
                    
                    
- 
                        

#### 

[Black Hat and DEF CON
                                    DEF CON Franklin project enlists hackers to harden critical infrastructure
                                    Voting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included](https://www.theregister.com/special-features/2024/08/12/def-con-launches-public-policy-report-volunteer-program/408600)
                    
                    
- 
                        

#### 

[Security
                                    EQT buys majority share in Swiss cybersecurity biz Acronis
                                    Went at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified](https://www.theregister.com/security/2024/08/07/eqt-buys-majority-share-in-cybersecurity-outfit-acronis/853853)
                    
                    
- 
                        

#### 

[Malware Month
                                    Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sight
                                    On the plus side, infosec's a good bet for a long, stable career](https://www.theregister.com/special-features/2024/05/08/10-years-since-the-first-corp-ransomware-and-no-end-in-sight/1259096)
                    
            
    

    
    
                

### [FOSS](https://beta.theregister.com/tag/FOSS)

            
                    
- 
                        

#### 

[Debian votes to let contributors code with AI 
                                    Disclosure optional, quality mandatory](https://www.theregister.com/ai-and-ml/2026/08/30/debian-votes-to-let-contributors-code-with-ai/5293421)
                    
                    
- 
                        

#### 

[LibreOffice 26.8 is out – local first, and with no AI
                                    It looks a bit clunky, but it does the job – and on your own computer](https://www.theregister.com/applications/2026/08/28/libreoffice-268-is-out-local-first-and-with-no-ai/5293301)
                    
                    
- 
                        

#### 

[Keepers of Noble Numbats to be offered a Resolute Racoon: Ubuntu 26.04.1 is coming
                                    GRUB's up for furry new update](https://www.theregister.com/os-platforms/2026/08/28/keepers-of-noble-numbats-to-be-offered-a-resolute-racoon-ubuntu-26041-is-coming/5293277)
                    
                    
- 
                        

#### 

[AROS, the FOSS recreation of AmigaOS, comes to Raspberry Pi
                                    Plus: new official Amiga-branded hardware is coming](https://www.theregister.com/os-platforms/2026/08/27/aros-the-foss-recreation-of-amigaos-comes-to-raspberry-pi/5292523)
                    
                    
- 
                        

#### 

[Emperor Penguin Linus Torvalds banishes a bug – with a bot
                                    The lad himself finds and fixes a tricky one… or does he?](https://www.theregister.com/os-platforms/2026/08/24/linus-torvalds-banishes-linux-bug-with-a-bot/5291784)
                    
                    
- 
                        

#### 

[FOSS smashed one Microsoft monopoly. After 20 years of failure, it's time to smash another
                                    Word up](https://www.theregister.com/columnists/2026/07/27/foss-smashed-one-microsoft-monopoly-after-20-years-of-failure-its-time-to-smash-another/5278040)
                    
            
    

    

                
            
            
            
        

            
                
                    
                        

                        
                        ✕
