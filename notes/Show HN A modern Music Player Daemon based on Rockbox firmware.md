---
title: "Show HN: A modern Music Player Daemon based on Rockbox firmware"
url: https://github.com/tsirysndr/rockbox-zig
clipped: 2026-06-17 01:04:04
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - audio processing
  - hybrid languages
  - stream routing
  - system daemons
  - rockbox firmware
related:
  - "[[Audio Processing]]"
  - "[[Hybrid Languages]]"
  - "[[System Daemons]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Rockbox Zig is a modern music player daemon that ports Rockbox's C audio engine to Rust and Zig, providing gapless playback, DSP, and multi-room streaming.
>
> **Key points:**
> - Integrates Rockbox's C-based audio engine (`libfirmware.a`) with Rust static libraries and Zig compiling for cross-platform playback.
> - Exposes gRPC, GraphQL, HTTP, and MPD-compatible APIs, allowing control via standard clients.
> - Audio routing supports CPAL (local output), Snapcast, AirPlay, Chromecast, and UPnP/DLNA media rendering.
>
> **Concept links:** [[Audio Processing]], [[Hybrid Languages]], [[Stream Routing]], [[System Daemons]], [[Rockbox Firmware]]
>
> **Suggested connections:**
> - [[Audio Processing]] — DSP algorithms, gapless playback, and digital audio decoding.
> - [[Hybrid Languages]] — linking and compiling C, Rust, and Zig in a unified binary.
> - [[System Daemons]] — background services managing persistent media playing and network APIs.
<!-- ai-summary:end -->

# [Show HN: A modern Music Player Daemon based on Rockbox firmware](https://github.com/tsirysndr/rockbox-zig)

## Digest Summary
Rockbox Zig is a modern music‑player daemon built on the Rockbox audio engine and written with Rust and Zig. It provides gapless playback, DSP, 20+ codecs and a tag database via gRPC, GraphQL, HTTP and MPD APIs, and adds multi‑room output options such as AirPlay, Snapcast, Squeezelite, Chromecast and UPnP/DLNA. A quick start is available through Docker (mount $HOME/Music, expose ports 6062, 1704‑1705, 1780). Configuration resides in ~/.config/rockbox.org/settings.toml, where music_dir and audio_output are required; other parameters control EQ, replaygain, crossfade, compressor, etc. Audio outputs include builtin CPAL, snapcast (TCP with mDNS auto‑discovery or FIFO), airplay (single or multi‑receiver), squeezelite (Slim protocol), chromecast (Cast + HTTP WAV), and UPnP modes (PCM sink, media server, media renderer). Installation options are Docker, native packages (apt, yum, brew), a universal curl script, or building from source (requires Zig ≥ 0.16, Rust stable, and various dev libraries). Building compiles the C firmware to libfirmware.a, links with Rust static libs (librockbox_cli.a, librockbox_server.a) and CPAL via Zig, producing a single rockboxd binary. Documentation, API references and a GTK4 desktop app (Flatpak) are provided.

## Discussion Summary
The comments convey a uniformly positive view of Rockbox, highlighting its well‑designed interface and strong performance as notable strengths. Contributors express personal affinity for the project, emphasizing its ongoing relevance and the satisfaction of seeing their own early code incorporated. Overall, the sentiment reflects enthusiasm for the software’s continued development and appreciation for its refined user experience.

---

## Full Article

