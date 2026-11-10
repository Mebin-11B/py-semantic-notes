---
title: "Mathematicians still don't know the fastest way to multiply numbers"
url: https://www.scientificamerican.com/article/mathematicians-still-dont-know-the-fastest-way-to-multiply-numbers/
clipped: 2026-08-31 12:22:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Mathematicians still don't know the fastest way to multiply numbers](https://www.scientificamerican.com/article/mathematicians-still-dont-know-the-fastest-way-to-multiply-numbers/)

## Digest Summary
- The traditional school algorithm multiplies two n‑digit numbers with O(n²) single‑digit multiplications; its work grows quadratically with digit length.  
- In 1960, Anatoly Karatsuba disproved the conjectured O(n²) lower bound by showing that three multiplications plus additions suffice for two halves of the numbers, yielding a recursive method with running time O(n¹·⁵⁸⁵). For example, multiplying two 1 000‑digit numbers drops from ~1 000 000 to < 57 000 elementary multiplications.  
- Modern libraries (e.g., Python’s big‑int implementation) switch from the grade‑school method to Karatsuba once operands exceed ≈630 decimal digits (≈70 base‑2³⁰ digits).  
- The quest for faster multiplication continued, culminating in 2019 with Harvey and van der Hoeven’s algorithm running in O(n log n) time, theoretically just above linear. Its advantage appears only for astronomically large inputs, classifying it as a “galactic algorithm.”  
- Theoretical computer scientists now regard O(n log n) as the likely optimal asymptotic bound, though a formal proof remains open.

---

## Full Article

