---
title: "Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine"
url: https://github.com/gainsec/autoprober
clipped: 2026-06-17 01:16:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://github.com/gainsec/autoprober)

## Digest Summary
AutoProber is an open‑source flying‑probe automation stack for hardware hacking, providing end‑to‑end target discovery, microscope mapping, safety‑monitored CNC motion, and controlled pin probing. The system is operated via a Flask web dashboard, Python scripts, or an autonomous agent, and includes Python control code, CAD files for a printable toolhead, and documentation. Core hardware comprises a GRBL‑compatible 3018‑style CNC controller (USB serial), a USB microscope served by mjpg_streamer, a Siglent oscilloscope (LAN/SCPI) for safety monitoring on Channel 4 and measurement on Channel 1, an optical endstop wired to the oscilloscope, and optional LAN‑controlled power outlet. Safety rules require continuous monitoring of Channel 4; any trigger, ambiguous voltage, CNC alarm, or limit pin forces an immediate stop, with manual operator recovery. Workflow: ingest project, connect hardware, run homing and calibration, attach probe, detect target, capture and stitch microscope frames with XYZ logging, annotate map, approve probe points on the dashboard, then execute bounded probe motions. Configuration is via environment files; runtime values include log path, calibration root, microscope URL, and oscilloscope host/port. The code is released under the PolyForm Non‑commercial License; commercial use requires a paid license.

## Discussion Summary
The comments recognize the demo as technically interesting but largely view it as premature for practical use. Concerns focus on the difficulty of achieving sub‑millimeter precision with a probabilistic AI, the lack of real probing hardware, and missing details on how the agent interprets designs. Several users note that commercial flying‑probe systems already exist and question the added cost and nondeterminism of an AI‑controlled approach, while a minority express enthusiasm about the concept’s creative potential. Overall sentiment is skeptical yet curious about future development.

---

## Full Article

AutoProber is the hardware hacker's flying probe automation stack for giving
your agent everything it needs to go from "there's a new target on the plate"
to probing individual pins in a safe way.

