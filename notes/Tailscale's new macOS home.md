---
title: "Tailscale's new macOS home"
url: https://tailscale.com/blog/macos-notch-escape
clipped: 2026-06-17 01:23:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tailscale's new macOS home](https://tailscale.com/blog/macos-notch-escape)

## Digest Summary
Tailscale’s original macOS client combined a command‑line tool with a menu‑bar status item. On MacBook models with a display notch (starting 2021), the status‑item icon can be rendered within the notch’s invisible zone when other menu‑bar icons fill the available space, making the icon inaccessible. macOS provides no native overflow or repositioning for third‑party items; Apple’s indirect work‑arounds (e.g., moving system icons to Control Center) and third‑party managers such as Bartender are the only options. Tailscale addressed the problem by observing the window’s occlusionState via NSWindow.didChangeOcclusionStateNotification; when the icon is not visible, the app displays a pop‑up warning. This solution is imperfect and may trigger on lid or monitor changes. A more robust fix arrived with the windowed macOS client (enabled by default in version 1.96.2), which runs alongside the menu‑bar app and offers:

- searchable device list with status,
- ping, IP copy, and Taildrop file transfer,
- exit‑node selection with latency‑based recommendation,
- Dock‑icon error indicator,
- optional “mini player” mode and onboarding tour.

The windowed UI reduces reliance on the notch‑prone menu‑bar icon.

## Discussion Summary
Users express strong frustration with macOS’s notch obscuring menu‑bar icons, citing lost sales, support headaches, and the lack of a native overflow solution, while adopting manual defaults tweaks or third‑party managers despite recent instability. Opinions about Apple’s design choices are uniformly critical, urging a redesign or overflow dropdown. Tailscale receives mixed feedback: many praise its ease of setup and reliability, yet complain about UI changes, SSO complications, occasional packet loss, and the need for CLI alternatives. Overall, there is a clear demand for better system UI handling and more stable, user‑friendly networking tools.

---

## Full Article

Tailscale should feel nearly invisible when it's connecting you and all your devices together. But on some MacBooks, for a time, it could be a little too invisible. We have two fixes for it: one small and slightly quirky, and another really useful one, available now on macOS.

The small, quirky fix might soon become a thing of the past for the vast majority of Tailscale users on Macs. I wanted to document it here: to help other developers, to mark this moment in time, and quietly crow about our **windowed macOS interface now being generally available**.

So here's the issue we had with Tailscale's icon slipping into darkness, its little work-around, and then our greater solution.

