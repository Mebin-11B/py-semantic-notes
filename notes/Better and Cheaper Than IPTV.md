---
title: "Better and Cheaper Than IPTV"
url: https://github.com/stupside/castor
clipped: 2026-08-31 12:22:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Better and Cheaper Than IPTV](https://github.com/stupside/castor)

## Digest Summary
Castor is a command‑line tool that extracts video streams from arbitrary web pages, transcodes them with ffmpeg, and casts the real‑time stream to any DLNA/UPnP MediaRenderer (e.g., Smart TVs, Kodi, VLC, Plex). It launches headless Chrome with randomized fingerprints and stealth scripts, monitors network traffic via the Chrome DevTools Protocol, solves simple Cloudflare Turnstiles, and selects the largest iframe to locate the video URL. Castor supports direct stream URLs, IMDB/TMDB IDs, and can burn auto‑generated subtitles using whisper.cpp.

Installation options:
- Native binary via Homebrew (`brew install --cask stupside/tap/castor`) requiring Chrome/Chromium, ffmpeg, ffprobe on PATH.
- Docker image (`ghcr.io/stupside/castor`) that bundles dependencies; must run with `--network host` on a Linux host for LAN discovery.

Configuration is a minimal `config.yaml` specifying the TV name and source proxies; optional TMDB API key enables an interactive TUI for browsing titles. Core commands include `castor scan`, `castor cast movie `, `castor cast url `, and debugging flags. The tool does not host content and relies on user‑provided sources.

---

## Full Article

[Skip to content](https://github.com/stupside/castor#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [stupside](https://github.com/stupside)    
    /
    
      [castor](https://github.com/stupside/castor)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fstupside%2Fcastor)    You must be signed in to change notification settings

  

  
- 
          [Fork
    80](https://github.com/login?return_to=%2Fstupside%2Fcastor)
  

  
- 
        
        [Star
          2.2k](https://github.com/login?return_to=%2Fstupside%2Fcastor)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/stupside/castor/branches)[Tags](https://github.com/stupside/castor/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[153 Commits](https://github.com/stupside/castor/commits/main/)153 Commits

## Folders and files

NameNameLast commit messageLast commit date[.githooks](https://github.com/stupside/castor/tree/main/.githooks)[.githooks](https://github.com/stupside/castor/tree/main/.githooks)  [.github](https://github.com/stupside/castor/tree/main/.github)[.github](https://github.com/stupside/castor/tree/main/.github)  [cmd](https://github.com/stupside/castor/tree/main/cmd)[cmd](https://github.com/stupside/castor/tree/main/cmd)  [internal](https://github.com/stupside/castor/tree/main/internal)[internal](https://github.com/stupside/castor/tree/main/internal)  [scripts](https://github.com/stupside/castor/tree/main/scripts)[scripts](https://github.com/stupside/castor/tree/main/scripts)  [third_party](https://github.com/stupside/castor/tree/main/third_party)[third_party](https://github.com/stupside/castor/tree/main/third_party)  [.dockerignore](https://github.com/stupside/castor/blob/main/.dockerignore)[.dockerignore](https://github.com/stupside/castor/blob/main/.dockerignore)  [.envrc](https://github.com/stupside/castor/blob/main/.envrc)[.envrc](https://github.com/stupside/castor/blob/main/.envrc)  [.gitignore](https://github.com/stupside/castor/blob/main/.gitignore)[.gitignore](https://github.com/stupside/castor/blob/main/.gitignore)  [.gitmodules](https://github.com/stupside/castor/blob/main/.gitmodules)[.gitmodules](https://github.com/stupside/castor/blob/main/.gitmodules)  [.release-please-manifest.json](https://github.com/stupside/castor/blob/main/.release-please-manifest.json)[.release-please-manifest.json](https://github.com/stupside/castor/blob/main/.release-please-manifest.json)  [CHANGELOG.md](https://github.com/stupside/castor/blob/main/CHANGELOG.md)[CHANGELOG.md](https://github.com/stupside/castor/blob/main/CHANGELOG.md)  [CONTRIBUTING.md](https://github.com/stupside/castor/blob/main/CONTRIBUTING.md)[CONTRIBUTING.md](https://github.com/stupside/castor/blob/main/CONTRIBUTING.md)  [Dockerfile](https://github.com/stupside/castor/blob/main/Dockerfile)[Dockerfile](https://github.com/stupside/castor/blob/main/Dockerfile)  [LICENSE](https://github.com/stupside/castor/blob/main/LICENSE)[LICENSE](https://github.com/stupside/castor/blob/main/LICENSE)  [Makefile](https://github.com/stupside/castor/blob/main/Makefile)[Makefile](https://github.com/stupside/castor/blob/main/Makefile)  [README.md](https://github.com/stupside/castor/blob/main/README.md)[README.md](https://github.com/stupside/castor/blob/main/README.md)  [SECURITY.md](https://github.com/stupside/castor/blob/main/SECURITY.md)[SECURITY.md](https://github.com/stupside/castor/blob/main/SECURITY.md)  [config.yaml](https://github.com/stupside/castor/blob/main/config.yaml)[config.yaml](https://github.com/stupside/castor/blob/main/config.yaml)  [docker-bake.hcl](https://github.com/stupside/castor/blob/main/docker-bake.hcl)[docker-bake.hcl](https://github.com/stupside/castor/blob/main/docker-bake.hcl)  [go.mod](https://github.com/stupside/castor/blob/main/go.mod)[go.mod](https://github.com/stupside/castor/blob/main/go.mod)  [go.sum](https://github.com/stupside/castor/blob/main/go.sum)[go.sum](https://github.com/stupside/castor/blob/main/go.sum)  [main.go](https://github.com/stupside/castor/blob/main/main.go)[main.go](https://github.com/stupside/castor/blob/main/main.go)  [release-please-config.json](https://github.com/stupside/castor/blob/main/release-please-config.json)[release-please-config.json](https://github.com/stupside/castor/blob/main/release-please-config.json)  View all files

## Repository files navigation

  

  

  
  
  
  
  

# Castor

Smart TVs won't cast arbitrary web video, and screen mirroring is laggy and drops resolution. Castor casts the real stream instead, at full quality, from your terminal.

Point Castor at a web page you are watching, or at a direct stream URL, and it finds the video, extracts the stream, transcodes it for your TV, and casts in real time. It can also resolve an IMDB/TMDB id against sources you configure yourself, and burn in auto-generated subtitles.

To extract, it launches headless Chrome and watches network traffic over the Chrome DevTools Protocol, then runs a short action pipeline to start playback: click the page, navigate into the largest iframe, and click again as a fallback. This works on pages that allow automated playback, and won't work everywhere.

A general-purpose casting tool: it casts only what you point it at. See [Purpose and disclaimer](https://github.com/stupside/castor#purpose-and-disclaimer).

  
  
  Run  `castor cast`  to browse titles and cast, without leaving the terminal.

## Installation

Run Castor as a native binary (recommended): it runs on your machine, so it shares your TV's network, which device discovery needs. The binary shells out to three tools that must be on your  `PATH` :

Tool
Version
Used for

Chrome / Chromium
Any recent
Headless stream extraction

ffmpeg
7.1+
Transcoding (and stream copy)

ffprobe
7.1+
Source format detection

ffmpeg and ffprobe must be 7.1 or newer: Castor uses flags ( `-readrate_initial_burst` , stricter HLS extension handling) that older builds reject. The [Docker image](https://github.com/stupside/castor#docker-optional) bundles a suitable build (Linux only).

### Homebrew (macOS)

 `brew install --cask stupside/tap/castor` 

Build from source (needs Go 1.26+ and cmake)

The whisper.cpp bindings are cgo and link a locally built  `libwhisper.a` , so clone with submodules and build with  `make` :
 `git clone --recurse-submodules https://github.com/stupside/castor.git
cd castor
make          # builds libwhisper.a, then the castor binary` 

 `go install`  won't work: the vendored whisper.cpp bindings come in through a local  `replace`  and need that prebuilt static lib.

## Quick start

Tell Castor which TV to use: find its name with  `castor scan`  and put it in  `config.yaml` .
 `device:
  name: "Living Room TV"   # exact name from `castor scan`
  type: dlna` 

### Can't discover the device? Pin it by address

If  `castor scan`  finds nothing, point Castor straight at the device by IP and it skips discovery:
 `device:
  name: "Living Room TV"   # now just a label
  type: dlna
  host: 192.168.0.3        # the device's LAN IP` 

Discovery uses SSDP/mDNS multicast, which doesn't cross VLANs/subnets and is blocked on Android/Termux (you'll see  `netlinkrib: permission denied` ). A pinned  `host`  reaches the device by unicast instead, so it works across those networks and skips the discovery wait on every cast.

- DLNA  `host`  is the device IP; Castor asks it for its description over a single unicast request. If your TV doesn't answer that, set  `host`  to its full description URL instead (e.g.  `http://192.168.0.3:9197/dmr` ).

- Chromecast / Roku  `host`  is the device IP.

On Android/Termux, also leave  `network.interface`  empty (the default): pinning one needs the same blocked interface lookup.

Now cast a page you are watching, or a stream URL you have:
 `castor cast player https://example.com/watch/some-video` 

For the interactive browser, which searches titles and casts them for you, add a TMDB key and a source (see [Configuration](https://github.com/stupside/castor#configuration)), then run  `castor cast` :

  

The commands you'll use most (run  `castor --help`  for all flags):

Command
What it does

 `castor scan` 
List cast targets on your network

 `castor cast` 
Browse titles and cast, interactively (needs a TMDB key)

 `castor cast player <url>` 
Cast a web page that has an embedded video player

 `castor cast url <url>` 
Cast a direct stream or video URL

 `castor cast movie <id>` 
Resolve a movie id against your sources and cast

 `castor cast episode <id> --season N --episode N` 
Resolve a TV episode and cast

## Configuration

Castor reads  `config.yaml`  from the working directory (or  `--config <path>` ). The only required key is the  `device`  shown in [Quick start](https://github.com/stupside/castor#quick-start); everything else (timeouts, probing, capture, transcoding, network interface, Chrome discovery) has working defaults.

Tip

Keep secrets like your TMDB key out of the committed file: put them in a git-ignored  `config.local.yaml`  that overlays  `config.yaml` , or in  `CASTOR_SECTION__FIELD`  environment variables. See [SECURITY.md](https://github.com/stupside/castor/blob/main/SECURITY.md).

Everything below is optional.

Sources: resolve movie / episode ids against sites you configure

 `cast movie` ,  `cast episode` , and the interactive browser resolve a title id against sources you configure. Castor bundles none, so add your own (sites you are authorized to use). There is no catalog and no lookup: Castor substitutes the id into the  `templates`  you write, prefixes each of your  `proxies` , and opens the resulting page, then extracts the stream exactly like  `cast player` . For example,  `castor cast movie tt12300742`  opens  `https://your-source.example/embed/movie/tt12300742` .
 `sources:
  - proxies: ["https://your-source.example"]   # base URLs, tried in order
    templates:
      movie: "/embed/movie/{itemID}"
      episode: "/embed/tv/{itemID}/{season}-{episode}"` 

Cast: force a local relay with  `delivery` 

Castor decides per source whether the device fetches the stream itself or Castor relays it: a source that only answers with the headers Castor captured is always relayed, since a device is handed the URL and none of those headers. A few sources look fetchable and are refused anyway, typically an HLS playlist whose segments are served under a disguised extension ( `.jpg`  with  `image/jpeg` ), which Castor reads fine but a Chromecast rejects, showing the idle Cast icon. Nothing in the stream reveals this, so  `delivery: serve`  is how you say it.
 `cast:
  delivery: serve   # always relay; "auto" (the default) decides per source` 

Relaying spends this machine's bandwidth and CPU on every cast, so try it as a one-off first:  `CASTOR_CAST__DELIVERY=serve castor cast url <url>` . Any key works that way, e.g.  `CASTOR_RESOLVER__MAX_HEIGHT=720` .

Resolver: cap resolution with  `max_height` 

Source selection and stream probing. All options have sensible defaults; you normally only set  `max_height`  to your TV's vertical resolution, which caps both the selected stream and the encoder output.
 `resolver:
  # The tallest video to cast. Source selection prefers the largest stream no
  # taller than this, and the encoder scales its output down to it. Defaults to
  # 1080; raise it to your TV's native height (e.g. 2160 for a 4K panel) to pass
  # 4K through, or lower it to save bandwidth.
  max_height: 2160
  # hls_timeout: 30s
  # probe_timeout: 30s
  # probe_max_concurrency: 2
  # ffprobe_path: ffprobe` 

TMDB: API key for the interactive browser

The interactive browser ( `castor cast` ) uses a TMDB API key to search titles; direct commands like  `cast movie <id>`  do not need it. Get a free key from [themoviedb.org](https://www.themoviedb.org/settings/api) and keep it in  `config.local.yaml` :
 `tmdb:
  api_key: "<KEY>"` 

Subtitles: auto-transcribe with whisper and burn in (off by default)

Auto-generated subtitles, transcribed with whisper and burned into the video:
 `whisper:
  enable: true             # off by default
  # language: "fr"         # default: English
  # model_path: ""         # default: ggml-tiny.en (~75 MB, auto-downloaded)` 

Roku: cast to a Roku TV or player (one-time Developer Mode setup)

Roku devices are not DLNA renderers, so Castor reaches them over Roku's ECP (External Control Protocol). Roku has no supported way to play an arbitrary URL from a preinstalled app, so Castor ships a tiny channel of its own and plays through it. A source Roku already accepts (HLS, MP4, MKV) is passed straight through; anything else is remuxed to live HLS on the fly.
 `device:
  name: "Living Room"   # the Roku's name, from `castor scan`
  type: roku
  roku:
    # Only needed the first time, to sideload Castor's channel (see below).
    password: "<dev-web-server-password>"` 

Sideloading the channel uses Roku's developer web server, which you turn on by hand once (there is no remote API for it):

- On the Roku remote press Home x3, Up x2, Right, Left, Right, Left, Right.

- Enable developer mode and set a web-server password (the device reboots).

- Put that password in  `device.roku.password`  (keep it in a git-ignored  `config.local.yaml` , or set  `CASTOR_DEVICE__ROKU__PASSWORD` ).

On the first cast Castor sideloads its channel automatically; later casts reuse it. If you publish the channel to your account instead, set  `device.roku.app_id`  to its numeric id (no dev mode or password needed).

[!NOTE]
Roku's live playback is a sliding-window HLS stream and stays roughly 30 s behind the live edge, so expect a longer start delay and more latency than DLNA.

## Supported devices

Run  `castor scan`  to list what is on your network.

Protocol
Works with
Status

DLNA / UPnP ( `MediaRenderer:1` )
Virtually every smart TV from the last decade (Samsung, LG, Sony Bravia, Panasonic Viera, Philips, Hisense, TCL, VIZIO, Sharp), plus networked players like Kodi, VLC, and Plex
Tested on Samsung

Chromecast
Google Cast devices
Experimental, untested (contributions welcome)

Roku
Roku TVs and streaming players (via a sideloaded channel over ECP)
Experimental, untested (contributions welcome)

## Docker (optional)

The prebuilt  `ghcr.io/stupside/castor`  image bundles Chrome, ffmpeg, and ffprobe, so you install nothing by hand. Run it on a Linux host on the same LAN as your TV.

Warning

 `--network host`  is required: device discovery (SSDP multicast) and the TV streaming back from Castor both need the container on your real LAN. On Docker Desktop (macOS/Windows) that flag is a no-op, so the container never reaches your TV and  `scan`  finds nothing. Use the [native binary](https://github.com/stupside/castor#homebrew-macos) there instead.

 `# Discover devices (no config needed)
docker run --rm --network host ghcr.io/stupside/castor:latest scan

# Cast, passing the Intel GPU through for hardware transcoding
docker run --rm --network host --device /dev/dri \
  -v "$PWD/config.yaml:/config.yaml" \
  -v castor-cache:/root/.cache \
  ghcr.io/stupside/castor:latest \
  cast player https://example.com/watch/some-video` 

 `--device /dev/dri`  hands the container your Intel GPU for VA-API hardware H.264 encoding; without it (or on a non-Intel host) Castor falls back to software  `libx264` . Either way, when your TV already accepts the source video Castor stream-copies it and skips encoding entirely.

Run commands from the directory holding your  `` [config.yaml](https://github.com/stupside/castor/blob/main/config.yaml) (mounted at  `/config.yaml` ). The  `castor-cache`  volume persists the auto-downloaded whisper models.

Tag
Build

 `:latest` 
Latest stable release

 `:canary` 
Latest preview build

 `:v1.7.0` 
A specific pinned version

## Purpose and disclaimer

Castor is a general-purpose caster, not a service tied to any particular site.

- It hosts nothing. No bundled video, catalog, or sources: Castor casts only a page, stream URL, or source you supply and are authorized to use, much like a Chromecast.

- It does not touch DRM. Castor does not decrypt or circumvent DRM, and cannot cast DRM-protected services.

- Using it lawfully is your responsibility. Whether a site's terms of use and your local law allow what you do with Castor is on you. Do not use it to infringe copyright.

Castor is provided as-is for lawful, personal, and educational use.

## Contributing

See [CONTRIBUTING.md](https://github.com/stupside/castor/blob/main/CONTRIBUTING.md).

## About

Point it at any web page and it finds the video, extracts the stream, transcodes it and casts in real time to your TV. It even burns subtitles….

### Topics

[chromecast](https://github.com/topics/chromecast)[dlna](https://github.com/topics/dlna)[ffmpeg](https://github.com/topics/ffmpeg)[iptv](https://github.com/topics/iptv)[streaming](https://github.com/topics/streaming)[video](https://github.com/topics/video)

### Resources

[Readme](https://github.com/stupside/castor#readme-ov-file)[MIT license](https://github.com/stupside/castor#MIT-1-ov-file)

### Contributing

[Contributing](https://github.com/stupside/castor#contributing-ov-file)

### Security policy

[Security policy](https://github.com/stupside/castor#security-ov-file)[Activity](https://github.com/stupside/castor/activity)

### Stars

2.2k stars

### Watchers

4 watching

### Forks

[80 forks](https://github.com/stupside/castor/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fstupside%2Fcastor&report=stupside+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
