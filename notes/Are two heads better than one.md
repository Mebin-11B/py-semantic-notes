---
title: "Are two heads better than one?"
url: https://eieio.games/blog/two-heads-arent-better-than-one/
clipped: 2026-06-17 01:58:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Are two heads better than one?](https://eieio.games/blog/two-heads-arent-better-than-one/)

## Digest Summary
The puzzle considers a fair coin flipped, observed by Alice who lies 20 % of the time. Trusting Alice alone yields an 80 % correct guess. Adding Bob, who also lies independently 20 % of the time, does not improve accuracy: the optimal strategy—guess the most likely outcome for each reported pattern—still gives 80 % success. A detailed probability table shows four cases (both truthful, both lying, one truthful/one lying) each contributing 64 %, 4 %, and two 16 % scenarios where a random guess yields 50 % correctness, summing to 80 %. Simulations of one‑million trials confirm the result. Introducing a third independent liar (Charlie) raises accuracy to 90 % because a majority vote breaks ties; a fourth (David) restores an even number of voters and the gain disappears. This mirrors Condorcet’s Jury Theorem: with independent voters each correct with probability > ½, the majority decision’s correctness approaches 100 % as the odd voter count grows, while even counts add no information without a tie‑breaker.

## Discussion Summary
The discussion emphasizes that when two sources have equal but opposite reliability the combined likelihood is symmetric, yielding no information gain in tie cases. It notes that trusting an additional low‑accuracy observer does not improve overall correctness unless their agreement provides a clear signal, and that strategies beyond unconditional trust offer no advantage. Extensions to multiple observers, relational coherence, and analogies to error‑correction or betting are explored, highlighting the limits of information gain from correlated or noisy inputs.

---

## Full Article

You’re playing a game with your lying friends Alice and Bob.

Bob flips a coin and shows it to Alice. Alice tells you what she saw - but she lies 20% of the time. Then you take your best guess on whether the coin is heads or tails.

Your best strategy is to trust whatever Alice says. You’re right 80% of the time.

Now Bob joins in. He makes up his mind independent of Alice, and he *also* lies 20% of the time 1.

1

Your friends are all liars!

You were right 80% of the time by trusting Alice.

How much better can you do with Bob’s help?

Here’s some empty space for you to think
----------------------------------------

I’m going to give you the answer below. So here’s some empty space for you to think in case you want to do the math yourself.

Alright, let’s do some math
---------------------------

The answer is 0% - you don’t do any better! You’re still exactly 80% to get the right answer.

To establish this, let’s write a simple simulation. We’ll flip a coin a million times, ask our friends what they saw, and observe the results.

For our strategy, we’ll look at a fact pattern (like “Alice says heads”), figure out what’s most likely (“the coin is heads”), and say “we guess the coin flip correctly whenever the most likely outcome occurs for this fact pattern” 2.

2

Given that Bob and Alice decide independently and aren’t playing
adversarially, “guess the most likely outcome” is optimal here. It may not be
optimal if the game was adversarial, although I think that’s a trickier
question than it might first seem.

Here’s the code for that simulation. We’ll start with the easy case (just Alice):

 The simulation code

```
from random import random
from collections import defaultdict

table = defaultdict(lambda: [0, 0])
LYING_PROB = 0.2
LYING_FRIENDS = ["Alice"]
ITERATIONS = 1_000_000

for _ in range(ITERATIONS):
    is_heads = random() > 0.5
    keys = []
    for lying_friend in LYING_FRIENDS:
        lied = random() < LYING_PROB
        answer = None
        if is_heads: answer = "T" if lied else "H"
        else: answer = "H" if lied else "T"
        keys.append(f"{lying_friend[0]}:{answer}")

    key = ", ".join(keys)

    table_idx = 0 if is_heads else 1
    table[key][table_idx] += 1

total_times_we_are_right = 0
for key, (times_heads, times_tails) in table.items():
    total = times_heads + times_tails
    heads_chance = 100 * round(times_heads / total, 2)
    tails_chance = 100 * round(times_tails / total, 2)
    pattern_chance = 100 * round(total / ITERATIONS, 2)

    print(f"{key} - chances -  H {heads_chance:4}% | T {tails_chance:4}% | occurs {pattern_chance}% of the time")

    
    
    total_times_we_are_right += max(times_heads, times_tails)

accuracy = round(total_times_we_are_right / ITERATIONS, 2)
print(f"\nOur accuracy: {100*accuracy}%")
```

This gives us:

```
% python heads.py
A:T - chances -  H 20.0% | T 80.0% | occurs 50.0% of the time
A:H - chances -  H 80.0% | T 20.0% | occurs 50.0% of the time

Our accuracy: 80.0%
```

Now let’s add Bob to the simulation. We see something like this:

```
% python heads.py
A:T, B:T - chances -  H  6.0% | T 94.0% | occurs 34.0% of the time
A:H, B:T - chances -  H 50.0% | T 50.0% | occurs 16.0% of the time
A:H, B:H - chances -  H 94.0% | T  6.0% | occurs 34.0% of the time
A:T, B:H - chances -  H 50.0% | T 50.0% | occurs 16.0% of the time

Our accuracy: 80.0%
```

That’s weird! But perhaps this gives you an intuition for what’s happening. By introducing a second player, *we introduce the possibility of a tie*.

A decent amount of the time, Alice and Bob agree. *Most* (~94%) of the time when that happens, they’re telling the truth. Occasionally they’re both lying, but that’s pretty unlikely.

But a meaningful portion of the time (32%) Alice says heads and Bob says tails, or vice versa. And in that case we don’t know anything at all! Alice and Bob are equally trustworthy and they disagreed - we’d be better off if we’d just gone and asked Alice 3!

3

I am deeply curious whether anyone else was read the book “Go Ask Alice” by
their middle school science teacher in order to scare them straight or whether
that was specific to my middle school experience.

### Let’s prove it

Now that we’ve simulated this result, let’s walk through each case assuming that the coin landed on heads.

```
- both tell the truth
Alice: Heads (80%), Bob: Heads (80%)
happens 80% * 80% = 64% of the time
we always guess correctly in this case

- both lie
Alice: Tails (20%), Bob: Tails (20%)
happens 20% * 20% = 4% of the time
we never guess correctly in this case

- alice tells the truth, bob lies
Alice: Heads (80%), Bob: Tails (20%)
happens 80% * 20% = 16% of the time
we guess at random in this case; we're right 50% of the time

- alice lies, bob tells the truth
Alice: Tails (20%), Bob: Heads (80%)
happens 20% * 80% = 16% of the time
we guess at random in this case; we're right 50% of the time

Our total chance to guess correctly is:
64% + 16% / 2 + 16% / 2 = 64% + 8% + 8% = 80%
```

There’s something beautiful here. Our total chance to guess remains at 80% because our additional chance to guess correctly when Alice and Bob agree is perfectly offset by the chance that Alice and Bob disagree!

### Meet Charlie (and David)

If our friend Charlie - who also lies 20% of the time - joins the fun, our odds improve substantially. If Bob and Alice disagree, Charlie can act as a tiebreaker.

```
% python heads.py
A:H, B:H, C:H - chances -  H 98.0% | T  2.0% | occurs 26.0% of the time
A:T, B:T, C:T - chances -  H  2.0% | T 98.0% | occurs 26.0% of the time
A:T, B:H, C:H - chances -  H 80.0% | T 20.0% | occurs 8.0% of the time
A:H, B:T, C:T - chances -  H 20.0% | T 80.0% | occurs 8.0% of the time
A:H, B:H, C:T - chances -  H 80.0% | T 20.0% | occurs 8.0% of the time
A:H, B:T, C:H - chances -  H 80.0% | T 20.0% | occurs 8.0% of the time
A:T, B:T, C:H - chances -  H 20.0% | T 80.0% | occurs 8.0% of the time
A:T, B:H, C:T - chances -  H 20.0% | T 80.0% | occurs 8.0% of the time

Our accuracy: 90.0%
```

But if David joins, the pattern repeats. David introduces the possibility of a 2-2 split, and our odds don’t improve at all!

```
% python heads.py
A:T, B:T, C:T, D:T - chances -  H  0.0% | T 100.0% | occurs 21.0% of the time
A:T, B:H, C:H, D:H - chances -  H 94.0% | T  6.0% | occurs 5.0% of the time
A:T, B:H, C:T, D:T - chances -  H  6.0% | T 94.0% | occurs 5.0% of the time
A:H, B:H, C:H, D:H - chances -  H 100.0% | T  0.0% | occurs 21.0% of the time
A:H, B:T, C:H, D:T - chances -  H 50.0% | T 50.0% | occurs 3.0% of the time
A:T, B:T, C:H, D:H - chances -  H 50.0% | T 50.0% | occurs 3.0% of the time
A:H, B:T, C:H, D:H - chances -  H 94.0% | T  6.0% | occurs 5.0% of the time
A:T, B:T, C:T, D:H - chances -  H  6.0% | T 94.0% | occurs 5.0% of the time
A:H, B:T, C:T, D:T - chances -  H  6.0% | T 94.0% | occurs 5.0% of the time
A:H, B:H, C:H, D:T - chances -  H 94.0% | T  6.0% | occurs 5.0% of the time
A:H, B:H, C:T, D:T - chances -  H 50.0% | T 50.0% | occurs 3.0% of the time
A:T, B:T, C:H, D:T - chances -  H  6.0% | T 94.0% | occurs 5.0% of the time
A:H, B:H, C:T, D:H - chances -  H 94.0% | T  6.0% | occurs 5.0% of the time
A:T, B:H, C:T, D:H - chances -  H 50.0% | T 50.0% | occurs 3.0% of the time
A:H, B:T, C:T, D:H - chances -  H 50.0% | T 50.0% | occurs 3.0% of the time
A:T, B:H, C:H, D:T - chances -  H 50.0% | T 50.0% | occurs 3.0% of the time

Our accuracy: 90.0%
```

And this continues, on and on, forever (as long as we have enough friends). If our number `N` of friends is odd, our chances of guessing correctly don’t improve when we move to `N+1` friends.

Is there a name for this?
-------------------------

As far as I can tell, there’s no name for this weird little phenomenon. But it *does* appear, implicitly, in voting literature.

[Condorcet’s jury theorem](https://en.wikipedia.org/wiki/Condorcet%27s_jury_theorem) is a famous theorem in political science. It states:

* If you have a group of voters of size `N`
* …and they all vote, independently, on an issue with a correct answer
* …and each voter votes the “right” way with probability `P`
* …and we make whatever decision the majority of the voters vote for
* …then if `P > 50%`, the chance that we make the right decision approaches 100% as we add more voters

Sounds a fair bit like our coin flipping problem. Here’s a simplifying assumption that Wikipedia makes when proving the theorem:

Hah! The proof explicitly recognizes (and dodges) the even-voter case precisely because that voter doesn’t add any information.

Why did I write this?
---------------------

I stumbled upon this result while writing a simulation for a more complex problem. I was *so* surprised at the simulation results that I assumed that I had a bug in my code. And when I walked through the math by hand I was absolutely delighted.

I suspect some of the surprise for me was because I typically encounter problems like these in the context of betting, not voting. If we’re *betting* on coin flips, we’re certainly excited to bet more if Alice and Bob agree than if we’re just listening to Alice.

But voting is a different beast; our outcome is binary. There’s no way to harvest the additional [EV](https://en.wikipedia.org/wiki/Expected_value) from the increased confidence Bob sometimes gives us.

By the way - I encountered this problem while working with a friend at [The Recurse Center](https://www.recurse.com/scout/click?t=4d29374c1894b0c33520021a254e0591) (a writers retreat for programmers). It’s a great place to get nerd sniped by silly math problems; If you enjoyed this blog consider [applying](https://www.recurse.com/apply)!

Anyway. I hope this delights you like it did me.