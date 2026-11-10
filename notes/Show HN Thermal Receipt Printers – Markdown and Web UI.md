---
title: "Show HN: Thermal Receipt Printers – Markdown and Web UI"
url: https://github.com/sadreck/ThermalMarky
clipped: 2026-06-17 01:31:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - thermal printing
  - markdown parsing
  - hobbyist electronics
  - local web interface
  - embedded tooling
related:
  - "[[Markdown Parsing]]"
  - "[[Hobbyist Electronics]]"
  - "[[Local Web Interface]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** ThermalMarky is a Python-based tool that formats and prints Markdown documents on thermal receipt printers using USB or network connections.
>
> **Key points:**
> - Supports basic Markdown styles along with custom tags for alignment, horizontal dividers, and dynamic QR codes.
> - Exposes a web-based UI editor, a CLI, and Docker setups for printing without complex host driver configuration.
> - Discussion highlights hobbyist interest in receipt printers for physical tasks (to-do lists, puzzles) and hardware troubleshooting.
>
> **Concept links:** [[Thermal Printing]], [[Markdown Parsing]], [[Hobbyist Electronics]], [[Local Web Interface]], [[Embedded Tooling]]
>
> **Suggested connections:**
> - [[Markdown Parsing]] — rendering markup languages for physical or non-standard outputs.
> - [[Hobbyist Electronics]] — repurposing commercial hardware for personal productivity.
> - [[Local Web Interface]] — lightweight self-hosted panels for controlling hardware devices.
<!-- ai-summary:end -->

# [Show HN: Thermal Receipt Printers – Markdown and Web UI](https://github.com/sadreck/ThermalMarky)

## Digest Summary
ThermalMarky is a Python‑based tool that formats Markdown for thermal receipt printers. It supports basic Markdown (headers, bold, underline, lists) plus custom tags for alignment (`[align=center]`), horizontal lines, QR codes, and line effects. Users can print via a web UI with built‑in editor shortcuts, a CLI (`print.py`), or by piping content. Configuration is provided through a `.env` file, specifying printer connection type (USB or network), vendor/product IDs for USB devices, or IP/port for network printers, and printer limits (`MARKY_MAX_LINES`, `MARKY_LINE_WIDTH`). The project is Docker‑ready; `docker compose up --build` launches a HTTPS server on `https://localhost:8000` (self‑signed certificate). Bare‑metal setup requires Python 3.12+, `python-escpos`, and development libraries (`libusb‑1.0‑0-dev`, `libjpeg-dev`, `zlib1g-dev`, `libcups2-dev`). Example usage includes `python print.py file.md`, piping markdown, or `curl` POST requests. Linux USB access may need udev rules or privileged Docker execution. Tested with MUNBYN Thermal Printer / ITPP047UE‑WH‑UK.

## Discussion Summary
The feedback is largely positive, praising the markdown extensions for their clarity and usefulness while expressing enthusiasm for experimenting with thermal printers in personal projects such as todo lists and Sudoku prints. Users share practical experience troubleshooting printers, note the reliability of thermal hardware, and discuss community interest in printer libraries and Discord activity. Requests for affordable Wi‑Fi or Bluetooth 80 mm models and mild caution about paper safety appear alongside a desire for broader HTML/CSS support, reflecting overall constructive interest.

---

## Full Article

🖨️ ThermalMarky - Markdown Thermal Printer
==========================================

Did you ever buy a thermal receipt printer "to do cool stuff" which is now collecting dust? No? Me neither.

But if you have a friend that did, **ThermalMarky** is here to help by supporting basic Markdown features and a basic WebUI to go with it.

* **Markdown Support:** Headers, Bold, Underline, and Lists.
* **Enhanced Formatting:** Custom tags for alignment (`[align=center]`), horizontal lines, and QR Codes.
* **Web UI:** A clean interface with built-in editor shortcuts.
* **CLI Mode:** Print directly from your terminal or pipe content into it.
* **Docker Ready:** You know exactly what this means.

