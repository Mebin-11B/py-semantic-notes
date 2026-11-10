---
title: "To study how chips work, MIT researchers built their own operating system"
url: https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610
clipped: 2026-08-31 12:22:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [To study how chips work, MIT researchers built their own operating system](https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610)

## Digest Summary
MIT’s CSAIL team built Fractal, a custom OS kernel designed to study processor microarchitecture with minimal software noise. By booting on bare metal and exposing “outer kernel threads” that can switch privilege levels within a single address space, Fractal enables precise experiments on internal structures such as branch predictors, caches, and TLBs. Using this platform on Apple’s M1 chip, researchers confirmed that CSV‑2 protections block speculative execution of indirect branches but discovered that instruction‑cache fetches still occur across privilege boundaries, exposing a side‑channel. They also provided the first evidence of “Phantom” speculative attacks on Apple Silicon and showed that conditional branch predictors lack privilege isolation on both performance and efficiency cores—contradicting earlier macOS‑based results. Fractal supports x86_64, ARM64, and RISC‑V, includes POSIX APIs, a C library, and common tools, and is intended as reusable infrastructure for microarchitectural research, analogous to QEMU or FFmpeg. The findings were disclosed to Apple, and the work was funded by NSF, the Air Force Office of Scientific Research, and DARPA‑related programs.

---

## Full Article

