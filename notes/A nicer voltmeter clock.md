---
title: A nicer voltmeter clock
url: https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock
clipped: 2026-06-17 01:01:34
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hardware hacking
  - analog displays
  - clock design
  - diy electronics
related:
  - "[[Hardware Hacking]]"
  - "[[Analog Displays]]"
  - "[[Clock Design]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The design process and hardware details of building a clock that uses analog panel voltmeters instead of a traditional digital display.
>
> **Key points:**
> - The project replaces traditional clock faces with three analog panel voltmeters indicating hours, minutes, and seconds.
> - Built using a custom 3D model designed in Rhino3D and custom-printed dial decals applied to cheap voltmeters.
> - The electronics control the needle position by outputting variable voltages corresponding to the current time.
> - Discussion indicates community interest in analog instrumentation, electronics learning, and CNC enclosure fabrication.
>
> **Concept links:** [[Hardware Hacking]], [[Analog Displays]], [[Clock Design]], [[Diy Electronics]]
>
> **Suggested connections:**
> - [[Hardware Hacking]] — Explores modifying analog voltmeters and designing custom physical interfaces.
> - [[DIY Electronics]] — Integrates analog voltage control with digital microcontrollers for a novelty timekeeper.
<!-- ai-summary:end -->

# [A nicer voltmeter clock](https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock)

## Digest Summary
None

## Discussion Summary
The comments express strong appreciation for the analog‑computer project, highlighting the satisfying blend of physical panel meters with digital displays and noting the artistic and inventive appeal. Enthusiasm is evident for replicating the setup, learning related electronics, and expanding into 3D modeling or CNC work. Minor criticisms include a desire for smoother needle motion, concerns about overshoot when transitioning low to high, and practical limitations such as space and tool availability. Overall, the response is overwhelmingly positive with a few technical suggestions.

---

## Full Article

Back in 2019, I built a simple voltmeter clock:

*The clock, version 1. Cherry enclosure.*

As the name implies, these clocks use analog panel voltmeters instead of traditional clock faces to display time. I didn’t come up with the idea, so I never really blogged about the design; I just built one and kept it on my office desk.

Other people keep building these too, but most of the designs I see on the internet are just… sort of janky. So, I figured it might be good to build a better-looking one and document the process more properly.

The design started with a rough mockup in a 3D design program:

*A mockup of the new design in Rhino3D.*

For this version of the meter clock, I used three generic, 90° panel voltmeters from Amazon ([link](https://www.amazon.com/dp/B092VBLGR2), about $9 a piece). I disassembled them, took careful measurements of the faces, and then printed replacement decals on adhesive paper. Printable PDF templates can be found [here](https://lcamtuf.coredump.cx/soft/embedded/meter_clock2.pdf).

*Customizing 5 V panel meters.*

Note that the new hour gauge has 13 divisions, from 0 to 12, while the minute and second templates have 61 divisions, from 00 to 60. This is because I wanted to implement continuous motion for each hand; this meant that at 11:30, the hour dial couldn’t be just stuck at 11; it needed to be moving toward the twelfth division, even if it was never to reach it.

In addition to a host of other problems, the cheap “Baomain 65C5” meters I’m using have a rather hideous plastic flange. I decided to hide this flange from view and use a decorative recessed pattern to keep the front panel interesting. This detail made it more expedient to cut the front and back on a CNC mill instead of making the entirety of the enclosure by hand (as I did for version 1).

The stock material for the enclosure is maple lumber — resawn, squared, and planed using conventional tools before letting the CNC machine take care of the finishing touches:

*Machined front and back faces.*

Without a CNC mill, the path of least resistance would be to construct the panel as two-part glue-up, each part cut by following a printed (paper) template. A simple way to get the curves perfectly right would be to use a spindle sander.

The curved side wall posed a different challenge. For a seamless appearance, I needed to bend a flat piece of wood to conform to a template. To accommodate the tight radius without a steam bending rig, I opted to cut a series of notches on the inside:

*Kerf-bending side walls using a template.*

The wood needed to be moistened, clamped, and then allowed to dry. After a couple of days, I glued the curved side wall to the front and back faces. Another template cut out of scrap plywood helped with precise fit without the need for gymnastics with clamps and ratchet straps:

*Gluing up clock body using an external template (plywood).*

Anyway — here’s the assembled piece after sanding and a coat of nitrocellulose lacquer:

Not bad, right?

The circuit is far less interesting than the enclosure. It took an hour or so to put it together: I grabbed the venerable [AVR128DB28](https://ww1.microchip.com/downloads/en/DeviceDoc/AVR128DB28-32-48-64-DataSheet-DS40002247A.pdf) MCU, powered it off a wall wart, and interfaced it to an 8 MHz crystal ([ECS-80-18-4X-CKM](https://www.ecsxtal.com/store/pdf/hc-49usx.pdf)). A 32.768 kHz crystal would also work fine. The panels are connected to three digital output pins (PC0, PC1, PC2). Finally, two input pins (PD6, PD7) are interfaced to two small pushbuttons mounted on the back and used to set time.

Note that the circuit doesn’t require digital-to-analog converters or any other additional components to drive the meters; I’m just using a relatively high-frequency, 1-bit digital pulse train. The inertia of the meter (and the inductance of the electromagnet coil) does the rest, settling in an intermediate position proportional to the software-controlled signal duty cycle.

The code can be viewed [here](https://lcamtuf.coredump.cx/soft/embedded/meter_clock2.c); it’s short and well-commented. The basic idea is to advance a 10 Hz counter using a timer interrupt synchronized with the crystal. With this out of the way, the main event loop computes the appropriate duty cycle and then manually toggles the output pins. Although the chip has a hardware PWM module, the application is simple enough that using the PWM circuitry wouldn’t really buy us anything.

Here’s the obligatory “rollover” video captured around 11:59:59:

Peace out.

---

**I**f you’re new here, you might enjoy some of my other articles:
