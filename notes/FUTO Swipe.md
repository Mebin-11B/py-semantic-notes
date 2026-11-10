---
title: "FUTO Swipe"
url: https://swipe.futo.tech/
clipped: 2026-08-31 12:26:33
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [FUTO Swipe](https://swipe.futo.tech/)

## Full Article

Fast, accurate swipe typing system. Use it today in FUTO Keyboard, our fully offline Android keyboard app. Or download the models and build with it.
            

            
                
            
            

This is a serverside demo to keep this webpage small. In production, it runs on-device, with much lower latency.

            
                [Get FUTO Keyboard v0.1.29+](https://keyboard.futo.org/)
                [or read more details below](https://swipe.futo.tech/#foreword)
                
            
        
    

    
        

            For a long time, good mobile swipe typing was locked behind privacy-invasive keyboard apps or unlicensed private libraries.
            
            FUTO Swipe is our family of open models and algorithms that aims to solve this problem. We developed this primarily for FUTO Keyboard, but we also welcome the broader community to make use of the FUTO Swipe models.
            The models are released under a permissive license with attribution, and the inference library is open-source.
        
    

  
  
    
    
      

      
        

            In August 2024, we launched a dataset collection effort on the swipe.futo.org domain to collect QWERTY English swipes.
            Users would voluntarily visit the webpage on their mobile phone and be given instructions and information about the dataset. After consenting,
            they would be given sentences, primarily from Wikipedia, and would be asked to swipe them word-by-word.
        
        

            In the end, this produced over 1 million swipes. We filtered out a small set of low-quality swipes. In March 2025, we released a dataset of 1 million swipes under the MIT license, and it is available today on HuggingFace.
        
        

            We made heavy use of this data to train our models and to evaluate different swipe typing systems.
        
      

    
  

  
  
    
      

      
        
        

Our architecture includes three model types.

        

The Encoder model is a universal layout-agnostic and language-agnostic, and is used for making swipe typing predictions in the general case. However, it does not offer cutting-edge accuracy.

        

The ContextLM model is a very small language model that is trained for a single language. It's used to improve the quality of predictions by eliminating nonsensical words given the preceding words in the sentence. It only requires text data for training.

        

Finally, the decoder is a language-specific and layout-specific model that learns layout's peculiarities and achieves leading accuracy. As it requires swipe typing data for a specific layout and language for training, we only have a QWERTY English decoder for now.

        

With all 3 models and with a beam width of 300, we achieve a top-4 fail rate of only ~4% on our test set. Ignoring out-of-vocabulary cases, the error rate is below 1%.
      

    
  

  
  
    
        
        
        

Note: These numbers heavily depend on the benchmark, so real-world use may vary, but we believe we match big tech's keyboards.
    
  

  
  
    
      

      
    

The encoder model is just 635,140 parameters, and the decoder is 304,155 extra. The biggest one is the ContextLM at 1.5 million, but 1.1 million of that is just embeddings. This brings us to 1,364,271 active parameters, or 2,494,767 total parameters.

This means the footprint of the models are very small, and the model can run on low-end devices in milliseconds. In addition, the environmental costs involved in training the models were also very low, because we never needed more than 1 workstation GPU!
      

    
  

  
  
    
    
      

The models themselves are only half of the story when going from a swipe to word predictions. The model predictions are not very useful on their own and it's necessary to perform a dictionary-constrained beam search to score a set of words and find the most likely candidates.

For this, we release swipe-library, a library written in C++ that handles the entire inference, decoding, and beam search part so you can easily go from swipe paths to word predictions.
      

    
  

  
  
    
    
        
            
            

Swipe typing in VR...
            

[resrec link for demo](resrec:///U-1ndAnBjY9wm/R-DD05FBF5B7486A4F8DFCA48EE94527DB314B19FCA9FF4A8B676B0EF60B42AF93)
        
        
            
            

...or on a laptop trackpad
        
    

  

    
        
            

## Want to build with FUTO Swipe?

            

                The FUTO Swipe models are available under the FUTO Model License, and the inference library is under GPL. Read more about our architecture and method in the technical report.
            
            
            
                [Technical Report](https://arxiv.org/abs/2606.25247)
            

            
                [🤗
                    
                    
                        HuggingFace models](https://huggingface.co/futo-org/futo-swipe)
                [Library](https://gitlab.futo.org/keyboard/swipe-library)