Unfortunately due to the different types of thermal printers out there, you will need to make sure your printer works before trying to use ThermalMarky.

This project has only been tested with [MUNBYN Thermal Printer / ITPP047UE-WH-UK](https://www.amazon.co.uk/Thermal-MUNBYN-Ethernet-Restaurant-Business/dp/B07872SDT9).

Rename `.env.example` to `.env` and fill in the required information.

```
#
# Printer Setup
#

# Printer Connection: usb or network
MARKY_TYPE=usb

# USB, get this information by running `lsusb` while your printer is connected. You should see something like this:
#
# Bus 001 Device 094: ID 04b8:0e20 Seiko Epson Corp. TM-m30-ii
MARKY_VENDOR_ID=0x04b8
MARKY_PRODUCT_ID=0x0e20

# Network, how you get this information depends on which printer you have.
MARKY_IP=192.168.1.100
MARKY_PORT=9100

#
# Configuration Setup
#

# Number of lines to print before truncating output to avoid printing out LOTR.
MARKY_MAX_LINES=30

# Max line width supported by the printer for text-wrapping.
MARKY_LINE_WIDTH=48

# ESC/POS text font. Try `a` or `b`. `b` is commonly the smaller text font.
MARKY_FONT=a
```

You can also override configuration via the contents of the data to be printed, by enclosing it in `<!-- -->`.

```
<!--
MARKY_FONT=b
MARKY_LINE_WIDTH=64
-->
# Hello World!

This will be printed in font 'b' and max line width will be 64!
```

Running with Docker (Recommended)
---------------------------------

Docker is the easiest way to get ThermalMarky up and running, especially for managing USB permissions.

**Build and Start:**

```
docker compose up --build
```

**Access the UI:**
Open `https://localhost:8000` in your browser.
*(Note: Uses self-signed certificates in `certs/` for secure transport)*

If you prefer to run it bare-metal, follow these steps:

* Python 3.12+
* System libraries (for `python-escpos`):

```
sudo apt install libusb-1.0-0-dev libjpeg-dev zlib1g-dev libcups2-dev python3-dev gcc
```

**Install Dependencies:**

```
python3 -m venv .venv
pip install -r requirements.txt
. .venv/bin/activate
```

**Launch the Web Server:**

You can print files directly without the web interface:

```
# Print a file
python print.py my_list.md

# Pipe content directly
echo "# Hello World" | python print.py

# HTTP request
curl --insecure -X POST "https://127.0.0.1:8000/print" -d "markdown=$(cat my-message.md)"
# or
curl --insecure -X POST "https://127.0.0.1:8000/print" --data-urlencode "markdown@my-message.md"
```

Beyond standard Markdown, ThermalMarky supports special tags:

| Tag | Description |
| --- | --- |
| `**word**` | Bold |
| `__word__` | Underline |
| `#` | H1 |
| `##` | H2 |
| `[align=center]` | Center-align the following text (also `left`, `right`) |
| `[qr=https://...]` | Generate and print a QR code |
| `[effect=line--]` | Print a horizontal line of dashes |
| `[effect=line-*]` | Print a horizontal line of asterisks |

```
[align=center]# Thermal Marky

This is **very important** but this __not so much__.

[align=right]This is on the right

[effect=line--]

[align=center][qr=https://github.com/sadreck/ThermalMarky]
```

[![Printer UI](https://github.com/sadreck/ThermalMarky/raw/main/ui.png)](https://github.com/sadreck/ThermalMarky/blob/main/ui.png)

**Result**

[![Printer Sample](https://github.com/sadreck/ThermalMarky/raw/main/sample.png)](https://github.com/sadreck/ThermalMarky/blob/main/sample.png)

* **USB Permissions:** On Linux, you might need to add a udev rule or run with `sudo` if the printer isn't detected. Docker-compose handles this by running as `privileged`.
* **Certificates:** The web server uses HTTPS. If your browser warns you about the certificate, it's because it's self-signed for local use.