At its debut on macOS, Tailscale was a command-line tool and a menu bar utility. Some MacBooks, starting with [2021 MacBook Pro models](https://www.theverge.com/2021/10/19/22734676/apple-macbook-pro-notch-botch-face-id-missing-feature-design), have a notch in the top-middle of their display. And depending on how many other apps with menu bar icons are running, the Tailscale app’s icon can be hidden inside that notch.

Apple, a company that traditionally favors simple functionality over dense settings, does not offer users, or developers, a path out of the darkness. If there are more menu bar icons then there is space to the right side of the notch, the menu bar items simply disappear into the notch-y ether. If you don’t see it, you can’t click it. There is no notification to the user, no overflow section, no options to rearrange the menu bar items.

![a tight screenshot of the Tailscale menu bar app, right next to a simulated notch on the gray top menu bar of a MacBook screen.](https://cdn.sanity.io/images/w77i7m8x/production/be2e4419f4669282a3b09ee31e6e32a9cc328d51-1576x886.png?w=3840&q=75&fit=clip&auto=format)

Author's rendition of the Tailscale menu bar applet, dangerously close to the inky depths.

As of this writing, Apple has some indirect work-arounds, like pushing more of its own system icons into [a revamped Control Center](https://9to5mac.com/2025/06/28/new-macos-tahoe-feature-solves-common-complaint), and offering a somewhat inelegant [“Scale to fit below camera” option](https://www.macrumors.com/how-to/scale-mac-app-menu-bar-for-macbook-pro-notch). Third-party menu-bar-managing apps like [ICE](https://icemenubar.app/) and [Bartender](https://www.macbartender.com/) can help, but they add complications and overhead.

“We don’t have any control over where things get rendered in the menu bar,” said one Tailscale engineer, who asked to go nameless so as to share their honest opinion. “You just say, ‘I want to be a menu bar app.’ They shove it up there, and that’s it, you end up where you end up.”

Given this there-or-not-there behavior, Tailscale developers received a number of bug reports from users when, after the notched MacBooks' debut, their Tailscale icons fell into the middle-screen distance. "They were like, 'Actually, I can't find my Tailscale. It's gone. It didn't start," the engineer said. "We're like, 'No, it's there, it's just hiding behind the notch.' But we kind of got sick of that."

Mac menu bar icons may not know they are trapped inside the no-pixel phantom zone, but they can report that something is blocking them. Using data from `occlusionState`, the Tailscale app can see that its icon is in mid-bar limbo.

And while it cannot move, it can speak. Specifically, a pop-up message can say:

![Mac pop-up dialog, reading: Sneaky! The Tailscale icon is hiding behind the notch [new line] The Tailscale icon is hidden due to limited space in the menu bar. To see the Tailscale menu, please rearrange or remove some of the other icons.](https://cdn.sanity.io/images/w77i7m8x/production/5bddebdfce4d155ad72ebc3bba3e316d2036fb50-660x764.png?w=1920&q=75&fit=clip&auto=format)

This affable warning is not perfect, by any means. The notch warning can be inadvertently triggered by other display quirks, like opening and closing the MacBook lid, moving between monitors, or some combination of the two. But it helped triage the "Where are my Tailscale settings?" issue for a while.

Apple could certainly make some changes to prevent this being an issue at all. The system could prevent menu bar icons from rendering in the notch area at all. An overflow mechanism could stack the icons that would otherwise drop into a negative notch zone. Or developers could be given more information and tools about icons' notch-itive states.

In the meantime, here’s a look at the Swift code that let our app know it should chirp a bit when hidden. It should be unnecessary with the new windowed app—unless you enable the “Hide Dock icon” option in the windowed client options, in which case it might still call out its hidden nature.

```
self.visibilityObserver = NotificationCenter.default.addObserver(
    forName: NSWindow.didChangeOcclusionStateNotification,
    object: statusItemButton.window,
    queue: .main
) { [weak self] _ in
    guard let self, statusItem.isVisible else { return }
    isIconOccluded = statusItem.button?.window?.occlusionState.contains(.visible) == false
}
```

As we noted at [its September beta release](https://tailscale.com/blog/windowed-macos-ui-beta), a windowed version of Tailscale’s macOS app doesn’t replace the menu bar app, but runs alongside it. It can be pulled up from the Dock or a Spotlight search, and makes a lot of Tailscale data and features more accessible.

![A screenshot showing Tailscale's macOS windowed UI, with a device selected (iPhone) and details of that device on the right. A Taildrop box offers drag-and-drop file sending.](https://cdn.sanity.io/images/w77i7m8x/production/3fb7d7dbe647e4f1d45e8e00c476af850424d91c-2600x1800.png?w=3840&q=75&fit=clip&auto=format)

The windowed interface, enabled by default starting with **version 1.96.2** of our macOS client, offers:

* A searchable list of tailnet devices and their connection status
* Easily ping, copy IP addresses, and send files through [Taildrop](https://tailscale.com/kb/1106/taildrop) to devices
* Easy access to exit nodes, searchable and with one recommended [based on latency, performance, and location](https://tailscale.com/kb/1392/auto-exit-nodes#how-it-works)
* A red dot on the Dock icon to note critical errors
* A “mini player” that shrinks Tailscale down to the bare minimum
* A product tour of all these things upon installing/updating

Let us know [what you think of the new interface](https://tailscale.typeform.com/to/TNNlpL58) so we can make it better. We’re working on a comparable UI for Windows devices. And we’re always looking for ways to bring a little bit of functional whimsy to our software.