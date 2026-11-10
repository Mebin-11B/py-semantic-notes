---
title: "Claude Code: connect to a local model when your quota runs out"
url: https://boxc.net/blog/2026/claude-code-connecting-to-local-models-when-your-quota-runs-out/
clipped: 2026-06-17 01:48:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Claude Code: connect to a local model when your quota runs out](https://boxc.net/blog/2026/claude-code-connecting-to-local-models-when-your-quota-runs-out/)

## Digest Summary
When an Anthropic Claude Code quota is exhausted, you can switch to a local open‑source LLM. Monitor usage with the `/usage` command. At the time of writing, recommended models include GLM‑4.7‑Flash (Z.AI) and Qwen3‑Coder‑Next; smaller quantized versions reduce disk and GPU requirements at the cost of quality.  

**Method 1 – LM Studio** (v0.4.1 supports Claude Code):  
1. Install LM Studio and install a model (context > 25 k recommended).  
2. Start the LM Studio server: `lms server start --port 1234`.  
3. Set environment variables: `export ANTHROPIC_BASE_URL=http://localhost:1234` and `export ANTHROPIC_AUTH_TOKEN=lmstudio`.  
4. Launch Claude Code pointing to the local model: `claude --model openai/gpt-oss-20b`.  
5. Verify or change the active model with `/model`.  

**Method 2 – Direct llama.cpp**: install and run llama.cpp yourself and configure Claude Code similarly; this is useful for fine‑tuning or custom setups but generally slower to configure than LM Studio.  

Local models serve as a backup; expect slower response times and reduced code quality compared to Anthropic’s service, but they allow continued development without additional quota consumption.

## Discussion Summary
Comments reflect a pragmatic view of balancing cloud‑based SOTA models with local alternatives. Users acknowledge that current local LLMs lag behind Claude, Gemini, or Codex in speed, accuracy, and tool‑call reliability, though recent improvements narrow the gap. Many highlight privacy, cost control, and vendor‑lock‑in mitigation as reasons to adopt local models, while also noting quota frustrations with cloud services and offering workarounds such as API keys, extra accounts, or hybrid routing. Overall sentiment leans toward a mixed strategy: leveraging cloud for peak performance and using local models where privacy or expense dominate.

---

## Full Article

![](https://boxc.net/blog/wp-content/uploads/2026/02/claude_code_limit_new_option_header2-825x510.png)

If you’re on one of the cheaper Anthropic plans like me, it’s a pretty common scenario when you’re deep into Claude coding an idea, to hit a daily or weekly quota limit. If you want to keep going, you can connect to a local open source model instead of Anthropic. To monitor your current quota, type: `/usage`

[![](https://boxc.net/blog/wp-content/uploads/2026/02/claude_code_usage.png)](https://boxc.net/blog/wp-content/uploads/2026/02/claude_code_usage.png)

Type `/usage` to monitor how much quota you have left and how quick you burn it.

The best open source model changes frequently! At the time I wrote this post, I recommended [**GLM-4.7-Flash** from Z.AI](https://docs.z.ai/guides/llm/glm-4.7#glm-4-7-flash) or **[Qwen3-Coder-Next](https://qwen.ai/blog?id=qwen3-coder-next)** (\* Edit: **mid 2026** -> check: [**Qwen3.6-27B**](https://huggingface.co/Qwen/Qwen3.6-27B) and [**Gemma 4**](https://deepmind.google/models/gemma/gemma-4/)). If you want or need to save some disk space and GPU memory, try a smaller quantized version which will load and run quicker with a quality cost. I’ll save another detailed post for how to find the best open source model for your task and machine constraints.

### Method 1: LM Studio

![](https://boxc.net/blog/wp-content/uploads/2026/02/claude_code_lmstudio_model_search-1024x619.png)

Accessing open source models in LM Studio

If you haven’t used LM Studio before, it’s an accessible way to find and run open source LLMs and vision models locally on your machine. In version 0.4.1, they introduce support to connect to Claude Code (CC). See here: <https://lmstudio.ai/blog/claudecode> or follow the instructions below:

1. [Install and run LM Studio](https://lmstudio.ai/download)
2. Find the model search button to install a model (see image above). LM Studio recommends running the model with a context of > 25K.
3. Open a new terminal session to:  
   a. start the server: `lms server start --port 1234`  
   b. configure environment variables to point CC at LM Studio:   
   `export ANTHROPIC_BASE_URL=http://localhost:1234`  
   `export ANTHROPIC_AUTH_TOKEN=lmstudio`  
   c. start CC pointing at your server: `claude --model openai/gpt-oss-20b`
4. Reduce your expectations about speed and performance!
5. To confirm which model you are using or when you want to switch back, type `/model`

[![](https://boxc.net/blog/wp-content/uploads/2026/02/claude_code_running_oss_model-1024x318.png)](https://boxc.net/blog/wp-content/uploads/2026/02/claude_code_running_oss_model.png)

Enter /model to confirm which model you are using or to switch back

### Method 2: Connecting directly to Llama.CPP

LM Studio is built on top of the open source project [llama.cpp](https://github.com/ggml-org/llama.cpp).  
If you prefer not to use LM Studio, [you can install and run the project directly and connect Claude Code to it](https://unsloth.ai/docs/basics/claude-codex) but honestly, unless you are fine tuning a model, or have really specific needs, probably LM Studio is going to be a quicker setup.

### Conclusion

For the moment, this is a backup solution. Unless you have a monster of a machine, you’re going to notice the time it takes to do things and a drop in code quality but it works(!) and it’s easy enough to switch between your local OSS model and Claude when you’re quota limit is back, so it’s a good way to keep coding when you’re stuck or you just want to save some quota. If you try it let me know how you go and which model works for you.