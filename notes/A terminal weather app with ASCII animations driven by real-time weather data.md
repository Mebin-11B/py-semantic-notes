---
title: "A terminal weather app with ASCII animations driven by real-time weather data"
url: https://github.com/Veirt/weathr
clipped: 2026-06-17 01:43:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A terminal weather app with ASCII animations driven by real-time weather data](https://github.com/Veirt/weathr)

## Digest Summary
The repository Veirt/weathr on GitHub is a terminal‑based weather application that renders weather data using ASCII‑style animation. The page currently shows a “You can’t perform that action at this time” notice, indicating restricted access. Visual elements referenced include badges for the crate on crates.io, download statistics, and licensing information, as well as example animations such as “Thunderstorm Night” and “Snow”. Additional images consist of avatar icons for contributors or collaborators identified by handles @Veirt, @Levizor, @natedenh, @claude, @greyltc, @marcohoovy, and @OrbitalPeriod. No further descriptive text, code snippets, or functional details are present in the scraped content.

## Discussion Summary
The comments express largely positive reactions to the terminal‑based projects, praising the visual details such as animated lightning and snow effects and noting the appeal of a clean, grid‑driven layout. Users discuss workflow choices, favoring Zellij for remote session continuity while still appreciating Ghostty’s features. There is interest in learning terminal animation techniques and curiosity about Rust’s growing role in similar tools. Overall sentiment is enthusiastic, with agreement on the projects’ aesthetic and functional strengths and modest technical curiosity.

---

## Full Article

[![Crates.io](https://camo.githubusercontent.com/51e431dc7a58fee82b0402a4d7ecbaf612394c776d527d60fad03530d92b6c19/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f7765617468722e737667)](https://crates.io/crates/weathr)
[![Downloads](https://camo.githubusercontent.com/254a77f209443e3442391dcff60e3b98e9666225aaa589cccb066f23a4463425/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f642f7765617468722e737667)](https://crates.io/crates/weathr)
[![License](https://camo.githubusercontent.com/55aba74869fcaaceed18e2e38785d9ac98c160b6c2284481de7c873b182b5228/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f6c2f7765617468722e737667)](https://github.com/veirt/weathr/blob/main/LICENSE)

A terminal weather app with ASCII animations driven by real-time weather data.

Features real-time weather from Open-Meteo with animated rain, snow, thunderstorms, flying airplanes, day/night cycles, and auto-location detection.

[![Thunderstorm night demo](https://github.com/Veirt/weathr/raw/main/docs/thunderstorm-night.gif)](https://github.com/Veirt/weathr/blob/main/docs/thunderstorm-night.gif)

[![Snow demo](https://github.com/Veirt/weathr/raw/main/docs/snow.gif)](https://github.com/Veirt/weathr/blob/main/docs/snow.gif)

[![Night demo](https://github.com/Veirt/weathr/raw/main/docs/night.gif)](https://github.com/Veirt/weathr/blob/main/docs/night.gif)

[![Packaging status](https://camo.githubusercontent.com/3f6c3ff6eba8daa0ef8ba2f06a4a3d4322026c1161c05adabec49e34fcefc7c2/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f766572746963616c2d616c6c7265706f732f7765617468722e737667)](https://repology.org/project/weathr/versions)  
[![Winget](https://camo.githubusercontent.com/bfee88763053787d4a862bd38d33606b4f399343f7d4ebb726d7c5352269411b/68747470733a2f2f696d672e736869656c64732e696f2f77696e6765742f762f56656972742e776561746872)](https://camo.githubusercontent.com/bfee88763053787d4a862bd38d33606b4f399343f7d4ebb726d7c5352269411b/68747470733a2f2f696d672e736869656c64732e696f2f77696e6765742f762f56656972742e776561746872)

### Quick Install (macOS, Linux, FreeBSD)

Download and install the latest binary with one command:

```
curl -fsSL https://raw.githubusercontent.com/Veirt/weathr/main/install.sh | sh
```

You need Rust installed.

```
git clone https://github.com/veirt/weathr.git
cd weathr
cargo install --path .
```

Run the published image from GHCR:

```
docker run --rm -it ghcr.io/veirt/weathr:latest
```

Mount your config if you want to use your existing settings:

```
docker run --rm -it \
  -v "$HOME/.config/weathr:/.config/weathr:ro" \
  ghcr.io/veirt/weathr:latest
```

Build the image locally:

Run it interactively so the TUI can access your terminal:

```
docker run --rm -it weathr
```

Mount your config if you want to use your existing settings:

```
docker run --rm -it \
  -v "$HOME/.config/weathr:/.config/weathr:ro" \
  weathr
```

```
brew install Veirt/veirt/weathr
```

Available in AUR:

or

Available as a flake:

```
inputs = {
    weathr.url = "github:Veirt/weathr";
};
```

Add to packages:

```
environment.systemPackages = [
    inputs.weathr.packages.${system}.default
];
```

or use home-manager module option:

```
imports = [
    inputs.weathr.homeModules.weathr
];

programs.weathr = {
    enable = true;
    settings = {
        hide_hud = true;
    };
};
```

Available through Winget:

```
winget install -i Veirt.weathr
```

The config file location depends on your platform:

* **Linux**: `~/.config/weathr/config.toml` (or `$XDG_CONFIG_HOME/weathr/config.toml`)
* **macOS**: `~/Library/Application Support/weathr/config.toml`
* **Windows**: `~/AppData/Roaming/weathr/config.toml`

```
# Linux
mkdir -p ~/.config/weathr

# macOS
mkdir -p ~/Library/Application\ Support/weathr

# Windows (PowerShell)
New-Item -Path $env:APPDATA/weathr -Type Directory

# Windows (Command Prompt)
mkdir %APPDATA%/weathr
```

Edit the config file at the appropriate path for your platform:

```
# Hide the HUD (Heads Up Display) with weather details
hide_hud = false

# Run silently without startup messages (errors still shown)
silent = false

[location]
# Location coordinates (overridden if auto = true)
latitude = 52.5200
longitude = 13.4050

# Auto-detect location via IP (defaults to true if config missing)
auto = false

# Hide the location name in the UI
hide = false

# How to display the location in the HUD: "coordinates" | "city" | "mixed"
display = "mixed"

# Optional: manually override the city name shown in the HUD.
# When set, skips reverse geocoding entirely.
# city = "Berlin"

# Language for the resolved city name. "auto" uses the locale of the coordinates.
# Accepts BCP-47 language tags: "en", "de", "ru", "ja", etc.
# city_name_language = "auto"

[units]
# Temperature unit: "celsius" or "fahrenheit"
temperature = "celsius"

# Wind speed unit: "kmh", "ms", "mph", or "kn"
wind_speed = "kmh"

# Precipitation unit: "mm" or "inch"
precipitation = "mm"
```

The `display` option controls how the location appears in the HUD. City names are resolved
via reverse geocoding (Nominatim/OpenStreetMap). When a city cannot be resolved (e.g. open
sea or no Nominatim match), all modes fall back to showing coordinates.

| Mode | City resolved | City not resolved |
| --- | --- | --- |
| `coordinates` | `Location: 52.52°N, 13.41°E` | `Location: 52.52°N, 13.41°E` |
| `city` | `Location: Berlin` | `Location: 52.52°N, 13.41°E` |
| `mixed` | `Location: Berlin (52.52°N, 13.41°E)` | `Location: 52.52°N, 13.41°E` |

```
# Tokyo, Japan
latitude = 35.6762
longitude = 139.6503

# Sydney, Australia
latitude = -33.8688
longitude = 151.2093
```

Run with real-time weather:

Simulate weather conditions for testing:

```
# Simulate rain
weathr --simulate rain

# Simulate snow at night
weathr --simulate snow --night

# Clear day with falling leaves
weathr --simulate clear --leaves
```

Available weather conditions:

* Clear Skies: `clear`, `partly-cloudy`, `cloudy`, `overcast`
* Precipitation: `fog`, `drizzle`, `rain`, `freezing-rain`, `rain-showers`
* Snow: `snow`, `snow-grains`, `snow-showers`
* Storms: `thunderstorm`, `thunderstorm-hail`

Override configuration:

```
# Use imperial units (°F, mph, inch)
weathr --imperial

# Use metric units (°C, km/h, mm) - default
weathr --metric

# Auto-detect location via IP
weathr --auto-location

# Hide location coordinates
weathr --hide-location

# Hide status HUD
weathr --hide-hud

# Run silently (suppress non-error output)
weathr --silent

# Combine flags
weathr --imperial --auto-location
```

* `q` or `Q` - Quit
* `Ctrl+C` - Exit

The application respects several environment variables:

* `NO_COLOR` - When set, disables all color output (accessibility feature)
* `COLORTERM` - Detects truecolor support (values: "truecolor", "24bit")
* `TERM` - Used for terminal capability detection (e.g., "xterm-256color")

Examples:

```
# Disable colors for accessibility
NO_COLOR=1 weathr
```

When using `auto = true` in config or the `--auto-location` flag, the application makes a request to `ipinfo.io` to detect your approximate location based on your IP address.

This is optional. You can disable auto-location and manually specify coordinates in your config file to avoid external API calls.

GPL-3.0-or-later

Weather data provided by [Open-Meteo.com](https://open-meteo.com/) under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

City name resolution powered by [Nominatim](https://nominatim.openstreetmap.org/) (OpenStreetMap).
Data © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), licensed under [ODbL](https://opendatacommons.org/licenses/odbl/).

* **Source**: <https://www.asciiart.eu/>
* **House**: Joan G. Stark
* **Airplane**: Joan G. Stark
* **Sun**: Hayley Jane Wakenshaw (Flump)
* **Moon**: Joan G. Stark

*Note: If any ASCII art is uncredited or misattributed, it belongs to the original owner.*