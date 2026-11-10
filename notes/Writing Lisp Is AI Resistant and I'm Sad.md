---
title: "Writing Lisp Is AI Resistant and I'm Sad"
url: https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/
clipped: 2026-06-17 01:22:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Writing Lisp Is AI Resistant and I'm Sad](https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/)

## Digest Summary
The author, a DevOps engineer, uses agentic AI (primarily Claude via OpenRouter) for code generation. When attempting to build an RSS‑reader conversion tool in Lisp, they encountered severe productivity issues: AI struggled with REPL interaction, required costly token usage, and produced low‑signal output compared to Python. To ease REPL access, they created a Python utility tmux‑repl‑mcp that forwards commands and returns output, but the AI still consumed $10–$20 in minutes with modest results. Experiments with cheaper models (DeepSeek, Qwen) performed worse. The author notes that AI favors languages with abundant training data (Python, Go) because high‑latency API calls conflict with REPL workflows, forcing batch code generation rather than incremental testing. Tooling preferences (e.g., OCICL over QuickLisp) also needed explicit instruction to the AI. Consequently, they consider rewriting the project in Go, observing that AI‑driven development makes high‑usage languages economically preferable, while Lisp remains “AI resistant” despite its historical resilience.

## Discussion Summary
The comment reports moderate success using an AI coding assistant for Clojure but highlights a persistent difficulty with correctly balancing parentheses, prompting the development of specialized tools to fix this issue. It suggests that simply giving the AI a REPL to iterate on code is not yet reliable for Lisp, emphasizing the importance of precise prompts, test generation, and verification steps. The overall tone is cautiously optimistic, recognizing current limitations while noting that targeted adaptations and testing can make the approach workable.

---

## Full Article

