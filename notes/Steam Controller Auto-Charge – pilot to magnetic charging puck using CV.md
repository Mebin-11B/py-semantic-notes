---
title: "Steam Controller Auto-Charge – pilot to magnetic charging puck using CV"
url: https://github.com/FossPrime/Steam-Controller-Auto-Charge
clipped: 2026-08-31 12:22:23
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Steam Controller Auto-Charge – pilot to magnetic charging puck using CV](https://github.com/FossPrime/Steam-Controller-Auto-Charge)

## Digest Summary
Steam Controller Auto‑Charge is an open‑source web app that autonomously pilots a Steam Controller into its magnetic charging puck using computer‑vision and WebHID. It tracks user‑selected points on the controller and puck via OpenCV.js optical flow (Lucas‑Kanade) from an overhead webcam. The app communicates with the controller through WebHID, sending 70 Hz asymmetric haptic pulses to the dual LRAs for navigation and reducing pulse frequency by 50 % within 150 px of the puck (Proximity Creep Mode). Battery status is read by intercepting HID Report 0x79 (ID 121) for charging confirmation and Report 0x43 (ID 67) for live percentage and cell voltage. The front‑end is built with Vue 3; tracking logic includes a PID loop, object‑avoidance via an in‑browser Rust/WASM CNN, and off‑loaded detection in a Web Worker. The only dependency is Nix; the app runs on Windows, macOS, and Linux in Chromium‑based browsers with WebHID support. MIT‑licensed.

---

## Full Article

[Skip to content](https://github.com/FossPrime/Steam-Controller-Auto-Charge#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [FossPrime](https://github.com/FossPrime)    
    /
    
      [Steam-Controller-Auto-Charge](https://github.com/FossPrime/Steam-Controller-Auto-Charge)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2FFossPrime%2FSteam-Controller-Auto-Charge)    You must be signed in to change notification settings

  

  
- 
          [Fork
    9](https://github.com/login?return_to=%2FFossPrime%2FSteam-Controller-Auto-Charge)
  

  
- 
        
        [Star
          343](https://github.com/login?return_to=%2FFossPrime%2FSteam-Controller-Auto-Charge)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     master[Branches](https://github.com/FossPrime/Steam-Controller-Auto-Charge/branches)[Tags](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[13 Commits](https://github.com/FossPrime/Steam-Controller-Auto-Charge/commits/master/)13 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github/workflows](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/.github/workflows)[.github/workflows](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/.github/workflows)  [data](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/data)[data](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/data)  [public](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/public)[public](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/public)  [scripts](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/scripts)[scripts](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/scripts)  [src](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/src)[src](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/src)  [tests](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/tests)[tests](https://github.com/FossPrime/Steam-Controller-Auto-Charge/tree/master/tests)  [.gitattributes](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/.gitattributes)[.gitattributes](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/.gitattributes)  [.gitignore](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/.gitignore)[.gitignore](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/.gitignore)  [AGENTS.md](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/AGENTS.md)[AGENTS.md](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/AGENTS.md)  [LICENSE](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/LICENSE)[LICENSE](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/LICENSE)  [README.md](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/README.md)[README.md](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/README.md)  [index.html](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/index.html)[index.html](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/index.html)  [package-lock.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/package-lock.json)[package-lock.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/package-lock.json)  [package.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/package.json)[package.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/package.json)  [playwright.config.ts](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/playwright.config.ts)[playwright.config.ts](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/playwright.config.ts)  [shell.nix](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/shell.nix)[shell.nix](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/shell.nix)  [triton_2026_steam_controller_spec.md](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/triton_2026_steam_controller_spec.md)[triton_2026_steam_controller_spec.md](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/triton_2026_steam_controller_spec.md)  [tsconfig.app.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/tsconfig.app.json)[tsconfig.app.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/tsconfig.app.json)  [tsconfig.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/tsconfig.json)[tsconfig.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/tsconfig.json)  [tsconfig.node.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/tsconfig.node.json)[tsconfig.node.json](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/tsconfig.node.json)  [vite.config.ts](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/vite.config.ts)[vite.config.ts](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/vite.config.ts)  View all files

## Repository files navigation

# Steam Controller Auto-Charge

Steam Controller Auto-Charge is an open-source web application designed to automatically pilot a Steam Controller into its magnetic charging puck using optical flow computer vision and WebHID telemetry.

## Features

- Optical Flow Tracking: Utilizes OpenCV.js to track user-selected points on the controller and the charging puck via an overhead camera.

- WebHID Telemetry & Haptic Navigation: Connects to the Triton Controller natively via WebHID, streaming input and telemetry (Report 67). Navigates the controller towards the puck by firing 70Hz asymmetric haptic pulses through the internal dual Linear Resonant Actuators (LRAs).

- Proximity Creep Mode: Automatically cuts haptic pulse frequency by 50% when the controller is within 150 pixels of the puck to ensure a gentle magnetic dock.

- Battery Status Polling: Intercepts Report ID  `121`  ( `0x79` ) to confirm successful magnetic charging, and parses Report ID  `67`  ( `0x43` ) to display live battery percentage and battery cell voltage (mV).

## Setup

### Requirements

- [Nix Package Manager](https://nixos.org/download): The only build dependency you need. It works seamlessly on Windows, Mac, and Linux.

- A Chromium-based browser supporting the WebHID API.

- An overhead webcam pointing down at your desk.

- Mount a webcam directly overhead pointing at the desk.

- Start the project with a single command (this will automatically fetch dependencies and build the WASM module):

 `nix-shell --run "npm install && npm run dev"` 

## Usage

- Mount a webcam directly overhead pointing at the desk.

- Place the Steam Controller Auto-Charge puck on the desk.

- Place your Steam Controller on the desk, upright.

- Open the web interface and click Connect Steam Controller to pair it via WebHID.

- Click ✨ Auto-Track to engage automatic tracking. The button will highlight to indicate it's active and will automatically resume tracking on page reload. Click it again to disengage.

- The controller will now autonomously navigate to the puck using a Lucas-Kanade optical flow loop combined with object avoidance powered by an in-browser Rust/WASM CNN!

(Note: Manual tracking is still available if you prefer. Just click the puck, then the top of the controller, then the bottom of the controller).

## Architecture

-  `App.vue` : Vue 3 application logic handling camera streams, UI reactivity, PID tracking loop, and OpenCV.js Lucas-Kanade optical flow ( `calcOpticalFlowPyrLK` ).

-  `steamController.ts` : WebHID abstraction class mapping standard API calls to the Steam Controller's specific byte payloads for LRA pulses and battery status polling.

-  `objectDetector.ts`  &  `objectWorker.ts` : Offloads object detection to a Web Worker to ensure the main tracking loop remains fluid.

-  `wasm-object-detect/` : Rust implementation compiled to WebAssembly for high-performance visual processing.

## Thanks

Huge thanks to Very Lazy Pixel for inspiring this project!
Check out their video here: [https://www.youtube.com/watch?v=g-8S8zk4dn8](https://www.youtube.com/watch?v=g-8S8zk4dn8)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/FossPrime/Steam-Controller-Auto-Charge/blob/master/LICENSE) file for details.

## About

Slam the controller into the magnetic puck until it charges[fossprime.github.io/Steam-Controller-Auto-Charge/](https://fossprime.github.io/Steam-Controller-Auto-Charge/)

### Resources

[Readme](https://github.com/FossPrime/Steam-Controller-Auto-Charge#readme-ov-file)[MIT license](https://github.com/FossPrime/Steam-Controller-Auto-Charge#MIT-1-ov-file)[Activity](https://github.com/FossPrime/Steam-Controller-Auto-Charge/activity)

### Stars

343 stars

### Watchers

2 watching

### Forks

[9 forks](https://github.com/FossPrime/Steam-Controller-Auto-Charge/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FFossPrime%2FSteam-Controller-Auto-Charge&report=FossPrime+%28user%29)

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
