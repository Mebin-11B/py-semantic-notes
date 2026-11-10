---
title: "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model"
url: https://github.com/cactus-compute/needle
clipped: 2026-06-17 01:03:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model](https://github.com/cactus-compute/needle)

## Digest Summary
Needle is a 26‑million‑parameter “Simple Attention Network” distilled from Gemini 3.1, designed for tiny consumer devices. The architecture uses a 512‑dimensional hidden size, 8 attention heads with 4 key/value heads, a BPE‑8192 tokenizer, and replaces feed‑forward layers with gated residual blocks and ZCRMSNorm. It employs masked self‑attention with RoPE, GQA, and cross‑attention from a 12‑layer encoder to an 8‑layer decoder; embeddings are shared between encoder and decoder. Pre‑training ran on 16 TPU v6e for 200 billion tokens (≈27 h), followed by 2 billion tokens of single‑shot function‑call data (≈45 min). Inference achieves ≈6000 tokens/s prefill and 1200 tokens/s decode, surpassing FunctionGemma‑270 M, Qwen‑0.6 B, Granite‑350 M, and LFM‑2.5‑350 M on single‑shot function‑call tasks, though larger models perform better in multi‑turn dialogue. The repository provides open weights, a CLI, and a web UI for testing and fine‑tuning (e.g., `needle finetune data.jsonl`). Citations list the development team and GitHub URL.

## Discussion Summary
The comments show strong interest in tiny, tool‑calling language models and their potential for personal assistants, home automation, and lightweight applications, with several users noting successful experiments such as setting alarms or adding items to shopping lists. Many ask about ambiguity handling, failure modes, dataset availability, and deployment constraints, while others report technical hurdles like repository access errors and CPU‑only execution problems. Opinions diverge on model selection—some praise the approach, others criticize the choice of Gemini as suboptimal—and there are repeated requests for demos and released data, alongside occasional concerns about licensing limits.

---

## Full Article

[![Logo](https://github.com/cactus-compute/needle/raw/main/assets/banner.png)](https://github.com/cactus-compute/needle/blob/main/assets/banner.png)

We distilled Gemini 3.1 into a 26m parameter "[Simple Attention Network](https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md)" that you can even finetune locally on your Mac/PC.
In production, Needle runs on [Cactus](https://github.com/cactus-compute/cactus) at 6000 toks/sec prefill and 1200 decode speed.
Weights are fully open on [Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle), as well as the dataset generation.

```
d=512, 8H/4KV, BPE=8192
                                  ┌──────────────┐
                                  │  Tool Call   │
                                  └──────┬───────┘
                                        ┌┴──────────┐
                                        │  Softmax  │
                                        └─────┬─────┘
                                        ┌─────┴─────┐
                                        │ Linear (T)│  ← tied
                                        └─────┬─────┘
                                        ┌─────┴─────┐
                                        │ ZCRMSNorm │
                                        └─────┬─────┘
                                     ┌────────┴────────┐
                                     │ Decoder x 8     │
                                     │┌───────────────┐│
                                     ││ ZCRMSNorm     ││
                                     ││ Masked Self   ││
                                     ││ Attn + RoPE   ││
                                     ││ Gated Residual││
                                     │├───────────────┤│
  ┌──────────────┐                   ││ ZCRMSNorm     ││
  │ Encoder x 12 │──────────────────────▶Cross Attn   ││
  │              │                   ││ Gated Residual││
  │ ┌──────────┐ │                   │└───────────────┘│
  │ │ZCRMSNorm │ │                   └────────┬────────┘
  │ │Self Attn │ │                      ┌─────┴─────┐
  │ │ GQA+RoPE │ │                      │ Embedding │  ← shared
  │ │Gated Res │ │                      └─────┬─────┘
  │ │          │ │                    ┌───────┴───────-┐
  │ │ (no FFN) │ │                    │[EOS]<tool_call>│
  │ └──────────┘ │                    │ + answer       │
  │              │                    └───────────────-┘
  └──────┬───────┘
         │
    ┌────┴──────┐
    │ Embedding │
    └────┬──────┘
         │
    ┌────┴──────┐
    │   Text    │
    │  query    │
    └───────────┘
```

* Pretrained on 16 TPU v6e for 200B tokens (27hrs).
* Post-trained on 2B tokens of single-shot function call dataset (45mins).

Needle is an experimental run for Simple Attention Networks, geared at redefining tiny AI for consumer devices (phones, watches, glasses...).
So while it beats FunctionGemma-270m, Qwen-0.6B, Graninte-350m, LFM2.5-350m on single-shot function call for personal AI,
Those model are have more scope/capacity and excel in conversational settings. Also, small models can be finicky.
Please use the UI in the next section to test on your own tools, and finetune accordingly, at the click of a button.

```
git clone https://github.com/cactus-compute/needle.git
cd needle && source ./setup
needle playground
```

Opens a web UI at <http://127.0.0.1:7860> where you can test and finetune on your own tools. Weights are auto-downloaded.

```
from needle import SimpleAttentionNetwork, load_checkpoint, generate, get_tokenizer

params, config = load_checkpoint("checkpoints/needle.pkl")
model = SimpleAttentionNetwork(config)
tokenizer = get_tokenizer()

result = generate(
    model, params, tokenizer,
    query="What's the weather in San Francisco?",
    tools='[{"name":"get_weather","description":"Get current weather for a city.","parameters":{"location":{"type":"string","description":"City name.","required":true}}}]',
    stream=False,
)
print(result)
# [{"name":"get_weather","arguments":{"location":"San Francisco"}}]
```

```
# Playground (generates data via Gemini, trains, evaluates, bundles result)
needle playground

# CLI (auto-downloads weights if not local)
needle finetune data.jsonl
```

Each line in the JSONL file has three fields: `query`, `tools`, and `answers`.

**Tool schema:**

```
{
  "name": "get_weather",
  "description": "Get current weather for a city.",
  "parameters": {
    "location": { "type": "string", "description": "City name.", "required": true }
  }
}
```

**Answer schema:**

```
{ "name": "get_weather", "arguments": { "location": "Paris" } }
```

**Full JSONL example** (each line is one training example, `tools` and `answers` are JSON-encoded strings):

```
{"query": "What's the weather in Paris?", "tools": "[{\"name\":\"get_weather\",\"description\":\"Get current weather for a city.\",\"parameters\":{\"location\":{\"type\":\"string\",\"description\":\"City name.\",\"required\":true}}}]", "answers": "[{\"name\":\"get_weather\",\"arguments\":{\"location\":\"Paris\"}}]"}
{"query": "Turn off the lights", "tools": "[{\"name\":\"get_weather\",\"description\":\"Get current weather for a city.\",\"parameters\":{\"location\":{\"type\":\"string\",\"description\":\"City name.\",\"required\":true}}},{\"name\":\"toggle_lights\",\"description\":\"Toggle smart lights on or off.\",\"parameters\":{\"state\":{\"type\":\"string\",\"description\":\"on or off.\",\"required\":true}}}]", "answers": "[{\"name\":\"toggle_lights\",\"arguments\":{\"state\":\"off\"}}]"}
```

Provide at least **120 examples per tool** (100 train / 10 val / 10 test). Fewer examples will overfit — you'll see perfect training metrics but the model won't generalize. Vary query phrasing and include examples with multiple tools available.

Finetuning saves the best checkpoint as `checkpoints/needle_finetuned_<id>_best.pkl`:

```
needle run --checkpoint checkpoints/needle_finetuned_*_best.pkl \
  --query "What's the weather?" --tools '[{"name":"get_weather","description":"Get current weather for a city.","parameters":{"location":{"type":"string","description":"City name.","required":true}}}]'
```

```
params, config = load_checkpoint("checkpoints/needle_finetuned_<id>_best.pkl")
model = SimpleAttentionNetwork(config)
result = generate(model, params, get_tokenizer(), query="...", tools='[...]', stream=False)
```

```
needle playground                  Test and finetune via web UI
needle finetune <data.jsonl>       Finetune on your own data
needle run --query "..." --tools   Single inference
needle train                       Full training run
needle pretrain                    Pretrain on PleIAs/SYNTH
needle eval --checkpoint <path>    Evaluate a checkpoint
needle tokenize                    Tokenize dataset
needle generate-data               Synthesize training data via Gemini
needle tpu <action>                TPU management (see docs/tpu.md)
```

```
@misc{ndubuaku2026needle,
  title={Needle},
  author={Henry Ndubuaku, Jakub Mroz,  Karen Mosoyan, Roman Shemet, Parkirat Sandhu, Satyajit Kumar, Noah Cylich, Justin H. Lee},
  year={2026},
  url={https://github.com/cactus-compute/needle}
}
```