In an insulting, ironic blow to [the neats, the
scruffies](https://en.wikipedia.org/wiki/Neats_and_scruffies) created an AI that
much prefers to write anything but Lisp.

I use agentic AI a lot at work to do my job as a DevOps engineer. I use
[OpenRouter](https://openrouter.ai/) with the [Goose CLI
tool](https://block.github.io/goose/), and I've gotten a pretty good
[configuration
file](https://github.com/djha-skin/dotfiles/blob/main/dot-config/goose/config.yaml)
going with it.

I have lately started writing a tool [that converts between different RSS reader
formats](https://github.com/djha-skin/rssm). I started writing it in Lisp, of
course. It's my favorite language.

I had a problem though. I had to teach the AI how to use the REPL. Initially, I
had it run commands to interact with the REPL via
[tmux](https://github.com/tmux/tmux), e.g. `tmux capture-pane
-t 0.0 -p | tail -n 1`. It worked okay, but I noticed that REPL development was
very hard for the AI. Claude really spun its wheels. Lesser AIs would be very
much worse. I'd blow $10-$20 in a handful of minutes with not much to show for
it but sort of OK lisp code that I ended up rewriting. I tried doing it with
cheaper AIs like [DeepSeek](https://openrouter.ai/deepseek/deepseek-v3.2) and
[Qwen](https://openrouter.ai/qwen/qwen3.5-27b), which I found did OK at work for
some tasks, but it wasn't working.

I figured maybe if I made REPL development smoother, the AI would do a better
job. I wanted to give goose unlimited rights to the REPL while still guarding
general command rights, too. So, I created a tool called
[tmux-repl-mcp](https://github.com/djha-skin/tmux-repl-mcp) that would make
interacting with the REPL more straightforward. Instead of consuming a ton of
tokens, executing a bunch of sleep commands, and parsing tmux output, the could
just run `execute_command` in the repl and get its output.

I wrote this tool in Python since a lot of my AI tooling in my goose
configuration file was built around
[uvx](https://docs.astral.sh/uv/guides/tools/) already. I liked that I just had
to install `uvx` and all of a sudden `goose` could use all these tools. I
already had all this stuff built up in my configuration file, so I figured it
would be easier for folks to use if it were distributed in the same way.
Besides, [the official guide to write an MCP
server](https://modelcontextprotocol.io/docs/develop/build-server) were in
non-lisp languages anyway.

The difference in writing Python and Lisp with AI was of course dramatic,
downright wild. I got it to write all of the code and all the tests for the
code. I had to debug it semi-manually, but I was still able to bang together
this more-than-nothing tool in like a day or two, and with cheap models at that. Worst
of all, the experience for me was the same in many ways: I wrote code by being a
poor man's product owner to the AI for both, only the AI would perform well with
the Python. I felt none of the happiness I usually feel just writing Lisp.

Going back to my actual project was painful. I ended up writing one of the files
(`src/newsboat.lisp`) by hand. I was in the middle of debugging it when I
realized how much harder it was to write with AI in Lisp. I had to switch back
to Claude, which at least makes *some progress* relative to the others. The
`tmux-repl-mcp` tool helped, but I still blew through $10 in like 30 minutes.
The signal-to-noise ratio, or in other words, the wheel-spinning-to-progress
ratio in the AI session was night and day compared to Python. And in AI, you pay
for the noise and the signal together.

Now I'm thinking of rewriting it in Go. With AI, [code is
cheap](https://www.dbreunig.com/2026/03/26/winchester-mystery-house.html), but
only if you use a language for which AI has a lot of training data.

Another frustration has been tooling. Lisp has a lot of tools to choose from. I
like using [OCICL](https://github.com/ocicl/ocicl) instead of QuickLisp, for
example, but I had to tell the AI to not use
[quicklisp](https://www.quicklisp.org/beta/) *every single session*. It was like
built into the AI to use it. This also helped me realize that AI generates code
sort of on a path of least resistance.

There are reasons other than a lack of training data that makes lisp
particularly AI resistant. The high-latency request-reponse way we interact with
AI APIs does not work well with REPLs. REPL development makes programming easier
and better by reducing that latency for humans, but there's already high latency
anyways in these APIs. The downside of not using REPLs is that you have to have
higher accuracy when writing code *and* you can only test big batches of code at
once, but AI can write hundreds of lines in one go so that it just makes sense
for the AI to use a language that doesn't use the REPL.

It is orders of magnitude easier and cheaper to write in high-internet-volume
languages like Go and Python than it is to write in Lisp. The advent of AI has
converted language popularity into real dollars-and-cents-per-million-tokens
cost savings. What's more, building in one language or the other makes no
difference to how *I* experience the language; either way, in the ideal case,
I'm a rather opinionated micro-managy product owner. That is really sad.

It reminds me of a tale that was told in my hometown about [Plank
Road](https://napersettlement.org/515/The-Plank-Road) in [Naperville,
IL](https://www.openstreetmap.org/way/1049211758). The nineteenth century roads
were always muddy, so a bunch of investors created a road that was planked, or
made of wood. The makers of the road would charge money for using the road.
Later, the railroad offered to build a railroad through Naperville, but they
declined, saying they were making plenty of money on the plank road, so the
railroad was built in another city. Everyone stopped using the plank road in
favor of rail, and it eventually survived only in name with no one using it in
its original form.

I know money is not an issue here, at least for me. However, I can't help but
make the comparison in my head. The Plank Road must have been way nicer to
traverse than the muddy roads, evoking joy in the travelers when comparing it
with travelling in the mud, just like Lisp makes me feel versus writing in
something else. However, when the railroad came along, all the farmers had to do
was load it into the cars. With ease like that, why use the silly road at all?

It's just another example of
[Worse is Better](https://dreamsongs.com/WorseIsBetter.html). However, Lisp has
survived this worse-is-better internet era for decades. I wonder what we'll
learn as it survives the AI era as well. I like the neats camp. It's more *fun*.
I wonder what adaptations will be necessary to make AIs work better on Lisp.