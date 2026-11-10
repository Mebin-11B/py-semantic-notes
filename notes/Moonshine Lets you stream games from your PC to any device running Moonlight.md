---
title: "Moonshine: Lets you stream games from your PC to any device running Moonlight"
url: https://github.com/hgaiser/moonshine
clipped: 2026-08-31 12:23:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Moonshine: Lets you stream games from your PC to any device running Moonlight](https://github.com/hgaiser/moonshine)

## Digest Summary
Moonshine is a Rust‑based, head‑less streaming server enabling Moonlight clients to stream games from a Linux PC. Each game runs in an isolated compositor, allowing the host to remain usable and eliminating the need for a physical monitor or HDMI dummy plug. It leverages GPU‑accelerated video encoding via Vulkan, supporting H.264, H.265, and experimental AV1 (the latter requires NVIDIA driver ≥ 595.44.3.0). Features include true 10‑bit HDR, full mouse/keyboard/gamepad input (including motion, touchpad, haptics), and low‑latency Opus‑encoded stereo or 5.1/7.1 audio. Moonshine requires systemd, a Vulkan‑capable GPU (NVIDIA RTX, AMD RDNA2+, Intel Arc), and Moonlight v6.0.0+. Installation is typically through the AUR; building needs clang, cmake, rust, Vulkan headers, Wayland, and related libraries. Configuration is via a TOML file where applications and optional pre/post commands are defined; scanners auto‑detect Steam games and desktop .desktop entries. Moonshine is Linux‑only, runs without an active desktop session, and is not intended for direct internet exposure—VPNs are recommended for remote access. Compared to Sunshine, Moonshine offers fewer platforms and features but provides isolated sessions on headless Linux hosts.

---

## Full Article

[Skip to content](https://github.com/hgaiser/moonshine#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [hgaiser](https://github.com/hgaiser)    
    /
    
      [moonshine](https://github.com/hgaiser/moonshine)
    

    Public
  

        

        
            
    
        
- 
          
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

        

      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fhgaiser%2Fmoonshine)    You must be signed in to change notification settings

  

  
- 
          [Fork
    74](https://github.com/login?return_to=%2Fhgaiser%2Fmoonshine)
  

  
- 
        
        [Star
          1.1k](https://github.com/login?return_to=%2Fhgaiser%2Fmoonshine)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/hgaiser/moonshine/branches)[Tags](https://github.com/hgaiser/moonshine/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[744 Commits](https://github.com/hgaiser/moonshine/commits/main/)744 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github](https://github.com/hgaiser/moonshine/tree/main/.github)[.github](https://github.com/hgaiser/moonshine/tree/main/.github)  [.vscode](https://github.com/hgaiser/moonshine/tree/main/.vscode)[.vscode](https://github.com/hgaiser/moonshine/tree/main/.vscode)  [assets](https://github.com/hgaiser/moonshine/tree/main/assets)[assets](https://github.com/hgaiser/moonshine/tree/main/assets)  [dist](https://github.com/hgaiser/moonshine/tree/main/dist)[dist](https://github.com/hgaiser/moonshine/tree/main/dist)  [moonshine-core](https://github.com/hgaiser/moonshine/tree/main/moonshine-core)[moonshine-core](https://github.com/hgaiser/moonshine/tree/main/moonshine-core)  [moonshine-tools](https://github.com/hgaiser/moonshine/tree/main/moonshine-tools)[moonshine-tools](https://github.com/hgaiser/moonshine/tree/main/moonshine-tools)  [moonshine-wsi](https://github.com/hgaiser/moonshine/tree/main/moonshine-wsi)[moonshine-wsi](https://github.com/hgaiser/moonshine/tree/main/moonshine-wsi)  [nix](https://github.com/hgaiser/moonshine/tree/main/nix)[nix](https://github.com/hgaiser/moonshine/tree/main/nix)  [src](https://github.com/hgaiser/moonshine/tree/main/src)[src](https://github.com/hgaiser/moonshine/tree/main/src)  [.editorconfig](https://github.com/hgaiser/moonshine/blob/main/.editorconfig)[.editorconfig](https://github.com/hgaiser/moonshine/blob/main/.editorconfig)  [.gitignore](https://github.com/hgaiser/moonshine/blob/main/.gitignore)[.gitignore](https://github.com/hgaiser/moonshine/blob/main/.gitignore)  [CHANGELOG.md](https://github.com/hgaiser/moonshine/blob/main/CHANGELOG.md)[CHANGELOG.md](https://github.com/hgaiser/moonshine/blob/main/CHANGELOG.md)  [Cargo.lock](https://github.com/hgaiser/moonshine/blob/main/Cargo.lock)[Cargo.lock](https://github.com/hgaiser/moonshine/blob/main/Cargo.lock)  [Cargo.toml](https://github.com/hgaiser/moonshine/blob/main/Cargo.toml)[Cargo.toml](https://github.com/hgaiser/moonshine/blob/main/Cargo.toml)  [LICENSE](https://github.com/hgaiser/moonshine/blob/main/LICENSE)[LICENSE](https://github.com/hgaiser/moonshine/blob/main/LICENSE)  [README.md](https://github.com/hgaiser/moonshine/blob/main/README.md)[README.md](https://github.com/hgaiser/moonshine/blob/main/README.md)  [TIPS.md](https://github.com/hgaiser/moonshine/blob/main/TIPS.md)[TIPS.md](https://github.com/hgaiser/moonshine/blob/main/TIPS.md)  [flake.lock](https://github.com/hgaiser/moonshine/blob/main/flake.lock)[flake.lock](https://github.com/hgaiser/moonshine/blob/main/flake.lock)  [flake.nix](https://github.com/hgaiser/moonshine/blob/main/flake.nix)[flake.nix](https://github.com/hgaiser/moonshine/blob/main/flake.nix)  [nfpm.yaml](https://github.com/hgaiser/moonshine/blob/main/nfpm.yaml)[nfpm.yaml](https://github.com/hgaiser/moonshine/blob/main/nfpm.yaml)  [rustfmt.toml](https://github.com/hgaiser/moonshine/blob/main/rustfmt.toml)[rustfmt.toml](https://github.com/hgaiser/moonshine/blob/main/rustfmt.toml)  View all files

## Repository files navigation

# Moonshine 🌙

Moonshine lets you stream games from your PC to any device running [Moonlight](https://moonlight-stream.org/).
Your keyboard, mouse, and controller inputs are sent back to the host so you can play games remotely as if you were sitting in front of it.

## Features

- Isolated streaming sessions: Each stream runs in its own compositor, completely separate from your desktop environment. Your host PC can still be used for other things while you stream.

- No monitor required: Works on headless servers — no HDMI dummy plug needed.

- Hardware video encoding: H.264, H.265, and AV1 encoding using the GPU.

- HDR support: True 10-bit HDR streaming for supported games.

- Full input support: Mouse, keyboard, touchscreen, pen/stylus, and gamepad (including motion, touchpad, and haptics).

- Audio streaming: Stereo and surround sound (5.1/7.1) with low-latency Opus encoding.

## Requirements

- Linux only. Available as  `.deb` ,  `.rpm` , Nix, AUR, and an install script for SteamOS. Tested on Arch Linux, but reported to work on other distributions too.

- systemd. Required for launching and managing application processes. Almost all modern Linux distributions include it by default.

- A GPU with Vulkan video encoding. NVIDIA RTX, AMD RDNA2+, or Intel Arc.

- Moonlight v6.0.0 or higher. Compatibility with older versions or unofficial ports is not guaranteed.

## Installation

### Arch

The recommended method is to install through the AUR using:
 ` `yay -S moonshine-bin
` ` 

After installing, follow the distro-agnostic [Enable the service](https://github.com/hgaiser/moonshine#enable-the-service) steps below.

### Debian / Ubuntu (.deb)

Download the latest  `.deb`  from the [releases page](https://github.com/hgaiser/moonshine/releases) and install it:
 `sudo apt install ./moonshine_*.deb` 

After installing, follow the [Enable the service](https://github.com/hgaiser/moonshine#enable-the-service) steps below.

### Fedora / RHEL (.rpm)

Download the latest  `.rpm`  from the [releases page](https://github.com/hgaiser/moonshine/releases) and install it:
 `sudo dnf install ./moonshine-*.rpm` 

The package's post-install scripts set up udev rules, kernel modules, and the  `moonshine`  group automatically.
After installing, follow the [Enable the service](https://github.com/hgaiser/moonshine#enable-the-service) steps below.

### Nix

This repository is also a nix flake, providing a package and a NixOS module that sets up the service for you.
See [nix/README.md](https://github.com/hgaiser/moonshine/blob/main/nix/README.md) for instructions, or install just the package on any distro with:
 `nix profile install github:hgaiser/moonshine` 

After installing, follow the [Enable the service](https://github.com/hgaiser/moonshine#enable-the-service) steps below (the NixOS module handles this for you when enabled).

### Bazzite / Silverblue / Atomic distros

On Fedora Atomic distros, download the  `.rpm`  from the [releases page](https://github.com/hgaiser/moonshine/releases) and layer it:
 `sudo rpm-ostree install ./moonshine-*.rpm
sudo systemctl reboot` 

After reboot, follow the [Enable the service](https://github.com/hgaiser/moonshine#enable-the-service) steps below.

### SteamOS

Use the installer script:
 `curl -fsSL https://github.com/hgaiser/moonshine/releases/latest/download/moonshine-install.sh | bash` 

This deploys moonshine to  `/opt/moonshine/`  and configuration drop-ins to  `/etc/` . The installer registers these files with SteamOS so they persist across atomic updates.

### Enable the service

These steps apply to every installation method above (the service is a systemd unit).

- 

Enable user lingering:
 `sudo loginctl enable-linger $USER` 

This allows Moonshine to run applications in the user's session even when the user is not logged in (when running headless).

If your user is always logged in when you want to stream, you can skip this step.

- 

Enable the service to start on boot and run immediately:
 `sudo systemctl enable --now moonshine@$USER` 

- 

Gamepad support when streaming headless (no active desktop session): add your user to the  `input`  group, then log out and back in (or reboot) for it to take effect:
 `sudo usermod -aG input $USER` 

Moonshine creates a virtual gamepad per streamed controller, and the streamed game must be able to read it. When streaming while a desktop session is active, your user is already granted access to input devices as the active seat, so this step is not needed there. Run  `moonshine healthcheck`  to verify — it reports an  `input group`  warning if the group is missing.

### Source

The following dependencies are required to build and run:
 `# Build dependencies
sudo pacman -S --asdeps \
   clang \
   cmake \
   libc++ \
   rust

# Runtime dependencies
sudo pacman -S \
   gcc-libs \
   glibc \
   libevdev \
   libxkbcommon \
   mesa \
   opus \
   wayland` 

Then build:
 `cargo build --release --workspace` 

Set up the environment:
 `# Install uinput/uhid kernel modules
sudo install -Dm644 dist/moonshine-modules.conf /usr/lib/modules-load.d/moonshine.conf
sudo modprobe uinput uhid

# Install udev rules for input device access
sudo install -Dm644 dist/60-moonshine.rules /usr/lib/udev/rules.d/60-moonshine.rules
sudo udevadm control --reload-rules

# Install the Vulkan WSI layer for game rendering
sudo install -Dm755 target/release/libmoonshine_wsi.so /usr/lib/moonshine/vulkan-layers/libmoonshine_wsi.so
sudo install -Dm644 dist/VkLayer_moonshine_wsi.json /usr/share/vulkan/implicit_layer.d/VkLayer_moonshine_wsi.json` 

Then run:
 `cargo run --release -- /path/to/config.toml` 

## Configuration

A configuration file is created automatically if the path you provide doesn't exist.
When using the AUR package, it defaults to  `$XDG_CONFIG_HOME/moonshine/config.toml` .

### Pairing with a client

When you connect with Moonlight for the first time, it will show a PIN.
A notification will appear on the host that you can click to open the pairing page, or you can visit it manually at [http://localhost:47989/pin](http://localhost:47989/pin) .

You can also pair from the command line:
 `curl -X POST "http://localhost:47989/submit-pin" -d "uniqueid=0123456789ABCDEF&pin=<PIN>"` 

### Adding applications

Each application runs in its own isolated streaming session. Add them to  `config.toml`  like this:
 `[[application]]
title = "Steam"
boxart = "/path/to/steam.png"  # optional
command = ["/usr/bin/steam", "steam://open/bigpicture"]` 

-  `title` : The name shown in Moonlight.

-  `boxart`  (optional): Path to a cover image.

-  `command` : The command to run. First entry is the executable, the rest are arguments.

-  `pre_command`  (optional): Commands to run before launching the application. Each entry is a separate command, executed in order. Runs synchronously — the session waits for all to finish.

-  `post_command`  (optional): Commands to run after the streaming session ends. Each entry is a separate command, executed in order. Runs synchronously — the server waits for all to finish.

Example:
 `[[application]]
title = "Steam"
command = ["/usr/bin/steam", "steam://open/bigpicture"]
pre_command = [
    ["/usr/bin/systemctl", "stop", "conflicting.service"],
]
post_command = [
    ["/usr/bin/systemctl", "start", "conflicting.service"],
]` 

### Application scanners

Scanners automatically detect installed applications so you don't have to add them manually.

Steam scanner — finds all installed Steam games:
 `[[application_scanner]]
type = "steam"
library = "$HOME/.local/share/Steam"
command = ["/usr/bin/steam", "-bigpicture", "steam://rungameid/{game_id}"]` 

Desktop scanner — finds applications from  `.desktop`  files:
 `[[application_scanner]]
type = "desktop"
directories = [
  "$HOME/.local/share/applications",
  "/usr/share/applications",
]
include_terminal = false
resolve_icons = true` 

Lutris scanner — finds all installed Lutris games:
 `[[application_scanner]]
type = "lutris"
command = ["/usr/bin/lutris", "lutris:rungame/{slug}"]` 

Games are matched by their Lutris slug.
Box art is automatically loaded from Lutris's  `coverart/`  directory when available.
The default database path is  `~/.local/share/lutris/pga.db` .
You can override it with the  `pga_db`  option to point at a custom database location.

Heroic scanner — finds all installed [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) games (Epic, GOG, Amazon and manually added games):
 `[[application_scanner]]
type = "heroic"
command = ["heroic", "--no-gui", "heroic://launch?appName={app_name}&runner={runner}"]` 

If you installed Heroic from Flathub, launch it through Flatpak instead:
 `[[application_scanner]]
type = "heroic"
command = [
  "dbus-run-session", "--",
  "flatpak", "run", "com.heroicgameslauncher.hgl",
  "--no-gui", "heroic://launch?appName={app_name}&runner={runner}",
]` 

The  `dbus-run-session`  prefix keeps the game inside Moonshine's compositor instead of on your desktop.
See [TIPS.md](https://github.com/hgaiser/moonshine/blob/main/TIPS.md) for why Flatpak needs it.

 `{app_name}`  is Heroic's internal game id and  `{runner}`  is the store it came from ( `legendary`  for Epic,  `gog`  for GOG,  `nile`  for Amazon,  `sideload`  for manually added games).
Commands are resolved against Moonshine's own  `PATH` , which under the packaged systemd service is systemd's default rather than your login shell's.
A bare  `heroic`  therefore works for packages that install into  `/usr/bin` , but not for an AppImage or anything under  `~/.local/bin` ; use an absolute path in those cases.
Box art is automatically loaded from Heroic's  `images-cache/`  directory for any art Heroic has already downloaded.

The default configuration directory is  `~/.config/heroic` , falling back to  `~/.var/app/com.heroicgameslauncher.hgl/config/heroic`  when only the Flatpak is installed.
You can override it with the  `config_dir`  option.

## Tips & Tricks

See [TIPS.md](https://github.com/hgaiser/moonshine/blob/main/TIPS.md) for practical recipes and workarounds.

## FAQ

- 

How does this compare to [Sunshine](https://github.com/LizardByte/Sunshine)?

- Sunshine supports more platforms and has more features overall. Moonshine is Linux-only.

- Moonshine runs each streaming session in its own isolated environment, separate from your desktop. This means your host PC stays usable while you stream, and it works without an active desktop session.

- 

Can I use Moonshine to stream to two clients simultaneously?

This is currently not a supported feature and not a focus of Moonshine. If you are interested in adding support for this, feel free to open an issue or discuss on [Discord](https://discord.com/invite/moonlight-stream-352065098472488960).

- 

How do I run the healthcheck?

Run  `moonshine healthcheck`  to check GPU capabilities, codec support, and port availability. Pass  `--config <path>`  to also check configured ports and GPU preferences.

## Security

Moonshine is not designed for use on public networks.
The underlying GameStream protocol has limitations that mean traffic is not fully encrypted at the application level.

If you need to stream over the internet, use a VPN such as [Tailscale](https://tailscale.com/), [WireGuard](https://www.wireguard.com/), or [ZeroTier](https://www.zerotier.com/).

Do not expose Moonshine ports directly to the internet.

## Acknowledgement

This wouldn't have been possible without the incredible work by the people behind the following projects:

- [Moonlight](https://moonlight-stream.org/), without it there would be no client for Moonshine.

- [Sunshine](https://github.com/LizardByte/Sunshine), which laid a lot of the groundwork for the host part of the API.

- [Inputtino](https://github.com/games-on-whales/inputtino), for a thorough implementation of input devices.

- [magic-mirror](https://github.com/colinmarc/magic-mirror), for inspiration of using Vulkan and a Wayland compositor for headless streaming.

## About

Headless streaming server for Moonlight clients, written in Rust.

### Resources

[Readme](https://github.com/hgaiser/moonshine#readme-ov-file)[BSD-2-Clause license](https://github.com/hgaiser/moonshine#BSD-2-Clause-1-ov-file)[Activity](https://github.com/hgaiser/moonshine/activity)

### Stars

1.1k stars

### Watchers

5 watching

### Forks

[74 forks](https://github.com/hgaiser/moonshine/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fhgaiser%2Fmoonshine&report=hgaiser+%28user%29)

## Releases

## Sponsor this project

## Packages

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
