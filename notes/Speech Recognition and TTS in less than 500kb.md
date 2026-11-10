---
title: "Speech Recognition and TTS in less than 500kb"
url: https://github.com/moonshine-ai/moonshine/tree/main/micro
clipped: 2026-08-31 12:22:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Speech Recognition and TTS in less than 500kb](https://github.com/moonshine-ai/moonshine/tree/main/micro)

## Digest Summary
Moonshine Micro is an open‑source AI toolkit for real‑time voice agents on embedded processors, demonstrated on the Raspberry Pi RP2350 (≈ $0.80). It integrates voice‑activity detection (VAD), command recognition (STT), and neural text‑to‑speech (TTS) that together occupy ~470 KB of SRAM on the RP2350’s 520 KB memory, sharing a ~384 KB TensorFlow Lite‑Micro arena. The flash footprint consists of .text and .rodata sections measured with arm‑none‑eabi‑size; .bss, heap and stacks comprise the SRAM usage. The system processes VAD, STT, and TTS sequentially, so RAM is not additive. Compute is expressed in MACs (multiply‑accumulate), with active‑stage performance in MMAC/s. All code, including the SpellingCNN and TinyVadCNN models, is released under the permissive MIT License, suitable for commercial use. The VAD, STT, and TTS libraries can operate independently, relying on the bundled TensorFlow Lite Micro library for neural inference, and an end‑to‑end example demonstrates voice‑controlled Wi‑Fi setup on the RP2350 MCU.

---

## Full Article

[Skip to content](https://github.com/moonshine-ai/moonshine/tree/main/micro#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [moonshine-ai](https://github.com/moonshine-ai)    
    /
    
      [moonshine](https://github.com/moonshine-ai/moonshine)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fmoonshine-ai%2Fmoonshine)    You must be signed in to change notification settings

  

  
- 
          [Fork
    602](https://github.com/login?return_to=%2Fmoonshine-ai%2Fmoonshine)
  

  
- 
        
        [Star
          11k](https://github.com/login?return_to=%2Fmoonshine-ai%2Fmoonshine)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     

## FilesExpand file tree

main/

# micro

/Copy path

## Directory actions

## More options

More options

## Directory actions

## More options

More options

## Latest commit

 

## History

[History](https://github.com/moonshine-ai/moonshine/commits/main/micro)Historymain/

# micro

/Copy pathTop

## Folders and files

NameNameLast commit messageLast commit date

### parent directory

[..](https://github.com/moonshine-ai/moonshine/tree/main)[cmake](https://github.com/moonshine-ai/moonshine/tree/main/micro/cmake)[cmake](https://github.com/moonshine-ai/moonshine/tree/main/micro/cmake)  [examples/rp2350](https://github.com/moonshine-ai/moonshine/tree/main/micro/examples/rp2350)[examples/rp2350](https://github.com/moonshine-ai/moonshine/tree/main/micro/examples/rp2350)  [feature-generation](https://github.com/moonshine-ai/moonshine/tree/main/micro/feature-generation)[feature-generation](https://github.com/moonshine-ai/moonshine/tree/main/micro/feature-generation)  [g2p](https://github.com/moonshine-ai/moonshine/tree/main/micro/g2p)[g2p](https://github.com/moonshine-ai/moonshine/tree/main/micro/g2p)  [images](https://github.com/moonshine-ai/moonshine/tree/main/micro/images)[images](https://github.com/moonshine-ai/moonshine/tree/main/micro/images)  [klatt-tts](https://github.com/moonshine-ai/moonshine/tree/main/micro/klatt-tts)[klatt-tts](https://github.com/moonshine-ai/moonshine/tree/main/micro/klatt-tts)  [models](https://github.com/moonshine-ai/moonshine/tree/main/micro/models)[models](https://github.com/moonshine-ai/moonshine/tree/main/micro/models)  [neural-tts](https://github.com/moonshine-ai/moonshine/tree/main/micro/neural-tts)[neural-tts](https://github.com/moonshine-ai/moonshine/tree/main/micro/neural-tts)  [stt-training](https://github.com/moonshine-ai/moonshine/tree/main/micro/stt-training)[stt-training](https://github.com/moonshine-ai/moonshine/tree/main/micro/stt-training)  [stt](https://github.com/moonshine-ai/moonshine/tree/main/micro/stt)[stt](https://github.com/moonshine-ai/moonshine/tree/main/micro/stt)  [test-support](https://github.com/moonshine-ai/moonshine/tree/main/micro/test-support)[test-support](https://github.com/moonshine-ai/moonshine/tree/main/micro/test-support)  [third-party](https://github.com/moonshine-ai/moonshine/tree/main/micro/third-party)[third-party](https://github.com/moonshine-ai/moonshine/tree/main/micro/third-party)  [vad](https://github.com/moonshine-ai/moonshine/tree/main/micro/vad)[vad](https://github.com/moonshine-ai/moonshine/tree/main/micro/vad)  [.clang-format](https://github.com/moonshine-ai/moonshine/blob/main/micro/.clang-format)[.clang-format](https://github.com/moonshine-ai/moonshine/blob/main/micro/.clang-format)  [CMakeLists.txt](https://github.com/moonshine-ai/moonshine/blob/main/micro/CMakeLists.txt)[CMakeLists.txt](https://github.com/moonshine-ai/moonshine/blob/main/micro/CMakeLists.txt)  [LICENSE](https://github.com/moonshine-ai/moonshine/blob/main/micro/LICENSE)[LICENSE](https://github.com/moonshine-ai/moonshine/blob/main/micro/LICENSE)  [README.md](https://github.com/moonshine-ai/moonshine/blob/main/micro/README.md)[README.md](https://github.com/moonshine-ai/moonshine/blob/main/micro/README.md)  [pico_sdk_import.cmake](https://github.com/moonshine-ai/moonshine/blob/main/micro/pico_sdk_import.cmake)[pico_sdk_import.cmake](https://github.com/moonshine-ai/moonshine/blob/main/micro/pico_sdk_import.cmake)  [video-thumbnail.gif](https://github.com/moonshine-ai/moonshine/blob/main/micro/video-thumbnail.gif)[video-thumbnail.gif](https://github.com/moonshine-ai/moonshine/blob/main/micro/video-thumbnail.gif)  View all files

## [README.md](https://github.com/moonshine-ai/moonshine/tree/main/micro#readme)

Outline

# Moonshine Micro — Voice Interfaces for Microcontrollers

[Moonshine Voice](https://github.com/moonshine-ai/moonshine) is an open source AI toolkit for developers building real-time voice agents and applications. Moonshine Micro is a version designed specifically for embedded system processors like microcontrollers and DSPs, and uses the Raspberry Pi RP2350, which retails for just 80 cents, as its reference platform. It includes [voice-activity detection](https://github.com/moonshine-ai/moonshine/blob/main/micro/vad/README.md), [command recognition](https://github.com/moonshine-ai/moonshine/blob/main/micro/stt/README.md), and [neural speech synthesis](https://github.com/moonshine-ai/moonshine/blob/main/micro/neural-tts/README.md) and can run in as little as 470 KB of RAM.

You can see a full walkthrough in the video below:

  

The memory and compute requirements are designed to fit resource-constrained
systems. Figures below are for [the RP2350 demo](https://github.com/moonshine-ai/moonshine/blob/main/micro/examples/rp2350/README.md); the
detailed [memory budget](https://github.com/moonshine-ai/moonshine/blob/main/micro/examples/rp2350/README.md#memory-budget) breaks each one down:

Component
Flash
SRAM (arena peak)
Compute

VAD (Voice Activity Detection)
~89 KiB
~36 KiB
~0.8 MMAC/frame (~25 MMAC/s)

STT (SpellingCNN Speech-to-Text)
~1.3 MiB
~346 KiB
~36 MMAC/s

TTS (neural diphone synth @ 16 kHz)
~1.8 MiB voice pack
~340 KiB
~37 MMAC typical reply (~65 MMAC/s out)

TOTAL (Demo pipeline)
~3.6 MiB
~468 KiB provisioned*
classify + speak ~0.7–1.0 s

Notes:

- Flash is  `.text`  +  `.rodata`  measured with  `arm-none-eabi-size`  on the default  `moonshine_micro_echo`  firmware (includes the embedded neural voice pack); SRAM is  `.bss`  + heap + stacks.

- *VAD, STT, and neural TTS run sequentially and time-share one ~384 KiB TFLM arena, so SRAM is not additive — ~468 KiB is the total RAM provisioned on the 520 KiB RP2350 ( `wifi_hardware`  ~491 KiB).

- A MAC is one multiply-accumulate; MMAC/s = millions per second during the active (non-idle) stage.

The code is released under [the permissive MIT License](https://github.com/moonshine-ai/moonshine/tree/main/micro#license), suitable for commercial applications.

There's a [complete end-to-end example](https://github.com/moonshine-ai/moonshine/blob/main/micro/examples/rp2350/README.md) showing how to set up a wifi connection on a microcontroller using voice on an RP2350 MCU.

The VAD, STT, and TTS libraries can be used independently of each other, relying on the included [TensorFlow Lite Micro](https://github.com/tensorflow/tflite-micro) library for the neural computations.

## Documentation

- [Voice Activity Detection](https://github.com/moonshine-ai/moonshine/blob/main/micro/vad/README.md)

- [Speech to Text](https://github.com/moonshine-ai/moonshine/blob/main/micro/stt/README.md)

- [Custom Word Recognition](https://github.com/moonshine-ai/moonshine/blob/main/micro/stt-training/README.md)

- [Neural Text to Speech](https://github.com/moonshine-ai/moonshine/blob/main/micro/neural-tts/README.md)

- [Wifi Setup Example](https://github.com/moonshine-ai/moonshine/blob/main/micro/examples/rp2350/README.md)

## License

This code, apart from the source in  `third-party/` , is licensed under the MIT
License — see [LICENSE](https://github.com/moonshine-ai/moonshine/blob/main/micro/LICENSE) in this directory (also at the repository root).

The SpellingCNN and TinyVadCNN models in  `` [models/](https://github.com/moonshine-ai/moonshine/blob/main/micro/models) are released under
the MIT License.

The code in  `third-party/`  is licensed according to the terms of the open
source projects it originates from, with details in a LICENSE file in each
subfolder.
   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
