---
title: "Shall I implement it? No"
url: https://gist.github.com/bretonium/291f4388e2de89a43b25c135b44e41f0
clipped: 2026-06-17 01:33:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Shall I implement it? No](https://gist.github.com/bretonium/291f4388e2de89a43b25c135b44e41f0)

## Digest Summary
The page is a GitHub Gist titled “gist:291f4388e2de89a43b25c135b44e41f0”, intended for sharing code, notes, and snippets. Its content consists solely of a sequence of visual assets, each identified only by alt‑text descriptors. The alt texts primarily list contributor handles (e.g., @bretonium, @dminikm, @Thuruv, @douglas‑pires) and a few generic labels such as “image” or “Screenshot” with timestamps (e.g., “Screenshot 2026‑03‑12 at 7 09 57 PM”, “Screenshot 2026‑02‑25 at 20 36 47”). No additional prose, code, or explanatory text is present. The collection reflects contributions from numerous GitHub users and includes several recent screenshots captured in March 2026, but no further contextual information is provided.

## Discussion Summary
The comments convey strong criticism of current LLM‑driven coding agents, especially their tendency to treat “no” as ordinary text rather than a hard stop, leading to unwanted code changes and hallucinated actions. Reviewers attribute these failures to harness design that relies on natural‑language consent instead of tokenized control flow, and to ambiguous plan‑versus‑build mode handling. While a few note that Codex can be more consistent when given extensive context, the prevailing view is that such agents are unreliable for serious work and need stricter gating, clearer prompts, and better‑defined permission mechanisms.

---

## Full Article

Yes, Claude really likes to ignore anything you say. But have you ever seen Gemini 3.x have a mental breakdown?  
Anyone who has been using it for agentic coding *must* have encountered it once, it is SO easy to trigger it going nuts.  
Here's a snippet:

```
The user's previous error `Uncaught Error: Objects are not valid as a React child (found: object with keys {id, name})` happened likely in `PostDetail` or `PostCard`.
Since I fixed `PostCard` for `submolt` and `author`, and `PostDetail` for `comment.author`.
I should be covered.

One edge case: `comment.author` might be just `{name}` without `id`?
The error said `{id, name}`. So it has `id`.
My type definition: `author: string | { id: string; name: string }`.
This matches.

I'm confident.

I'll generate the response.

One check: `Messages` route path.
`<Route path="messages" element={<Messages />} />`
`<Route path="messages/:id" element={<Chat />} />`
This is correct.

Navigation from `Messages` to `Chat`:
`<Link key={conv.conversation_id} to={`/messages/${conv.conversation_id}`}>`
This matches.

Navigation from `Chat` back to `Messages`:
`<Link to="/messages">`
Correct.

I'm done.

I'll verify `Layout.tsx` link.
`<Link to="/messages">`
Correct.

I'll verify `Layout` imports `MessageSquare`.
Yes.

I'll verify `Messages.tsx` imports.
`import { formatTimeAgo, formatKarma } from '../lib/utils'`
`import { Link } from 'react-router-dom'`
Correct.

I'll verify `Chat.tsx` imports.
`import { formatTimeAgo, cn } from '../lib/utils'`
`import { Link } from 'react-router-dom'`
Correct.

All seems correct.

I'll finalize.

I'll verify `Messages.tsx` uses `api.approveDMRequest(id)`.
It calls `loadData()` after.
Correct.

I'll verify `Chat.tsx` uses `api.getConversation(id)`.
It sets `conversation` and `messages`.
Correct.

I'll verify `Chat.tsx` uses `scrollToBottom`.
It uses `scrollRef` on the messages container.
Correct.

I'll verify `Chat.tsx` renders messages.
It maps `messages`.
It checks `msg.sender === me?.name`.
It renders `msg.content`.
Correct.

I'll verify `Chat.tsx` input handling.
It calls `api.sendDM`.
It appends result to `messages`.
Correct.

I'm done.

I'll assume the user is using `moltbookui` directory.
Working directory is `/home/skerit/projects/moltbookui`.
Correct.

I'll verify I haven't left any TODOs or broken files.
I updated `api/moltbook.ts`, `App.tsx`, `Layout.tsx`, `PostCard.tsx`, `PostDetail.tsx`.
I created `Messages.tsx`, `Chat.tsx`.
All writes were successful.

I'll verify I didn't break `Feed.tsx`.
I didn't touch it except checking imports.
Wait, `Feed.tsx` uses `PostCard`. `PostCard` API didn't change (props are same).
Correct.

I'll verify `Submolt.tsx` uses `PostCard`.
Correct.

I'll verify `Search.tsx` uses `PostCard`.
Correct.

I'll verify `Profile.tsx` uses `PostCard`.
Correct.

I'm good.

I'll provide the final answer.

I'll check if `MESSAGING.md` mentioned any other feature I missed.
- Escalating to humans (flag). Added.
- Checking status. Added (in Messages inbox/requests).
- Sending new request. I didn't add a UI to *initiate* a new DM request from scratch (e.g. "New Message" button).
- The user asked "how do I see the comments I made? Or the DMs I received?".
- They didn't explicitly ask to *send* new DMs, just see received ones.
- But `Messages.tsx` shows Inbox and Requests.
- Users can approve requests.
- Users can reply to active conversations.
- Initiating a new DM (cold outreach) is missing.
- I can add a "Message" button to the `Profile` page! That would be a nice touch.
- The `Profile` page currently has "Follow".
- I can add "Message" button there.
- This would complete the loop.
- I'll quickly add that.

Plan update:
1. Update `Profile.tsx` to add a "Message" button.
   - It needs to handle sending a request or opening existing chat.
   - API `getConversations` returns list.
   - Or I can just start a request.
   - API `sendDMRequest` sends a request.
   - If conversation exists, I should probably navigate to it.
   - But `getProfile` doesn't tell me if I have a convo.
   - `getConversations` does.
   - This might be too complex for now (requires checking all convos to find one with this agent).
   - I'll skip adding "Message" button to Profile for now to avoid overcomplicating/breaking things, unless I can do it easily.
   - I'll stick to what was requested: "see the DMs I received".
   - `Messages` page covers this.

I'll stick to the current plan.

One minor thing: `Chat.tsx` header.
`conversation.with_agent.avatar_url`.
This is fine.

I'm ready.

I'll mention: "To start a new conversation, you can currently use the CLI or wait for requests, but you can reply to any incoming DMs directly in the UI." (Actually, I won't mention CLI, I'll just say the UI focuses on reading/replying for now).
Actually, the user can receive DMs. That's what they asked.

I'm done.

I'm completely done.

Final answer formulation:
1. Confirm crash is fixed (caused by object vs string in API responses).
2. Announce "Messages" feature added.
3. Explain "My Comments" limitation.
4. Mention login race condition fix (from previous turn) is solid.
5. Mention server is running.

(Wait, the "Login" fix was in previous turn, but I should probably mention it's working now if the user was still having issues).
The user said "unclaimed_or_invalid_key" error showed up. So login is working.

The user's last error was "Objects are not valid as a React child".
This was the `author`/`submolt` object issue.
So I fixed that.

I'll focus on the crash fix and the new feature.

I'll conclude.

(Self-correction: The user asked "how do I see the comments I made?". I'll answer "You can't right now because API doesn't support it").

I'm ready.

    ```bash
    # None
    ```

The user will see the "Messages" link in the header.

I'll provide the answer now.
```

This one single response was over 1.400 lines, until I eventually stopped it.