---
title: "GitHub - cactus-compute/cactus-hybrid: On-device models that know when they're wrong: every answer carries a confidence score for cloud handoff. · GitHub"
url: https://github.com/cactus-compute/cactus-hybrid
clipped: 2026-08-31 12:26:33
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GitHub - cactus-compute/cactus-hybrid: On-device models that know when they're wrong: every answer carries a confidence score for cloud handoff. · GitHub](https://github.com/cactus-compute/cactus-hybrid)

## Full Article

[Skip to content](https://github.com/cactus-compute/cactus-hybrid#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [cactus-compute](https://github.com/cactus-compute)    
    /
    
      [cactus-hybrid](https://github.com/cactus-compute/cactus-hybrid)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fcactus-compute%2Fcactus-hybrid)    You must be signed in to change notification settings

  

  
- 
          [Fork
    8](https://github.com/login?return_to=%2Fcactus-compute%2Fcactus-hybrid)
  

  
- 
        
        [Star
          258](https://github.com/login?return_to=%2Fcactus-compute%2Fcactus-hybrid)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/cactus-compute/cactus-hybrid/branches)[Tags](https://github.com/cactus-compute/cactus-hybrid/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[10 Commits](https://github.com/cactus-compute/cactus-hybrid/commits/main/)10 Commits

## Folders and files

NameNameLast commit messageLast commit date[patches/llama.cpp](https://github.com/cactus-compute/cactus-hybrid/tree/main/patches/llama.cpp)[patches/llama.cpp](https://github.com/cactus-compute/cactus-hybrid/tree/main/patches/llama.cpp)  [.gitignore](https://github.com/cactus-compute/cactus-hybrid/blob/main/.gitignore)[.gitignore](https://github.com/cactus-compute/cactus-hybrid/blob/main/.gitignore)  [LICENSE](https://github.com/cactus-compute/cactus-hybrid/blob/main/LICENSE)[LICENSE](https://github.com/cactus-compute/cactus-hybrid/blob/main/LICENSE)  [README.md](https://github.com/cactus-compute/cactus-hybrid/blob/main/README.md)[README.md](https://github.com/cactus-compute/cactus-hybrid/blob/main/README.md)  View all files

## Repository files navigation

# Cactus Hybrid

A small, on-device model is fast and private, but sometimes wrong.
At Cactus we post-train models to know when they are wrong: we ship probes
inside the checkpoint that score every answer with a confidence between
0 and 1, returned as structured data (never parsed out of the answer text).
Answer on-device when confidence is high; you can re-route to a bigger
model when it's low:
 `if confidence < 0.85:
    answer = ask_a_bigger_model(prompt)` 

We start the rollout with  `Gemma 4 E2B Hybrid` , all builds live in the
[Cactus Hybrid collection](https://huggingface.co/collections/Cactus-Compute/cactus-hybrid-6a60da4551074db058e8bb64)
on Hugging Face.

Gemma 4 E2B hybrid, the smallest Gemma model, matches Gemini 3.1 Flash-Lite
on common benchmarks by routing only 15–55% of queries to the Gemini 3.1 Flash-Lite and
running the remnant itself.

Benchmark
Handoff to match Flash-Lite (FP16)
At 4-bit
At 3-bit

ChartQA
15–20%
25–30%
40–50%

MMBench
30–35%
40–45%
50–55%

LibriSpeech
25–30%
35–40%
55–65%

GigaSpeech
30–35%
40–45%
50–55%

MMAU
30–35%
35–40%
50–55%

MMLU-Pro
45–55%
~90%
n/a

- N/B: Quantisation quality is measured on [Cactus Quants](https://github.com/cactus-compute/cactus/blob/main/docs/cactus_quants.md)
which performs well at uniform quantization.

- Developers are encouraged to benchmark for Unsloth, GGUF, and MLX quantization independently.

## Cactus

 `# pip install cactus-compute
import json
from cactus.bindings.cactus import cactus_complete, cactus_init
from cactus.cli.download import download_bundle

lm = cactus_init(str(download_bundle("Cactus-Compute/gemma-4-E2B-it")))
result = cactus_complete(
    lm,
    [{"role": "user", "content": "What is the capital of France?"}],
    json.dumps({"max_tokens": 512, "auto_handoff": False}),
    None,
    lambda *_: None,
)
print(result["response"].strip())
print("confidence:", result["confidence"])` 

## MLX

 `# pip install mlx-lm
import re
from mlx_lm import load, generate

model, tokenizer = load(
    "Cactus-Compute/gemma-4-e2b-it-hybrid-mlx",
    tokenizer_config={"trust_remote_code": True},
)

messages = [{"role": "user", "content": "What is the capital of France?"}]
answer = generate(
    model,
    tokenizer,
    prompt=tokenizer.apply_chat_template(messages, add_generation_prompt=True),
    max_tokens=512,
)
# the checkpoint reasons before answering; keep only the final answer
answer = re.split(r"<\|?channel\|?>", answer)[-1]
answer = re.sub(r"^(thought|final)\b\s*", "", answer).strip()
print(answer)
print("confidence:", model.last_confidence)` 

## Transformers

 `# pip install "transformers>=5.5.4,<5.6" torch   (5.14+ segfaults on this checkpoint)
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Cactus-Compute/gemma-4-e2b-it-hybrid"
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, dtype="auto").to(device)

messages = [{"role": "user", "content": "What is the capital of France?"}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
).to(device)
out = model.generate(**inputs, return_confidence=True, max_new_tokens=512)

print(tokenizer.decode(out.sequences[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
print("confidence:", out.confidence)` 

Load the model with an explicit  `.to(device)` , not  `device_map="auto"` : the
probe scores generations outside the module  `forward()`  path, so weights that
accelerate offloads (left on the  `meta`  device) crash the confidence read.

## llama.cpp

llama.cpp is C++, so the probe is a patch you compile into the engine (see
 `` [patches/llama.cpp/](https://github.com/cactus-compute/cactus-hybrid/blob/main/patches/llama.cpp)). Build the patched server once:
 `git clone https://github.com/cactus-compute/cactus-hybrid && cd cactus-hybrid
./patches/llama.cpp/install.sh && rehash` 

Then serve and query it like any llama-server — the response carries a
top-level  `confidence`  field:
 `llama-server -hf Cactus-Compute/gemma-4-e2b-it-hybrid-GGUF:Q4_K_M --jinja` 
 `curl -s http://localhost:8080/v1/chat/completions \
  -d '{"messages":[{"role":"user","content":"What is the capital of France?"}],"max_tokens":512}' \
  | jq '{answer: .choices[0].message.content, confidence}'` 

## Routing Quality (AUROC)

 `Gemma 4 E2B Hybrid`  AUROC measures how well the the separates wrong answers from right ones
(higher = better, 0.5 is random, 1.0 is perfect):

Hold-out
Modality
Cactus Hybrid
Token Entropy

MMLU
text MCQ
0.770
0.697

MMLU-Pro
text MCQ
0.771
0.692

ARC-Easy
text MCQ
0.888
0.655

ARC-Challenge
text MCQ
0.834
0.646

GSM8K (3-shot)
text gen
0.782
0.731

MMBench-EN-Dev
vision MCQ
0.840
0.435

ChartQA
vision QA
0.779
0.615

DocVQA
vision QA
0.781
0.512

MMAU
audio MCQ
0.789
0.517

GigaSpeech
audio
0.876
0.343

Earnings-22
audio
0.839
0.323

LibriSpeech
audio
0.822
0.427

Mean

0.814
0.549

The strongest result: the probe was trained on zero audio data, yet achieves
0.79–0.88 AUROC on four audio benchmarks (two transcription, one audio MCQ, one
out-of-domain transcription).

This rules out surface-level explanations, the probe
is reading a modality-independent correctness signal from the hidden state, not
memorizing patterns from training data.

MIT-licensed. Gemma model use is subject to the Gemma terms.

## About

On-device models that know when they're wrong: every answer carries a confidence score for cloud handoff.[huggingface.co/collections/Cactus-Compute/cactus-hybrid-6a60da4551074db058e8bb64](https://huggingface.co/collections/Cactus-Compute/cactus-hybrid-6a60da4551074db058e8bb64)

### Resources

[Readme](https://github.com/cactus-compute/cactus-hybrid#readme-ov-file)[MIT license](https://github.com/cactus-compute/cactus-hybrid#MIT-1-ov-file)[Activity](https://github.com/cactus-compute/cactus-hybrid/activity)[Custom properties](https://github.com/cactus-compute/cactus-hybrid/custom-properties)

### Stars

258 stars

### Watchers

0 watching

### Forks

[8 forks](https://github.com/cactus-compute/cactus-hybrid/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fcactus-compute%2Fcactus-hybrid&report=cactus-compute+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
