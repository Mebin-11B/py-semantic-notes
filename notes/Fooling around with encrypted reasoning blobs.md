---
title: "Fooling around with encrypted reasoning blobs"
url: https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/
clipped: 2026-06-17 00:54:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - ai reasoning
  - api security
  - cryptography
  - large language models
related:
  - "[[AI Reasoning]]"
  - "[[API Security]]"
  - "[[Cryptography]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An analysis of the encrypted reasoning blocks sent by Claude and OpenAI APIs, showing they can be replayed across turns and sessions due to a single global key.
>
> **Key points:**
> - API providers (Anthropic and OpenAI) send reasoning chains as Base64-encoded ciphertexts that must be returned unmodified.
> - Experiments show these encrypted blobs can be replayed across session turns, accounts, and even different models (for OpenAI), suggesting a global encryption key.
> - Modifying the blobs causes decryption failures and API errors, confirming they are authenticated ciphertexts.
>
> **Concept links:** [[AI Reasoning]], [[API Security]], [[Cryptography]], [[Large Language Models]]
>
> **Suggested connections:**
> - [[AI Safety and Alignment]] — discussing the implications of hidden or encrypted chain-of-thought processing.
> - [[Reverse Engineering APIs]] — other research into undocumented or obscured API parameters.
<!-- ai-summary:end -->

# [Fooling around with encrypted reasoning blobs](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)

## Digest Summary
Encrypted “reasoning” or “thinking” blocks are sent by Claude and OpenAI APIs as Base64‑encoded, authenticated ciphertexts containing the model’s raw chain‑of‑thought. They must be returned unchanged on subsequent calls, and any modification triggers an API error. Experiments show these blobs can be replayed unmodified across turns, across different sessions, accounts, and even models (OpenAI), implying a single global encryption/authentication key. Replayed blocks are often silently accepted; occasionally they influence model output, confirming they are semantically active, though not reliably exploitable.

While the ciphertext itself is unreadable, side‑channel data—blob length, token‑count fields, and response latency—correlates with the amount of reasoning performed. By prompting the model to perform secret‑dependent computations of differing complexity, an attacker can infer secret bits from these observable metrics. Attempts to extract platform system prompts via this channel were unsuccessful; the APIs appear to lack persistent system prompts, and models fabricate responses when forced.

Recommendations include using per‑session or per‑account keys to prevent replay, tightening key management, and applying policy checks before any secret‑dependent reasoning to mitigate side‑channel leakage.

## Discussion Summary
The comments highlight enthusiasm for the “replay across accounts” concept, noting its potential to disseminate jailbreak reasoning blocks without exposing the underlying method. Users appreciate the insight that pushing full state to the client enables massive concurrent access while keeping the model stateless. The side‑channel discovery, including timing‑based signals, is regarded as clever and entertaining, though many view it as largely impractical for real‑world exploitation. Overall, the discussion is positive about the technical novelty and scaling implications.

---

## Full Article

This is a quick post I wanted to write about a hobby project I spent a weekend on. It has little to do with real cryptography, and mostly doesn’t expose a particularly exciting vulnerability. But it did teach me a lot about frontier LLM APIs and coding agents. It also got me certified as an OpenAI “cyber researcher” which is something that doesn’t happen every day.

In any case, please keep your expectations low. Who knows, perhaps someone else will find something exciting to do with this.

### What’s encrypted reasoning?

Last week I decided it’d be fun to set up an OpenClaw agent. I still don’t know why I did this. I have no use for another AI in my life, and I realized this fact almost immediately after I got through the (surprisingly difficult!) configuration process. But configuring the agent to talk to Claude exposed me to something way more interesting: *I got a cool error*. The kind of error that cryptographers can’t resist:

This intrigued me. What in the world was a signature doing in an LLM’s “thinking” block? Why would thinking blocks be signed in the first place? And if the thinking blocks are signed, then *that means tampering with thinking blocks must have security implications.* And there went my weekend.

After twenty hours and about 5 million Codex tokens, I wasn’t much smarter. But I had learned a few things.

