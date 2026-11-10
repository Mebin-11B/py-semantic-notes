---
title: "Tea5767-Radio-Tuner"
url: https://github.com/turtushig22-blip/tea5767-radio-tuner
clipped: 2026-08-31 12:22:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tea5767-Radio-Tuner](https://github.com/turtushig22-blip/tea5767-radio-tuner)

## Digest Summary
The repository documents an ESP32‑based FM radio built around a TEA5767 tuner, KY‑040 rotary encoder, PAM8403 stereo amplifier, and a 0.96″ OLED display, with a fully custom PCB.  

Original prototype used an Arduino UNO, 16×2 LCD, and wired headphones; the new design swaps the UNO for an ESP32‑DevKit‑32E, the LCD for the OLED, and adds the PAM8403 to drive two 3 W / 4 Ω speakers.  
TEA5767 is powered at 3.3 V to keep its I²C pins within the ESP32’s 3.6 V I/O limit; powering it at 5 V would over‑voltage the ESP32 pins.  
PAM8403 receives a separate 5 V supply (≥1 A) because its current demand (≈1.2 A at full output) far exceeds the ESP32’s per‑pin limit; the amplifier and MCU share the same transformer but are wired in parallel.  
KiCad was used for schematic capture and PCB layout; custom footprints were created for ESP32‑DevKit‑32E, TEA5767, PAM8403, KY‑040, and the OLED.  
Gerber files, source code, and board images are provided; a YouTube demo showcases the assembled device. The project serves as a reference for similar low‑cost FM radio and first‑PCB design efforts.

---

## Full Article

[Skip to content](https://github.com/turtushig22-blip/tea5767-radio-tuner#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [turtushig22-blip](https://github.com/turtushig22-blip)    
    /
    
      [tea5767-radio-tuner](https://github.com/turtushig22-blip/tea5767-radio-tuner)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fturtushig22-blip%2Ftea5767-radio-tuner)    You must be signed in to change notification settings

  

  
- 
          [Fork
    1](https://github.com/login?return_to=%2Fturtushig22-blip%2Ftea5767-radio-tuner)
  

  
- 
        
        [Star
          44](https://github.com/login?return_to=%2Fturtushig22-blip%2Ftea5767-radio-tuner)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/turtushig22-blip/tea5767-radio-tuner/branches)[Tags](https://github.com/turtushig22-blip/tea5767-radio-tuner/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[59 Commits](https://github.com/turtushig22-blip/tea5767-radio-tuner/commits/main/)59 Commits

## Folders and files

NameNameLast commit messageLast commit date[CustomFootprints.pretty](https://github.com/turtushig22-blip/tea5767-radio-tuner/tree/main/CustomFootprints.pretty)[CustomFootprints.pretty](https://github.com/turtushig22-blip/tea5767-radio-tuner/tree/main/CustomFootprints.pretty)  [gerbers](https://github.com/turtushig22-blip/tea5767-radio-tuner/tree/main/gerbers)[gerbers](https://github.com/turtushig22-blip/tea5767-radio-tuner/tree/main/gerbers)  [LICENSE](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/LICENSE)[LICENSE](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/LICENSE)  [Producing_an_FM_Radio_Tuner.pdf](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/Producing_an_FM_Radio_Tuner.pdf)[Producing_an_FM_Radio_Tuner.pdf](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/Producing_an_FM_Radio_Tuner.pdf)  [README.md](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/README.md)[README.md](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/README.md)  [code](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/code)[code](https://github.com/turtushig22-blip/tea5767-radio-tuner/blob/main/code)  View all files

## Repository files navigation

# TEA5767-based Radio Tuner

ESP32-based FM radio with TEA5767 tuner, KY-040 rotary encoder, PAM8403 amplifier, and 0.96" OLED display. Custom PCB design.

### Project History

The project built an FM radio device using the TEA5767 radio module and the Arduino UNO in January 2026. Phase 2 includes designing a compact, custom-designed PCB board with further improvements while keeping the design simple and reproducible. The steps will be documented in this repository as I work on the PCB design (so, hopefully, I can finish this project).

The primary functions of the prototype Arduino circuit include manual and preset FM tuning, displaying the current frequency on a 16x2 LCD, and outputting audio via wired headphones. We could not use speakers to output sound as the TEA5767 module does not have a built-in speaker amplifier, which required us to solder directly onto the module. Photos of the prototype circuit and the circuit diagrams are shown in Figures 1 and 2.
   

Figure 1 [Photo of the prototype that used Arduino UNO].
   

Figure 2 [Circuit Diagram of the prototype].

To see a video demonstration of the prototype, please follow [https://youtu.be/HQ7OcgIyThs](https://youtu.be/HQ7OcgIyThs), and for a detailed breakdown of the theory, component selection, and circuit design, you can read this [PDF File](Producing_an_FM_Radio_Tuner.pdf).

## Evolving into a PCB design project

### Schematic

To further improve the project, I decided to let it be my first PCB design while improving the radio device as well. The improvements that have been made include PAM8403 amplifier that will feed the audio into two 3-Watt, 4-Ohm speakers while working as a volume control, an ESP32 Development Board instead of the Arduino UNO to save space on the PCB, a 0.96 OLED display replacing the 16x2 Liquid Crystal Display for a similar reason, and a KY-040 rotary encoder that will serve as both the manual frequency and preset frequency control.

Before diving into the PCB design, I took my time to make sure that the circuit works on a breadboard. During this process, I realized some important things which include how although the TEA5767 module is designed to be powered by 5V, it can be (and should) be powered by 3.3V to protect the data pins on the ESP32 module. The manufacturer of the microcontroller Nulllab mentioned that a voltage larger than 3.6V on the I/O pins can cause chip damage, and powering the TEA5767 module from 5V and connecting the SCL and SDA pins to the data pins on the microcontroller will drive them up to 5V, exposing them to the risk of being burnt out. More information about the ESP32-DevKit-32E can be found at [esp32-devkit-32e] ([https://github.com/nulllaborg/esp32-devkit-32e](https://github.com/nulllaborg/esp32-devkit-32e)).

Furthermore, what has caught attention includes how the PAM8403 needs to be powered by a source other than the microcontroller. The speakers I used are 3-Watt speakers (6-Watts in total since I have two speakers), so assuming that we power the amplifier with 5V, the amount of current we get is I = P / V = 6W / 5V = 1.2A. This amount of current through the microcontroller pins exceeds the manufacturer's specified limit (absolute MAX per pin: 40mA) by a huge amount. Therefore, the amplifier and the microcontroller are wired in parallel to a single transformer of 5V 1.5A capacity. As the amplifier required large current to operate and even larger current to blast music, it is recommended to use adapters that can supply more than 1A to avoid brownouts in other regions of the circuit when the volume is turned up.

Having that in mind, I started drawing the circuit diagram in KiCad's schematic editor. The schematic can be seen in Figure 3.

Figure 3 [Schematic of the ESP32-based Circuit].

(To feed the audio signal from the TEA5767 module to the PAM8403 amplifier, I used a 3.5mm jack with a bare wire end, which was then connected to the L, G, and B pins on the amplifier. Note that these connections are not reflected in the schematic of the circuit as KiCad does not allow the schematic symbol of a device to have more pins than the device's footprint, which becomes a bit complicated for the TEA5767 module as it does not have designated pins for the L, G, R. One way to solve this is to draw the 3.5mm jack in the schematic editor; however, as the jack and the connection between the two modules will never actually touch the PCB, I decided to simply leave the pins on the amplifier not connected and draw the TEA5767 with only its physical pins).

### Footprints.

As the project required modules whose footprints do not readily exist in KiCad, I used it to learn to create custom footprints as well. The footprints for the ESP32-DevKit-32E, TEA5767, PAM8403, KY-040, and the 0.96 OLED Display are included in the  `Custom_Footprints.pretty`  folder. Photos of the custom footprints are attached below.

    Figure 4 [ESP32-DevKit-32E Footprint].

    Figure 5 [TEA5767 footprint].

    Figure 6 [PAM8403 footprint].

(Note that the PAM8403 used in this project is the "knobby" version of the PAM8403 amplifier board, which allows it to work as the volume control. Furthermore, note that the knobs on the PAM8403 and KY-040 modules are not included in their corresponding footprints for the ease of drawing the footprint and because the boards will not physically touch the PCB).

     Figure 7 [KY-040 footprint].

    Figure 8 [0.96 OLED Display footprint].

### PCB Layout

After creating the custom footprints, I created the PCB design inside KiCad's PCB editor. A picture of the PCB layout from KiCad's PCB editor is shown in Figure 9.

Figure 9 [PCB Layout of the Radio Module]. 

For this PCB project, I chose JLC PCB as the manufacturer. When making PCB orders, being aware of the manufacturer's capabilities is just as important as not shorting your circuit. Therefore, I paid close attention to whether the settings when generating the gerber files matched JLC's requirements, which can be seen from [https://jlcpcb.com/capabilities/pcb-capabilities](https://jlcpcb.com/capabilities/pcb-capabilities). 

The final Gerber files sent to the manufacturer can be found in the  `gerbers`  folder. Note that the silkscreen text reading “The first of many. Grateful for everyone who supported me.” has been removed from the manufacturing files, as it is personal and unnecessary for reproducing the board.

To see the code I used for this project, see the file named  `code` .

The image of the PCB can be seen in Figures 10 and 11.
 
Figure 10 [The Front face of the PCB]. 

 
Figure 11 [The Backside of the PCB]. 

The image of the device itself can be seen in Figure 12.
 
Figure 12 [An image of the ESP32-based Radio Module using TEA5767].

To see a video demonstration of the PCB and the radio device, please follow [https://www.youtube.com/watch?v=WM1Qq82G7yY](https://www.youtube.com/watch?v=WM1Qq82G7yY).

Lastly, designing my first PCB has been a valuable learning experience and has strengthened my interest in electronics and hardware design. I hope this repository is useful to anyone building a similar project or beginning their own PCB design journey. I would like to thank the HTM Workshop team for their informative YouTube tutorial series, as well as my family and my girlfriend, Amy, for their encouragement and support throughout this project. 

## About

ESP32-based FM radio with TEA5767 tuner, KY-040 rotary encoder, PAM8403 amplifier, and 0.96" OLED display. Custom PCB design.

### Resources

[Readme](https://github.com/turtushig22-blip/tea5767-radio-tuner#readme-ov-file)[MIT license](https://github.com/turtushig22-blip/tea5767-radio-tuner#MIT-1-ov-file)[Activity](https://github.com/turtushig22-blip/tea5767-radio-tuner/activity)

### Stars

44 stars

### Watchers

0 watching

### Forks

[1 fork](https://github.com/turtushig22-blip/tea5767-radio-tuner/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fturtushig22-blip%2Ftea5767-radio-tuner&report=turtushig22-blip+%28user%29)

## Releases

## Packages

## Contributors

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
