---
title: "Y2Z/monolith: ⬛️ CLI tool and library for saving complete web pages as a single HTML file"
source: "https://github.com/Y2Z/monolith"
author:
published:
created: 2026-06-23
description: "⬛️ CLI tool and library for saving complete web pages as a single HTML file - Y2Z/monolith"
tags:
  - "clippings"
---
```
_____    _____________   __________     ___________________    ___
|     \  /             \ |          |   |                   |  |   |
|      \/       __      \|    __    |   |    ___     ___    |__|   |
|              |  |          |  |   |   |   |   |   |   |          |
|   |\    /|   |__|          |__|   |___|   |   |   |   |    __    |
|   | \__/ |          |\                    |   |   |   |   |  |   |
|___|      |__________| \___________________|   |___|   |___|  |___|
```

A data hoarder’s dream come true: bundle any web page into a single HTML file. You can finally replace that gazillion of open tabs with a gazillion of.html files stored somewhere on your precious little drive.

Unlike the conventional “Save page as”, `monolith` not only saves the target document, it embeds CSS, image, and JavaScript assets **all at once**, producing a single HTML5 document that is a joy to store and share.

If compared to saving websites with `wget -mpk`, this tool embeds all assets as data URLs and therefore lets browsers render the saved page exactly the way it was on the Internet, even when no network connection is available.

---

## Installation

#### Using Cargo (cross-platform)

```
cargo install monolith
```

#### Via Homebrew (macOS and GNU/Linux)

```
brew install monolith
```

#### Via Chocolatey (Windows)

```
choco install monolith
```

#### Via Scoop (Windows)

```
scoop install main/monolith
```

#### Via Winget (Windows)

```
winget install --id=Y2Z.Monolith -e
```

#### Via MacPorts (macOS)

```
sudo port install monolith
```

#### Using Snapcraft (GNU/Linux)

```
snap install monolith
```

#### Using Guix (GNU/Linux)

```
guix install monolith
```

#### Using NixPkgs

```
nix-env -iA nixpkgs.monolith
```

#### Using Flox

```
flox install monolith
```

#### Using Pacman (Arch Linux)

```
pacman -S monolith
```

#### Using aports (Alpine Linux)

```
apk add monolith
```

#### Using XBPS Package Manager (Void Linux)

```
xbps-install -S monolith
```

#### Using FreeBSD packages (FreeBSD)

```
pkg install monolith
```

#### Using FreeBSD ports (FreeBSD)

```
cd /usr/ports/www/monolith/
make install clean
```

#### Using pkgsrc (NetBSD, OpenBSD, Haiku, etc)

```
cd /usr/pkgsrc/www/monolith
make install clean
```

#### Using containers

```
docker build -t y2z/monolith .
sudo install -b dist/run-in-container.sh /usr/local/bin/monolith
```

#### From source

Dependencies: `libssl`, `cargo`

Install cargo (GNU/Linux) Check if cargo is installed
```
cargo -v
```

If cargo is not already installed, install and add it to your existing `$PATH` (paraphrasing the [official installation instructions](https://doc.rust-lang.org/cargo/getting-started/installation.html)):

```
curl https://sh.rustup.rs -sSf | sh
. "$HOME/.cargo/env"
```

Proceed with installing from source:

```
git clone https://github.com/Y2Z/monolith.git
cd monolith
make install
```

#### Using pre-built binaries (Windows, ARM-based devices, etc)

Every release contains pre-built binaries for Windows, GNU/Linux, as well as platforms with non-standard CPU architecture.

---

## Usage

```
monolith https://lyrics.github.io/db/P/Portishead/Dummy/Roads/ -o %title%.%timestamp%.html
```
```
cat some-site-page.html | monolith -aIiFfcMv -b https://some.site/ - > some-site-page-with-assets.html
```

---

## Options

- `-a`: Exclude audio sources
- `-b`: Use `custom base URL`
- `-B`: Forbid retrieving assets from specified domain(s)
- `-c`: Exclude CSS
- `-C`: Read cookies from `file`
- `-d`: Allow retrieving assets only from specified `domain(s)`
- `-e`: Ignore network errors
- `-E`: Save document using `custom encoding`
- `-f`: Omit frames
- `-F`: Exclude web fonts
- `-h`: Print help information
- `-i`: Remove images
- `-I`: Isolate the document
- `-j`: Exclude JavaScript
- `-k`: Accept invalid X.509 (TLS) certificates
- `-m`: Output in MHTML format instead of HTML
- `-M`: Don't add timestamp and URL information
- `-n`: Extract contents of NOSCRIPT elements
- `-o`: Write output to `file` (use “-” for STDOUT)
- `-q`: Be quiet
- `-t`: Adjust `network request timeout`
- `-u`: Provide `custom User-Agent`
- `-v`: Exclude videos
- `-V`: Print version number

---

## Whitelisting and blacklisting domains

Options `-d` and `-B` provide control over what domains can be used to retrieve assets from, e.g.:

```
monolith -I -d example.com -d www.example.com https://example.com -o example-only.html
```
```
monolith -I -B -d .googleusercontent.com -d googleanalytics.com -d .google.com https://example.com -o example-no-ads.html
```

---

## Dynamic content

Monolith doesn't feature a JavaScript engine, hence websites that retrieve and display data after initial load may require usage of additional tools.

For example, Chromium (Chrome) can be used to act as a pre-processor for such pages:

```
chromium --headless --window-size=1920,1080 --run-all-compositor-stages-before-draw --virtual-time-budget=9000 --incognito --dump-dom https://github.com | monolith - -I -b https://github.com -o github.html
```

---

## Authentication

```
monolith https://username:password@example.com -o example-basic-auth.html
```

---

## Proxies

Please set `https_proxy`, `http_proxy`, and `no_proxy` environment variables.

---

### Apify Actor Usage

[![Run Monolith Actor on Apify](https://camo.githubusercontent.com/56edb2998968fa5c5be895c73ef204ca64379fda5f7ec9d1c987fbcc12bdf125/68747470733a2f2f61706966792e636f6d2f6578742f72756e2d6f6e2d61706966792e706e67)](https://apify.com/snshn/monolith?fpr=snshn)

You can run Monolith in the cloud without installation using the [Monolith Actor](https://apify.com/snshn/monolith?fpr=snshn) on [Apify](https://apify.com/?fpr=snshn) free of charge.

```
echo '{"urls": ["https://news.ycombinator.com/"]}' | apify call -so snshn/monolith
[{
  "url": "https://news.ycombinator.com/",
  "status": "0",
  "kvsUrl": "https://api.apify.com/v2/key-value-stores/of9xNgvpon4elPLbc/records/https___news.ycombinator.com_"
}]
```

Read more about the [Monolith Actor](https://github.com/Y2Z/monolith/blob/master/.actor/README.md), including how to use it via the Apify UI, API and CLI without installation.

---

## Contributing

Please open an issue if something is wrong, that helps make this project better.

---

## License

To the extent possible under law, the author(s) have dedicated all copyright related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.