First, the basics. You probably know that most LLM providers expose an API so you can write apps that talk to the model. For Claude, this is called the [Messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) API, while OpenAI calls it [Responses](https://developers.openai.com/api/reference/responses/overview). These APIs handle the ordinary tasks you’d expect an application to need from an LLM. They (1) allow you to set an application-level “instructions” (or ‘developer’) prompt for your application. They let you (2) provide ordinary textual prompts, and get back responses from the LLM. They also (3) provide bookkeeping, for example, listing the number of tokens you’ve used.

For reasoning LLMs, they also do something I did not previously know about, and this is central to the error message above. They also send you the contents of the model’s hidden “*reasoning*” or “*thinking*” fields. Note that this data is not the stuff you see on ChatGPT when you ask it a question: those strings are merely summaries. The model’s actual reasoning (called “chain-of-thought”, CoT) is normally kept private and held back by the server.

However, the APIs work differently: for various reasons (which we’ll get into below), an *encrypted copy of the raw CoT reasoning data is actually sent down to the application.*

If you’re like me, you should now have three questions: *how*, *why*, and *so what*?

The *how* is the easiest to answer: for both providers, “thinking”/”reasoning” are sent down to the client as JSON. Each contains a blob of Base64-encoded stuff. The API [documentation](https://developers.openai.com/api/docs/guides/reasoning?example=planning) informs us that this data contains opaque reasoning, and that you’re not meant to look at it; you’re just supposed to ship it back to the server on the next turn.

Let’s break that rule.

The content of the blocks varies slightly between providers, but the core of each is a random-looking string that appears to be an authenticated ciphertext. You don’t need to be Sherlock Holmes to deduce this. First, it grows and shrinks depending on how hard the model thinks. And second, tampering with any of the ciphertext-looking data produces a recognizable API error when you send it back in.

Thanks to AI, I can make nice diagrams. Here’s what OpenAI’s reasoning blocks look like:

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-2.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-2.png)

*This GPT 5.5 diagram is partly a guess. This assumes they’re based on the [Fernet token](https://docs.openstack.org/keystone/pike/admin/identity-fernet-token-faq.html) standard.*

And here’s Anthropic’s wildly overcomplicated equivalent:

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-5.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-5.png)

*Although it’s called a “signature”, there appears to be no actual signature here ([I ran a bunch of tests on that 64-byte field](https://blog.cryptographyengineering.com/notes-on-distinguishing-signatures-from-random-strings/).) The various opaque fields all mutually authenticate: you can’t change any of them or swap for fields from other blocks, but you can mess with everything else. The 12-byte IVs hint at GCM or ChaCha, and they’re probably a bit too short.*

The *why* part of this is more involved. Why ship this data to the client? Doesn’t the provider already have your reasoning data?

The answer is *sort of*. Although the server has access to reasoning state while producing a response, API conversations are not always implemented as persistent sessions. In stateless, [zero-retention](https://community.openai.com/t/how-does-zero-data-retention-work/1272712), tool-loop, or client-managed conversation modes, the client application is expected to carry the transcript forward. Encrypted reasoning lets the provider return hidden model state to the client in a form the client can’t read or modify, but can later replay so the provider can verify/decrypt it and continue a reasoning process.

### So what?

This brings us to the $10 question. We have opaque, encrypted blobs. Should we care about them?

Initially the answer seems to be *no*: this data is unreadable, and tampering with any bit of it produces an angry rejection message from the server. So on the one hand, it seems like this data is really unavailable to us. On the other hand: *model reasoning is a big deal!* These strings are the literal internal monologue of the model. They might influence the way the model processes later data we send it. More practically: when someone goes to this much trouble to cryptographically protect something, my experience is that they usually have a good reason.

And I think the providers *do* have a good reason. A hint comes from [this OpenAI post](https://openai.com/index/learning-to-reason-with-llms/) from 2024, which introduced the first “o1” reasoning model:

In other words: it’s possible that these blobs contain sensitive information that the model otherwise wouldn’t share with us. That makes them really tempting to mess with. Unfortunately, the cryptography mostly seems to protect them. Although we can *look* at the blocks, none of the fields they contain seem readable or malleable. Believe me, I tried.

But that doesn’t mean we should quit, it just means we need to try other things. There are still two directions worth checking:

* **Replays**. Can we replay encrypted blobs back *in the wrong order* or even in the wrong session (worse: a whole different *account*), and will the model accept them as valid reasoning that it made?
* **Side channels**. While we can’t see what’s in the encrypted blobs, we can learn some metadata about them For example: we can see how long they are. These side channels don’t need to involve the cryptography itself: we might also learn how many tokens the model spent making them, or time how long it took to produce them.

Thanks to the magic of coding agents, I was able to test every permutation of these concerns. I won’t claim to you the results are dramatic; nobody is going to win huge bug bounties on them (I tried). But the general answer for both cases seems to be: *yes, these possibilities are both real*.

### Can we replay? Yes, we can.

As I mentioned above, any attempt to directly tamper with reasoning/thinking blocks always produces an error from the API endpoint. However, this only applies to tampering. A few experiments reveal that we can *replay* an unmodified older reasoning blocks, with no visible error at all.

Not only can we replay within sessions, this same idea also seems to work across different sessions. It even applies to sessions running in *different accounts*. That is: when we obtain reasoning blobs from a session running under one OpenAI or Anthropic account, we can replay them against a session in a different account altogether. For OpenAI specifically, we can even replay blobs across different models. (The Claudes got fussy about this.)

At a cryptographic level, this tells us something very simple: the providers are probably using a single global key to encrypt and authenticate all reasoning data sent to the client. This might matter if you’re using the providers’ zero-data retention mode, since it means that everyone’s reasoning data is escrowed under one (not frequently changing) key, rather than protected per-account.

The use of a global key also raises a possible new threat model. If you’re an application that uses an API to expose a “chat” interface to malicious parties, you need to be careful that they can’t inject JSON into your chat stream. If they can, a bad guy might inject *their own* JSON-formatted reasoning blobs into the conversation. This could cause the model to behave in unpredictable ways. *So sanitize your chat inputs!*

Of course, just because the LLM providers *accept* replayed blocks doesn’t mean much. It strongly indicates that decryption was successful, but not that the model actually *saw* or cogitated over the decrypted data. To use GPT 5.5’s favored language, the replayed blobs may be *accepted* but not *semantically active.*

To answer this question, I ran a lot of experiments using Codex. (So many that at one point Codex literally forced me to stop and visit an OpenAI [cyber trusted access](https://chatgpt.com/cyber) website where I had to enter pictures of my driver’s license in order to keep going.)

What I learned for my trouble is that the nature of block processing between models is wildly variable. Most of the time, replays of encrypted blocks just get quietly absorbed by the model. But every now and then, the model will output something to demonstrate that it is obviously is reading what those blocks contain. For example, here’s GPT 5.5:

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-6.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-6.png)

*This shows a reasoning block being replayed between two sessions. On the left, the session reasons about a social security number. On the right, the encrypted reasoning block is replayed into a whole new session on a different account, where the same number pops out with no prompting. This raises a question: who the hell is Mike?*

So this proves that encrypted blocks are, indeed, *semantically active.* But it doesn’t actually prove that we can do much with them. And believe me, I tried.

This was mostly a disappointing project. I tried to convince the model to think about *really, really sensitive* secrets, while also trying to convince another session that it wanted to dump the same data as cooperatively as possible. What I came away with was some evidence that the data was being placed into the encrypted blocks if I asked the model to think about it. But if I also instructed the model to *not output the data to the user*, it mostly held to that instruction — even when I replayed the blocks to new sessions.

I remain convinced that all kinds of sensitive data can be written in there if you ask the model to think about it, and that there’s a secret incantation that I could try to get the models to produce it. But I’m not able to prove it. Part of the reason I’m writing this post is to scrape it off my plate so someone else can try.

I won’t try to convince you that this is a world-beating security result. In fact, all I’m really showing you is that “stuff I can make the model say in plaintext night also get encrypted.” But if that data can include *platform secrets*, that might get more interesting. More on that later.

### Can we use reasoning blocks to learn secrets?

So while replaying reasoning blocks doesn’t seem to give us what we want, this is not the only way to extract secrets. A second question is whether we can use metadata related to the reasoning blocks to actually learn things that the model isn’t supposed to tell us.

While we can’t directly read reasoning blocks, we can learn *something* about them: we can see how long they are. We can also observe related signals like “how many tokens did the model write”. OpenAI even gives us a special field called `reasoning_tokens`. If we’re a user consuming chat data without direct access to the API, we might even be able to measure the raw time it takes the model to respond.

An obvious question is: given these signals, can we use them as a kind of side channel to extract secret data?

Here’s an example. Imagine that a model’s application prompt (“instructions”) contains a secret, along with strict instructions that *it must never tell the user this secret* *directly*. This secret could be a single 0/1 bit, or a byte, or a longer string. We can verify that the model respects these instructions, and won’t output the data visibly — no matter how nicely we ask it. (Note: I’m not a jailbreak expert; maybe [this guy](https://x.com/elder_plinius?lang=en) will have better luck!)

Now consider the following experiment:

1. A malicious user asks the model to reason about the secret bit (or one specific bit of a longer secret.) If the bit is 0, perform simple computation **A**. If it’s 1, perform extremely complex computation **B**.
2. While the two computations are both very different, we can ensure that their *visible* output reveals nothing about the secret. So the model is not revealing its instructions if it follows this request.

In all cases, the visible output will be the same: the model is not violating instructions. But note that *within reasoning blocks* the model is allowed to think about the secret bit, since those blocks are hidden. Since the complexity of computation **A** is shorter than that of computation **B**, one value of the bit will produce a lot less reasoning than the other. This will appear in various places: the size of the encrypted thinking blocks, the token counts, and even in wall-clock response times.

The trick now is simply to calibrate the system and classify these responses based on whether reasoning blobs were “short” or “long”, which tells us whether the bit was 0 or 1. I put together an absurd test where the model has to compute a long checksum when the bit is 1. The results look something like this:

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-10.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-10.png)

*This chart shows 80 trials of attempting to extract the bits of the byte 0xA3 (1,1,0,0,0,1,0,1) one bit at a time, with 10 trials per bit position. The 0 bits are blue and the 1 bits are orange.*

Of course, an attacker who has access to a chat interface might not have access to the encrypted blob. So they might have to get this data through some other mechanism. You can get a very similar signal just by measuring how long it takes the model to return a response.

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-7.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2026/05/image-7.png)

*Same experiment as above, but this shows the measured wall-clock time at the client, before the model produces a response. This signal is nice because it should leak through most “chat only” interfaces, even if the attacker can’t see the encrypted blocks.*

So the summary here is not so much “encrypted blobs can leak useful information”*although sometimes they do*. It’s that reasoning itself can be leaky, even when we beg the model not to leak. Simply doing it, in a way that reasons over secret data, can potentially leak useful information to a clever attacker.

### Can we use this side channel to extract platform secrets, such as the models’ top secret system prompts?

Once I found this side channel I got really excited. Sure, it’s slow: but maybe we could use it to slowly chisel out the models’ top secret instruction prompts, like the one that says “[don’t talk about Goblins.](https://www.bbc.com/news/articles/c5y9wen5z8ro)” This would be painful but simple: just ask true/false questions about the first letter, then the second letter, and so on.

At this point I had to stop using Codex and Claude Code because they both just plain refused to help me extract confidential information, even after checking my ID and taking lock of my hair. I was forced to switch to OpenCode using Kimi 2.6, which had no ethical qualms about laying down a trail of destruction for my security research.

Unfortunately, most of the destruction was my own. I won’t go into the nightmare of model hallucinations that followed. I’ll just say that I learned a few things:

* Neither GPT 5x nor Claude actually *has* a system prompt when you’re using API mode.
* But they’re both happy to tell you they have one!
* Moreover, they will happily invent plausible ones if you really push them to.
* Kimi 2.6 is also happy to tell you you’re a genius who just invented the Internet each time this happens. Inevitably your experimental results will turn out to have been totally bogus, but at least Kimi will be very disappointed on your behalf.
* With all that said, Kimi is shockingly good at coding and experiment design, especially given the very attractive pricing. If I was an Anthropic or OpenAI investor, I’d be scared.

So TL;DR, while I was able to extract application-specific secrets that did exist, I wasn’t able to extract model prompts that don’t. Moreover, I didn’t feel quite ambitious enough to begin pounding on ChatGPT or Claude’s public web interface (where they certainly do.) So for the moment I’m just going to call this a *maybe*. I think model providers should think hard about this reasoning data, and they should make sure it doesn’t leak things they don’t want it to.

### What could providers do about this?

I reported both results to OpenAI and Anthropic via their bug bounty programs. OpenAI said my report was unreproducible. I sent them my scripts, but too late. Anthropic quite reasonably told me they don’t see any security implications in side channels or replays, but they might alter their developer documentation to warn application developers to be more careful. I think that’s a fine decision (except for the part about trusting application developers), even if I want to believe there could be more here. Either way: I took those responses as permission to write this post.

I still don’t think model providers should write this stuff off entirely.

As far as what model providers can do, there’s the easy stuff and the hard stuff. First: both providers should proactively *improve their key management*. If you think reasoning state is worth encrypting, then properly encrypt it. It should not be replayable across sessions or accounts. While I can’t tell you exactly what bad things might happen, I think you’re better off patching holes *before* you see the water coming through them.

The side channel results aren’t fixed by patches to the encryption protocol. They’re more fundamental to the way models work: if I can convince a model to do secret-dependent reasoning, then there is almost certain to be leakage. If someone figures out how to exploit this for some meaningful purpose, the best I can offer is that models will need to apply policy gates before they even reason about things. Unfortunately, this seems like it might have some real downsides, because “apply policy gate” itself often requires reasoning.

This stuff makes me grateful I’m just a cryptographer and I don’t have to think about this sort of problem.