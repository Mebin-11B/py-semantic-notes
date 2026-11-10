---
title: "GitHub - End2End-Diffusion/diffusion-bench: Towards Holistic evaluation of Generative Diffusion Transformers! · GitHub"
url: https://github.com/End2End-Diffusion/diffusion-bench
clipped: 2026-08-31 12:26:33
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GitHub - End2End-Diffusion/diffusion-bench: Towards Holistic evaluation of Generative Diffusion Transformers! · GitHub](https://github.com/End2End-Diffusion/diffusion-bench)

## Full Article

[Skip to content](https://github.com/End2End-Diffusion/diffusion-bench#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [End2End-Diffusion](https://github.com/End2End-Diffusion)    
    /
    
      [diffusion-bench](https://github.com/End2End-Diffusion/diffusion-bench)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2FEnd2End-Diffusion%2Fdiffusion-bench)    You must be signed in to change notification settings

  

  
- 
          [Fork
    6](https://github.com/login?return_to=%2FEnd2End-Diffusion%2Fdiffusion-bench)
  

  
- 
        
        [Star
          104](https://github.com/login?return_to=%2FEnd2End-Diffusion%2Fdiffusion-bench)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/End2End-Diffusion/diffusion-bench/branches)[Tags](https://github.com/End2End-Diffusion/diffusion-bench/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[4 Commits](https://github.com/End2End-Diffusion/diffusion-bench/commits/main/)4 Commits

## Folders and files

NameNameLast commit messageLast commit date[assets](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/assets)[assets](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/assets)  [configs](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/configs)[configs](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/configs)  [docs](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/docs)[docs](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/docs)  [scripts](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/scripts)[scripts](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/scripts)  [skills](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/skills)[skills](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/skills)  [src](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/src)[src](https://github.com/End2End-Diffusion/diffusion-bench/tree/main/src)  [.gitignore](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/.gitignore)[.gitignore](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/.gitignore)  [.pre-commit-config.yaml](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/.pre-commit-config.yaml)[.pre-commit-config.yaml](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/.pre-commit-config.yaml)  [README.md](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/README.md)[README.md](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/README.md)  [pyproject.toml](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/pyproject.toml)[pyproject.toml](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/pyproject.toml)  [uv.lock](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/uv.lock)[uv.lock](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/uv.lock)  View all files

## Repository files navigation

# 
  
  diffusion-bench

 ` `##############################################################################
#                                                                            #
#   ____  _  __  __           _                            .-----------.     #
#  |  _ \(_)/ _|/ _|_   _ ___(_) ___  _ __                 |           |     #
#  | | | | | |_| |_| | | / __| |/ _ \| '_ \                | ░▒▓█▓▒░▒▓ |     #
#  | |_| | |  _|  _| |_| \__ \ | (_) | | | |               | ▒▓█████▓▒ |     #
#  |____/|_|_| |_|  \__,_|___/_|\___/|_| |_|               | ▓███████▓ |     #
#                                                          |     ↓     |     #
#   ____                  _                                | █████████ |     #
#  | __ )  ___ _ __   ___| |__                             | ▓███████▓ |     #
#  |  _ \ / _ \ '_ \ / __| '_ \                            | ▒▓█████▓▒ |     #
#  | |_) |  __/ | | | (__| | | |                           |           |     #
#  |____/ \___|_| |_|\___|_| |_|                           '-----------'     #
#                                                                            #
#           Because ImageNet evaluation alone is no longer enough!           #
#                                                                            #
##############################################################################
` ` 

    

## News

🎉 New: 512-res T2I checkpoints. We've released pretrained 512×512 T2I models on three VAEs:  `Qwen-Image-VAE` ,  `E2E-Qwen-Image-VAE` , and  `FLUX.2-VAE` ; trained at batch size 1024 for 10 epochs on BLIP3o (pretrained-only, no SFT). The checkpoints and training logs are on [HuggingFace](https://huggingface.co/diffusion-bench), and their  `training/`  +  `sampling/`  configs are now in the repo; prepare the data with  `scripts/prepare.py --data t2i-res512` .

We have released a very preliminary technical report for DiffusionBench v0.1! We plan to update it heavily going forward, add new contributors/authors, and work with the community to make DiffusionBench more robust and better. Please join us!

Please refer to  `` [docs/contributors.md](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/docs/contributors.md) and  `` [docs/contributing.md](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/docs/contributing.md) for further details.

This repo contains the unified codebase for DiffusionBench. It supports training and evaluation across different generation tasks (ImageNet, T2I, ...) through a single interface. Please see the sections below for the detailed structure. Come join us!

  
  
  Text-to-image samples at 256×256 from models trained for 200K iterations using DiffusionBench.

## Quickstart

### Setup

 `# install uv project manager (if you don't already have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# install dependencies
uv sync

# prepare data
uv run python scripts/prepare.py --data {all,imagenet,t2i,t2i-res512,eval}

# download pretrained models
uv run hf download diffusion-bench/diffusion-bench --local-dir pretrained_models --exclude .gitattributes` 

### Training

Reproduction flow: Stage 1 → Stage 2. Set these environment variables first (used for the output directory and W&B logging):
 `export EXPERIMENT_NAME=<run-name>
export ENTITY=<wandb-entity>
export PROJECT=<wandb-project>
export WANDB_KEY=<key>` 

Stage 1. Train the RAE tokenizer:
 `uv run torchrun --standalone --nproc_per_node=8 \
    src/train_stage1.py \
    --config [STAGE1_CONFIG_PATH] \
    --results-dir results/stage1 --precision bf16 --compile --wandb` 

Stage 2. Train the diffusion model on VAE/RAE/Pixel space:
 `uv run torchrun --standalone --nproc_per_node=8 \
    src/train.py \
    --config [STAGE2_CONFIG_PATH] \
    --results-dir results/stage2 --precision bf16 --compile --wandb` 

### Evaluation

Stage 2 training configs run online evaluation during training (the  `eval:`  block). For standalone evaluation of a released checkpoint, use the  `sampling/`  configs — each embeds  `stage_2.ckpt`  (pointing into  `pretrained_models/` ) and the eval-time guidance, so the weights load automatically:
 `export EXPERIMENT_NAME=<run-name>

# stage 1 reconstruction (rFID/PSNR/SSIM/LPIPS)
uv run torchrun --nproc_per_node=8 src/offline_eval_stage1.py --config [STAGE1_CONFIG_PATH]

# stage 2 generation (FID/IS, GenEval/DPGBench/...)
uv run torchrun --nproc_per_node=8 src/offline_eval.py --config [STAGE2_CONFIG_PATH]` 

### Available Configs

 ` `configs/
├── stage1/
└── stage2/
    ├── training/
    │   ├── imagenet/
    │   └── t2i/
    └── sampling/
        ├── imagenet/
        └── t2i/
` ` 

Stage 2 spans VAE (11), RAE (6), REG (4), and Pixel (3) families, identical across ImageNet and T2I. Swap any config between tasks with a single path change. The  `sampling/`  set mirrors  `training/`  but adds the trained checkpoint and eval-time guidance, so it runs offline eval directly.

For ImageNet, pick the CFG-off baseline ( `[STAGE2_CONFIG_PATH].yaml` ) or the per-model best-CFG variant ( `[STAGE2_CONFIG_PATH]-cfg<scale>-t0.0-0.9.yaml` ).

## Supported Methods

Category
Methods

Latent Space
 `Pixel Space`   `RAE`  (30+ representation encoders):  `DINOv2`   `SigLIP2`   `WebSSL`   `PE`   `LangPE`  and more  `RAEv2`  (30+ representation encoders):  `DINOv2`   `SigLIP2`   `WebSSL`   `PE`   `LangPE`  etc  `VAE`  (10+ VAEs):  `FLUX.2`   `FLUX.1`   `SD3.5`   `VA-VAE`   `E2E-VAE`  and more

Output Prediction
 `x-prediction`   `v-prediction` 

Transport
 `Rectified-Flow`   `MeanFlow`   `Improved-MeanFlow`   `Pixel-MeanFlow`   `Drifting` 

Loss
 `Flow Matching`   `REPA`   `iREPA` 

Architecture
 `LightningDiT`   `JiT`   `DDT` 

Tasks
 `ImageNet` : class-conditional generation  `T2I` : text-to-image generation

Evaluation
ImageNet:  `FID`   `IS`  T2I:  `GenEval`   `DPGBench`   `GenAIBench`   `VQAScore` 

Training Backend
 `DDP`   `FSDP [TODO]` 

## Compatibility

Status
Details

Coding Agents
Yes
Agent-compatible. See  `` [skills/](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/skills) for setup and workflow skills.

AutoResearch
[TODO]
AutoResearch integration is planned (not yet available).

## Contributing

We welcome contributions! Please refer to  `` [docs/contributors.md](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/docs/contributors.md) and  `` [docs/contributing.md](https://github.com/End2End-Diffusion/diffusion-bench/blob/main/docs/contributing.md) for further details.

## Acknowledgments

The codebase is built upon some amazing projects:

- [RAE](https://github.com/bytetriper/RAE)

- [RAEv2](https://github.com/nanovisionx/RAEv2)

- [REPA](https://github.com/sihyun-yu/REPA)

- [REPA-E](https://github.com/End2End-Diffusion/REPA-E)

- [JiT](https://github.com/LTH14/JiT)

We thank the authors for making their work publicly available.

## About

Towards Holistic evaluation of Generative Diffusion Transformers![end2end-diffusion.github.io/blog/posts/diffusion-bench](https://end2end-diffusion.github.io/blog/posts/diffusion-bench)

### Resources

[Readme](https://github.com/End2End-Diffusion/diffusion-bench#readme-ov-file)

### Contributing

[Contributing](https://github.com/End2End-Diffusion/diffusion-bench#contributing-ov-file)[Activity](https://github.com/End2End-Diffusion/diffusion-bench/activity)[Custom properties](https://github.com/End2End-Diffusion/diffusion-bench/custom-properties)

### Stars

104 stars

### Watchers

1 watching

### Forks

[6 forks](https://github.com/End2End-Diffusion/diffusion-bench/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FEnd2End-Diffusion%2Fdiffusion-bench&report=End2End-Diffusion+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
