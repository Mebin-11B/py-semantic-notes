---
title: "For first time, a cell built from scratch grows and divides"
url: https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/
clipped: 2026-08-31 12:22:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [For first time, a cell built from scratch grows and divides](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/)

## Digest Summary
Researchers led by Kate Adamala reported the first synthetic cell built from non‑living components that can grow and divide. The team combined DNA replication systems, feeder liposomes, and membrane‑bound proteins that crowd and bend the membrane to induce division, bypassing a cytoskeleton. The resulting “spudcells” have genomes far smaller than bacterial chromosomes and require external feeding of raw materials; they cannot yet produce ribosomes or sustain autonomous replication. Experiments introducing engineered DNA variations showed larger cells produced more daughters, indicating a selectable trait, but true evolutionary dynamics are missing because mutations must be introduced artificially; the DNA polymerase used is too accurate. Future work will need error‑prone polymerases, internal ribosome synthesis, and possibly a cytoskeleton to improve efficiency. The authors released all data and methods via a new nonprofit, Biotic, aiming to enable broader synthetic‑biology research and eventual applications such as bio‑derived plastics, fertilizers, or drugs, while also providing a platform to study the origins of life.

---

## Full Article

[Home](https://www.quantamagazine.org/)
        
        
        
        
                        
                For the First Time, a Cell Built From Scratch Grows and Divides            
        
                    
                
    

                
                
    
            
    
    
        
        
                            
                    Read Later
                
                        
    

                
                
                    
                                                

###### Share

                    
                    
                        
    
                
                
                Copied!
                
            
    
        
                    
                
                
                
                
    
    
            

                    
                
                            
            
                
                    
- 
                    
                        
                            
                            
                            
                        
                    
                    
                
            
                    
                    
                
- 
                    
    [Comments](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/#comments)

                
                
- 
                    
    
                    
                Read Later
            
            
    
    
        
        
                            
                    Read Later
                
                        
    

                
            
                    
            
        
    

            
                
        
        
            
            
                
        
        [synthetic biology](https://www.quantamagazine.org/tag/synthetic-biology/)    
    

# For the First Time, a Cell Built From Scratch Grows and Divides

    
        
    
        By 
        [Yasemin Saplakoglu](https://www.quantamagazine.org/authors/yasemin-saplakoglu/)
            

July 1, 2026    
    
        
            Scientists built a synthetic cell that combines more lifelike properties than ever before — proof of concept that it’s possible to bring nonliving materials to life, or something close to it, in the lab.        
        
            
                
    

                
                
    
            
    
    
        
        
                            
                    Read Later
                
                        
    

            
        
    
    
            
        
    
    
    
        
                            
                                    
                        
        
    
        
            
    

Ada Zejun Shen/Quanta Magazine

        
    

    

            

## Introduction

            
            
                
                    

    
                
            
    

For the very first time, biologists packed nonliving components into a cell-like membrane, piece by piece, and witnessed the bag of molecules start to behave like life. The lab-made synthetic cell grew, replicated its DNA, and divided, demonstrating the basic functions of a cell cycle.

It’s “an impressive step,” said [Jack Szostak](https://chemistry.uchicago.edu/jack-w-szostak), who studies the origins of life at the University of Chicago and was not involved in the research. “I don’t know of any other effort to put together an artificial cell from biological components that has progressed so far.”

The cell is not alive by any definition. It can’t survive without constant deliveries of food and ribosomes, the machinery needed to make proteins. It has no defenses or a good waste removal system. But it’s the strongest demonstration yet that it is possible to generate life from nonlife, a goal that synthetic biologists have been chasing for decades.

“It’s a big step forward to this holy grail of making a living thing out of dead components,” said [Sijbren Otto](https://otto-lab.com/home/sijbren-otto/), a systems chemist at the Stratingh Institute for Chemistry in the Netherlands who was not involved in the work. “It’s not completely there yet, but it’s definitely getting quite close.”

Since these cells were pieced together from scratch, and all the molecular parts were crafted in the lab, scientists can tinker with the system and switch components in and out. “I have a blueprint, I have a full chemical ingredient list of every component,” said [Kate Adamala](https://cbs.umn.edu/directory/kate-adamala), a synthetic biologist at the University of Minnesota who led the new study, which is not yet peer-reviewed; [the paper](https://doi.org/10.64898/2026.07.01.735724) was posted on the scientific preprint site biorxiv.org on July 2. With such flexibility, this kind of synthetic cell could eventually be coaxed to create new materials, such as biofuels and drugs, and help researchers study disease.

    
            
            
                            
                    

The synthetic biologist Kate Adamala coaxed a cellular soup of nonliving biomolecules enclosed in a membrane to act somewhat like a living thing, even growing and dividing into daughter cells.
                
            
    

Courtesy of Kate Adamala

        
    

It could also give scientists insight into some of their deepest existential questions: What is the minimum needed to sustain life? How could life start? What happens if we alter the biology that composes life on Earth today?

Or, as Adamala put it: “What else can biology do?”

## Building Life

Some 4 billion years ago, a bunch of nonliving molecules got together to form the first protocells. They fed, grew, and divided. Then, over time, evolutionary processes emerged that let these cells change and diversify into many different types, decorating a barren world with all manner of strange beings. A purely chemical world blossomed into a biological one. Scientists cannot agree on how this shift from nonlife to life, or abiogenesis, happened, but some have turned their sights on trying it out for themselves in the lab.

For decades, researchers have taken different approaches to this challenge. Some, like the synthetic biologist [John Glass](https://www.jcvi.org/about/john-glass) at the J. Craig Venter Institute, are stripping down bacterial cells to their smallest, barest genomes to reveal a cell’s minimum requirements to stay alive. Others, like Otto, try to build cells with molecules that differ from those found in Earth biology.

Adamala also works from the ground up, but with biological molecules found in nature today. When she started her lab in 2016, she envisioned assembling a synthetic cell, a proof of concept, that could undergo a complete cycle of cell division using its own genome.

She found an instruction manual in what all known cells have in common: They grow, they duplicate their DNA, they divide, and they evolve. They transcribe their DNA into RNA and then make proteins to carry out these tasks and others that keep a cell running, such as metabolizing molecules for energy. All of this is done inside a lipid membrane, which holds all the necessary materials in one place. Adamala’s team needed to build their synthetic cell a genome and supply it with all the materials to carry out those tasks.

They developed and optimized different ingredients, most inspired by other labs, before combining them together inside liposomes — hollow sacs enclosed by a simple lipid membrane. This would serve as the cellular body.

They started with a cell’s most fundamental system: its mechanism for copying its DNA and passing it down to daughter cells. They adopted [a DNA replication system](https://doi.org/10.1038/s41467-018-03926-1), pioneered by the synthetic biologists [Hannes Mutschler](https://ccb.tu-dortmund.de/en/professorships/cb/mutschler/) and [Christophe Danelon](https://www.toulouse-biotechnology-institute.fr/en/christophe-danelon/), and tweaked it to work alongside other systems, including a commercial pack of 36 enzymes that let the cell read DNA and make proteins. Adamala’s team fiddled with their cellular brew, switching genes in and out and adjusting concentrations of various molecules, to get the crucial information-carrying and protein-making genetic systems to jibe.

Their tiny synthetic genome did not encode any metabolic genes, which would let the cell process food and energy, or many of the complex molecules a cell needs. So, in parallel, the researchers prepped some supply packs.

They filled other liposomes with sugar, lipids, and enzymes, as well as complex molecules, such as transfer RNA (tRNA) and ribosomes, which work together to translate genetic instructions into proteins. For their protocell to accept these crucial supplies, the team also modified a protein that would sit in the cell membrane and attract the lipid bubbles. When a bubble bumped into the cell, their membranes would fuse, releasing the supplies inside.

It wasn’t easy to get all these genetic systems to work together successfully. After some more tweaking and optimizing, the cell started growing and replicating its DNA.

“I was almost ready to say ‘Done’ and ‘We’re going to publish it,’” Adamala recalled. But her vision for a synthetic cell had one more step: division.

        
    

                
            
        
    
    
        
                            
                                    
                        
        
    
        
                            
                    

Fluorescent microscopy shows a synthetic cell undergoing cell division: elongating, pinching, and separating into two daughter cells.
                
            
    

Kate Adamala/Adamala Lab

        
    

    

    
    
                
            
    

This was where the field had been stuck for some time. Researchers before Adamala had figured out different ways to feed and grow synthetic cells and to replicate their DNA. But cell division is a different beast. A typical cell [reorganizes its cytoskeleton](https://www.quantamagazine.org/what-breaks-a-cells-ribs-can-make-it-stronger-20260629/) — a network of protein fibers that provide structural support — to halve its DNA and split. Synthetic biologists could not figure out how to get their cells to undergo this complex process.

So Adamala decided to ditch the cytoskeleton. One day, while tearing through the literature, she came across an [interesting mechanism in a paper](https://doi.org/10.1038/s41467-020-14696-0). By attaching protein tags to a cell membrane, the synthetic biologist [Reinhard Lipowsky](https://www.mpikg.mpg.de/lipowsky) at the Max Planck Institute of Colloids and Interfaces attracted other proteins to crowd around and physically bend the membrane, forcing the cell to divide. Following this approach, Adamala tweaked a cell-membrane protein and tested it in her protocells. After several tries, it worked.

“I wasn’t allowing myself to believe it for a while,” she said. “It was like, ‘Holy shit, did I actually make a dividing cell?’ … At some point, you’ve been checking enough that [you think], ‘OK, now it’s real.’”

This paper “beautifully demonstrates this division mechanism,” said [Job Boekhoven](https://boekhovenlab.com/jobboekhoven/), a systems chemist at the Technical University of Munich who was not involved in the study. “That has been a huge achievement.”

By putting together systems inspired by different labs — DNA replication; feeder liposomes; and swarming, division-inducing proteins — and then optimizing them to work together, Adamala’s team showed that it is possible to induce the chemical world to form a biological one in the lab.

“Combining all of these things is a staggering technical accomplishment,” Glass said. “I think it will prove to be a watershed event for the synthetic-cell field and biology in general.”

[Michael Lynch](https://search.asu.edu/profile/3175331), an evolutionary biologist at Arizona State University who was also not involved in the study, agreed. It is “a synthetic biology tour de force,” he said. However, he also cautioned against over-hyping the cell since it’s not yet self-sustaining.

Once the synthetic cells were created, her students and others started calling them Adamala cells — a moniker she hated. She insisted that they name the cells after anything else, jokingly suggesting potatoes. So her students started calling them spudcells. “I’m Polish, I’m mostly made of potatoes, so that’s fine with me,” Adamala said.

Each cell is tiny. Its genome is way smaller than bacterial genomes, and it doesn’t look like anything special. It’s “beautiful to me because I’m super excited about it,” Adamala said. “But if you look at it under the microscope, it’s like, ‘OK, it’s a blob.’”

## Evolution and Beyond

The cell could grow and divide. But could it take the next step toward life by evolving?

The researchers started fiddling with the synthetic cell’s DNA to see if they could get some cells to grow larger or divide faster — in effect, creating genetic variation in the cell population. They found that the cells that grew bigger also had more daughter cells and started to become more populous. In other words, those traits started being selected for within the population, the first step toward evolution.

What Adamala’s team demonstrated was not quite natural selection, the primary mechanism that drives evolutionary change, in which organisms that are better adapted to their environment are more likely to survive. Even if she got their cell to produce more daughter cells, she doesn’t think it would lead to evolution. That’s because Adamala’s team had to create genetic variation synthetically, instead of allowing for random mutations in DNA. The enzyme that builds new DNA strands works too well, she said; it doesn’t introduce meaningful mutations into the sequence. They will need to find an enzyme that is more error-prone — but not so error-prone that the genome’s integrity and the cell’s function is lost.

“Biology needs to change fast enough, but not too fast,” Adamala said. She said that she needs to find the sweet spot between order and chaos, referencing the biochemist and complexity theorist [Stuart Kauffman](https://www.med.upenn.edu/apps/faculty/index.php/g275/p51417), a professor emeritus at the University of Pennsylvania, who argues that biology works best at the “edge of chaos.”

A clear demonstration of an evolutionary process is “clearly something that’s missing,” Boekhoven said. “I’m sure that that’s the next big step.” Other researchers have shown [adaptive evolution in other types of synthetic cells](https://www.quantamagazine.org/even-synthetic-life-forms-with-a-tiny-genome-can-evolve-20230809/). But those cells were bacteria stripped of all but the bare minimum of genes — they weren’t built from the ground up.

The cells are also limited by the fact that they need to be fed many of their raw materials. That the cells can’t make their own ribosomes, the way natural cells do, “limits [their] potential for growth and sustained reproduction,” said Szostak, who was Adamala’s doctoral adviser. “If their system was able to generate its own ribosomes and other proteins and RNAs, it would be much closer to existing biological cells such as bacteria.”

Adamala also thinks they will need to figure out a way to add a cytoskeleton to improve their replication system. Currently, the cells waste a lot of energy and time attracting molecules to crowd around and help them divide.

All told, scientists are far from building anything remotely close to a modern living cell — but this new one is still the most lifelike yet. “The modern cell is like a Dreamliner,” Adamala said, referring to the Boeing 787 airplane. “We built a Wright flyer… the first bike frame with wings that flies 100 feet.”
        
            
        
        

Alongside sharing the new results, Adamala and other synthetic biologists announced the formation of a nonprofit called Biotic, which they will use to make their synthetic biology tools available to researchers around the world. The team is releasing their data and methods so that synthetic biologists can start building and improving on their cell. The hope is that the work can be used, decades from now, to create plastics without fossil fuels, for example, or fertilizers or drugs.

These synthetic cells could also pave the way to the past, to the origins of biology itself. Life on Earth would have started from much simpler molecules than the ones that spudcells use. Still, Adamala’s creation of a synthetic cell system from non-living materials brings researchers a step closer to exploring, in the lab, deeper questions about life’s origins and requirements, a dream she shares with others.

“If you want to understand what life is,” Boekhoven said, “you need to first build life.”

    
            
    

Update: July 2, 2026
The paper link was updated after the preprint was accepted by and posted on biorxiv.org.

        
    

                
                
    
        
            
                
                    
                
            
            
                
                    
                
            
        
    

            
                
        
                        
                The Quanta Newsletter            
                            

                    Get highlights of the most important news delivered to your email inbox
                
                        
                
                    
                        
                            Email
                            
                        
                        
                        
                            
                        
                        Subscribe
                    
                
                
                    
                    
                
            
        
        
    
    
        
            

## Also in Biology

            
                                    
                        
    
                    
                [A New Framework for How the Brain Compresses Our Noisy World](https://www.quantamagazine.org/a-new-framework-for-how-the-brain-compresses-our-noisy-world-20260824/)
            
                
            
                [neuroscience](https://www.quantamagazine.org/tag/neuroscience/)            
            

### 

[A New Framework for How the Brain Compresses Our Noisy World](https://www.quantamagazine.org/a-new-framework-for-how-the-brain-compresses-our-noisy-world-20260824/)
            
    
    
        By 
        [Conor Feehly](https://www.quantamagazine.org/authors/conorfeehly/)
            
        
                
            August 24, 2026
            
        
            
        
    

        
        
    
            
    
    
        
        
                            
                    Read Later
                
                        
    

    

            
                            
        
            
                    
                                    
                        
    
                    
                [Why Aging May Be a Program, Not a Breakdown](https://www.quantamagazine.org/why-aging-may-be-a-program-not-a-breakdown-20260814/)
            
                
            
                [Q&A](https://www.quantamagazine.org/tag/qa/)            
            

### 

[Why Aging May Be a Program, Not a Breakdown](https://www.quantamagazine.org/why-aging-may-be-a-program-not-a-breakdown-20260814/)
            
    
    
        By 
        [Ingrid Wickelgren](https://www.quantamagazine.org/authors/ingrid-wickelgren/)
            
        
                
            August 14, 2026
            
        
            
        
    

        
        
    
            
    
    
        
        
                            
                    Read Later
                
                        
    

    

            
                            
        
            
                    
                                    
                        
    
                    
                [How Does Touch Lead To Pain Or Pleasure?](https://www.quantamagazine.org/how-does-touch-lead-to-pain-or-pleasure-20260806/)
            
                
            
                [The Joy of Why](https://www.quantamagazine.org/tag/the-joy-of-why/)            
            

### 

[How Does Touch Lead To Pain Or Pleasure?](https://www.quantamagazine.org/how-does-touch-lead-to-pain-or-pleasure-20260806/)
            
    
    
        By 
        [Janna Levin](https://www.quantamagazine.org/authors/jannalevin/)
                     +1 author
            
    
        
        
                            
                    [Steven Strogatz](https://www.quantamagazine.org/authors/stevenstrogatz/)
                
                        
    

            
        
                
            August 6, 2026
            
        
            
        
    

        
        
    
            
    
    
        
        
                            
                    Read Later
                
                        
    

    

            
                            
        
            
                    
                            
        
    

    

## Comment on this article

    
        
            
                
                    

Quanta Magazine moderates comments to facilitate an informed, substantive, civil conversation. Abusive, profane, self-promotional, misleading, incoherent or off-topic comments will be rejected. Moderators are staffed during regular business hours (New York time) and can only accept comments written in English. 
                
                
                    
                    
                
            
        
    
    
        Show comments
    

    
        
            
    
            

        
        
        
            
                

## Next article

                What Breaks a Cell’s Ribs Can Make It Stronger
            
        
        
    
        
    
    
    

    
        
        
        
            
                
                                    
            
            
    Log in to Quanta
    
                
    
    
        
            

## Use your social network

            
                [Connect with Facebook](https://www.quantamagazine.org/mechanix?loginSocial=facebook)
            
            
                [Connect with Google](https://www.quantamagazine.org/mechanix?loginSocial=google)
            
        
        
            or
        
        
            
                
                    
                    email
                
                
                    
                    password
                
                
                    
                    
                    Remember me
                
                
                    
                    

                        Forgot your password ?
                                            
                
            
        
    
    
        Don't have an account yet?
        Sign up
    

        
    

    
        
        
        
            
                
                                    
            
            
    
        Forgot your password?
        

We’ll email you instructions to reset your password
    
    
        
    
    
    
        
            
                
                email
            
            
        
    

        
    

    
        
        
        
            
                
                                    
            
            
    
        Change your password
        

Enter your new password
    
    
    
        
    
    
        
            
                
                Password
            
            
                
                Retype new password
            
            
        
    

        
    

    
        
        
        
            
                
                                    
            
            
    
        Sign Up
    
    
                        
    

    
        
                            
                    
                    First Name
                
                            
                    
                    Last Name
                
                            
                    
                    Email
                
                            
                    
                    Password
                
                            
                    
                    Retype Password
                
            
            
                
            
        
        
            Creating an account means you accept Quanta Magazine's
            
            [Terms & Conditions](https://www.quantamagazine.org/terms-conditions) and [Privacy Policy](https://www.quantamagazine.org/privacy-policy)
