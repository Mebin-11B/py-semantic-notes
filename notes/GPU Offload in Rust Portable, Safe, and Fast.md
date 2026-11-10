---
title: "GPU Offload in Rust: Portable, Safe, and Fast"
url: https://arxiv.org/abs/2608.13759
clipped: 2026-08-31 12:22:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [GPU Offload in Rust: Portable, Safe, and Fast](https://arxiv.org/abs/2608.13759)

## Digest Summary
GPU Offload in Rust introduces a zero‑overhead, multi‑vendor compilation framework integrated directly into the Rust compiler (rustc) and LLVM back‑ends. By exploiting Rust’s ownership model, strict aliasing (noalias), and rich type system, the framework manages data transfers and generates LLVM IR for GPU kernels without resorting to vendor‑locked DSLs or unsafe raw pointers. It addresses cross‑vendor ABI mismatches between host and device targets through a two‑pass compilation pipeline that supports both manually specified and compiler‑generated memory movements. Evaluation on the RAJAPerf benchmark suite shows that the rustc‑based approach produces kernel performance comparable to hand‑optimized CUDA and HIP C++ implementations, while maintaining Rust’s compile‑time memory safety guarantees. The work demonstrates that safe, portable, and high‑performance GPU offloading can be achieved within the existing Rust toolchain.

---

## Full Article

[Skip to main content](https://arxiv.org/abs/2608.13759#content)
  
  
  

  
    
      Search arXiv
      
      
      
    
    
      Press Enter to search · [Advanced search](https://arxiv.org/search/advanced)
    
  

    
      

  
    
      

# Computer Science > Programming Languages

    

    
      arXiv:2608.13759 (cs)
    

  
    
  [Submitted on 13 Aug 2026]
    

# Title:GPU Offload in Rust: Portable, Safe, and Fast

    Authors:[Manuel S. Drehwald](https://arxiv.org/search/cs?searchtype=author&query=Drehwald,+M+S), [Marcelo Domínguez](https://arxiv.org/search/cs?searchtype=author&query=Dom%C3%ADnguez,+M), [Kevin Sala](https://arxiv.org/search/cs?searchtype=author&query=Sala,+K), [Alán Aspuru-Guzik](https://arxiv.org/search/cs?searchtype=author&query=Aspuru-Guzik,+A), [Johannes Doerfert](https://arxiv.org/search/cs?searchtype=author&query=Doerfert,+J)            View a PDF of the paper titled GPU Offload in Rust: Portable, Safe, and Fast, by Manuel S. Drehwald and 4 other authors
    [View PDF](https://arxiv.org/pdf/2608.13759)
    [HTML (experimental)](https://arxiv.org/html/2608.13759v1)

    
            Abstract:High-performance GPU programming has traditionally forced a compromise between execution efficiency and memory safety. While Rust guarantees compile-time memory safety for host CPUs via its strict ownership model, applying these constraints to massively parallel GPU execution environments has previously mandated either vendor-locked Domain-Specific Languages (DSLs) or escaping to explicit unsafe raw pointers. This paper presents a zero-overhead, multi-vendor GPU compilation framework built natively into the Rust compiler (rustc) and LLVM backends.
We leverage Rust's rich type system, ownership system, and strict aliasing guarantees (noalias) to efficiently manage and optimize data transfers through LLVM's Offload infrastructure. We expose the technical challenges of cross-vendor ABI lowering mismatches between Host and Device targets and introduce a two-pass compilation pipeline capable of safely handling both manual and compiler-generated memory movements. Evaluating our framework on RAJAPerf demonstrates that our rustc-based solution can generate competitive LLVM IR for GPU kernels, achieving a solid kernel performance against native, hand-optimized CUDA and HIP C++ baselines.
    

    
    
              
          Comments:
          13 pages, 5 figures
        

          Subjects:
          
            Programming Languages (cs.PL)
        
          Cite as:
          [arXiv:2608.13759](https://arxiv.org/abs/2608.13759) [cs.PL]
        
        
           
          (or 
              [arXiv:2608.13759v1](https://arxiv.org/abs/2608.13759v1) [cs.PL] for this version)
          
        
        
           
                        [https://doi.org/10.48550/arXiv.2608.13759](https://doi.org/10.48550/arXiv.2608.13759)
              
                
                Focus to learn more
              
              
              
                                  arXiv-issued DOI via DataCite
            
          
        
    
  

    
      

## Submission history

 From: Manuel Sebastian Drehwald [[view email](https://arxiv.org/show-email/78b8a686/2608.13759)]          [v1]
        Thu, 13 Aug 2026 20:37:48 UTC (88 KB)

  
  
    
      
      Full-text links:
      

## Access Paper:

      
  
View a PDF of the paper titled GPU Offload in Rust: Portable, Safe, and Fast, by Manuel S. Drehwald and 4 other authors
- [View PDF](https://arxiv.org/pdf/2608.13759)
- [HTML (experimental)](https://arxiv.org/html/2608.13759v1)
- [TeX Source](https://arxiv.org/src/2608.13759)
      [view license](http://creativecommons.org/licenses/by/4.0/)
    
        
    

### Current browse context:

  cs.PL

  

      [< prev](https://arxiv.org/prevnext?id=2608.13759&function=prev&context=cs.PL)
    
      |      
      [next >](https://arxiv.org/prevnext?id=2608.13759&function=next&context=cs.PL)
    
  
    [new](https://arxiv.org/list/cs.PL/new)
     | 
    [recent](https://arxiv.org/list/cs.PL/recent)
     | [2026-08](https://arxiv.org/list/cs.PL/2026-08)
  
    Change to browse by:
    
        [cs](https://arxiv.org/abs/2608.13759?context=cs)
    
  

    
      
        

### References & Citations

        
          
- [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13759)
- [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13759)
          
- [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13759)
        
        
      

    export BibTeX citation
    Loading...

    
        
            

## BibTeX formatted citation

            ×
        
        
            loading...
        
        
            Data provided by: 
            
        
    

  

### Bookmark

  
  
  

  
    Bibliographic Tools
    
      

# Bibliographic and Citation Tools

      
        
          
            
              
              
              Bibliographic Explorer Toggle
            
          
          
            Bibliographic Explorer ([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))
          
        
        
          
            
              
              
              Connected Papers Toggle
            
          
          
            Connected Papers ([What is Connected Papers?](https://www.connectedpapers.com/about))
          
        
          
            
              
              
              Litmaps Toggle
            
          
          
            Litmaps ([What is Litmaps?](https://www.litmaps.co/))
          
        
        
          
            
              
              
              scite.ai Toggle
            
          
          
            scite Smart Citations ([What are Smart Citations?](https://www.scite.ai/))
          
        
      
        
        
        
        
    

    
    Code, Data, Media
    
      

# Code, Data and Media Associated with this Article

      
        
          
            
              
              
              alphaXiv Toggle
            
          
          
            alphaXiv ([What is alphaXiv?](https://alphaxiv.org/))
          
        

        
          
            
              
              
              Links to Code Toggle
            
          
          
            CatalyzeX Code Finder for Papers ([What is CatalyzeX?](https://www.catalyzex.com))
          
        

        
          
            
              
              
              DagsHub Toggle
            
          
          
            DagsHub ([What is DagsHub?](https://dagshub.com/))
          
        
  
        
          
            
              
              
              GotitPub Toggle
            
          
          
            Gotit.pub ([What is GotitPub?](http://gotit.pub/faq))
          
        

        
          
            
              
              
              Huggingface Toggle
            
          
          
            Hugging Face ([What is Huggingface?](https://huggingface.co/huggingface))
          
        

        
          
            
              
              
              ScienceCast Toggle
            
          
          
            ScienceCast ([What is ScienceCast?](https://sciencecast.org/welcome))
          
        
      

      
      
      
      
      
      
    

      
      Demos
      
        

# Demos

        
          
            
              
                
                
                Replicate Toggle
              
            
            
              Replicate ([What is Replicate?](https://replicate.com/docs/arxiv/about))
            
          
          
            
              
                
                
                Spaces Toggle
              
            
            
              Hugging Face Spaces ([What is Spaces?](https://huggingface.co/docs/hub/spaces))
            
          
          
            
              
                
                
                Spaces Toggle
              
            
            
              TXYZ.AI ([What is TXYZ.AI?](https://txyz.ai))
            
          
        
        
        
        
      
      
      Related Papers
      
        

# Recommenders and Search Tools

        
          
            
              
                
                
                Link to Influence Flower
              
            
            
              Influence Flower ([What are Influence Flowers?](https://influencemap.cmlab.dev/))
            
          
          
            
              
                
                
                Core recommender toggle
              
            
            
              CORE Recommender ([What is CORE?](https://core.ac.uk/services/recommender))
            
          
        
        
          
            
- Author
            
- Venue
            
- Institution
            
- Topic
          
          
            
            
            
            
          
        
        
        
      

      
      
        About arXivLabs
      
      
        
          
            

# arXivLabs: experimental projects with community collaborators

            

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
            

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
            

Have an idea for a project that will add value for arXiv's community? [Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
          
          
            

          
        
      

    

  
    [Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2608.13759) |
    Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