[New Issue: Orbital Catastrophe Ahead? Read Now](https://www.scientificamerican.com/issue/sa/2026/09-01/)

July 13, 2026

6 min read[Add Us On GoogleAdd SciAm](https://www.google.com/preferences/source?q=scientificamerican.com)

# 

Mathematicians still don’t know the fastest way to multiply numbers

A 23-year-old student overturned an ancient conjecture about one of math’s simplest operations

By [Jack Murtagh](https://www.scientificamerican.com/author/jack-murtagh/) edited by [Jeanna Bryner](https://www.scientificamerican.com/author/jeanna-bryner/) 

Justin Lewis/Getty ImagesLove math? Sign up for our weekly newsletter Proof PositiveEnter your emailI agree my information will be processed in accordance with the Scientific American and Springer Nature Limited [Privacy Policy](https://www.scientificamerican.com/page/privacy-policy/). We leverage third party services to both verify and deliver email. By providing your email address, you also consent to having the email address shared with third parties for those purposes.Sign Up

Elementary school students might memorize their times tables for single-digit numbers, but memorization won’t cut it when the teacher asks for three-digit multiplication. This requires an algorithm: students are taught to stack one number atop another and multiply each digit of the bottom number by each digit of the top one. For millennia, mathematicians believed this to be the fastest multiplication method, until a 23-year-old made a shocking discovery in 1960, which led to a mystery that remains unsolved to this day.

This mystery is critical to anyone who partakes in the digital world because multiplication is a foundational operation for computers. [Encryption](https://www.scientificamerican.com/article/how-two-mathematicians-solved-a-cryptography-mystery/), robotics, [artificial intelligence](https://www.scientificamerican.com/artificial-intelligence/), audio processing and pretty much everything else we task [silicon chips](https://www.scientificamerican.com/article/how-human-neurons-on-a-chip-learned-to-play-doom/) with involves multiplication, sometimes of huge numbers many times over. At this scale, even a simple operation becomes a bottleneck, and any extra efficiency has global economic consequences.

To understand the nature of that bottleneck, observe how the grade-school algorithm handles growth. When you multiply two two-digit numbers, you perform four single-digit multiplications. If you bump that up to a three-digit pair of numbers, you do nine single-digit multiplications. The workload scales with the square of the number of digits (n2, where n is the number of digits in the numbers being multiplied). When analyzing an algorithm like this, computer scientists don’t measure speed in seconds, because that depends on the hardware. Instead they count the computational steps. They also ignore minor bookkeeping details, such as the time it takes to carry a one when multiplying. When numbers get large enough, those lower-level operations cease to matter, entirely eclipsed by the more intensive operations involved. Computer scientists denote the number of steps using what’s called Big O notation: the grade-school algorithm, for example, takes O(n2) steps, which is read as “order n squared.” Broadly speaking, if the numbers are twice as long, the algorithm takes four times as much computational work to execute. If the numbers are a thousand times as long, it takes a million (1,000 squared) times as much work.

## On supporting science journalism

If you're enjoying this article, consider supporting our award-winning journalism by [subscribing](https://www.scientificamerican.com/getsciam/). By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.

Since antiquity, mathematicians have suspected that O(n2) was an inherent speed limit for multiplication. The celebrated Soviet math professor Andrey Kolmogorov posed the O(n2) speed limit as a formal conjecture and mentioned it during a 1960 seminar at Moscow State University. Whenever mathematicians propose a conjecture, they are planting a flag of sorts and waiting for others to either prove or disprove them. It took just a week for Anatoly Karatsuba, then a 23-year-old student in the audience, to return and prove Kolmogorov wrong. Kolmogorov was stunned. The result was [published in the prestigious Proceedings of the USSR Academy of Sciences](https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=dan&paperid=26729&option_lang=eng), but amusingly, Karatsuba didn’t write it. Kolmogorov wrote the formal proof himself and submitted it for publication with Karatsuba listed as the lead author. Karatsuba only found out about the paper when he received the reprints in the mail.

Karatsuba’s genius was realizing that you can trade expensive, time-consuming multiplications for cheap, fast additions. Adding two n-digit numbers takes only O(n) time because it entails a single sweep through the digits rather than a complete sweep through the top number for every digit of the bottom number, as in multiplication. To see how Karatsuba traded multiplication for addition, let’s look at a small example. The method would be overly complicated for such a simple problem, but it saves a meaningful amount of time when numbers get larger.

In this simple example, let’s calculate 12 × 34.

First, we split both numbers into their tens and ones digits. Assign a = 1 and b = 2 (for 12), and c = 3 and d = 4 (for 34). Algebraically, we can rewrite 12 × 34 as (10a + b) × (10c + d).

Expanding this gives 100(ac) + 10(ad + bc) + (bd).

To solve the equation in the traditional way, one must perform four distinct multiplications: ac = 3, ad = 4, bc = 6 and bd = 8, which is exactly what the grade-school stacking method entails. (Note that we don’t count the multiplications by 100 or by 10 because those only involve plopping zeroes at the ends of numbers.) Karatsuba noticed a brilliant algebraic trick. Once you compute the first and last terms, ac and bd, you can figure out that pesky middle term (ad + bc) with one more multiplication step rather than two. You don’t need to calculate ad and bc individually:

(ad + bc) = ((a + b) × (c + d)) – ac – bd,

Or with our concrete numbers:

((1 × 4) + (2 × 3)) = ((1 + 2) × (3 + 4)) – 3 – 8 = 10.

Pause to notice the weirdness in the equation above. It suggests that to multiply 12 × 34 quickly, you should add the 1 and the 2 in 12 and the 3 and the 4 in 34. This is hardly a natural thing to do. No wonder it took so long for someone to figure it out. It ends up reducing the workload, however: because we’ve already computed ac and bd, the right-hand side only contains one more multiplication, plus some additions and subtractions.

Returning to 100(ac) + 10(ad + bc) + (bd), we only need three multiplications rather than four. We compute ac and bd in the straightforward way and then use Karatsuba’s trick to compute (ad + bc) with a single multiplication. Plugging in ac = 3, bd = 8 and (ad + bc) = 10 gives our answer of 408.

We shaved one multiplication off the procedure. If that seems measly, Karatsuba has another insight in store. Say we’re multiplying bigger numbers: 1,234 × 5,678. We split them in half like we did before: a = 12, b = 34, c = 56 and d = 78, and we write the problem as (100a + b) × (100c + d) = 10,000(ac) + 100(ad + bc) + (bd).

We can solve this with three multiplications. Those multiplications, however, now involve two-digit numbers. Luckily, we know a way to multiply two-digit numbers with only three single-digit multiplications each! In total, a problem that would take 16 single-digit multiplications the traditional way now needs only nine. By recursively applying Karatsuba’s trick on large numbers, the savings compound. It splits the input numbers in half, then splits those halves in half, and so on, applying this four-for-three trade all the way down. The algorithm works out to have a running time of roughly O(n1.585), which is drastically faster than O(n2). For reference, multiplying a pair of thousand-digit numbers involves a million single-digit multiplications using the grade-school method but fewer than 57,000 using Karatsuba’s algorithm.

The 23-year-old’s efficiency is baked into software that runs every day. Because of its extra overhead (the additions, managing the repeated splitting and recombining of numbers, and so on) its advantages over the grade-school algorithm don’t kick in until numbers grow relatively big. [Python](https://www.scientificamerican.com/blog/guest-blog/programming-as-a-way-of-thinking/), for example, is a popular programming language that is famously smooth at handling integers of any size. If you peek into Python's underlying source code (search “Karatsuba” [here](https://github.com/python/cpython/blob/main/Objects/longobject.c)), you will see it relies on a hybrid approach. For modestly sized inputs, it uses the grade-school math, but once numbers reach around 630 decimal digits, it flips a switch and employs Karatsuba’s algorithm. That many digits might seem gargantuan by terrestrial standards, but computers deal with [much bigger](https://www.scientificamerican.com/article/new-prime-number-41-million-digits-long-breaks-math-records/). (Technical aside: On most modern machines [Python stores large numbers in base 230](https://github.com/python/cpython/blob/main/Include/cpython/longintrepr.h#L64-L71), so the linked Karatsuba cutoff of 70 digits in base 230 translates to roughly 630 decimal digits).

Karatsuba’s algorithm ignited a decades-long race to find the ultimate speed limit of multiplication. That pursuit culminated in 2019, when mathematicians David Harvey and Joris van der Hoeven [described an extremely sophisticated algorithm](https://annals.math.princeton.edu/2021/193-2/p04) that beat Karatsuba’s by more than any of the previous breakthroughs. The new algorithm runs in O(n × log n) time. Here log denotes the logarithm of n, which is a function that grows very slowly. It’s a staggering result. The function n × log n is just a little bit bigger than n itself. This means that calculating the product of two massive numbers requires only a little more time than adding them, or even reading them, would in the first place (it takes n computational steps to read all n digits of a number).

The triumph comes with a crucial caveat, though. Just as Karatsuba’s algorithm only outperforms the grade-school approach when numbers get reasonably large, the Harvey-van der Hoeven algorithm doesn’t pull ahead until the numbers become truly galactic. In computer science, a “[galactic algorithm](https://books.google.com/books?id=eLC9BAAAQBAJ&pg=PA109#v=onepage&q&f=false)” is a formal term for a method that is impressively efficient on sufficiently large numbers but will never be useful in practice because the numbers are so large.

Even with that asterisk, it was a watershed achievement. It secured the record for the fastest known multiplication method in principle and could pave the way for algorithms that run in O(n × log n) steps, not just in principle, but in practice. Today, theoretical computer scientists widely suspect that O(n × log n) is the fastest possible speed for multiplication, and formally proving it has become the holy grail for this niche field of mathematics. But as history reminds us, widespread consensus is not a mathematical proof. Conjectures about the speed limit of multiplication have been overturned before.

## It’s Time to Stand Up for Science

If you enjoyed this article, I’d like to ask for your support. Scientific American has served as an advocate for science and industry for 180 years, and right now may be the most critical moment in that two-century history.

SciAm always educates and delights me, and inspires a sense of awe for our vast, beautiful universe. I hope it does that for you, too.

If you [subscribe to Scientific American](https://www.scientificamerican.com/getsciam/), you help ensure that our coverage is centered on meaningful research and discovery; that we have the resources to report on the decisions that threaten labs across the U.S.; and that we support both budding and working scientists at a time when the value of science itself too often goes unrecognized.

In return, you get essential news, [captivating podcasts](https://www.scientificamerican.com/podcasts/), brilliant infographics, [can't-miss newsletters](https://www.scientificamerican.com/newsletters/), must-watch videos, [challenging games](https://www.scientificamerican.com/games/), and the science world's best writing and reporting. You can even [gift someone a subscription](https://www.scientificamerican.com/getsciam/gift/).

There has never been a more important time for us to stand up and show why science matters. I hope you’ll support us in that mission.

Thank you,

Jeanna Bryner, Editor in Chief, Scientific American[Subscribe](https://www.scientificamerican.com/getsciam/?utm_source=site&utm_medium=display&utm_term=eic_stand_up_for_science)

Subscribe to Scientific American to learn and share the most exciting discoveries, innovations and ideas shaping our world today.[Subscription Plans](https://www.scientificamerican.com/getsciam/)[Give a Gift Subscription](https://www.scientificamerican.com/getsciam/gift/)