[Skip to content ↓](https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610#main)
    
      
    

    
  
    
      [Massachusetts Institute of Technology](http://web.mit.edu)
    
  
  
 

  
    
      Search websites, locations, and people
      
         
        
        
          
        
      
    
    
      
        
        
        
        
          See More Results
        
      
      

[Suggestions or feedback?](http://web.mit.edu/feedback)
        
  

  
    
      
        Enter keywords to search for news articles:
        
                Submit 
      
    

              
      
  
  
  

  
  
  

      
  
    
      

## Browse By

      
    
      

      

### Topics

    [View All](https://news.mit.edu/topics) →
    
    Explore:
    
          
- [Machine learning](https://news.mit.edu/topic/machine-learning)
          
- [Sustainability](https://news.mit.edu/topic/sustainability)
          
- [Startups](https://news.mit.edu/topic/startups)
          
- [Black holes](https://news.mit.edu/topic/black-holes)
          
- [Classes and programs](https://news.mit.edu/topic/classes-and-programs)
        
  

    
    
      

      

### Departments

    [View All](https://news.mit.edu/departments) →
    
    Explore:
    
          
- [Aeronautics and Astronautics](https://news.mit.edu/department/aeronautics-and-astronautics)
          
- [Brain and Cognitive Sciences](https://news.mit.edu/department/brain-and-cognitive-sciences)
          
- [Architecture](https://news.mit.edu/department/architecture)
          
- [Political Science](https://news.mit.edu/department/political-science)
          
- [Mechanical Engineering](https://news.mit.edu/department/mechanical-engineering)
        
  

    
    
      

      

### Centers, Labs, & Programs

    [View All](https://news.mit.edu/centers-labs-programs) →
    
    Explore:
    
          
- [Abdul Latif Jameel Poverty Action Lab (J-PAL)](https://news.mit.edu/clp/abdul-latif-jameel-poverty-action-lab-j-pal)
          
- [Picower Institute for Learning and Memory](https://news.mit.edu/clp/picower-institute)
          
- [Media Lab](https://news.mit.edu/clp/media-lab)
          
- [Lincoln Laboratory](https://news.mit.edu/clp/lincoln-laboratory)
        
  

    
    
      

      

### Schools

    
    
          
- [School of Architecture + Planning](https://news.mit.edu/school/architecture-and-planning)
          
- [School of Engineering](https://news.mit.edu/school/engineering)
          
- [School of Humanities, Arts, and Social Sciences](https://news.mit.edu/school/humanities-arts-and-social-sciences)
          
- [Sloan School of Management](https://news.mit.edu/school/management)
          
- [School of Science](https://news.mit.edu/school/science)
          
- [MIT Schwarzman College of Computing](https://news.mit.edu/school/mit-schwarzman-college-computing)
        
  

      
    
      [View all news coverage of MIT in the media](https://news.mit.edu/in-the-media) →
       
    
      [Listen to audio content from MIT News](https://news.mit.edu/podcasts) →
                 
    
      [Subscribe to MIT newsletter](http://web.mit.edu/subscribe/) →
         
    
      [Close](https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610#)
                 
  

    

  
  

  
  

      

    
    
              
  
    
        
            

#### Breadcrumb

  
      
- 
              [MIT News](https://news.mit.edu/)
          
      
- 
              To study how chips really work, MIT researchers built their own operating system
          
    

      

  
            
  
    
        
          
  

# To study how chips really work, MIT researchers built their own operating system 

      

  
    
        
          

  
    

  
  
    

      A new kernel called Fractal gives researchers a cleaner view of what’s happening inside a processor, and has already surfaced previously unknown behavior in Apple’s M1. 
  

    
  

      Rachel Gordon
  |
  MIT CSAIL
  
  

    

                    Publication Date:
        
              June 10, 2026
      
  

  [Press Inquiries](https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610#press-inquiries)
    
    

            

###         Press Contact:
      

  
              
  
    
  

    
            Rachel        

            Gordon        

  

    
            Email:
              [rachelg@csail.mit.edu](mailto:rachelg@csail.mit.edu)      
  

    
            Phone:
              617-258-0675      
  

    
            MIT Computer Science and Artificial Intelligence Laboratory        

  

      
    
      [Close](https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610#)
        
  

  
        
          
                  
  
    
      
                  

              

        

              

      
        
          
            

                    Caption:
        
              Fractal relies on a new construct: the outer kernel thread, which sits inside a user process’s memory but executes with kernel privileges. “If you’ve got a hand magnifying glass, you can see a little bit. But if you had an electron microscope, now we’re really talking. That’s what Fractal is. The electron microscope of operating systems,” says lead author and MIT PhD student Joseph Ravichandran.      
          
          
            

                    Credits:
        
              Image: Gabriel Maragaño      
                    
        
      
            

              
      
        

          
Previous image
          Next image
        
            
    
  

  
    
    

    
            
          

            

A new kernel, or core program within an operating system, gives researchers a cleaner view of what’s happening inside a processor. Called [Fractal](https://people.csail.mit.edu/mengjia/data/2026.SP.fractal.pdf) and developed at MIT, the kernel has already surfaced previously unknown behavior in Apple’s M1.

When security researchers want to understand what a modern processor is really doing with the kind of detail that determines whether attacks like Spectre and Meltdown are possible, they usually run their experiments on top of an operating system that was never built for the job. They open up macOS or Linux, patch the kernel by hand, and hope the modifications hold. The approach is unstable, hard to reproduce, and on Apple’s platforms, slated for deprecation.

A team at MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) decided to build something different. Fractal, an operating system kernel written from the ground up, treats the hardware itself as the object of study. Its first major use, a deep look at branch predictors — a CPU’s way of guessing what code to run next, before it knows for certain, so it doesn’t have to waste time waiting to find out — inside Apple’s M1 processor, has already turned up findings that prior work missed, including the first evidence that a class of speculative attack known as “Phantom” affects Apple Silicon.

“We’re using hardware in ways it wasn’t designed for,” says Joseph Ravichandran, the MIT PhD student in electrical engineering and computer science (EECS) who led the project. “It’s not even obvious that this is a possible thing you could do with the hardware. But we found a way to pull all these different primitives off. It’s like a microscope. If you’ve got a hand magnifying glass, you can see a little bit. But if you had an electron microscope, now we’re really talking. That’s what Fractal is. The electron microscope of operating systems.”

A clean room for chip research

The core problem Fractal solves is one that researchers have worked around for years. Modern processors keep state in many internal structures: branch predictors, caches, translation lookaside buffers, and more. To study how those structures behave across the boundary between user code and kernel code, two domains the chip is supposed to keep isolated, researchers need to run nearly identical experiments on each side of that boundary. On a general-purpose operating system, that is very difficult. The system itself manages privilege levels, address spaces, and scheduling, and it injects its own activity into every measurement.

Fractal inverts the model. It boots directly on bare metal, with no other software running, and exposes primitives that let a single experiment switch privilege levels at runtime while executing the same instructions in the same address space. The team calls the underlying technique multi-privilege concurrency, and it relies on a new construct they introduced: the outer kernel thread, which sits inside a user process’s memory but executes with kernel privileges.

The result is an experimental setup with almost no background noise. Where measurements taken under macOS or Linux are blurred by interrupts, scheduler activity, and address-space management, Fractal produces flat baselines and clean signals.

What Fractal found on the M1

Apple’s M1 implements an ARM specification called CSV2, which is supposed to prevent code running in one privilege level from steering speculation in another. Using Fractal, the MIT team confirmed that the protection works for the execute stage of indirect branch prediction: a user-mode program cannot make the kernel speculatively execute a chosen target through the indirect branch predictor.

But the team also found something the chip’s designers may not have intended. The CPU still fetches the target into the instruction cache before the protection kicks in. That fetch is observable through a side channel, which means user code can still influence what the kernel pulls into its caches across the privilege boundary. The same pattern appeared between processes assigned different address space identifiers.

The team also produced the first evidence that Apple Silicon exhibits Phantom speculation, a class of misprediction previously demonstrated only on AMD and Intel processors. In Phantom, ordinary instructions, including a no-op, can be misinterpreted by the CPU as branches, triggering speculative behavior the program never asked for. On the M1, Fractal showed that Phantom fetches succeed across both privilege levels and address spaces, though the execute phase remains blocked.

A separate Fractal experiment overturned a finding from earlier work on the M1’s conditional branch predictor, which had reported that cross-privilege training worked on Apple’s performance cores, but not its efficiency cores. The Fractal team showed that the conditional branch predictor has no privilege isolation at all, on either core type, and that the earlier result was likely an artifact of macOS quietly migrating threads between cores during system calls.

“For us, it is a true independent variable,” Ravichandran says. “You change the privilege level, nothing else changes. The only thing that could explain whether the attack succeeds or not is the privilege level.”

A tool, not a one-off

Fractal supports x86_64, ARM64, and RISC-V, and consists of more than 31,000 lines of code. The team designed it as infrastructure rather than as a single experiment, with familiar POSIX system calls, a C library, and ports of standard tools like vim, GCC, and the dash shell, so that researchers can move existing experiment code over with minimal friction.

The MIT team disclosed its M1 findings to Apple’s product security team. In an unusual reversal, Apple’s engineers also examined Fractal. 

The longer-term ambition is bigger than any single result. Ravichandran wants Fractal to become to microarchitecture research what tools like QEMU and FFmpeg are to their fields: shared infrastructure that the whole community builds on. 

“My hope is that our results as a community get significantly more reliable, significantly more accurate,” says Ravichadran. “With this reduced noise, this clarity, and this guarantee that you’re running on the right core, on the right system.”

“Fractal is a strong architecture contribution because it turns an often ad hoc microarchitectural reverse-engineering workflow into reusable research infrastructure,” says University of Southern California assistant professor Mengyuan Li, who wasn’t involved in the paper. “By reducing software noise and giving researchers tighter control across privilege boundaries, it makes difficult hardware experiments much easier to interpret.”

Ravichandran worked with Mengjia Yan, an MIT associate professor of EECS and CSAIL principal investigator, on the paper. Their work was supported, in part, by the National Science Foundation, the U.S. Air Force Office of Scientific Research, and ACE, which is part of a program sponsored by the U.S. Defense Advanced Research Projects Agency. They presented their work at the IEEE Symposium on Security and Privacy in San Francisco, California.        

      
        
  

  

    
  
    
        
          
  
    

### Share this news article on:

    
      
- 
        [X](https://twitter.com/share?url=https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610)
      
      
- 
        [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610)
      
      
- 
        [LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610)
      
      
- 
        [Reddit](http://www.reddit.com/submit?url=https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610&title=To%20study%20how%20chips%20really%20work%2C%20MIT%20researchers%20built%20their%20own%20operating%20system)
      
      
- 
        [Print](https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610#)
      
    
  

      

            
      
  
  
  

      
  
  
  

      

[Paper: "Fractal: An Operating System Designed for Microarchitecture Reverse Engineering"](https://people.csail.mit.edu/mengjia/data/2026.SP.fractal.pdf)

    

  
  

  
  

    
          

          

                          
        
  
  
  

      
  
  
  

  
    

### IEEE Spectrum

Writing for IEEE Spectrum, reporter Matthew S. Smith highlights Fractal, a new operating system hand-coded by CSAIL researchers to provide a clear view of security vulnerabilities. “We paved the way with techniques such as custom kernel patches and kernel extensions,” says graduate student Joseph Ravichandran. “The dream was always to have a completely custom operating system which would make these hacks unnecessary.”
 [Full story via IEEE Spectrum](https://spectrum.ieee.org/fractal-os-operating-system-security) →

  

    
Previous item
    Next item
    

    

  
  

  
  

      
           

                
      

## Related Links

      
  
  
  

  
  
  

      
- [Fractal project website](https://fractal-os.com/)
- [Joseph Ravichandran](https://jprx.io/)
- [Mengjia Yan](https://people.csail.mit.edu/mengjia/)
- [Computer Science and Artificial Intelligence Laboratory (CSAIL)](https://www.csail.mit.edu/)
- [Department of Electrical Engineering and Computer Science (EECS)](https://www.eecs.mit.edu/)
- [School of Engineering](https://engineering.mit.edu/)
- [MIT Schwarzman College of Computing](https://computing.mit.edu/)

    

  
  

  
  

    
      
    
  

 

    

## Related Topics

    
- [Research](https://news.mit.edu/topic/research)
    
- [Computer chips](https://news.mit.edu/topic/computer-chips)
    
- [Cybersecurity](https://news.mit.edu/topic/cyber-security)
    
- [Computing](https://news.mit.edu/topic/computing)
    
- [Computer science and technology](https://news.mit.edu/topic/computers)
    
- [Electrical engineering and computer science (EECS)](https://news.mit.edu/topic/electrical-engineering-computer-science-eecs)
    
- [Computer Science and Artificial Intelligence Laboratory (CSAIL)](https://news.mit.edu/topic/computer-science-and-artificial-intelligence-laboratory-csail)
    
- [MIT Schwarzman College of Computing](https://news.mit.edu/topic/mit-schwarzman-college-computing)
    
- [National Science Foundation (NSF)](https://news.mit.edu/topic/nsf)
    
- [School of Engineering](https://news.mit.edu/topic/school-engineering)
    
- [Defense Advanced Research Projects Agency (DARPA)](https://news.mit.edu/topic/darpa)
  
  

  

## Related Articles

  

              
  
  
    

            
    
          
      
      
        
   

  

    
          

### 
        [To keep hardware safe, cut out the code’s clues](https://news.mit.edu/2025/to-keep-hardware-safe-cut-out-codes-clues-0211)
      

        

  

              
  
  
    

            
    
          
      
      
        
   

  

    
          

### 
        [Accelerating AI tasks while preserving data security](https://news.mit.edu/2023/accelerating-ai-tasks-while-preserving-data-security-1030)
      

        

  

              
  
  
    

            
    
          
      
      
        
   

  

    
          

### 
        [Thinking like a cyber-attacker to protect user data](https://news.mit.edu/index%2Ephp/2022/chip-interconnect-side-channel-attacks-0811)
      

        

  

              
  
  
    

            
    
          
      
      
        
   

  

    
          

### 
        [Researchers discover a new hardware vulnerability in the Apple M1 chip](https://news.mit.edu/2022/researchers-discover-hardware-vulnerability-apple-m1-0610)
      

        

  

      
  
  

    
Previous item
    Next item
        

  

      

  
      
  
    

      
  
    
          

## More MIT News

        
          
      
                
        
          
            
          
          
            

### 
              [How an MIT research project became a global programming language](https://news.mit.edu/2026/how-mit-research-project-became-global-programming-language-0831)
                  
                                             
            

            
              With millions of users across the world, Julia has been used to conduct cutting-edge research and to design new drugs, jet engines, heat pumps, and more.
            
            

              [Read full story](https://news.mit.edu/2026/how-mit-research-project-became-global-programming-language-0831) →
            
                    
        
      
                
        
          
            
          
          
            

### 
              [How an MIT graduate student helped a team of young scientists test their experiment at CERN](https://news.mit.edu/2026/how-mit-grad-student-helped-young-scientists-test-their-experiment-cern-0828)
                  
                                             
            

            
              Physics PhD student Manu Srivastava helped high school students in India develop a test that could contribute to one of the world’s largest neutrino experiments.
            
            

              [Read full story](https://news.mit.edu/2026/how-mit-grad-student-helped-young-scientists-test-their-experiment-cern-0828) →
            
                    
        
      
        
    
      
                
        
          
            
          
          
            

### 
              [How MIT Sandbox has turned student ideas into $8.7 billion in global impact](https://news.mit.edu/2026/how-mit-sandbox-turned-student-ideas-into-global-impact-0828)
                  
                                             
            

            
              Through a decade of non-dilutive funding, hands-on mentorship, and a safe space to fail fast, the MIT Sandbox Innovation Fund Program has helped students translate curiosity into real-world impact.
            
            

              [Read full story](https://news.mit.edu/2026/how-mit-sandbox-turned-student-ideas-into-global-impact-0828) →
            
                    
        
      
                
        
          
            
          
          
            

### 
              [Gage Coon: An Earth scientist exploring the power of microbes](https://news.mit.edu/2026/gage-coon-earth-scientist-exploring-power-microbes-0828)
                  
                                             
            

            
              The PhD student’s research on how microorganisms digest compounds in their environment could enable advances in wastewater treatment. 
            
            

              [Read full story](https://news.mit.edu/2026/gage-coon-earth-scientist-exploring-power-microbes-0828) →
            
                    
        
      
        
    
      
                
        
          
            
          
          
            

### 
              [Looking beyond natural sequences](https://news.mit.edu/2026/looking-beyond-natural-sequences-0827)
                  
                                             
            

            
              A new machine-learning framework aims to improve the success rate of computational protein design while moving away from results that reproduce sequences found in nature.
            
            

              [Read full story](https://news.mit.edu/2026/looking-beyond-natural-sequences-0827) →
            
                    
        
      
                
        
          
            
          
          
            

### 
              [New type of attack can slip past the defenses in your computer’s processor](https://news.mit.edu/2026/new-type-of-attack-can-slip-past-computer-processor-defenses-0827)
                                
                  
                                             
            

            
              MIT CSAIL researchers found a way to exploit a split-second gap in chip security — and used it to acquire a Linux system’s password file.
            
            

              [Read full story](https://news.mit.edu/2026/new-type-of-attack-can-slip-past-computer-processor-defenses-0827) →
            
                    
        
      
        
    
  
        
      
- [More news on MIT News homepage](https://news.mit.edu/) →
        
  

  

    
  
    
      [Massachusetts Institute of Technology](http://web.mit.edu)
    
    
  
  
    

[Massachusetts Institute of Technology](http://web.mit.edu)77 Massachusetts Avenue, Cambridge, MA, USA
    Recommended Links:
    
      
- [Visit](http://web.mit.edu/visitmit)
      
- [Map (opens in new window)](http://whereis.mit.edu/)
      
- [Events (opens in new window)](http://calendar.mit.edu/)
      
- [People (opens in new window)](http://web.mit.edu/people.html)
      
- [Careers (opens in new window)](http://careers.mit.edu/)
      
- [Contact](http://web.mit.edu/contact)
      
- [Privacy](http://web.mit.edu/privacy)
      
- [Accessibility](http://web.mit.edu/accessibility)    
      
- 
        
          
- [Social Media Hub](http://socialmediahub.mit.edu)
          
- [MIT on X](https://twitter.com/mit)
          
- [MIT on Facebook](https://www.facebook.com/MITnews)
          
- [MIT on YouTube](https://www.youtube.com/mit)
          
- [MIT on Instagram](https://www.instagram.com/mit)