[![AutoProber assembly](https://github.com/GainSec/AutoProber/raw/main/docs/images/autoprober-assembly-2.jpg)](https://github.com/GainSec/AutoProber/blob/main/docs/images/autoprober-assembly-2.jpg)

Demo video: <https://gainsec.com/autoprober-demo-mp4/>

1. Tell the agent to ingest the project.
2. Connect all the hardware.
3. Tell the agent to confirm that all parts are functioning.

[![Top of the AutoProber web dashboard](https://github.com/GainSec/AutoProber/raw/main/docs/images/Public-Release-Images/TopofWebDash.png)](https://github.com/GainSec/AutoProber/blob/main/docs/images/Public-Release-Images/TopofWebDash.png)

4. Have it run homing and then calibration.
5. Attach the custom probe and microscope header.
6. Tell the agent that there is a new target on the plate.
7. It will find where the target is on the plate, then take individual frames,
   keeping a record of the XYZ while noting pads, pins, chips, and other
   interesting features.

[![Detected labels and target features](https://github.com/GainSec/AutoProber/raw/main/docs/images/Public-Release-Images/labels.png)](https://github.com/GainSec/AutoProber/blob/main/docs/images/Public-Release-Images/labels.png)

8. It will stitch the frames together and annotate the map, including pins and
   interesting components it identified.

[![Annotated map view](https://github.com/GainSec/AutoProber/raw/main/docs/images/Public-Release-Images/mapview.png)](https://github.com/GainSec/AutoProber/blob/main/docs/images/Public-Release-Images/mapview.png)

9. It will add probe targets to the web dashboard for you to approve or deny.

[![Probe review dashboard section](https://github.com/GainSec/AutoProber/raw/main/docs/images/Public-Release-Images/bottomdash.png)](https://github.com/GainSec/AutoProber/blob/main/docs/images/Public-Release-Images/bottomdash.png)

10. It will probe the approved targets and report back.

All hardware can be controlled through the web dashboard, Python scripts, or by
the agent itself.

[![Manual controls and hardware panels](https://github.com/GainSec/AutoProber/raw/main/docs/images/Public-Release-Images/MidofDash1.png)](https://github.com/GainSec/AutoProber/blob/main/docs/images/Public-Release-Images/MidofDash1.png)

This repo is a self-contained source-available release candidate. It contains
the Python control code, dashboard, CAD files, and documentation needed to
create your own AutoProber.

This project can move physical hardware. Treat it as a machine-control system,
not a normal web app.

The required safety design is:

* GRBL `Pn:P` is ignored. The CNC probe pin is not a trusted endstop.
* The independent safety endstop is read from oscilloscope Channel 4.
* Channel 4 must be continuously monitored during any motion.
* Any Channel 4 trigger, ambiguous voltage, CNC alarm, or real X/Y/Z limit pin
  is a stop condition.
* The agent/operator must stop and report. Recovery motion is not automatic.

Read [docs/safety.md](https://github.com/GainSec/AutoProber/blob/main/docs/safety.md) and [docs/operations.md](https://github.com/GainSec/AutoProber/blob/main/docs/operations.md)
before running hardware.

```
apps/                 Operator-facing scripts and Flask dashboard entrypoint
autoprober/           Reusable Python package for CNC, scope, microscope, logging, safety
dashboard/            Single-page web dashboard
docs/                 Architecture, device references, operations, and safety guidance
cad/                  Printable STL files for the current custom toolhead
config/               Example environment/configuration files
AGENTS.md             Agent/operator safety rules
LICENSE               PolyForm Noncommercial 1.0.0 license and commercial contact
pyproject.toml        Python project metadata
uv.lock               Locked Python dependency resolution
```

The tested project architecture uses:

* GRBL-compatible 3018-style CNC controller over USB serial
* USB microscope served by `mjpg_streamer`
* Siglent oscilloscope over LAN/SCPI for Channel 4 safety monitoring and
  Channel 1 measurement
* Optical endstop wired to an external 5V supply and oscilloscope Channel 4
* Optional network-controlled outlet for lab power control
* Current printable custom toolhead parts in `cad/`

Default runtime assumptions are documented in the device docs. Replace them
with your own lab settings before use.

For a shopping-oriented hardware list, see [docs/BOM.md](https://github.com/GainSec/AutoProber/blob/main/docs/BOM.md).

These are the specific parts or part classes used for the prototype release.
Verify current listings, dimensions, voltage, and connector compatibility
before buying.

My build:

Optional / interchangeable:

```
flowchart LR
    Operator[Operator] --> Dashboard[Web Dashboard]
    Dashboard --> Apps[Python Apps]
    Apps --> CNC[GRBL CNC over USB serial]
    Apps --> Microscope[USB Microscope via mjpg-streamer]
    Apps --> Scope[Oscilloscope over LAN / SCPI]
    Apps --> Outlet[Optional LAN Power Outlet]

    Endstop[Optical Endstop] --> ScopeC4[Scope C4 Safety Voltage]
    Pogo[Pogo Measurement] --> ScopeC1[Scope C1 Measurement]
    ScopeC4 --> Apps
    ScopeC1 --> Apps
```

 Loading

```
flowchart TD
    Preflight[Preflight] --> SafetyCheck{Channel 4 clear?}
    SafetyCheck -- no --> Stop[STOP State]
    SafetyCheck -- yes --> Motion[Monitored Motion]
    Motion --> Monitor[EndstopMonitor thread >= 10 Hz]
    Monitor --> C4{C4 clear?}
    C4 -- yes --> Capture[Microscope Capture]
    C4 -- no --> FeedHold[Immediate feed hold]
    FeedHold --> Stop
    Capture --> Stitch[Stitch / Map]
    Stitch --> Review[Manual Probe Review]
    Review --> Approved{Approved target and measured probe offset?}
    Approved -- no --> Stop
    Approved -- yes --> Probe[Bounded probe motion]
```

 Loading

```
stateDiagram-v2
    [*] --> Running
    Running --> STOP: C4 triggered / C4 fault / CNC alarm / real limit pin
    STOP --> Report: log voltage, status, action
    Report --> WaitForOperator: no automatic recovery motion
    WaitForOperator --> Running: operator explicitly clears condition
```

 Loading

Install dependencies:

Start the dashboard on a configured hardware host:

```
PYTHONPATH=. python3 apps/dashboard.py
```

The dashboard defaults to port `5000`.

Start from [config/autoprober.example.env](https://github.com/GainSec/AutoProber/blob/main/config/autoprober.example.env). Do
not publish lab-specific IPs, hostnames, credentials, calibration files, or
captured target images unless you intend to release them.

Important runtime values are configurable:

* `AUTOPROBER_LOG_PATH`: runtime log path
* `AUTOPROBER_RUNTIME_ROOT`: calibration, flat-field, and runtime state directory
* `AUTOPROBER_MICROSCOPE_SNAPSHOT_URL`: microscope snapshot endpoint
* `AUTOPROBER_SCOPE_HOST` / `AUTOPROBER_SCOPE_PORT`: oscilloscope SCPI endpoint
* Dashboard: Flask on port `5000`

Do not commit local environment files that contain lab-specific hosts, paths,
or target data.

1. Run preflight checks.
2. Verify Channel 4 is clear.
3. Home and calibrate only when the physical setup is ready.
4. Capture microscope frames with monitored motion.
5. Import or generate target map artifacts for review.
6. Approve probe candidates manually.
7. Execute any probe motion only after microscope-to-probe offset is measured
   and stored.

This release candidate intentionally excludes:

* Trial microscope captures and stitched target images
* Uploaded reference images
* Local backups and archives
* `.venv`, `__pycache__`, Playwright artifacts
* Runtime logs, calibration cache, flat-field images
* Machine-specific SSH/deploy state

See [RELEASE\_MANIFEST.md](https://github.com/GainSec/AutoProber/blob/main/RELEASE_MANIFEST.md) for details.

This project is source-available under the PolyForm Noncommercial License 1.0.0.

You may use, modify, and share this project for noncommercial purposes.

Commercial use requires a separate paid commercial license.

For commercial licensing, contact: [autoprober@gainsecmail.com](mailto:autoprober@gainsecmail.com)

* The microscope-to-pogo XY offset must be measured before real probing.
* Calibration must not be fabricated; the runtime calibration file should be
  generated on the machine that will move.
* The dashboard is a lab-control tool and should not be exposed to untrusted
  networks.

This project is intended for controlled lab work on equipment and targets you
are authorized to test. Do not use it to probe, damage, or analyze systems
without permission.

[Jon 'GainSec' Gaines](https://gainsec.com/)