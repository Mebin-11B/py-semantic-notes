---
title: "The circuit that lets your brain think and see"
url: https://www.engineering.columbia.edu/about/news/circuit-lets-your-brain-think-and-see
clipped: 2026-08-31 12:22:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The circuit that lets your brain think and see](https://www.engineering.columbia.edu/about/news/circuit-lets-your-brain-think-and-see)

## Digest Summary
None

---

## Full Article

The artwork depicts patterns of activity within a biologically constrained neural network embedded in a stylized cortex. The colored trajectories show how neural activity evolves differently depending on what information is currently relevant.
                        
                                                                Image credit: Nuttida Rungratsameetaweemana
                                        
                
                                                                                
                 
                
                    
                                            
                        The artwork depicts patterns of activity within a biologically constrained neural network embedded in a stylized cortex. The colored trajectories show how neural activity evolves differently depending on what information is currently relevant.
                        
                                                                Image credit: Nuttida Rungratsameetaweemana
                                        
                
                

                                            
                
                    
                        
                            

                                                                    Research
                                                            
                            

# 
                                The Circuit that Lets Your Brain Think and See
                            

                                                            

The circuitry underlying the brain’s remarkable efficiency is coming into sharper focus.
                                                        
                                
                                    
                                    July 02, 2026
                                
                                                                    
                                        
                                        Grant Currin
                                    
                                                            
                        
                    
                
            
        

        
        
            

                

            
                
                    

    
                          

[Nuttida Rungratsameetaweemana](https://www.engineering.columbia.edu/faculty-staff/directory/nuttida-rungratsameetaweemana) is challenging a story neuroscience has told for decades. According to the conventional account, our eyes collect raw information and relay it through a series of nerves and waystations that lead deep into the brain, eventually reaching the cortex. There, the thinking begins as information is processed and put to use for higher tasks such as reasoning, judgment, and decision-making.

Her group's work is complicating that account. Last year, the team [published](https://www.engineering.columbia.edu/about/news/how-thoughts-influence-what-eyes-see) fMRI scans showing unexpected levels of activity in the earliest visual areas of the cortex, the regions that first receive visual signals. Rather than passively relaying what the eyes take in, those early areas seemed to process the same information differently depending on what the research participant was doing. When asked to sort shapes by one set of rules, a participant's early visual system behaved one way. When asked to apply a different set of rules to the same shape, it behaved differently.

In a new paper published today in [PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003831), Rungratsameetaweemana and her team at Columbia Engineering show how the brain might pull this off. They built a simple neural network that follows many of the rules that govern real brains. Like the brain, their model contained one class of neurons that drive other neurons to fire and another class that suppress firing.

The team had the model perform a task similar to what the human participants had done while in an fMRI machine. When the researchers looked inside the model to see how the neural network had solved the problem, they found that it relied on one arrangement of digital neurons. Inhibitory neurons that suppress other inhibitory neurons seem to pass key information from the “thinking” part of the system to the “sensing” component of the system. 

To test whether that wiring was essential, they weakened those connections in the model, and its ability to switch between tasks collapsed. Weakening other types of connections left performance largely intact. The pattern held up against the living brain as well. In recordings from the visual cortex of mice, silencing the inhibitory cells that anchor this circuit reduced the cortex's ability to track the task context, just as the model predicted.

We caught up with Rungratsameetaweemana, Maa-Liao Assistant Professor of [Biomedical Engineering](https://www.engineering.columbia.edu/academics/departments/biomedical-engineering-department), to learn more about the research. 

  
  
    
        Image
                                      

                            

Nuttida Rungratsameetaweemana (far right) with the study's coauthors, Robert Kim and Tomas Aquino (center). Credit: Rungratsameetaweemana lab

This builds on last year's fMRI study. Why turn to AI models next?

A brain scan gives you a picture of the whole brain, but it’s coarse — you can't see what individual cells are doing, or what's happening at the level of circuits. Seeing which regions light up and patterns of activity gave us a reason to go deeper. To get at the mechanism, we needed something we could take apart and change, so we turned to neural models. We build these from scratch, so it’s possible to see exactly what the network is doing to solve the task.

Why keep the models so simple?

If a model has abilities the brain doesn't have, then anything we find inside it won't tell us much about real brains. So we did the opposite and built something that only includes features we know to be true about biology. A lot of that builds on earlier work from Tomas Gallo Aquino and Robert Kim, the paper's co-first authors, among other studies. We know there are excitatory and inhibitory neurons, so we built those in. We know the brain is organized in a hierarchy, so in the second part of the paper we gave the network two regions: a sensory module that receives input directly, and a higher-level module downstream. Then we can ask how the network uses those ingredients to do the task.

Why do these inhibitory-on-inhibitory connections matter so much?

They give the system very fine control over how information gets represented. These inhibitory neurons turn out to be really important for keeping everything well-controlled, for making sure the right thing is represented in the right way. There are four kinds of connections you can have between these cells, and the one that matters for this kind of flexible processing is inhibition acting on inhibition. We know it's important, because the model fails when we take it away. We don't yet know why it has to be this particular wiring. That question is an important topic for research teams across the world.

How did you get started with this line of research?

Back in 2015, I began working with patients who are missing the hippocampus, the region that lets us form and hold onto memories. If the brain were truly modular, losing that middle piece should leave you unable to do a great many things. But it doesn't. These patients can still do all sorts of tasks. That was the first real evidence, to me, that the early regions of the brain are doing more than just relaying sensory information. And it points to something useful: if information is stored redundantly, you can lose a part and still get by. I think that's how the brain actually works.

What could it mean for AI?

Compare the brain to something like ChatGPT or a large language model. We can do far more, across far more situations, on a tiny fraction of the energy — and without being trained on the whole internet. The brain got there through evolution, through the redundancy built into its wiring. Our models are recurrent neural networks, which are quite different from the transformers behind today's large language models. The goal is to work out these principles one by one and use them to make AI leaner and more adaptive. This inhibition-on-inhibition motif is one of them.

What's next?

We've gone back to humans. We're working closely with clinical collaborators who monitor epilepsy patients with electrodes placed deep inside the brain, letting us record neural activity directly while those patients perform cognitive tasks. These fine-grained measurements will give us data to test our hypotheses against real neural activity.

## About the Study

Title: [Disinhibitory signaling enables flexible coding of top-down information in cortical networks](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003831)

Authors: Tomas Gallo Aquino, Robert Kim, Nuttida Rungratsameetaweemana

Funding/Acknowledgements: We thank Jorge Aldana and the Computational Neurobiology Laboratory at the Salk Institute for assistance with computing resources. We thank Lisa Kirchberger of the Netherlands Institute for Neuroscience for the support in providing access to mouse data for this manuscript. We are also grateful to Mackenzie Mathis for her invaluable feedback on our work. This work was funded by the ARL Human Guided Intelligent Systems grant (W911NF-23-2-0067) and the Strengthening Teamwork for Robust Operations in Novel Groups (STRONG) grant (W911NF-22-2-0148).
