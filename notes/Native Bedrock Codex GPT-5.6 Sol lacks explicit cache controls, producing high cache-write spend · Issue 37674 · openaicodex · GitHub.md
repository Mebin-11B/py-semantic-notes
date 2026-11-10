---
title: "Native Bedrock Codex GPT-5.6 Sol lacks explicit cache controls, producing high cache-write spend · Issue #37674 · openai/codex · GitHub"
url: https://github.com/openai/codex/issues/37674
clipped: 2026-08-31 12:26:32
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Native Bedrock Codex GPT-5.6 Sol lacks explicit cache controls, producing high cache-write spend · Issue #37674 · openai/codex · GitHub](https://github.com/openai/codex/issues/37674)

## Full Article

[Skip to content](https://github.com/openai/codex/issues/37674#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
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
  

        
      

        

          

  
  

    
    

    
      
    

  

  
  
  

# Native Bedrock Codex GPT-5.6 Sol lacks explicit cache controls, producing high cache-write spend #37674

New issueCopy linkNew issueCopy linkClosedClosed[Native Bedrock Codex GPT-5.6 Sol lacks explicit cache controls, producing high cache-write spend](https://github.com/openai/codex/issues/37674#top)#37674Copy linkAssignees Labels[CLIIssues related to the Codex CLI](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22CLI%22)Issues related to the Codex CLI[aws-bedrockIssues related to AWS Bedrock provider](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22aws-bedrock%22)Issues related to AWS Bedrock provider[enhancementNew feature or request](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request[rate-limitsIssues related to rate limits, quotas, and token usage reporting](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22rate-limits%22)Issues related to rate limits, quotas, and token usage reporting

## Description

[apexethdev](https://github.com/apexethdev)opened [on Aug 9, 2026](https://github.com/openai/codex/issues/37674#issue-5101353034)Issue body actions

## Summary

Native Codex CLI requests to Amazon Bedrock Mantle cannot opt into GPT-5.6 Sol explicit prompt caching. On an agentic coding workload, this has produced a large volume of cache-write tokens and materially higher cost.

This is related to [#35300](https://github.com/openai/codex/issues/35300), but adds independent production usage evidence from the native  `amazon-bedrock`  provider.

## Environment

- Codex CLI:  `0.147.0` 

- Provider: native  `amazon-bedrock` 

- Endpoint: Bedrock Mantle Responses API,  `us-east-1` 

- Model:  `openai.gpt-5.6-sol` 

## Observed production usage

For the completed days 2026-08-05 through 2026-08-08, Cost Explorer usage quantities and the Bedrock rate card produced the following cache-aware estimate for Sol:

Requests
Cache-write tokens
Estimated cache-write cost
Estimated total cost

3,656
171.94M
$1,182.09
$1,386.46

Cache writes were about 85% of the model's estimated spend.

A local Codex session also reported 76 Sol requests with 6.709M  `cache_write_input_tokens` , zero  `cached_input_tokens` , and an average of about 88K cache-write tokens per request. There were no client errors in the corresponding CloudWatch metrics.

These are usage-derived estimates, not finalized AWS invoice amounts.

## Investigation

Codex already emits a session-scoped  `prompt_cache_key` , but the request types for both HTTP and WebSocket Responses requests do not include either:

-  `prompt_cache_options` 

-  `prompt_cache_breakpoint` 

The built-in Amazon Bedrock provider config exposes transport/auth settings, not structured request-body transformation, so this cannot be configured through  `config.toml` .

AWS documents explicit cache mode for GPT-5.6 on Bedrock specifically for agentic workflows with long stable instructions/tool definitions followed by changing tool and user content. That matches the workload above.

## Requested behavior

- Add support for serializing  `prompt_cache_options`  for GPT-5.6-capable Responses providers.

- Add a typed  `prompt_cache_breakpoint`  field to supported input content blocks.

- Provide a provider/model capability gate and a safe placement strategy at the end of Codex's measured stable instruction/tool prefix.

- Surface cache reads and cache writes in per-turn usage telemetry so users can diagnose costly full-prefix rewrites.

## Scope

This report does not claim that every cache write is a defect. Cold starts, genuinely distinct prompts, forks, and compaction can all require writes. The issue is that native Bedrock Codex currently has no way to use the documented explicit-cache mechanism for the stable-prefix case.Reactions are currently unavailable

## Metadata

## Metadata

### Assignees

- [celia-oai](https://github.com/celia-oai)

### Labels

[CLIIssues related to the Codex CLI](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22CLI%22)Issues related to the Codex CLI[aws-bedrockIssues related to AWS Bedrock provider](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22aws-bedrock%22)Issues related to AWS Bedrock provider[enhancementNew feature or request](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request[rate-limitsIssues related to rate limits, quotas, and token usage reporting](https://github.com/openai/codex/issues?q=state%3Aopen%20label%3A%22rate-limits%22)Issues related to rate limits, quotas, and token usage reporting

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
