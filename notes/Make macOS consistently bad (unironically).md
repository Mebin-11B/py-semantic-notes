---
title: "Make macOS consistently bad (unironically)"
url: https://lr0.org/blog/p/macos/
clipped: 2026-06-17 01:26:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Make macOS consistently bad (unironically)](https://lr0.org/blog/p/macos/)

## Digest Summary
The post discusses the UI inconsistency of rounded window corners in macOS 26 and proposes a programmatic fix that enforces a uniform corner radius for third‑party GUI applications. The author supplies Objective‑C source that swizzles private NSThemeFrame methods (_cornerRadius, _getCachedWindowCornerRadius, _topCornerSize, _bottomCornerSize) to return a constant radius of 23.0 points. The code is compiled as a universal dynamic library (arm64e + x86_64) with clang, signed, and placed in /usr/local/lib. A launch‑agent plist (com.local.dyld‑inject.plist) sets the environment variable DYLD_INSERT_LIBRARIES to load the library at login via launchctl. Because the tweak modifies system‑level libraries, System Integrity Protection must be disabled, which reduces security. The author frames the change as a way to make macOS 26 “consistently bad” rather than having mixed corner radii across apps, and includes the full compile command, file placement steps, and plist XML needed to activate the tweak.

## Discussion Summary
Comments focus on recent macOS UI changes, especially inconsistent window corner rounding and new tab designs, which many describe as visually unappealing and unnecessary. Performance complaints cite high CPU usage by WindowServer and sluggish dialogs, prompting users to apply tweaks or third‑party tools. Opinions diverge: some dismiss the issues as minor or adapt by using tiling managers, while others prefer alternative operating systems for stability and customization. Discussions also touch on security misunderstandings about System Integrity Protection and broader dissatisfaction with forced design decisions, though a few users remain neutral or indifferent.

---

## Full Article

Make macOS 26 consistently bad (unironically)
=============================================

Alongside the various bugs you get, one of the issues of upgrading to MacOS 26 is that it has one of the most notorious inconsistency issues in window corners. I'm not sure what exactly pushes product designers to like the excessive roundness1. One of the ugliest roundness examples I've ever seen is the current one in the YouTube UI design. I believe that UI design is the most influencive2. that's to say, contagious form inwards field ever since designers just try to follow whatever big companies do (in fact I see this a lot in my work, when two designers are having an argument, one of them would resolve it to, let's see how Apple draw that button), which means that we are probably going to see this ugly effect elsewhere very soon.

![../i/2026-03-27_19-51-20_screenshot.png](https://lr0.org/i/2026-03-27_19-51-20_screenshot.png "../i/2026-03-27_19-51-20_screenshot.png") Anyway, recently I had to upgrade to [macOS](https://lr0.org/blog/t/macos/#r5k8p3q6m2x9) 26. And I found the edges ugly, like everyone else did. However, what's even uglier, is the inconsistency. Many people try to resolve this by disabling MacOS system integrity protection, which results in making them possibly vulnerable3. Arguable, since you just lose security over /root, which is not a big deal if someone already gained access to your machine, at least for me. Edit: I learnt that this is not the case from comments, however, I still believe that if you're already pwned, SIP can't do much there.. The reason why you need to disable SIP, is that to edit the dynamic libraries that system apps like Safari (which has crazy bad corners) use, you need to edit system libraries that exist the root. To me though, I don't find the corners so bad, but I find the inconsistency very annoying. So I think a better solution to this is; instead of making everything roundless, make everything more rounded, which requires you to edit only user apps (i.e. no SIP disabling needed). I forked a solution that makes things roundless to modify it to have my approach. It's simply as follows:

```
#import <AppKit/AppKit.h>
#import <objc/runtime.h>

static CGFloat kDesiredCornerRadius = 23.0;

static double swizzled_cornerRadius(id self, SEL _cmd) {
    return kDesiredCornerRadius;
}

static double swizzled_getCachedCornerRadius(id self, SEL _cmd) {
    return kDesiredCornerRadius;
}

static CGSize swizzled_topCornerSize(id self, SEL _cmd) {
    return CGSizeMake(kDesiredCornerRadius, kDesiredCornerRadius);
}

static CGSize swizzled_bottomCornerSize(id self, SEL _cmd) {
    return CGSizeMake(kDesiredCornerRadius, kDesiredCornerRadius);
}

__attribute__((constructor))
static void init(void) {
    // Only apply to third-party GUI apps; skip CLI tools, daemons, and Apple system apps
    NSString *bid = [[NSBundle mainBundle] bundleIdentifier];
    if (!bid || [bid hasPrefix:@"com.apple."]) return;

    Class cls = NSClassFromString(@"NSThemeFrame");
    if (!cls) return;

    Method m1 = class_getInstanceMethod(cls, @selector(_cornerRadius));
    if (m1) method_setImplementation(m1, (IMP)swizzled_cornerRadius);

    Method m2 = class_getInstanceMethod(cls, @selector(_getCachedWindowCornerRadius));
    if (m2) method_setImplementation(m2, (IMP)swizzled_getCachedCornerRadius);

    Method m3 = class_getInstanceMethod(cls, @selector(_topCornerSize));
    if (m3) method_setImplementation(m3, (IMP)swizzled_topCornerSize);

    Method m4 = class_getInstanceMethod(cls, @selector(_bottomCornerSize));
    if (m4) method_setImplementation(m4, (IMP)swizzled_bottomCornerSize);
}
```

Then compile, sign, and store:

```
clang -arch arm64e -arch x86_64 -dynamiclib -framework AppKit \
  -o SafariCornerTweak.dylib \
  SafariCornerTweak.m

sudo mkdir -p /usr/local/lib/
sudo cp SafariCornerTweak.dylib /usr/local/lib/
sudo codesign -f -s - /usr/local/lib/SafariCornerTweak.dylib
```

You can have this plist too to load it in once your computer loads:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.local.dyld-inject</string>
  <key>ProgramArguments</key>
  <array>
    <string>launchctl</string>
    <string>setenv</string>
    <string>DYLD_INSERT_LIBRARIES</string>
    <string>/usr/local/lib/SafariCornerTweak.dylib</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
```

Name it as `com.local.dyld-inject.plist`, and:

```
cp com.local.dyld-inject.plist ~/Library/LaunchAgents/com.local.dyld-inject.plist
```

Load it:

```
launchctl load ~/Library/LaunchAgents/com.local.dyld-inject.plist
```

Now at least everything is consistently bad. #[Programming](https://lr0.org/blog/t/programming/)

Footnotes
---------