---
title: "If you're a button, you have one job"
url: https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/
clipped: 2026-08-31 12:22:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [If you're a button, you have one job](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/)

## Digest Summary
The essay compares how iPhone and Nothing Phone/Android handle rapid taps on a photo‑rotation button. On iOS, taps are buffered: each tap is queued, so eight quick 90° taps result in two full rotations and the image returns to its original orientation. On the Nothing Phone, the UI provides haptic and auditory feedback for the first tap but then ignores subsequent taps while an animation is in progress, preventing the “no‑op” result. The author argues this difference matters for accessibility and situational disability, noting that all users can encounter moments when UI responsiveness is critical (e.g., rotating many landscape‑oriented photos). They advocate designs that never force users to wait for an animation to finish—either by buffering input or by allowing the animation to be interrupted or accelerated. This principle supports both casual and power‑user scenarios and improves predictability for diverse users.

---

## Full Article

One thing I was (and still am) worried about when it comes to my [recent big interactive essay](https://aresluna.org/show-your-hands-honor/) is that by showing all these classic desktop examples, the whole thing might appear old-fashioned, relevant only to a bygone era.

Yet, the challenges it shows are universal. Hereâs something I just spotted. This is how you rotate an image on an iPhone and on a Nothing Phone:

        
            
            
            
            
            
          

        
            
            
            
            
            
          

Itâs a pretty standard control â tap once to rotate counterclockwise, tap a second time to do it again, etc. â with a helpful transition of the photoâs orientation so that you donât lose yours.

Now, Iâm going to exaggerate the problem a bit and tap 90-degree rotation quickly eight times. Eight times should result in what engineers call a âno opâ â the image rotating twice in full, and ending up where it started. That indeed happens on the iPhone:

        
            
            
            
            
            
          

But itâs a different story on the Nothing Phone/​Android:

        
            
            
            
            
            
          

iPhone will remember and buffer the taps, so that the second, pending rotation will happen as soon as the first is done. The Nothing Phone button gives you a tap confirmation via both haptics and sound, and then ignores the tap if a previous rotation is still animating.

Why does it matter? 

I often keep thinking about the framework of [situational disability](https://accessibility.education.gov.uk/training/accessibility-inclusion/page-10), stating that disability is not just something that happens to a few people and no one else. No, pretty much everyone will occasionally encounter a situation that will make them effectively disabled, and this is why accessibility matters much more than many of us assume:

        
        
        
        
        
      

I think similarly about casual and non-casual use. Photo-taking on phones is typically casual. Phone cameras are typically very good at detecting the photo orientation â but get confused when youâre pointing down. Now, as an example, if you had to take photos of a bunch of landscape documents, you might end up having to rotate dozens of photos, one by one. And it would be so much more predictable and pleasant if you could just tap the button three times at any pace you wanted without thinking, without paying attention, without getting your UI blocked by an animation that no longer helps you.

This is, I suppose, âsituational power user-ness.â Given a long enough timeframe â or, in this case, a large enough population â even a casual interface like phone photo editing (or, [GarageBand](https://unsung.aresluna.org/the-surprising-richness-of-garageband/)) will meet someone who will have no choice but to treat it more seriously and expect more from it.

By the way, buffering the taps is not the only answer. You can also stop/​accelerate the animation after an interrupting tap, and it seems the iPhone does that as well. But the rule is: never force the user to wait for the animation to finish.
  [Jul 4, 2026](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/if-youre-a-button-you-have-one-job/)
- [android 3](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/tags/android/) 
- [flow 56](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/tags/flow/) 
- [ios 14](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/tags/ios/) 
- [popular 16](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/tags/popular/) 
- [touch 22](https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/tags/touch/)
