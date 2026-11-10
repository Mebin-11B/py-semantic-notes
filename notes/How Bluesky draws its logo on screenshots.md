---
title: "How Bluesky draws its logo on screenshots"
url: https://timmarinin.net/2026/bluesky-screenshots/
clipped: 2026-08-31 12:22:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How Bluesky draws its logo on screenshots](https://timmarinin.net/2026/bluesky-screenshots/)

## Digest Summary
The post explains how the Bluesky iOS app reveals its logo only in screenshots. The implementation resides in a file named GrowthHack.tsx (added Jan 2026) and relies on the expo‑privacy‑sensitive package. That package creates a UITextField with isSecureTextEntry set to true, then renders the UI element (the “Follow” button) into the field’s layer. When iOS captures a screenshot, it blanks layers belonging to secure text fields, causing the button to disappear and exposing the underlying logo that is always present in the view hierarchy. For non‑iOS platforms the content is rendered normally without masking. The behavior does not trigger when switching apps because iOS takes a snapshot before the gesture, before the secure‑text field can blank its layer, leaving the static snapshot unchanged. Similar techniques are used by Telegram’s secret chats and Signal, leveraging the privacy‑oriented API rather than a bug, and have not been patched by Apple.

---

## Full Article

# How Bluesky draws its logo on screenshots

	
	

	
		

Sometimes I take a screenshot of a post I like, either to send it to friends/meme channel or to save a “durable” copy. Like this one (I’ve cropped out the rest of the interface):

  
  [Original](https://bsky.app/profile/eroston.bsky.social/post/3mt5gs2fdyk2l), if you want to reskeet it

I noticed the Bluesky logo in the right corner and thought that it was weird that the logo doesn’t bother me when I use the app. Then I looked at the post in the app again—logo wasn’t there, replaced by the “Follow” button.

I remembered that a few apps hide their logo where the iPhone notch is, so that it doesn’t stick out, unless you take a screenshot. But here the logo is placed in the open, so how do they do it?

I tried to take another screenshot, this time mid-switching to the other app:

  
  The “Follow” button is visible when I take the screenshot mid-switch.

Did they somehow set up a listener for two buttons I’m pressing to take a screenshot and do a switcheroo at the last moment? I’m not an iOS developer, so I’m not sure what’s possible and what is not over there.

At this point I was mildly intrigued. Thankfully, I remembered that Bluesky app is open source (or at least the code is available to look at).

The answer was in the file literally called [GrowthHack.tsx](https://github.com/bluesky-social/social-app/blob/main/src/screens/PostThread/components/GrowthHack.tsx) , introduced in January 2026 by [mozzius](https://github.com/mozzius). But it merely used a dependency, so to understand I looked into package [expo-privacy-sensitive](https://github.com/mozzius/expo-privacy-sensitive), also by them.

The package creates  `UITextField`  with  `isSecureTextEntry`  property set to true and renders the actual content (the button) into that field’s   `.layer` . When I take the screenshot, iOS hides this UITextField by blanking the layer, allowing the Bluesky logo to flutter its wings through (it was here the whooole time). For other platforms it simply renders content as-is, without masking.

Why doesn’t it work when I switch between the apps? I suppose that iOS takes a snapshot itself at the start of the gesture (without triggering blanking), and when I do a screenshot, there is no live UITextField instance to react to that, only the inert snapshot. But once again, I’m not an iOS developer.

Nifty trick or an abuse of API meant for privacy? The people in [the thread adding the behavior](https://github.com/bluesky-social/social-app/pull/9637) mostly didn’t like it, before the thread got locked. I think it’s cute.

I googled a bit, and the trick is well-known. Telegram implemented [similar thing for its "secret" chats](https://github.com/TelegramMessenger/Telegram-iOS/blob/master/submodules/UIKitRuntimeUtils/Source/UIKitRuntimeUtils/UIKitUtils.m#L299-L328), as did [Signal](https://github.com/signalapp/Signal-iOS/blob/a9f55ea599561e6d3bcee87d4f1540a7191b28dc/Signal/util/ScreenshotBlocking.swift), so I don’t expect it to be patched by Apple any time soon.

Comments on [Lobste.rs](https://lobste.rs/s/05ocit/how_bluesky_draws_its_logo_on_screenshots), [Hacker News](https://news.ycombinator.com/item?id=49338459).
Also: [Daring Fireball](https://daringfireball.net/linked/2026/08/20/bluesky-threads-sneak-logo-into-screenshots).

	

	

	
	
		
		
			
			Published
			at Sunday, 16 August 2026 
			by [mt](https://timmarinin.net)
