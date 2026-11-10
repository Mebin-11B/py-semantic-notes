---
title: "RustDesk now supports true unattended remote access on Wayland"
url: https://rustdesk.com/blog/unattended-remote-access-wayland/
clipped: 2026-08-31 12:22:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [RustDesk now supports true unattended remote access on Wayland](https://rustdesk.com/blog/unattended-remote-access-wayland/)

## Digest Summary
RustDesk now offers true unattended remote access on Wayland, eliminating the need for a remote‑side user to approve each session. The feature supports multi‑monitor configurations and can connect from the login screen after a reboot. A preview build for x86_64 Debian/Ubuntu‑based systems is available for testing. Compared with competitors, AnyDesk still requires Xorg for inbound Linux sessions, and TeamViewer’s Wayland support remains experimental for common desktop environments. RustDesk plans to gather real‑world feedback before making the implementation default, then extend unattended Wayland access to additional distributions such as Fedora and Arch Linux and integrate it into standard releases. Users of Wayland, especially those with multiple monitors, are encouraged to try the preview and report functionality and issues.

---

## Full Article

New[Unattended Remote Access on Wayland with RustDesk Â»](https://rustdesk.com/blog/unattended-remote-access-wayland)

Wayland support has been one of the harder parts of Linux remote desktop.

RustDesk can now provide true unattended access on Wayland, without requiring someone at the remote machine to approve every session. Multi-monitor setups are supported as well.

After the initial setup, you can connect even when no one is at the remote machine â including from the login screen after a reboot.[Watch the demo video on X](https://twitter.com/rustdesk/status/2087945266855026744)

For now, we are releasing this as a separate preview build for x86_64 Debian/Ubuntu-based systems:

[Download the Wayland unattended access build](https://github.com/rustdesk/rustdesk/releases/download/nightly/rustdesk-unattended-wayland-1.4.9-x86_64.deb)

Wayland support is still limited in several major remote desktop products. AnyDesk currently requires Xorg for incoming Linux sessions, while TeamViewer still describes Wayland support as experimental for common desktop environments.

We would like to get more real-world testing before making this the default.

Once the implementation is stable, we plan to bring unattended Wayland access to more Linux distributions, including Fedora and Arch Linux, and eventually include it in the standard RustDesk releases.

If you use Wayland, especially with multiple monitors, please give the preview build a try and let us know what worksâand what doesnât.

## Related reading

- [RustDesk for Linux](https://rustdesk.com/blog/rustdesk-for-linux)
- [RustDesk Unattended Access](https://rustdesk.com/blog/rustdesk-unattended-access-setup)
- [RustDesk vs AnyDesk](https://rustdesk.com/blog/rustdesk-vs-anydesk)
- [RustDesk vs TeamViewer](https://rustdesk.com/blog/rustdesk-vs-teamviewer)
- [RustDesk](https://rustdesk.com/tag/rustdesk)
- [Wayland](https://rustdesk.com/tag/wayland)
- [Linux](https://rustdesk.com/tag/linux)
- [unattended-access](https://rustdesk.com/tag/unattended-access)Share:     [Back to Blog](https://rustdesk.com/blog)

## Related Posts

[View All Posts Â»](https://rustdesk.com/blog)

### [Enhanced ACL in RustDesk Server Pro 1.5.0](https://rustdesk.com/blog/enhanced-acl-in-rustdesk-server-pro-1-5-0)

RustDesk Server Pro now supports user-level ACL and device groups in addition of user groups.

### [How to make Flutter 3.24 run on Windows 7?](https://rustdesk.com/blog/how-to-make-flutter-3-24-run-on-windows-7)

Since Flutter 3.22 starts to drop support for Windows 7 / 8, we need to modify Flutter engine to restore support for Windows 7.

### [RustDesk web client V2 Preview](https://rustdesk.com/blog/rustdesk-web-client-v2-preview)

V2 offers better codecs, international keyboard support, clipboard support, file transfer etc.

### [RustDesk for Linux: The Open-Source Remote Desktop](https://rustdesk.com/blog/rustdesk-for-linux)

Install and run RustDesk on Linux: .deb, .rpm, Flatpak and AppImage, X11 vs Wayland, headless and unattended access, and self-hosting the server.
