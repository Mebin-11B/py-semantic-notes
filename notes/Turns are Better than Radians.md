---
title: "Turns are Better than Radians"
url: https://www.computerenhance.com/p/turns-are-better-than-radians
clipped: 2026-08-31 12:23:02
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Turns are Better than Radians](https://www.computerenhance.com/p/turns-are-better-than-radians)

## Digest Summary
The article argues that angles should be expressed in “turns” (full circle = 1) rather than radians, eliminating the need for π or τ constants in most code. In typical applications, a normalized value h ∈ [0, 1] is multiplied by τ before calling sin, yet the sin implementation immediately multiplies by 4/π to convert back to radians, wasting a multiplication and re‑introducing π. Using turns removes this redundant conversion, saves a multiply, and yields exact representations for common angles (e.g., 0.25 turn = 90°) that cannot be represented exactly in radians. Existing libraries already contain turn‑based interfaces: CUDA’s sincospi operates on half‑turns (0 → 2). Switching requires adjusting the constant in the sin/cos wrappers or providing thin “thunk” functions that convert legacy radian calls to turn‑based ones. The change simplifies code, improves precision for typical angles, and can be applied with minimal modifications across a codebase.

---

## Full Article

# [Computer, Enhance!](https://www.computerenhance.com/)

SubscribeSign in

# Turns are Better than Radians

### Switching away from radians makes code simpler, faster, and more precise.

[Casey Muratori](https://substack.com/@cmuratori)Sep 26, 2022152471Share

Some time ago, much effort was expended to convince people to replace approximations of “pi” (3.14159…) with approximations of “tau” (6. 28318…). The idea, according to numerous blog posts and [YouTube videos](https://www.youtube.com/results?search_query=tau+pi), was that common formulas become simpler, and it’s easier to work with a constant describing an entire circle instead of half a circle.

Generally, I agree. While it’s a minor point, it’s worth making. Most code does get slightly better if you replace pi with tau. 

However, in all the fanfare, a far more impactful opportunity was overlooked. Instead of replacing pi with tau, most of the time pi can be removed entirely.

## Here’s how that works.

First, consider the common case for pi and tau in code: converting things to and from radians for calls to trigonometric functions. If you’ve ever used these constants, the vast majority of what you wrote probably did something like this: ` `y = center.y + (center.y * Math::sin(h * Math_TAU) * s) - 
    (cursor->get_height() / 2);` ` 

That’s not me constructing an example, that’s me randomly opening the source code for the [Godot Engine](https://godotengine.org/) on github and searching for “tau”. [The piece of code above](https://github.com/godotengine/godot/blob/61c0cb712d854881def4f266ca419de8c6fc6f37/scene/gui/color_picker.cpp#L786), and dozens of similar uses, is what comes up.

There is nothing special here about Godot. If you opened any random game engine codebase, you could do the exact same search and see the exact same kind of usage.

Notice what is going on here: the programmer has a value h which is already periodic on the range 0 to 1, but they multiply by tau because they need to call sin.

This may seem very sensible if that’s as far as you look. But what about the implementation of sin?

There are many implementations of sin, but no matter which one you look at, near the entry point of the function you’ll see something like this: ` `_PS256_CONST(cephes_FOPI, 1.27323954473516);
...
y = _mm256_mul_ps(x, *(v8sf*)_ps256_cephes_FOPI);` ` 

Again, not me making up an example - that’s from [this commonly referenced AVX2 implementation of sin](https://github.com/reyoung/avx_mathfun/blob/be617bbcf66993c4f7e7d267ed9926cd8e7d4f02/avx_mathfun.h#L346). It’s not unusual or weird - pretty much every fast trig library is going to do something very similar.

What does this line do? It multiplies the input by the constant 1.27323954473516. 

Which just so happens to be 4/pi.

So the calling code is doing this: ` `sin(h * 2 * pi)` ` 

but the library code immediately does this: ` `y = (4 / pi) * x` ` 

which means the calling code is multiplying by a factor of pi just so the library code can immediately divide it back out again. It’s literally a conversion to radians and back for no reason. If both programmers had just agreed not to use radians, and instead used the original [0, 1] domain that h was already on, both their jobs get simpler: the caller saves a multiply, while the library gets a simpler-to-understand, exact constant.

And the “exact” part is actually quite interesting. Not only do you pay for an extra multiply when you spuriously convert to radians, but it’s also worth noting that all common radian angles besides 0 are difficult to represent. Want to store 90 degrees in radians? No matter how many bits you use, it will never be exact.

90 degrees on [0, 1], however, is just 0.25 - a bit pattern that doesn’t even require any bits of mantissa at all! 0.5? Same! 0.75? Just one bit of mantissa to represent exactly.

So the [0, 1] range is not only more computationally efficient than radians, it is also more compact and precise when representing typical values that frequently occur in practical use.

## Math doesn’t require radians.

I can understand why some people would be worried about making this switch. Even if you believe me that all user-side code multiplies by pi or tau, and all library-side code divides it back out, you still may have that sinking “math class feeling” that you’d be doing something wrong if you stopped using radians.

But math never decreed that sine and cosine have to take radian arguments!

The idea of parameterizing a circle from zero to one instead of from zero to tau is not a random idea I made up for this blog post. It’s actually a legitimate, existing mathematical construct, and it even has a name: it’s called a [turn](https://en.wikipedia.org/wiki/Turn_(angle)#:~:text=A%20turn%20is%20a%20unit,rot.)%20or%20full%20circle.).

In turns, 0 is 0 degrees, 0.5 is 180 degrees, 1 is 360 degrees, 2 is 720 degrees, and so on. It’s exactly what we wanted.

So if you are worried that your math teacher will get mad at you, there is no cause for concern. Just tell them that you considered the matter carefully, and decided that parameterizing your angles in turns instead of in radians was the most efficient method for the problem at hand!

## Making the switch is easy.

If you wrote your own math library, or you copied someone else’s into your project, hopefully it is quite clear how you can switch away from radians and eliminate pi and tau from your codebase. All you have to do is take your sin and cos functions and make them take turns instead of radians, which usually involves nothing but a quick adjustment to a single constant.

If you want to support legacy code, pick a different name for the new turn-based trig functions. Then, for legacy code, you can still support the old radian-based sin and cos by making those routines thunk through to the new routines, doing the divide-by-tau along the way.

It’s very simple - just a few lines of code to make the switch.

However, although I find turns to be the most convenient reparameterization, it’s not the only alternative. Especially if you don’t roll your own math routines (and perhaps even if you do), you may instead want to consider using half turns, where a full circle is [0, 2]. It’s a bit more confusing, but…

## It already exists in some libraries!

It turns out (pun intended!) that if you go looking for it, in some math libraries you will already find sin and cos functions parameterized on half-turns instead of radians. For example, [the CUDA sincospi intrinsic](https://docs.nvidia.com/cuda/cuda-math-api/group__CUDA__MATH__SINGLE.html#group__CUDA__MATH__SINGLE_1gab8978300988c385e0aa4b6cba44225e) computes the sine and cosine of the input multiplied by pi, which is a half-turn.

This is great. If you’re targeting a platform with sincospi already available, you can stop using pi and tau constants in your code right now without touching your libraries at all. Just start calling sincospi with half-turns instead of sin and cos with radians, and you’re good to go.

## The less tau and pi, the better.

Having now managed entire codebases where I stopped using radians, I can safely say I never miss them. All the superfluous tau’s and pi’s disappear, and everything reads more clearly. 

The same logic for modifying sin and cos applies to the rest of the standard trig functions as well, so you can eliminate radians everywhere if you choose. Libraries almost always convert away from radians internally anyway, and then convert back to radians on the way out, so switching to turns or half-turns everywhere is usually just a matter of deleting code and not much else.

Thanks for reading Computer, Enhance! Subscribe for free to receive new posts.Subscribe152471SharePreviousNext

#### 47 Comments

[Eduardo Vasquez](https://substack.com/profile/105459323-eduardo-vasquez?utm_source=substack-feed-item)[Sep 26, 2022](https://www.computerenhance.com/p/turns-are-better-than-radians/comment/9307577)Liked by Casey Muratori

Just keep in mind,  though, that all those formulas of derivatives and primitives of trig functions in standard calculus books assume that arguments are expressed in radians. Say, the derivative of sin x w.r.t. x  is cos x --- that is only true if x is in radians. Otherwise, you would get an extra factor, due to the chain rule. So, if the mathematical expression you are working with happens to come, somehow, from derivatives or primitives, chances are that you will miss those extra factors, by simply deleting every ocurrence of pi or tau.ReplyShare[10 replies by Casey Muratori and others](https://www.computerenhance.com/p/turns-are-better-than-radians/comment/9307577)[Greg](https://substack.com/profile/105447034-greg?utm_source=substack-feed-item)[Sep 26, 2022](https://www.computerenhance.com/p/turns-are-better-than-radians/comment/9304994)

pico-8 does it this way: [https://pico-8.fandom.com/wiki/Cos](https://pico-8.fandom.com/wiki/Cos)ReplyShare[2 replies by Casey Muratori and others](https://www.computerenhance.com/p/turns-are-better-than-radians/comment/9304994)[45 more comments...](https://www.computerenhance.com/p/turns-are-better-than-radians/comments)TopLatestDiscussions

No posts

### Ready for more?

Subscribe© 2026 Casey Muratori · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)[Substack](https://substack.com) is the home for great culture
