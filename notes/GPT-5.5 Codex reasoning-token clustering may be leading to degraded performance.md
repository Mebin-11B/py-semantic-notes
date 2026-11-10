---
title: "GPT-5.5 Codex reasoning-token clustering may be leading to degraded performance"
url: https://github.com/openai/codex/issues/30364
clipped: 2026-08-31 12:22:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [GPT-5.5 Codex reasoning-token clustering may be leading to degraded performance](https://github.com/openai/codex/issues/30364)

## Digest Summary
The issue reports a consistent clustering of Codex responses from the GPT‑5.5 model at exact reasoning‑output token counts of 516, with secondary spikes at 1,034 and 1,552. This pattern appears model‑specific: GPT‑5.5 accounts for only 19.3 % of total responses but 82.0 % of exact‑516 events, yielding an exact‑516/>=516 ratio roughly 33.6× higher than non‑GPT‑5.5 baselines. Concurrently, average and 90th‑percentile reasoning‑token intensity declined from February‑April to May‑June, while exact‑516 clustering rose sharply. Similar clustering is weak or absent in GPT‑5.4, GPT‑5.2, and other Codex variants. The fixed token values suggest possible internal thresholds (budget caps, routing, truncation, or scheduler limits) rather than natural variation. The report asks the Codex team to investigate whether GPT‑5.5 employs a reasoning‑budget mechanism causing termination near these token counts, and to clarify if the 516‑token stop point represents a normal limit, degraded tier, or other internal behavior.

---

## Full Article

[Skip to content](https://github.com/openai/codex/issues/30364#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [openai](https://github.com/openai)    
    /
    
      [codex](https://github.com/openai/codex)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fopenai%2Fcodex)    You must be signed in to change notification settings

  

  
- 
          [Fork
    18.4k](https://github.com/login?return_to=%2Fopenai%2Fcodex)
  

  
- 
        
        [Star
          120k](https://github.com/login?return_to=%2Fopenai%2Fcodex)
  

        
      

        

          

  
  

    
    

    
      
    

  

  
  
  

# GPT-5.5 Codex reasoning-token clustering at 516/1034/1552 may be leading to degraded performance on complex tasks #30364

New issueCopy linkNew issueCopy linkClosedClosed[GPT-5.5 Codex reasoning-token clustering at 516/1034/1552 may be leading to degraded performance on complex tasks](https://github.com/openai/codex/issues/30364#top)#30364Copy linkLabels[bugSomething isn't working](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[model-behaviorIssues related to behaviors exhibited by the model](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22model-behavior%22)Issues related to behaviors exhibited by the model[rate-limitsIssues related to rate limits, quotas, and token usage reporting](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22rate-limits%22)Issues related to rate limits, quotas, and token usage reporting

## Description

[vguptaa45](https://github.com/vguptaa45)opened [on Jun 27, 2026](https://github.com/openai/codex/issues/30364#issue-4758717065)Issue body actions

## Summary

I found an aggregate pattern in Codex  `token_count`  metadata:  `gpt-5.5`  responses disproportionately land at exactly  `reasoning_output_tokens = 516` , with additional fixed-boundary spikes around  `1034`  and  `1552` .

This appears model-specific and coincides with lower overall reasoning-token intensity, which may help explain degraded performance on complex/high-stakes Codex tasks.

This is related to [#29353](https://github.com/openai/codex/issues/29353), which reported a task-level reproduction where  `gpt-5.5`  runs ending at exactly 516 reasoning tokens returned the wrong answer. This issue adds aggregate evidence across a larger Feb-Jun window.

I am not claiming this proves hidden chain-of-thought truncation. The narrower claim is that Codex telemetry shows a GPT-5.5-specific fixed-token clustering anomaly that looks consistent with thresholded reasoning-budget behavior.

## Environment

- Product: Codex

- Model most implicated:  `gpt-5.5` 

- Data source: Codex  `token_count`  metadata

- Time window analyzed: Feb 1-Jun 27, 2026 UTC

- Related issue: [gpt-5.5 xhigh sometimes short-circuits with reasoning_output_tokens=516 and wrong final_answer in Codex Desktop #29353](https://github.com/openai/codex/issues/29353)

## Evidence

Metric
Value

Response-level token records analyzed
390,195

Sessions represented
865

Exact  `reasoning_output_tokens = 516`  events
3,363

GPT-5.5 share of all responses
19.3%

GPT-5.5 share of exact-516 events
82.0%

GPT-5.5 exact-516 / >=516 ratio
44.0%

Non-GPT-5.5 exact-516 / >=516 ratio
1.3%

Model-level result:

Model
Response records
Exact 516 / >=516

 `gpt-5.5` 
75,401
44.0%

 `gpt-5.4` 
25,214
19.8%

 `gpt-5.2` 
247,575
0.34%

 `gpt-5.3-codex` 
13,333
0.0%

 `gpt-5.3-codex-spark` 
26,179
0.0%

Monthly exact-516 clustering increased sharply:

Month
Exact 516 / >=516

Feb 2026
0.11%

Mar 2026
2.45%

Apr 2026
4.25%

May 2026
53.30%

Jun 2026
35.84%

At the same time, overall reasoning-token intensity decreased:

Month
Mean reasoning tokens
P90 reasoning tokens

Feb 2026
268.1
772

Mar 2026
256.8
723

Apr 2026
228.7
669

May 2026
106.9
344

Jun 2026
168.5
515

## Why this looks suspicious

The anomaly is not simply higher reasoning-token usage overall. Mean and P90 reasoning-token intensity fell from February-April to May-June, while exact-516 clustering rose sharply.

The clustering is also not evenly distributed across models.  `gpt-5.5`  accounts for only 19.3% of responses but 82.0% of exact-516 events. Its exact-516 / >=516 ratio is about 33.6x higher than the non-GPT-5.5 baseline.

The fixed values are also notable:  `516` ,  `1034` , and  `1552`  look like repeated threshold boundaries rather than a naturally varying reasoning-token distribution.

## Expected behavior

Reasoning-token counts for complex Codex tasks should vary naturally with task complexity and should not disproportionately cluster at exact fixed values for one model family.

## Actual behavior

 `gpt-5.5`  responses cluster heavily at exactly 516 reasoning tokens, with related spikes around 1034 and 1552. This pattern is much weaker or absent in several other models.

## Ask

Could the Codex team investigate whether  `gpt-5.5`  has a reasoning-budget, routing, truncation, fallback, or scheduler behavior that causes responses to terminate around 516/1034/1552 reasoning tokens?

If this is expected behavior, it would be useful to know whether exact 516 indicates a normal stopping point, a budget cap, a degraded tier, or another internal threshold.

Useful internal validation checks:

- Query  `token_count`  events with  `reasoning_output_tokens`  by model.

- Compare exact-value counts for  `0` ,  `516` ,  `1034` , and  `1552` .

- Compute  `count(reasoning_output_tokens = 516) / count(reasoning_output_tokens >= 516)`  by model and day.

- Compare  `gpt-5.5`  against  `gpt-5.2` ,  `gpt-5.4` , and Codex-specific variants.

- Replay matched complex tasks across GPT-5.2 and GPT-5.5 with quality evals, especially separating exact-516 responses from longer-reasoning responses.
Reactions are currently unavailable

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

[bugSomething isn't working](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[model-behaviorIssues related to behaviors exhibited by the model](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22model-behavior%22)Issues related to behaviors exhibited by the model[rate-limitsIssues related to rate limits, quotas, and token usage reporting](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22rate-limits%22)Issues related to rate limits, quotas, and token usage reporting

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

- Open in GitHub Copilot app

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
