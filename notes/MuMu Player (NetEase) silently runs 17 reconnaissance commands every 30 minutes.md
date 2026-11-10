---
title: "MuMu Player (NetEase) silently runs 17 reconnaissance commands every 30 minutes"
url: https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea
clipped: 2026-06-17 01:42:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [MuMu Player (NetEase) silently runs 17 reconnaissance commands every 30 minutes](https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea)

## Digest Summary
MuMu Player Pro (v1.8.5, bundle com.netease.mumu.nemux‑global) on macOS runs a silent data‑collection routine every 30 minutes while the emulator is active. It creates a timestamped folder in ~/Library/Application Support/com.netease.mumu.nemux‑global/logs/ and stores the output of commands that enumerate network devices ( arp ‑a), interface configuration (ifconfig), DNS and proxy settings (scutil --dns, --proxy), hosts file (cat /etc/hosts), network connections (netstat), all processes with full arguments (ps aux), installed applications (ls ‑laeTO ‑@ /Applications/, mdls /Applications/*.app), kernel parameters (sysctl ‑a), launch agents/daemons, mounted volumes, and two curl requests to MuMu’s APIs. Each run logs success/failure per file and produces ~400 KB of data; about 23 runs are retained before rotation. The collected data—process list, software inventory, network topology, DNS configuration, kernel settings, and the Mac’s serial number—are packaged into SensorsData analytics files (identities, super_properties, message queue) and transmitted to MuMu’s servers. The privacy policy does not disclose these commands, the recurring schedule, or the hardware identifier, representing a transparency shortfall.

## Discussion Summary
The comments express strong distrust of Chinese technology firms, emphasizing concerns that their products—particularly video games—collect extensive user data and could compromise privacy. The author argues that such practices threaten personal security and cultural influence, suggesting that Western authorities have been insufficiently proactive, favoring economic ties over protective measures. The overall tone is critical, highlighting apprehension about data harvesting, advocating for stricter regulation, and questioning the adequacy of current Western policy responses.

---

## Full Article

MuMu Player Pro for macOS (by NetEase) executes a comprehensive system data collection routine every 30 minutes while the emulator is running. This includes enumerating all devices on your local network, capturing every running process with full command-line arguments, inventorying all installed applications, reading your hosts file, and dumping kernel parameters -- all tied to your Mac's serial number via SensorsData analytics.

None of this is disclosed in MuMu's privacy policy. None of it is necessary for an Android emulator to function.

* App: MuMu Player Pro for macOS (v1.8.5)
* Bundle ID: `com.netease.mumu.nemux-global`
* macOS version: 26.3 (Apple Silicon)

Every 30 minutes, MuMu creates a timestamped directory under:

```
~/Library/Application Support/com.netease.mumu.nemux-global/logs/
```

Each directory (e.g. `20260220-071645`) contains the output of the following commands, all executed automatically in the background:

| File | Command executed | What it captures |
| --- | --- | --- |
| `arpAll.txt` | `arp -a` | Every device on your local network (IPs + MAC addresses) |
| `ifconfig.txt` | `ifconfig` | All network interfaces, MAC addresses, IP addresses, VPN tunnels |
| `networkDNS.txt` | `scutil --dns` | Full DNS resolver configuration |
| `networkProxy.txt` | `scutil --proxy` | Proxy settings |
| `catHosts.txt` | `cat /etc/hosts` | Your entire hosts file (exposes custom domains, dev environments) |
| `netstat.txt` | `netstat` | Active network connections (times out after 15s) |
| `listProcess.txt` | `ps aux` | **Every running process** with full arguments (~200KB) |
| `listApplications.txt` | `ls -laeTO -@ /Applications/` | All installed applications with metadata |
| `mdlsApplications.txt` | `mdls /Applications/*.app` | Spotlight metadata for every app (name, version, bundle ID, size, dates) |
| `sysctl.txt` | `sysctl -a` | Kernel parameters, hostname, hardware info, boot time (~60KB) |
| `launchctlPrintSystem.txt` | `launchctl print system` | Full system service dump (~64KB) |
| `launchctlLimit.txt` | `launchctl limit` | System resource limits |
| `listLaunchAgents.txt` | `ls -laeTO -@ /Library/LaunchAgents` | All system launch agents |
| `listLaunchDaemons.txt` | `ls -laeTO -@ /Library/LaunchDaemons` | All system launch daemons |
| `mount.txt` | `mount` | All mounted filesystems |
| `custom-curl-apipro.txt` | `curl -v https://pro-api.mumuplayer.com` | Connectivity test to MuMu API |
| `custom-curl-mumuapipro.txt` | `curl -v https://api.mumuglobal.com` | Connectivity test to MuMu global API |

A `collect-finished` manifest file logs the success/failure of each collection.

The process list captures full command-line arguments for every process on the system. In practice this exposes:

* What applications you're running and when (browsers, chat apps, trading platforms, security tools)
* VPN usage and configuration (e.g. NordVPN/NordLynx with arguments)
* Development tools and infrastructure (Docker, IDEs, terminal sessions with arguments)
* Session tokens and IDs passed as command-line arguments
* User data directory paths revealing your username and app configurations
* What security/firewall software you use (useful for evasion)

This is captured every 30 minutes, creating a detailed behavioral timeline of your computer usage.

Analytics and device fingerprinting
-----------------------------------

MuMu uses **SensorsData** (a Chinese analytics platform) for tracking. Files in the `report/` directory include:

**Identity tracking** (`sensorsanalytics-com.sensorsdata.identities.plist`):

```
{
  "$identity_login_id": "<user_id>",
  "$identity_anonymous_id": "<anonymous_id>",
  "$identity_mac_serial_id": "<your_mac_serial_number>"
}
```

Your Mac's hardware serial number is collected and used as a persistent identifier.

**Campaign tracking** (`sensorsanalytics-super_properties.plist`):

```
player_version: 1.8.5
player_channel: MACPRO
player_uuid: <UUID>
player_utm_source: SEO001
player_engine: (tracked)
```

An 86KB analytics message queue (`sensorsanalytics-message-v2.plist`) is maintained and sent to their servers.

On a single day of normal use, MuMu ran the collection routine **16 times** (once every ~30 minutes). Each collection generates ~400KB of system data. The logs directory retains approximately 23 collection runs before rotating.

If you have MuMu Player Pro installed on macOS, check:

```
ls ~/Library/Application\ Support/com.netease.mumu.nemux-global/logs/
```

If you see timestamped directories, open any one and read the files. Each file contains the exact command that was executed, its arguments, and the full captured output.

What MuMu's privacy policy says
-------------------------------

The [MuMu Player Pro Privacy Policy](https://www.mumuglobal.com/mac/license/privacy-policy.html) does not disclose:

* Running `ps aux` to capture all system processes
* Running `arp -a` to enumerate local network devices
* Reading `/etc/hosts`
* Dumping `sysctl -a` kernel parameters
* Inventorying all installed applications via `mdls`
* Collecting your Mac serial number
* Performing any of this on a 30-minute recurring schedule

This goes well beyond what any Android emulator needs. The data collected -- local network topology, complete process lists, installed software inventory, DNS configuration, hosts file, and kernel parameters -- constitutes a comprehensive system profile. Combined with SensorsData analytics and your hardware serial number, this creates a persistent, detailed fingerprint of your machine and usage patterns.

The fact that this runs silently every 30 minutes, is not disclosed in the privacy policy, and is not necessary for emulator functionality makes this, at minimum, a serious transparency failure.