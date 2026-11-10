---
title: "DeepSeek v4"
url: https://api-docs.deepseek.com/
clipped: 2026-06-17 01:12:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [DeepSeek v4](https://api-docs.deepseek.com/)

## Digest Summary
The document provides a basic example for making a chat completion request to the DeepSeek API using the OpenAI Python client. It initializes the client with an API key retrieved from the `DEEPSEEK_API_KEY` environment variable and sets the base URL to `https://api.deepseek.com`. The request calls the `deepseek-v4-pro` model, sending a system prompt (“You are a helpful assistant”) and a user message (“Hello”). Parameters include `stream=False`, `reasoning_effort="high"`, and an `extra_body` payload enabling a “thinking” mode (`{"thinking":{"type":"enabled"}}`). The response’s content is printed from `response.choices[0].message.content`. The page also displays two images: the DeepSeek API Docs logo and a WeChat QR code.

## Discussion Summary
The release is regarded as a strong technical advance, with benchmark results positioned at or above leading models and notable throughput efficiency. The early availability of developer documentation is praised as an open‑source best practice. At the same time, there is disappointment that the model lacks native multimodal capability, and some users express fatigue from the rapid pace of AI progress, calling for community support to manage burnout. Overall sentiment combines enthusiasm for performance gains with modest concerns about feature gaps and the sustainability of keeping up.

---

## Full Article

```
import os  
from openai import OpenAI  
  
client = OpenAI(  
    api_key=os.environ.get('DEEPSEEK_API_KEY'),  
    base_url="https://api.deepseek.com")  
  
response = client.chat.completions.create(  
    model="deepseek-v4-pro",  
    messages=[  
        {"role": "system", "content": "You are a helpful assistant"},  
        {"role": "user", "content": "Hello"},  
    ],  
    stream=False,  
    reasoning_effort="high",  
    extra_body={"thinking": {"type": "enabled"}}  
)  
  
print(response.choices[0].message.content)
```