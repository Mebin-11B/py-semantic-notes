---
title: "Autoresearch on an old research idea"
url: https://ykumar.me/blog/eclip-autoresearch/
clipped: 2026-06-17 01:28:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Autoresearch on an old research idea](https://ykumar.me/blog/eclip-autoresearch/)

## Digest Summary
None

## Discussion Summary
The comments recognize that LLM‑driven autoresearch can automate bug fixing and hyper‑parameter tuning, often yielding modest performance gains at relatively low effort. Users note that the approach is effective for optimization but rarely produces novel architectural ideas, and its value depends heavily on the quality of evaluation metrics and available data. Cost of token usage and compute is seen as a concern, while some view it as a useful substitute for repetitive consulting advice. Overall sentiment is cautiously optimistic about its utility for routine engineering tasks but skeptical about broader research impact.

---

## Full Article

Ever since it showed up on my GH feed, Karpathyâs  [Autoresearch](https://ykumar.me/notes#autoresearch)  was rattling around in the back of my mind. I wanted to try it on a research problem I fully understood. So this weekend, I picked up my old research code from  [eCLIP](https://ykumar.me/notes#eclip) , dusted it off the legacy dependencies and gave it to Claude Code. And just let it cook while I did some chores around the house.

This is my journeyâ¦

Core Idea
---------

[Autoresearch](https://ykumar.me/notes#autoresearch)  is a simple constrained optimization loop with an LLM agent in the middle. The agent iteratively improves some eval metric by modifying a single file (`train.py`), while reading instructions from `program.md`. I added a `scratchpad.md` file for the agent to use as working memory to document its thought process and experiment history.

In the `program.md`, I split the exploration into âphasesâ, starting with some obvious hyperparameter tuning, then moving on to small architectural changes and finally some moonshot ideas. In the final phase, I basically let the agent run with minimal constraints, and gave it web access to read papers and look for new ideas.

The whole thing is a tight loop: hypothesize â edit â train â evaluate â commit or revert â repeat.

![Autoresearch agent loop](https://ykumar.me/blog-images/eclip/agent_loop_light.webp)
![Autoresearch agent loop](https://ykumar.me/blog-images/eclip/agent_loop_dark.webp)

The experiment should be short, around 5 minutes wall clock per run, to encourage quick iterations and prevent overfitting to noise. The agent is free to change anything in `train.py` as long as it runs within the time budget.

### Sandboxing

Since I was paranoid about letting the agent run arbitrary code in my workstation, I containerized the training loop and removed network access. The whole experimentation flow is orchestrated by a `run.sh`. Then I lock down Claude Codeâs permissions to only edit these two files and run `run.sh`. No direct Python execution, no pip installs, no network access, no git push, etc.

I wonât bore you with the details, you can [check out the repo here!](https://github.com/ykumards/eCLIP/tree/main/autoresearch)

Dataset
-------

The original paper used several medical X-ray datasets which I donât have access to anymore, so I needed a new dataset with spatial annotations to test the expert attention mechanism. I picked the [Ukiyo-eVG](https://zenodo.org/records/13120879) dataset: ~11K Japanese woodblock prints with phrase â bounding box annotations from the [CIGAr](https://arxiv.org/abs/2410.12369) paper (ECCV 2024 VISART).

![Expert spatial annotations: bounding boxes converted to gaussian heatmaps guide the model to focus on specific regions](https://ykumar.me/blog-images/eclip/heatmap_girls.webp)

*Heatmaps obtained from bounding boxes guide the model to focus on specific regions.*

The bounding boxes were converted to  [gaussian heatmaps](https://ykumar.me/notes#gaussian-heatmaps)  and fed into the model as an additional input, similar to how radiologist eye-gaze heatmaps work in the original  [eCLIP](https://ykumar.me/notes#eclip)  paper.

Hello â Claude Code
---------------------

I had a busy week and a lot of chores piling up, so I just pointed Claude at my old research code and went to do laundry. It upgraded the python env of my old research codebase, wrote the ingestion code for the new dataset, and wrote the scaffolding for the experiment loop.

I set up the CV splits, evaluation logic and some initial ideas for the `program.md`.

For the eval metric we picked  [Mean Rank](https://ykumar.me/notes#mean-rank)  of the retrieved embeddings. I didnât put much thought into it â in hindsight, Median Rank wouldâve been a better choice since itâs more robust to outliers. But we just needed something intuitive that clearly tells the agent whether a change is good or bad. Since Recall@K is the standard for reporting final results anyway, Mean Rank just needed to point in the right direction.

### Other details

* [CLIP](https://ykumar.me/notes#clip)  backbone :  [ViT-Small](https://ykumar.me/notes#vit)  (22M) + DistilBERT (66M) + HeatmapProcessor Â· ~90M params
* Training: 800 steps (~3 min per run on a RTX 4090)
* Eval:  [Mean Rank](https://ykumar.me/notes#mean-rank)  on a held-out test set of 1K images, with Recall@K as a sanity check.
* Baseline: Val mean rank of 344.68, with imgâ\rightarrowâtxt R@1 of 17.2% and txtâ\rightarrowâimg R@1 of 16.5%.

So how did it do?
-----------------

I kicked off the loop on Saturday morning and let it run through the day, occasionally checking in to nudge the agent in the right direction. By the time I was done with groceries, the agent had already burned through a couple of dozen experiments and knocked off a huge chunk of the eval mean rank.

![eCLIP Autoresearch Progress](https://ykumar.me/blog-images/eclip/progress.webp)
![eCLIP Autoresearch Progress](https://ykumar.me/blog-images/eclip/progress_dark.webp)

**42 experiments** Â· 13 committed Â· 29 reverted Â· 1 Saturday Â· 1 4090 GPU

By the end of the day, the agent ran 42 experiments, committing 13 and reverting 29. The mean rank dropped from 344.68 to 157.43 (**54% reduction**).

After the agent finished its exploration, I did one final training run on the full dataset. The test scores actually came out better than the validation scores. This meant we were underfitting during the short 800-step experiment runs, leaving performance on the table.

|  | Mean Rank | imgâtxt R@5 | txtâimg R@5 |
| --- | --- | --- | --- |
| **Test** | **34.30** | **53.0%** | **51.4%** |

So AGI?
-------

Wellâ¦

* *Temperature clamp fix (â113 mean rank):* It immediately went for a bug in my code. I had clamped the learnable  [temperature](https://ykumar.me/notes#contrastive-learning)  param at 2. It relaxed the limit, and boom, the eval dropped by 113 points. This was the single biggest win, worth more than all the architecture changes combined.
* *Optuna++ (-30 mean rank):* Further gains came mostly from hyperparameter tuning. The agent acted like a hyperparameter optimization algorithm with some basic reasoning baked in. Increasing projection dimension and re-tuning the LR knocked off another 30 points. This is still tedious work that a human would do (and get minimal pleasure from), but the agent did it faster and more methodically.
* *Diminishing Returns:* By the time we got to Phase 4 with the architectural changes, the success rate of the LLMâs hypotheses dropped significantly. The changes to the  [attention mechanism](https://ykumar.me/notes#attention-mechanism)  in the heatmap processor didnât work out. Neither did the moonshot ideas in Phase 5. The agent was just throwing spaghetti at the wall, and most of it did not stick.
* *Sandbox is important:* Towards the end, Claude Code sometimes forgot its permissions and started making weird bash calls, then complained and stopped looping. At one point it got tired of waiting for training to finish and just ended the conversation. I wouldnât give it full autonomy just yet :)

### Closing thoughts

Like with any LLM project, the first 90% of the work was super smooth and barely needed my intervention. The last 10% was a slog. This was a fun experiment that showed how an LLM agent can drive ML research in a structured way. When the search space is clearly defined, the commit-or-revert loop proposed in  [Autoresearch](https://ykumar.me/notes#autoresearch)  is a surprisingly effective search strategy. But when the agent ventured into the âunknown unknownsâ, the optimization loop just exploded.

It is possible that the âmake only one change per experimentâ constraint was too tight for the moonshot ideas. Maybe we could have injected a planning stage into the Agent loop so it could think ahead. Or maybe deployed some subagents.

Maybe. But it was already time for dinner, and we were planning to watch a movie after that, so this was where Claude and I parted waysâ¦ until Monday of course.

Epilogue
--------

This post reached #1 on [Hacker News](https://news.ycombinator.com/item?id=47493460). Thanks to everyone who read, shared, and commented!

Acknowledgements
----------------

* [Ukiyo-eVG](https://zenodo.org/records/13120879) â ~11K Japanese woodblock prints with phraseâbounding box annotations from the [CIGAr](https://arxiv.org/abs/2410.12369) paper (ECCV 2024 VISART).
* [Autoresearch](https://github.com/karpathy/autoresearch) by Andrej Karpathy for the original idea.