[![GPL-2.0 licensed](https://camo.githubusercontent.com/d7343ab30d2b14bffa5d36496e86f67baa89143e4fe68e259707602342f9e9ec/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c2d626c75652e737667)](https://github.com/tsirysndr/rockbox-zig/blob/master/LICENSE)
[![ci](https://github.com/tsirysndr/rockbox-zig/actions/workflows/ci.yml/badge.svg)](https://github.com/tsirysndr/rockbox-zig/actions/workflows/ci.yml)
[![Docker Pulls](https://camo.githubusercontent.com/60693fc909b990dcd4c2576140431260dffdea7c0d49dc4d8fd698ea513aa9d5/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f74736972792f726f636b626f78)](https://hub.docker.com/r/tsiry/rockbox)
[![GitHub Downloads (all assets, all releases)](https://camo.githubusercontent.com/fcfb9ea7fc4dc472568417f9c4903184453f86c1a3cb2d4144887de5296e1e1f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f7473697279736e64722f726f636b626f782d7a69672f746f74616c)](https://camo.githubusercontent.com/fcfb9ea7fc4dc472568417f9c4903184453f86c1a3cb2d4144887de5296e1e1f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f7473697279736e64722f726f636b626f782d7a69672f746f74616c)
[![discord](https://camo.githubusercontent.com/f4ea878051eda7052881aa83ff58b81504ac0582e29ad40241fbf9b0d98a90b9/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313239323835353136373932313831353731353f6c6162656c3d646973636f7264266c6f676f3d646973636f726426636f6c6f723d353836354632)](https://discord.gg/tXPrgcPKSt)
[![storybook](https://raw.githubusercontent.com/storybooks/brand/master/badge/badge-storybook.svg)](https://master--670ceec25af685dcdc87c0df.chromatic.com/?path=/story/components-albums--default)

[![Rockbox UI](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/gpui.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/gpui.png)

A modern take on the [Rockbox](https://www.rockbox.org) open source audio
player, extended with Rust and Zig. Rockbox Zig exposes the full Rockbox audio
engine — gapless playback, DSP, 20+ codecs, tag database — through gRPC,
GraphQL, HTTP, and MPD APIs, in a single binary (`rockboxd`) and adds multi-room output via AirPlay, Snapcast,
and Squeezelite.

[![Preview](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/preview.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/preview.png)
[![Desktop](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/desktop.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/desktop.png)
[![macOS media controls](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/media-controls.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/media-controls.png)
[![macOS preview](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/preview-mac.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/preview-mac.png)

---

* Built-in [CPAL](https://github.com/RustAudio/cpal) audio
* [HLS](https://developer.apple.com/streaming/) + [MPEG-DASH](https://dashif.org) (CMAF / fMP4) — plays directly in any browser, no extra client needed
* [AirPlay](https://en.wikipedia.org/wiki/AirPlay) (RAOP) — single or multi-room fan-out to Apple TV, HomePod, Airport Express, shairport-sync
* [Snapcast](https://github.com/snapcast/snapcast) — synchronised multi-room via snapserver (FIFO/pipe **and** direct TCP with mDNS auto-discovery)
* [Squeezelite](https://github.com/ralph-irving/squeezelite) (Slim Protocol + HTTP broadcast) — synchronised multi-room
* [Chromecast](https://developers.google.com/cast)
* Gapless playback and crossfading
* Supports 20+ codecs: MP3, OGG, FLAC, WAV, AAC, Opus, and more

---

The fastest way to get started — no install, no config file, no external client needed.
The default `audio_output` is **CMAF (HLS + DASH)**, so audio plays straight in
your browser:

```
docker run -v $HOME/Music:/root/Music \
  -p 6062:6062 \
  -p 7882:7882 \
  tsiry/rockbox
```

Open the web UI at <http://localhost:6062> and start
playing — the page attaches to the HLS stream on port `7882` automatically.

Prefer the terminal? Any HLS-capable player can consume the stream directly:

```
ffplay http://localhost:7882/hls/master.m3u8
# or: vlc http://localhost:7882/hls/master.m3u8
# or: mpv  http://localhost:7882/hls/master.m3u8
```

Want Snapcast multi-room instead of HLS?

The image still ships a `snapserver` so you can opt into the FIFO/Snapcast path
without rebuilding. Expose its ports and edit
`~/.config/rockbox.org/settings.toml` inside the container to set
`audio_output = "fifo"`:

```
docker run -v $HOME/Music:/root/Music \
  -p 6062:6062 \
  -p 1704:1704 \
  -p 1705:1705 \
  -p 1780:1780 \
  tsiry/rockbox
```

Then connect a [Snapcast](https://github.com/snapcast/snapcast) client:

```
snapclient tcp://localhost
```



---

1. **Install** (see [Installation](https://github.com/tsirysndr/rockbox-zig#-installation) below).
2. **Create `~/.config/rockbox.org/settings.toml`**:

```
music_dir    = "/path/to/your/Music"
audio_output = "builtin"   # CPAL audio — see Audio Output for other options
playlist_shuffle = false
repeat_mode = 1
bass = 3
treble = 3
bass_cutoff = 0
treble_cutoff = 0
crossfade = 5
fade_on_stop = false
fade_in_delay = 2
fade_in_duration = 7
fade_out_delay = 4
fade_out_duration = 0
fade_out_mixmode = 2
balance = 0
stereo_width = 100
stereosw_mode = 0
surround_enabled = 0
surround_balance = 0
surround_fx1 = 0
surround_fx2 = 0
party_mode = true
channel_config = 0
player_name = ""
eq_enabled = true


[[eq_band_settings]]
cutoff = 60
q = 70
gain = 25

[[eq_band_settings]]
cutoff = 200
q = 70
gain = 55

[[eq_band_settings]]
cutoff = 500
q = 70
gain = 40

[[eq_band_settings]]
cutoff = 1000
q = 70
gain = -140

[[eq_band_settings]]
cutoff = 2000
q = 70
gain = -115

[[eq_band_settings]]
cutoff = 4000
q = 70
gain = -60

[[eq_band_settings]]
cutoff = 7000
q = 70
gain = 10

[[eq_band_settings]]
cutoff = 10000
q = 70
gain = 50

[[eq_band_settings]]
cutoff = 14000
q = 70
gain = 65

[[eq_band_settings]]
cutoff = 20000
q = 70
gain = 50

[replaygain_settings]
noclip = true
type = 0
preamp = 0

[compressor_settings]
threshold = -24
makeup_gain = 0
ratio = 4
knee = 1
release_time = 300
attack_time = 5
```

3. **Start Rockbox**:

4. **Open the web UI** at <http://localhost:6062> or connect any MPD client to `localhost:6600`.

---



| Service | Default port | Protocol |
| --- | --- | --- |
| gRPC | 6061 | gRPC / gRPC-Web |
| GraphQL + Web UI | 6062 | HTTP |
| HTTP REST API | 6063 | HTTP |
| MPD server | 6600 | MPD protocol |
| Subsonic / Navidrome API | 4533 | HTTP |
| CMAF (HLS + DASH) | 7882 | HTTP |
| Slim Protocol (squeezelite) | 3483 | TCP |
| HTTP PCM stream (squeezelite) | 9999 | HTTP |
| Chromecast WAV stream | 7881 | HTTP |
| UPnP Media Server (ContentDirectory) | 7878 | HTTP / SSDP |
| UPnP WAV broadcast (PCM sink) | 7879 | HTTP |
| UPnP MediaRenderer (AVTransport) | 7880 | HTTP / SSDP |



---

⚙️ Audio Output Configuration
-----------------------------

Rockbox reads `~/.config/rockbox.org/settings.toml` at startup.
`music_dir` is always required. `audio_output` defaults to `"builtin"` if
omitted.

```
music_dir    = "/path/to/Music"
audio_output = "builtin"
```

Uses [CPAL](https://github.com/RustAudio/cpal) — plays through the OS default device. No extra setup needed.

```
music_dir      = "/path/to/Music"
audio_output   = "cmaf"           # also accepts "hls" or "dash"
cmaf_http_port = 7882             # optional, default 7882
cmaf_bitrate   = 128000           # optional, AAC-LC bitrate in bps
```

Encodes live audio as AAC-LC in fragmented MP4 (CMAF) and serves it as both
HLS and MPEG-DASH from the same in-memory ring buffer. Any HLS-capable client
can play the stream — including every modern browser — with no extra software:

```
http://<host>:7882/hls/master.m3u8     # HLS
http://<host>:7882/dash/manifest.mpd   # MPEG-DASH
```

This is the default for the Docker image: the web UI's `<audio>` element
attaches to the HLS stream automatically as soon as the active output is set
to `cmaf` / `hls` / `dash`. Try it from the terminal too:

```
ffplay http://localhost:7882/hls/master.m3u8
vlc    http://localhost:7882/hls/master.m3u8
mpv    http://localhost:7882/hls/master.m3u8
```

A 2-second sliding window of segments is kept in memory; clients always join at
the live edge. Optionally mirror segments + manifests to disk for an external
HTTP server (nginx, Caddy, a CDN origin) by adding:

```
cmaf_segment_dir = "/var/www/rockbox-cmaf"
```

Rockbox supports two ways to feed [Snapcast](https://github.com/snapcast/snapcast)
for synchronised multi-room playback. Both write raw **S16LE stereo 44100 Hz**
PCM to snapserver.

#### TCP (recommended — auto-discovery)

```
music_dir         = "/path/to/Music"
audio_output      = "snapcast_tcp"
snapcast_tcp_host = "192.168.1.x"   # IP of the machine running snapserver
snapcast_tcp_port = 4953            # default snapserver TCP source port
```

Connects directly to snapserver's TCP source port. No named FIFO or filesystem
dependency needed.

```
# /etc/snapserver.conf  (or /usr/local/etc/snapserver.conf on macOS)
[stream]
source = tcp://0.0.0.0:4953?name=default&sampleformat=44100:16:2
```

> **Startup order**: start `snapserver` first so it is already listening when
> rockboxd begins playback. If the connection drops (e.g. snapserver restarts),
> it is re-established automatically on the next play call.

> **Auto-discovery**: rockboxd scans for `_snapcast._tcp.local.` via mDNS at
> startup. Discovered servers appear in the web UI and desktop app device
> picker — just click to connect, no config file editing needed.

```
music_dir    = "/path/to/Music"
audio_output = "fifo"
fifo_path    = "/tmp/snapfifo"   # named FIFO for snapserver; use "-" for stdout
```

Writes to a named FIFO. Use this when you need stdout piping or prefer the
traditional pipe model.

```
# /etc/snapserver.conf  (or /usr/local/etc/snapserver.conf on macOS)
[stream]
source = pipe:///tmp/snapfifo?name=default&sampleformat=44100:16:2
```

> **Startup order**: start `rockboxd` before `snapserver`. Rockbox holds a
> permanent write reference on the FIFO so snapserver never sees a premature
> EOF between tracks.

Pipe to any PCM consumer with `fifo_path = "-"`:

```
rockboxd | ffplay -f s16le -ar 44100 -ac 2 -
```

See [SNAPCAST.md](https://github.com/tsirysndr/rockbox-zig/blob/master/SNAPCAST.md) for a detailed comparison of both modes,
connection lifecycle, reconnect behaviour, and macOS quirks.

### AirPlay (RAOP) — single or multi-room

Single receiver:

```
music_dir    = "/path/to/Music"
audio_output = "airplay"
airplay_host = "192.168.1.50"   # IP of the AirPlay receiver
airplay_port = 5000             # optional, default 5000
```

Multi-room (fan-out to N receivers simultaneously):

```
music_dir    = "/path/to/Music"
audio_output = "airplay"

[[airplay_receivers]]
host = "192.168.1.50"   # living room
port = 5000             # optional, default 5000

[[airplay_receivers]]
host = "192.168.1.51"   # bedroom
# port defaults to 5000
```

Streams ALAC-encoded audio over RTP to any RAOP-compatible receiver — Apple
TV, HomePod, Airport Express, or
[shairport-sync](https://github.com/mikebrady/shairport-sync). All receivers
share the same `initial_rtptime`, so RTP-level playback synchronisation is
within one frame (~8 ms) across the LAN.

### Squeezelite (Slim Protocol — multi-room)

```
music_dir             = "/path/to/Music"
audio_output          = "squeezelite"
squeezelite_port      = 3483   # Slim Protocol TCP port, default 3483
squeezelite_http_port = 9999   # HTTP PCM broadcast port, default 9999
```

Rockbox acts as a minimal Logitech Media Server. Any number of
[squeezelite](https://github.com/ralph-irving/squeezelite) clients can connect
simultaneously; Rockbox sends a `sync` packet to every client once per second
so they all align to the same playback clock:

```
squeezelite -s localhost -n "Living Room"
squeezelite -s localhost -n "Kitchen"
squeezelite -s localhost -n "Bedroom"
```

Select a specific output device:

```
squeezelite -s localhost -l              # list available devices
squeezelite -s localhost -o ""           # system default
squeezelite -s localhost -o "Built-in Output"
```

```
music_dir            = "/path/to/Music"
audio_output         = "chromecast"
chromecast_host      = "192.168.1.60"  # LAN IP of the target Chromecast
chromecast_port      = 8009            # optional, default 8009 (Cast protocol)
chromecast_http_port = 7881            # optional, default 7881 (WAV HTTP stream)
```

Rockbox streams audio to any Google Cast-compatible device — Google Home,
Chromecast Audio, Chromecast with Google TV, Nest Hub, or third-party Cast
receivers. It uses two channels simultaneously:

* **Cast protocol** (TCP 8009, TLS + Protobuf) — sends playback commands and
  tells the device where to fetch the audio stream.
* **WAV over HTTP** (port 7881) — serves a live `audio/wav` stream with a
  finite `Content-Length` so the Chromecast can show a progress bar and
  auto-advance the queue at track boundaries.

Track metadata (title, artist, album, duration) and album art are pushed to the
device on every track change. Chromecast devices on the LAN are also discovered
automatically via mDNS (`_googlecast._tcp.local.`) and appear in the UI device
picker; connecting through the picker starts the Cast session on demand without
requiring `audio_output = "chromecast"` in the config file.

> **Network requirement**: the Chromecast device must be able to reach port 7881
> on the machine running rockboxd. If rockboxd is inside a VM or container,
> forward that port to the host.

See [`crates/chromecast/README.md`](https://github.com/tsirysndr/rockbox-zig/blob/master/crates/chromecast/README.md) for a detailed
description of the architecture, protocols, and FFI surface.

Rockbox has three independent UPnP/DLNA modes that can be combined freely.

#### PCM sink — stream live audio to a UPnP renderer (Kodi, VLC, …)

```
music_dir          = "/path/to/Music"
audio_output       = "upnp"

# AVTransport controlURL of the target renderer (required for metadata push)
upnp_renderer_url  = "http://192.168.1.x:7777/AVTransport/control"

# Port for the WAV HTTP broadcast server (default: 7879)
upnp_http_port     = 7879
```

Rockbox encodes live PCM as a continuous WAV-over-HTTP stream and commands the
renderer to play it via AVTransport SOAP. Track metadata (title, artist, album,
album art, duration) is sent as DIDL-Lite XML in `SetAVTransportURI` and
auto-refreshed on every track change so the renderer's "Now Playing" display
stays accurate.

> **Finding `upnp_renderer_url`**: start `rockboxd` with `RUST_LOG=info` — it
> scans the LAN on startup and logs `upnp scan: found renderer "…" av=http://…`
> for every discovered renderer.

#### Media Server — expose library to control points (BubbleUPnP, Kodi, …)

```
upnp_server_enabled = true
upnp_server_port    = 7878        # default
upnp_friendly_name  = "Rockbox"  # name shown in apps
```

Starts a ContentDirectory service so control points can browse artists, albums,
and tracks and pull audio directly from Rockbox.

#### MediaRenderer — let control points push media to Rockbox

```
upnp_renderer_enabled = true
upnp_renderer_port    = 7880        # default
upnp_friendly_name    = "Rockbox"
```

Rockbox registers as a `MediaRenderer:1`. Any DLNA control point (BubbleUPnP,
Foobar2000, etc.) can push a URI to Rockbox and control playback remotely.
Incoming DIDL-Lite metadata (title, artist, album, album art, duration) is
parsed and displayed.

| Key | Default | Description |
| --- | --- | --- |
| `audio_output = "upnp"` | — | Enable the PCM → WAV streaming sink |
| `upnp_renderer_url` | — | AVTransport controlURL of the target renderer |
| `upnp_http_port` | `7879` | WAV broadcast HTTP port |
| `upnp_server_enabled` | `false` | Start the ContentDirectory media server |
| `upnp_server_port` | `7878` | Media server HTTP port |
| `upnp_renderer_enabled` | `false` | Start the MediaRenderer endpoint |
| `upnp_renderer_port` | `7880` | MediaRenderer HTTP port |
| `upnp_friendly_name` | `"Rockbox"` | Display name shown to control points |



---

```
echo "deb [trusted=yes] https://apt.fury.io/tsiry/ /" | sudo tee /etc/apt/sources.list.d/fury.list
sudo apt-get update
sudo apt-get install rockbox
```

Add the following to `/etc/yum.repos.d/fury.repo`:

```
[fury]
name=Gemfury Private Repo
baseurl=https://yum.fury.io/tsiry/
enabled=1
gpgcheck=0
```

Then run:

```
brew install tsirysndr/tap/rockbox
```

### Universal (curl installer)

```
curl -fsSL https://raw.githubusercontent.com/tsirysndr/rockbox-zig/HEAD/install.sh | bash
```

---

Pre-built binaries for the latest release are available on the
[Releases page](https://github.com/tsirysndr/rockbox-zig/releases/latest).

| Platform | Architecture | Package |
| --- | --- | --- |
| Linux | x86\_64 | `.tar.gz` |
| Linux | aarch64 | `.tar.gz` |
| macOS | x86\_64 | `.pkg` |
| macOS | aarch64 (Apple Silicon) | `.pkg` |



---

```
rockbox service install    # enable and start
rockbox service uninstall  # stop and disable
rockbox service status     # check status
```

[![Systemd service screenshot](https://private-user-images.githubusercontent.com/15877106/404545879-1fbd2b58-0e29-4db4-9791-6e377de72728.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2Mzg3NDMsIm5iZiI6MTc4MTYzODQ0MywicGF0aCI6Ii8xNTg3NzEwNi80MDQ1NDU4NzktMWZiZDJiNTgtMGUyOS00ZGI0LTk3OTEtNmUzNzdkZTcyNzI4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjE2VDE5MzQwM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY0OWI1NzMwNzQxYTIxYzNjOGZkNDYyZWI4NDM4MDcyYjg1YzMzOTBiYmU5YTc0MmZjOGI0Y2UwNDE0ZjJiZmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.rizxW7QqfF4HmhFlLvUwBgRON5waqwTpdO-jqLCnjGw)](https://private-user-images.githubusercontent.com/15877106/404545879-1fbd2b58-0e29-4db4-9791-6e377de72728.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2Mzg3NDMsIm5iZiI6MTc4MTYzODQ0MywicGF0aCI6Ii8xNTg3NzEwNi80MDQ1NDU4NzktMWZiZDJiNTgtMGUyOS00ZGI0LTk3OTEtNmUzNzdkZTcyNzI4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjE2VDE5MzQwM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY0OWI1NzMwNzQxYTIxYzNjOGZkNDYyZWI4NDM4MDcyYjg1YzMzOTBiYmU5YTc0MmZjOGI0Y2UwNDE0ZjJiZmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.rizxW7QqfF4HmhFlLvUwBgRON5waqwTpdO-jqLCnjGw)

---

**Ubuntu / Debian**

```
sudo apt-get install libsdl2-dev libfreetype6-dev libdbus-1-dev libunwind-dev zip protobuf-compiler cmake libxkbcommon-dev libxkbcommon-x11-dev libxcb1-dev libxcb-render0-dev libxcb-shape0-dev libxcb-xfixes0-dev
```

**Fedora**

```
sudo dnf install SDL2-devel freetype-devel libunwind-devel zip protobuf-compiler cmake libxkbcommon-devel libxkbcommon-x11-devel libxcb-devel
```

**macOS**

```
brew install sdl2 freetype cmake protobuf
```

You also need [Zig](https://ziglang.org/download/) ≥ 0.16 and a recent stable
Rust toolchain (`rustup update stable`).

```
# 1. Clone
git clone https://github.com/tsirysndr/rockbox-zig.git
cd rockbox-zig
git submodule update --init --recursive

# 2. Build the web UI
cd webui/rockbox
deno install
deno run build
cd ../..

# 3. Configure and build the C firmware (one-time setup)
mkdir -p build-lib && cd build-lib
../tools/configure --target=sdlapp --type=N --lcdwidth=320 --lcdheight=240 --prefix=/usr/local
cp ../autoconf/autoconf.h .
make lib
cd ..

# 4. Build Rust crates
cargo build --release -p rockbox-cli -p rockbox-server

# 5. Link everything with Zig
cd zig && zig build
```

The binary is at `zig/zig-out/bin/rockboxd`.

> **Rebuilding after changes**: after editing C code run `make lib` in
> `build-lib`; after editing Rust run `cargo build --release`. Then re-run
> `zig build`. Zig only re-links when the `.a` files are newer than the binary.

### Build the GTK4 desktop app

```
sudo apt-get install flatpak
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install --user flathub org.flatpak.Builder
flatpak install --user flathub org.gnome.Sdk/x86_64/47
flatpak install --user flathub org.gnome.Platform/x86_64/47
flatpak install --user org.freedesktop.Sdk.Extension.rust-stable
flatpak install --user org.freedesktop.Sdk.Extension.llvm18
cd gtk
flatpak run org.flatpak.Builder --user --disable-rofiles-fuse --repo=repo flatpak_app build-aux/io.github.tsirysndr.Rockbox.json --force-clean
flatpak run org.flatpak.Builder --run flatpak_app build-aux/io.github.tsirysndr.Rockbox.json rockbox-gtk
```

---

[![Architecture diagram](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/rockbox-arch.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/rockbox-arch.png)

The Rockbox C firmware (audio engine, codecs, DSP) is compiled into
`libfirmware.a` and linked with two Rust static libraries
(`librockbox_cli.a`, `librockbox_server.a`) and [CPAL](https://github.com/RustAudio/cpal) by the Zig build script.
The result is a single `rockboxd` binary. Rust crates expose the firmware over
gRPC, GraphQL, HTTP, and MPD, and implement output sinks (AirPlay, Squeezelite,
Snapcast) and the Typesense search integration.

---

Open <http://localhost:6062/graphiql> in your browser.

[![](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/graphql.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/graphql.png)

Open <http://localhost:6063> in your browser.

[![](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/http-api.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/http-api.png)

Docs: [buf.build/tsiry/rockboxapis](https://buf.build/tsiry/rockboxapis/docs/main:rockbox.v1alpha1)

Try it live with
[Buf Studio](https://buf.build/studio/tsiry/rockboxapis/rockbox.v1alpha1.LibraryService/GetAlbums?target=http%3A%2F%2Flocalhost%3A6061&selectedProtocol=grpc-web).

[![](https://github.com/tsirysndr/rockbox-zig/raw/master/docs/grpc.png)](https://github.com/tsirysndr/rockbox-zig/blob/master/docs/grpc.png)

---

Full guides, configuration reference, audio-output setup, API reference, and
SDK docs are published at:

**[👉 View full documentation](https://rockboxzig.mintlify.app)**

The Mintlify source lives in [`mintlify/`](https://github.com/tsirysndr/rockbox-zig/blob/master/mintlify). Topics covered:

* **Getting started** — install, quickstart, configuration
* **Audio output** — built-in [CPAL](https://github.com/RustAudio/cpal), [Snapcast](https://github.com/snapcast/snapcast), [AirPlay](https://en.wikipedia.org/wiki/AirPlay), [Squeezelite](https://github.com/ralph-irving/squeezelite), [Chromecast](https://developers.google.com/cast), [UPnP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play)
* **Audio settings** — parametric EQ, DSP, ReplayGain, crossfade
* **Clients** — web UI, desktop apps, MPD, MPRIS
* **API reference** — HTTP REST (auto-generated from OpenAPI), GraphQL, gRPC, MPD
* **SDKs** — TypeScript, Python, Ruby, Elixir, Clojure, Gleam
* **Architecture** — build system, PCM sinks, cross-cutting concerns
* **Reference** — `rockbox` and `rockboxd` CLI, ports, `settings.toml`, troubleshooting, FAQ