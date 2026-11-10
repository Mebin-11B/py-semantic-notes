---
title: "GitHub - AminBlg/SimpleEnglish: Agent skill: make LLMs write docs in ASD-STE100 Simplified Technical · GitHub"
url: https://github.com/AminBlg/SimpleEnglish
clipped: 2026-08-31 12:26:39
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [GitHub - AminBlg/SimpleEnglish: Agent skill: make LLMs write docs in ASD-STE100 Simplified Technical · GitHub](https://github.com/AminBlg/SimpleEnglish)

## Full Article

[Skip to content](https://github.com/AminBlg/SimpleEnglish#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [AminBlg](https://github.com/AminBlg)    
    /
    
      [SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2FAminBlg%2FSimpleEnglish)    You must be signed in to change notification settings

  

  
- 
          [Fork
    105](https://github.com/login?return_to=%2FAminBlg%2FSimpleEnglish)
  

  
- 
        
        [Star
          3k](https://github.com/login?return_to=%2FAminBlg%2FSimpleEnglish)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/AminBlg/SimpleEnglish/branches)[Tags](https://github.com/AminBlg/SimpleEnglish/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[31 Commits](https://github.com/AminBlg/SimpleEnglish/commits/main/)31 Commits

## Folders and files

NameNameLast commit messageLast commit date[.claude-plugin](https://github.com/AminBlg/SimpleEnglish/tree/main/.claude-plugin)[.claude-plugin](https://github.com/AminBlg/SimpleEnglish/tree/main/.claude-plugin)  [evals](https://github.com/AminBlg/SimpleEnglish/tree/main/evals)[evals](https://github.com/AminBlg/SimpleEnglish/tree/main/evals)  [examples](https://github.com/AminBlg/SimpleEnglish/tree/main/examples)[examples](https://github.com/AminBlg/SimpleEnglish/tree/main/examples)  [output-styles](https://github.com/AminBlg/SimpleEnglish/tree/main/output-styles)[output-styles](https://github.com/AminBlg/SimpleEnglish/tree/main/output-styles)  [package/results/raw](https://github.com/AminBlg/SimpleEnglish/tree/main/package/results/raw)[package/results/raw](https://github.com/AminBlg/SimpleEnglish/tree/main/package/results/raw)  [prompts](https://github.com/AminBlg/SimpleEnglish/tree/main/prompts)[prompts](https://github.com/AminBlg/SimpleEnglish/tree/main/prompts)  [skills/simple-english](https://github.com/AminBlg/SimpleEnglish/tree/main/skills/simple-english)[skills/simple-english](https://github.com/AminBlg/SimpleEnglish/tree/main/skills/simple-english)  [.gitignore](https://github.com/AminBlg/SimpleEnglish/blob/main/.gitignore)[.gitignore](https://github.com/AminBlg/SimpleEnglish/blob/main/.gitignore)  [LICENSE](https://github.com/AminBlg/SimpleEnglish/blob/main/LICENSE)[LICENSE](https://github.com/AminBlg/SimpleEnglish/blob/main/LICENSE)  [README.md](https://github.com/AminBlg/SimpleEnglish/blob/main/README.md)[README.md](https://github.com/AminBlg/SimpleEnglish/blob/main/README.md)  View all files

## Repository files navigation

  ✈️ your AI writes like a LinkedIn post. make it write like a Boeing manual.

  An agent skill that forces LLMs to write docs in [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/):
  the controlled language aerospace has used since 1983 so a tired mechanic cannot misread an instruction.
  AI slop dies as a side effect.

  
  
  
  
  
  

  

  [See it](https://github.com/AminBlg/SimpleEnglish#-before--after) ·
  [Install](https://github.com/AminBlg/SimpleEnglish#-install) ·
  [The rules](https://github.com/AminBlg/SimpleEnglish#-the-rules) ·
  [Not just docs](https://github.com/AminBlg/SimpleEnglish#-not-just-docs) ·
  [Receipts](https://github.com/AminBlg/SimpleEnglish#-receipts) ·
  [FAQ](https://github.com/AminBlg/SimpleEnglish#-faq)

Works in every harness that speaks the [Agent Skills standard](https://agentskills.io): Claude Code, Cursor, VS Code Copilot, OpenAI Codex, Gemini CLI, Goose, OpenCode, and ~25 more. One folder, no dependencies, MIT.

## 🔥 Before / after

Left column is real unedited Claude output. Right column is the same model with the skill loaded.

🤖 Without skill
✈️ With skill

Leveraging sqlpipe's robust architecture, users can seamlessly synchronize their Postgres tables to S3 with minimal configuration overhead. Before getting started, you should ensure that your AWS credentials have been properly configured — this is crucial for avoiding frustrating permission issues down the line.

sqlpipe copies your Postgres tables to S3. It needs one configuration file.

Before you start, make sure that your AWS credentials are correct. If they are not, S3 rejects the upload with a permission error.

Oops! Something went wrong while attempting to establish a connection. Please ensure your credentials have been properly configured and try again, or reach out to your administrator if the issue persists.

Connection to the database failed: the password for user  `app`  was not correct.
Set  `DB_PASSWORD`  to the correct value, then connect again.

We have identified an issue that may have impacted some users' ability to access the service. We sincerely apologize for any inconvenience this may have caused.

Between 14:02 and 14:31 UTC, 12% of requests failed. A deploy at 14:00 removed the cache warmup step. We reverted it at 14:27.

More rewrites in  `` [examples/before-after.md](https://github.com/AminBlg/SimpleEnglish/blob/main/examples/before-after.md): READMEs, error messages, incident reports, release notes.

## 📦 Install

 `npx skills add AminBlg/SimpleEnglish` 

That is it. The [skills CLI](https://github.com/vercel-labs/skills) detects your agents (Claude Code, Cursor, Codex, Copilot, Gemini CLI, and more) and installs for the ones you pick. Try before installing:
 `npx skills use AminBlg/SimpleEnglish@simple-english` 

Claude Code plugin: this repo is also a plugin marketplace. From your terminal:
 `claude plugin marketplace add AminBlg/SimpleEnglish && claude plugin install simple-english@simple-english` 

Or inside Claude Code:  `/plugin marketplace add AminBlg/SimpleEnglish` , then  `/plugin install simple-english@simple-english` .

Output style (Claude Code): the plugin also ships simple-english as an [output style](https://code.claude.com/docs/en/output-styles). The skill triggers when a writing task fits; the style is always on, for every reply. After you install the plugin, run  `/config` , open Output style, and pick  `simple-english` . Claude then writes all its prose in STE and codes as before.

No SKILL.md support at all? Paste  `` [prompts/system-prompt.md](https://github.com/AminBlg/SimpleEnglish/blob/main/prompts/system-prompt.md) into your system prompt, AGENTS.md, or  `.cursorrules` . There is even a ~60-token version for tight budgets.

Then ask for any technical writing, or say: "rewrite this with simple-english".

## 🖱️ No terminal? (claude.ai, ChatGPT, Gemini)

Claude.ai (paid plans) supports skills natively:

- Download the skill file: open [SKILL.md](https://github.com/AminBlg/SimpleEnglish/raw/main/skills/simple-english/SKILL.md) and save it (Ctrl+S / Cmd+S).

- In claude.ai, go to Settings → Capabilities and turn on code execution.

- Go to Settings → Customize → Skills → Upload and upload the saved  `SKILL.md` .

- Toggle the skill on. Done. Claude applies it when you ask for technical writing.

ChatGPT: no skill support, so use the prompt version. Copy the block from  `` [prompts/system-prompt.md](https://github.com/AminBlg/SimpleEnglish/blob/main/prompts/system-prompt.md) into Settings → Personalization → Custom Instructions, or into the instructions of a Project or Custom GPT.

Gemini: create a Gem and paste the same block into its instructions.

Any other chatbot: attach or paste  `prompts/system-prompt.md`  into the chat and say "apply this to everything you write for me".

## 📏 The rules

53 numbered rules, 9 sections, written in 1983 by people whose readers die when a sentence is ambiguous. The ones doing the heavy lifting:

Rule
What it kills

Max 20 words per instruction, 25 per description
The run-on sentence

One word = one meaning, whole document
check/verify/confirm/validate roulette

Simple tenses only
"has been updated" → "we updated"

No "-ing" verb forms
", making it easy to..." clauses

Active voice
"it should be noted that"

No should/would/may/might
Hedging. ( `can` ,  `will` ,  `must`  survive)

Condition BEFORE command
Trailing "...if the flag is set" that readers execute too late

One instruction per sentence
Steps nobody can follow at 2 a.m.

Keep articles, keep "that"
Telegraph style. STE is short, not terse

Full paraphrased set with software examples:  `` [SKILL.md](https://github.com/AminBlg/SimpleEnglish/blob/main/skills/simple-english/SKILL.md). Yes, this README breaks half of them. Marketing is explicitly out of STE scope. The skill knows that and stays in the docs.

## 🧰 Not just docs

The skill ships adaptations ( `` [use-cases.md](https://github.com/AminBlg/SimpleEnglish/blob/main/skills/simple-english/references/use-cases.md)) for:

- Error messages: what happened → why → what to do, in that order

- Runbooks: STE's home turf; a runbook IS a maintenance manual

- Incident reports: simple past murders "we have identified an issue that may have impacted"

- Release notes: breaking changes as warnings: command first, risk second

- Your AGENTS.md / prompts: a system prompt is a procedure for a reader that cannot ask questions. Models read "should" as optional. STE bans "should".

- Translation prep: STE's original job: readable for non-natives, cheap to localize

Where it refuses to go: marketing copy, blog voice, brand writing. Flat on purpose.

## 📊 Benchmarks

74.6% fewer STE violations per 100 words with the skill on, averaged across 7 models × 8 writing tasks (112 generations, measured).

Model
Baseline viol/100w
Skill viol/100w
Reduction

claude-opus-5
2.13
0.32
85%

claude-opus-4-8
1.05
0.62
41%

claude-opus-4-7
2.28
0.42
82%

claude-opus-4-6
2.24
0.40
82%

claude-opus-4-5
2.55
0.57
78%

claude-sonnet-5
2.67
0.53
80%

claude-sonnet-4-6
2.06
0.52
75%

A blind pairwise judge (claude-opus-4-8, both text orders, no labels) preferred the skill output in 45 of 56 pairs, with 5 ties and 6 losses. Mean rubric score: 8.1 with the skill, 6.0 without.

Output tokens went DOWN on all seven Claude models too. Deterministic regex linter, same rules for both conditions, reasoning effort pinned to  `low` , honest-caveat list and full method in  `` [evals/results/RESULTS.md](https://github.com/AminBlg/SimpleEnglish/blob/main/evals/results/RESULTS.md). Reproduce with  `python3 evals/run_bench.py`  — needs only a logged-in Claude Code CLI.

### Pi cross-check

A separate Pi run tested four models on the same 8 tasks and 2 conditions. All 64 generations completed.

Model
Baseline viol/100w
Skill viol/100w
Reduction

GLM-5.2 max
2.56
0.40
84.4%

GPT-5.6 Sol medium
1.33
0.16
88.0%

GPT-5.6 Terra medium
1.69
0.48
71.6%

GPT-5.6 Luna medium
1.28
0.42
67.2%

The skill reduced measured violations on all four models. It shortened final text only on GLM-5.2; the three GPT-5.6 models wrote slightly more words.

See the [Pi results, method, raw responses, and reproduction command](https://github.com/AminBlg/SimpleEnglish/blob/main/evals/results/pi-2026-07-31/RESULTS.md). Run other configured models with  `python3 evals/run_pi_bench.py --model PROVIDER/MODEL:THINKING` .

## 🧾 Receipts

Built TDD-style against the primary Issue 9 text (2025), not blog summaries:

- Baseline agents without the skill wrote 40-word sentences and invented rule numbers. One confidently cited "Rule 3.1: short sentences" (real Rule 3.1 is verb forms)

- Secondary sources online are wrong about the modals:  `can`  and  `will`  ARE approved. We checked the PDF.

- The skill was written to close each recorded baseline failure, then re-tested until agents pass. Scenarios + recorded results:  `` [evals/pressure-tests.md](https://github.com/AminBlg/SimpleEnglish/blob/main/evals/pressure-tests.md)

- A community audit ([#4](https://github.com/AminBlg/SimpleEnglish/issues/4)) checked the vocabulary tables against the Issue 9 dictionary and found the consistency pass offered "pick one" where the dictionary had already chosen. We fixed it, then A/B-tested the fix: two agents, same input, strict mode. The agent with the old skill picked the rejected verb "run". The agent with the fixed skill wrote operate, do, erase, show, and make sure that. Zero rejected words survived.

## ❓ FAQ

Does this make output STE-certified? No. Nothing does, because ASD certifies no tool. Default mode is pragmatic: structural rules + your domain vocabulary. Strict mode gets close; word-level rulings live in the official standard, a [free download](https://www.asd-ste100.org/request.html).

Will my docs sound robotic? They will sound like Airbus manuals: flat and impossible to misread. For docs that is the whole point. Keep your voice for your blog.

Why not just prompt "write clearly"? "Clearly" is an opinion. "No sentence over 20 words" is a spec. Agents follow specs.

Why a 40-year-old aerospace standard? Because it is not vibes. It is maintained (Issue 9, January 2025), numbered, and testable. And it happens to be a near-perfect negative of every AI writing tell.

## ⭐ Star history

## ⚖️ License and status

MIT for everything here. The repo paraphrases the rules for teaching and reproduces zero spec text or dictionary content. Unofficial project, not affiliated with or endorsed by ASD or STEMG. ASD-STE100 is a registered trademark of ASD.

## About

Agent skill: make LLMs write docs in ASD-STE100 Simplified Technical

### Resources

[Readme](https://github.com/AminBlg/SimpleEnglish#readme-ov-file)[MIT license](https://github.com/AminBlg/SimpleEnglish#MIT-1-ov-file)[Activity](https://github.com/AminBlg/SimpleEnglish/activity)

### Stars

3.0k stars

### Watchers

6 watching

### Forks

[105 forks](https://github.com/AminBlg/SimpleEnglish/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FAminBlg%2FSimpleEnglish&report=AminBlg+%28user%29)

## Releases

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
