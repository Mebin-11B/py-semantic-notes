---
title: "A 3D fruit fly on macOS desktop powered by the real FlyWire connectome"
url: https://github.com/DenisSergeevitch/desktop-fly
clipped: 2026-08-31 12:22:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A 3D fruit fly on macOS desktop powered by the real FlyWire connectome](https://github.com/DenisSergeevitch/desktop-fly)

## Digest Summary
A macOS application renders a 3‑D fruit‑fly model whose behavior is driven by a live spiking simulation of a real FlyWire connectome (FAFB v783). The brain window displays 23 210 neuron somata (a subset of 139 255) colored by coarse cell‑type, with spikes visualized at their positions. Core circuitry comprises 668 neurons and ~19 000 synapses, simulated at 1 kHz using leaky‑integrate‑and‑fire dynamics. Key components include LC4/LPLC2 looming‑detector visual neurons, the Giant Fiber (escape command), steering neurons DNa01/DNa02, forward‑walking DNp09, grooming DNg11, backward‑walking MDN, and escape‑maneuver neurons DNp02/DNp04/DNp11, plus their 330 strongest partners (proprioceptive and wind sensory neurons). Escape responses emerge from genuine network activity: cursor motion generates looming input to LC4/LPLC2, triggering Giant Fiber spikes after ~4 ms when feed‑forward inhibition is overcome. The procedural body exhibits tripod gait, wing beats, altitude‑scaled flight, grooming and sleep postures, and interacts with desktop elements (window edges, appearances, clicks) without requiring permissions. Requires macOS 13+ and Swift 5.9; source and derived data are MIT‑licensed, with FlyWire data under CC BY‑NC 4.0.

---

## Full Article

[Skip to content](https://github.com/DenisSergeevitch/desktop-fly#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [DenisSergeevitch](https://github.com/DenisSergeevitch)    
    /
    
      [desktop-fly](https://github.com/DenisSergeevitch/desktop-fly)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2FDenisSergeevitch%2Fdesktop-fly)    You must be signed in to change notification settings

  

  
- 
          [Fork
    47](https://github.com/login?return_to=%2FDenisSergeevitch%2Fdesktop-fly)
  

  
- 
        
        [Star
          746](https://github.com/login?return_to=%2FDenisSergeevitch%2Fdesktop-fly)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     master[Branches](https://github.com/DenisSergeevitch/desktop-fly/branches)[Tags](https://github.com/DenisSergeevitch/desktop-fly/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[13 Commits](https://github.com/DenisSergeevitch/desktop-fly/commits/master/)13 Commits

## Folders and files

NameNameLast commit messageLast commit date[assets](https://github.com/DenisSergeevitch/desktop-fly/tree/master/assets)[assets](https://github.com/DenisSergeevitch/desktop-fly/tree/master/assets)  [data](https://github.com/DenisSergeevitch/desktop-fly/tree/master/data)[data](https://github.com/DenisSergeevitch/desktop-fly/tree/master/data)  [windows](https://github.com/DenisSergeevitch/desktop-fly/tree/master/windows)[windows](https://github.com/DenisSergeevitch/desktop-fly/tree/master/windows)  [.gitignore](https://github.com/DenisSergeevitch/desktop-fly/blob/master/.gitignore)[.gitignore](https://github.com/DenisSergeevitch/desktop-fly/blob/master/.gitignore)  [BeetleModel.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/BeetleModel.swift)[BeetleModel.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/BeetleModel.swift)  [BrainView.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/BrainView.swift)[BrainView.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/BrainView.swift)  [CLAUDE.md](https://github.com/DenisSergeevitch/desktop-fly/blob/master/CLAUDE.md)[CLAUDE.md](https://github.com/DenisSergeevitch/desktop-fly/blob/master/CLAUDE.md)  [Environment.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/Environment.swift)[Environment.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/Environment.swift)  [FlyModel.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/FlyModel.swift)[FlyModel.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/FlyModel.swift)  [LICENSE](https://github.com/DenisSergeevitch/desktop-fly/blob/master/LICENSE)[LICENSE](https://github.com/DenisSergeevitch/desktop-fly/blob/master/LICENSE)  [README.md](https://github.com/DenisSergeevitch/desktop-fly/blob/master/README.md)[README.md](https://github.com/DenisSergeevitch/desktop-fly/blob/master/README.md)  [Sim.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/Sim.swift)[Sim.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/Sim.swift)  [build.sh](https://github.com/DenisSergeevitch/desktop-fly/blob/master/build.sh)[build.sh](https://github.com/DenisSergeevitch/desktop-fly/blob/master/build.sh)  [etl.py](https://github.com/DenisSergeevitch/desktop-fly/blob/master/etl.py)[etl.py](https://github.com/DenisSergeevitch/desktop-fly/blob/master/etl.py)  [main.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/main.swift)[main.swift](https://github.com/DenisSergeevitch/desktop-fly/blob/master/main.swift)  View all files

## Repository files navigation

  

# DesktopFly 🪰

A 3D fruit fly that lives on your macOS desktop — driven by a live spiking
simulation of the real [FlyWire](https://codex.flywire.ai)
connectome. It walks across your windows, grooms, sleeps, and decides to flee
your cursor with the same neurons a real fly uses.

  

The fly's brain window: 23,210 real neuron soma positions from FlyWire v783,
with live spikes flashing at real neuron locations. The two glowing yellow
markers are the Giant Fibers — the escape command neurons. Click any region
to stimulate it.

## What's real

- 23,210 neuron soma positions (of 139,255 in FlyWire v783) render the
rotating brain window, colored by super-class (FlyWire's coarse cell-type
grouping).

- A 668-neuron circuit with ~19,000 real synaptic connections (synapse
counts, signed by neurotransmitter prediction) runs as a 1 kHz
leaky-integrate-and-fire (LIF) simulation:

- LC4 (104) + LPLC2 (210) looming-detector visual neurons

- DNp01 / Giant Fiber (GF) (2) — the escape command neuron

- DNa01 + DNa02 (4) steering neurons · DNp09 (2) forward walking

- DNg11 (6) grooming · MDN (4) backward walking ("moonwalker")

- DNp02/DNp04/DNp11 (6) escape-maneuver (wing) neurons

- their 330 strongest partners, including ascending (proprioceptive) and
sensory (wind) neurons

- Escape is not scripted. Your cursor's approach becomes looming input to
the real LC4/LPLC2 cells; the fly takes off only when the Giant Fiber
actually spikes through its real synapses — ~1,200 synapses of feedforward
inhibition push back, which is why slow approaches are tolerated and fast
lunges trigger escape in ~4 ms, just like the real animal.

The body itself is procedural (FlyWire is a brain connectome — no body
geometry exists), with a tripod gait, visible wing-beat, altitude-scaled
flight, grooming, and sleep postures.

## Installation

Requirements: macOS 13+, Xcode Command Line Tools (Swift 5.9+).
No permissions or entitlements needed — everything it senses
(cursor, window frames, clicks-as-taps, thermal state) is permission-free.
 `git clone https://github.com/DenisSergeevitch/desktop-fly.git
cd desktop-fly
./build.sh
./DesktopFly` 

A 🪰 item appears in the menu bar; quit from there. The fly wanders your
desktop on a transparent, click-through overlay — it never intercepts your
mouse or keyboard.

### Windows

An Electron + three.js port with the same connectome, the same circuit, and
the same test suites lives in  `` [windows/](https://github.com/DenisSergeevitch/desktop-fly/blob/master/windows) (contributed by
[@MikeMike88](https://github.com/MikeMike88)). Requires Windows 10/11 and
[Node.js](https://nodejs.org) 18+:
 `cd desktop-fly/windows
npm install
npm start          # tray icon 🪰; quit from there
npm test           # both suites, headless` 

See [windows/README.md](https://github.com/DenisSergeevitch/desktop-fly/blob/master/windows/README.md) for the macOS→Windows mapping
table and platform notes (the fly there roams all monitors on its own).
The optional stag-beetle body is macOS-only for now.

## Controls (menu bar 🪰)

item
effect

Pause / Resume
freeze the world

Show/Hide Brain
toggle the live brain window

Escape Test (loom)
inject a looming stimulus, watch the GF fire

Move to Next Display
hop the fly across monitors (shown when >1 display)

Add / Remove Fly
extra flies (only fly #1 carries the brain)

Scare Flies
startle everyone

Body: Fruit Fly / Stag Beetle
swap the body geometry — behavior is unchanged

  

The same connectome, the same state machine, a different shell. The behavior
layer only ever touches the body through one struct, so a second geometry drops
in without a line of behavior code: the elytra open when it flies or when the
escape descending neurons fire a grounded threat posture, and the membranous
hindwings underneath are the surfaces that actually beat.

The brain window is interactive: hovering pauses the rotation; clicking a
region "optogenetically" stimulates the ~60 nearest circuit neurons for
400 ms. The fly's reaction is whatever the real network does downstream —
click the Giant Fiber and it escapes; click DNg11 and it grooms; click one
side's DNa01/02 and it turns.

## How real neurons drive the body

body behavior
driven by

escape takeoff
DNp01 giant fiber spike

walk vs. rest, walking speed
DNp09 rate

steering
DNa01+DNa02 left−right rate difference

grooming
DNg11 rate

backward scoot
MDN burst

nervous darting
LC4/LPLC2 population rate

wing-beat effort, threat wing-raise
DNp02/04/11 rate

spontaneous takeoff
whole-population arousal

The loop also closes body→brain: the gait rhythm feeds the circuit's real
ascending (proprioceptive) neurons in phase with the legs, and fast cursor
motion stimulates its sensory (wind) partners.

## Desktop ecology (all permission-free macOS senses)

- Window terrain: window top edges are ledges — the fly lands on them,
walks along them, rides a window you drag, and startles when one closes
under its feet.

- Window looms: a window appearing near the fly feeds the looming
pathway; the circuit decides whether to flee your dialogs.

- Clicks are substrate taps; clicking next to the fly startles it through
the wind→GF pathway. Typing is vibration (idle-time API — knows when
keys were pressed, never which).

- Circadian rhythm: dawn/dusk activity peaks, midday siesta, night
quiescence. Sleep: idle at night → it sleeps, breathing slowly, with
raised arousal threshold; it grooms after waking.

- Temperature: flies are ectotherms — a hot Mac is a faster fly.

## Regenerating the data

 `data/`  ships with compact derived files. To rebuild them from the raw
FlyWire Codex dumps (~60 MB download):
 `mkdir -p /tmp/flywire && cd /tmp/flywire
B=https://storage.googleapis.com/flywire-data/codex/data/fafb/783
curl -O "$B/classification.csv.gz" -O "$B/coordinates.csv.gz" \
     -O "$B/connections.csv.gz" -O "$B/consolidated_cell_types.csv.gz"
cd - && python3 etl.py /tmp/flywire` 

## Diagnostics

 `./DesktopFly --simtest        # circuit invariants: GF silent at rest, 4 ms loom latency, ...
./DesktopFly --behaviortest   # 23 end-to-end checks: stimulate neurons -> body reacts
./DesktopFly --snapshot f.png  # offscreen body render (3/4 perspective)
./DesktopFly --snapshot f.png --top [--flying] [--beetle]   # the overlay's own
                               # top-down orthographic view, the one users see
./DesktopFly --brainshot b.png # offscreen brain render` 

## What's modeled vs. measured

Honesty section: the connectome gives wiring, not physiology. The LIF
dynamics, neurotransmitter signs (ACh+, GABA−, Glu−), the gap-junction boost
on LC→GF and wind→GF (documented electrical coupling), synaptic delays, and
the sensory transduction (cursor → looming value) are standard modeling
choices layered on the real graph. Everything downstream of the sensory
neurons — who connects to whom, and how strongly — is FlyWire data.

## License & citation

Code is MIT. The files in  `data/`  are derived from FlyWire (FAFB v783) and
are CC BY-NC 4.0 — see [data/DATA_LICENSE.md](https://github.com/DenisSergeevitch/desktop-fly/blob/master/data/DATA_LICENSE.md).
If you use this, cite:

- Dorkenwald, S. et al. Neuronal wiring diagram of an adult brain. Nature 634, 124–138 (2024). [https://doi.org/10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)

- Schlegel, P. et al. Whole-brain annotation and multi-connectome cell typing of Drosophila. Nature 634, 139–152 (2024). [https://doi.org/10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)

## About

A 3D fruit fly living on your macOS desktop, driven by a live spiking simulation of the real FlyWire connectome

### Resources

[Readme](https://github.com/DenisSergeevitch/desktop-fly#readme-ov-file)[License](https://github.com/DenisSergeevitch/desktop-fly#License-1-ov-file)[Activity](https://github.com/DenisSergeevitch/desktop-fly/activity)

### Stars

746 stars

### Watchers

0 watching

### Forks

[47 forks](https://github.com/DenisSergeevitch/desktop-fly/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FDenisSergeevitch%2Fdesktop-fly&report=DenisSergeevitch+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
