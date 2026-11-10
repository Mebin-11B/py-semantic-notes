---
title: "Building a 24-bit arcade CRT display adapter from scratch"
url: https://www.scd31.com/posts/building-an-arcade-display-adapter
clipped: 2026-06-17 01:48:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Building a 24-bit arcade CRT display adapter from scratch](https://www.scd31.com/posts/building-an-arcade-display-adapter)

## Digest Summary
The project creates a USB‑connected VGA adapter to drive a 24‑bit arcade CRT (JAMMA connector) with non‑standard resolutions (e.g., 336 × 262). Initial attempts used a Raspberry Pi RP2040’s PIO to generate HSYNC, VSYNC, and RGB signals, but bandwidth limits of USB Full‑Speed (11 Mbps) capped frame rates to ~10 FPS at 16‑bit colour. Switching to the GUD (USB Display) protocol allowed compressed, delta‑based framebuffer updates, but the RP2040 still lacked HS USB. The design was migrated to an STM32H723/H750, exploiting its USB OTG HS (with external ULPI PHY) and LTDC peripheral to output native VGA signals. Custom 8‑bit resistor‑DACs were calculated via SAT solving to meet VGA voltage and 75 Ω impedance requirements. A HyperRAM provides framebuffer storage, with length‑matched routing for memory and LTDC signals. Board revisions encountered PCB shorts, crystal oscillator instability, and USB PHY failures, leading to iterative hardware fixes. Final hardware achieves 24‑bit colour, 60 Hz refresh, and stable VGA output, with future work planned for audio, input handling, double‑buffering, and GUD protocol documentation.

## Discussion Summary
The comments express strong enthusiasm for the project, praising its detail and creativity while offering extensive technical suggestions such as adding ESD protection, using buffers or dedicated DAC chips, improving schematic organization, and optimizing PCB trace and via sizes. Contributors share related resources, note alternative hardware options, and discuss historical arcade and CRT contexts, highlighting both nostalgic appreciation and practical considerations. Overall, the tone is supportive, combining admiration with constructive advice to enhance reliability, manufacturability, and performance.

---

## Full Article

In November, my friend and fellow Recurser, [Frank](https://www.frankchiarulli.com/), picked up an arcade machine for the [Recurse Center](https://www.recurse.com/). We call it the RCade. He wanted to leave the original CRT in - which I think is a great choice! - and drove it off of a Raspberry Pi. Eventually we wanted to move to a more powerful computer, but we needed a way to connect it to the display. Off-hand, I mentioned that I could build a CRT display adapter that interfaces with a normal computer over USB. This is that project.

What the display expects
------------------------

The CRT in the RCade has a JAMMA connector, and Frank bought a converter that goes between VGA and JAMMA.

You might think we could just use an off-the-shelf VGA adapter to drive it at this point, but it's not that simple. The CRT runs at a weird resolution; We started with 320x240 but eventually wanted to target 336x262, which is super non-standard. Even 320x240 is unattainable by most display adapters, which typically can't go below 640x480. A custom solution would allow us to output any arbitrary resolution we wanted.

The other thing is that the Pi, with the [VGA board](https://github.com/fenlogic/vga666) we were using, only supports 18-bit colour, and we wanted to improve this. Even on the RCade's CRT, colour banding was an obvious issue.

We also wanted to use a laptop, not a desktop, which meant not using a PCI-e card. Instead, a USB interface would be preferable.

Wait, but what is VGA?
----------------------

VGA is a signaling protocol that maps almost exactly 1:1 with what a CRT actually does.

[![](https://www.scd31.com/thumb/rcade/crt-diagram.webp)](https://www.scd31.com/img/rcade/crt-diagram.webp)

Taken from wikimedia.org

Inside of a CRT, there are 3 electron guns, which correspond to red, green, and blue colour values. Two electromagnets in the neck of the tube are responsible for steering the beam - one steers horizontally and one steers vertically. To draw an image, the beam moves across the screen one horizontal line at a time, and the electron guns are rapidly modulated in order to display the correct colour at each pixel.

VGA contains analog signals for these R, G, and B electron guns. It also contains an HSYNC and VSYNC signal, which are used so that the driver and the CRT can agree on what pixel is being drawn at a given time. Between the VGA input and the CRT is a very simple circuit which locks onto these HSYNC and VSYNC pulses and synchronizes the sweeping of the beam.

[![](https://www.scd31.com/thumb/rcade/vga-timing.webp)](https://www.scd31.com/img/rcade/vga-timing.webp)

Taken from pyroelectro.com

The HSYNC pulses happen in between horizontal lines, and the VSYNC pulses happen in between frames. There are dead zones around each pulse - referred to as the front and back porch - which give the electron beam time to sweep back across the screen.

So, all we really need are those R, G, B, HSYNC, and VSYNC signals, running at precise timing, and synced properly relative to each other. Conceptually this is actually pretty simple!

Attempt 1: Using the RP2040's PIO
---------------------------------

I like the Raspberry Pi RP2040 a lot. It's relatively cheap (around $1 USD) and has tons of on-board RAM - 264 KB in fact! It also has what is called Programmable IO, or PIO.

I've never used the PIO before, but the basic idea is that you can write assembly programs where every instruction takes exactly one cycle, and has useful primitives for interacting with GPIO. It's a fairly limited instruction set, but it allows for bit-banging precise cycle-accurate custom protocols. It's exactly what I need to modulate a VGA signal.

The PIO code ended up looking like this:

```
  // 1. low for 320+16=336 pixels
  // 2. high for 30 pixels
  // 3. low for 34 pixels
  // 4. repeat
  // runs on sm0
  // 6 instrs -> can save some with sidesetting
  let hsync = pio::pio_asm!(
      ".wrap_target",
      /* begin pixels + front porch */
      "irq set 0 [2]",    // tell vsync we're doing 1 line
      "set pins, 1 [31]", // go low for 32
      "set X, 8 [15]",    // +16 = 48
      "a:",
      "jmp X-- a [31]", // each loop 32, * 9 = 288, total = 336
      /* end front porch, being assert hsync */
      "set pins, 0 [29]", // assert hsync for 30
      /* end assert hsync, begin back porch */
      "set pins, 1 [29]", // deassert, wait 32 (note there is extra delay after the wrap)
      ".wrap"
    );

  // NOTE - we get irq at *end* of line so we have to time things accordingly
  // 1. low for 242 lines -> but irq 2 every line for the first 240
  // 2. high for 3 lines
  // 3. low for 22 lines
  // 4. repeat
  // runs on sm1
  // 19 instr
  let vsync = pio::pio_asm!(
      ".side_set 1 opt",
      ".wrap_target",
      "set Y, 6",
      "a_outer:",
      "set X, 31",
      "a:",
      "wait 1 irq 0",
      "irq set 2",
      "jmp X-- a", // 32 lines per inner loop
      "jmp Y-- a_outer", // 7 outer loops = 224

      "set X, 15", // 16 more lines = 240
      "z:"
      "wait 1 irq 0",
      "irq set 2",
      "jmp X-- z",

      "wait 1 irq 0", // wait for end of last rgb line
      "wait 1 irq 0", // 2 more lines for front porch
      "wait 1 irq 0",

      "set X, 2 side 0", // assert vsync
      "b:",
      "wait 1 irq 0",
      "jmp X-- b", // wait for 3 lines
      "set X, 20 side 1", // deassert vsync
      "c:",
      "wait 1 irq 0",
      "jmp X-- c" // wait for 21 lines (back porch)
      ".wrap",
  );

  // 2 cycles per pixel so we run at double speed
  // 6 instr
  let rgb = pio::pio_asm!(
      "out X, 32", // holds 319, which we have to read from the FIFO
      ".wrap_target",
      "mov Y, X",
      "wait 1 irq 2", // wait until start of line
      "a:",
      "out pins, 16", // write to rgb from dma
      "jmp Y-- a",
      "mov pins, NULL", // output black
      ".wrap"
  );
```

The full code lives [here](https://gitlab.scd31.com/sophie/rp2040-rcade-crt-driver/-/blob/master/src/main.rs).

There are 3 separate PIO programs. `hsync` is responsible for keeping time and generating HSYNC pulses. At the start of each line, it generates an IRQ event that the other programs use for synchronization. `vsync` counts these events and generates the VSYNC pulses. Finally, `rgb` reads pixel data from DMA and outputs to the RGB pins in precise time with the other signals. The `out pins, 16` signifies that we're only doing 16-bit colour for now.

There's a lot of weirdness in here to get around the constraints of the PIO. For example, between all 3 programs, only a maximum of 31 instructions are allowed. All of the VGA parameters (resolution, porch length, etc.) are hard-coded, and changing these would require at least a small rewrite. It's pretty brittle in that regard, but for our use-case it's sufficient as a proof-of-concept.

Here it is running the actual CRT in the RCade:

[![](https://www.scd31.com/thumb/rcade/pio-crt.webp)](https://www.scd31.com/img/rcade/pio-crt.webp)

I wanted to fill the framebuffer with a repeating pattern, but I messed up my code, hence it looking weird. That's fine - it was enough to verify my VGA program worked!

As an aside, every time I popped off the back of the RCade to work on it was terrifying. Not because of the lethal voltages inside, but because Recursers absolutely *love* the RCade. I often joke that if I were to break it, I would basically be the anti-Frank!

Now that I had something that could take a framebuffer and throw it onto the CRT, it was time to get the image from my computer to the RP2040.

Let's write a kernel module!
----------------------------

My plan was to write a Linux kernel module that would expose itself as a framebuffer, and then send that framebuffer over USB to the RP2040. On the framebuffer side, this involved interfacing with the [DRM layer](https://www.kernel.org/doc/html/v4.11/gpu/drm-internals.html).

I actually made decent progress here, although I kernel panicked many, many times. I never bothered to set up a proper development environment (oops), so pretty much any bug would require me to reboot my computer. This was super annoying and tedious, although I did learn a lot. I found cursed things in the official documentation, like [interrobangs!](https://www.kernel.org/doc/html/v5.5/gpu/drm-kms.html#c.drm_display_mode)

[![](https://www.scd31.com/thumb/rcade/interrobangs.webp)](https://www.scd31.com/img/rcade/interrobangs.webp)

Linus pls

I got as far as getting a framebuffer to show up at the correct resolution and refresh rate. Along this journey though, I discovered the [GUD kernel module](https://github.com/notro/gud/wiki), and quickly realized I should use that instead.

GUD is... pretty good
---------------------

Okay so this GUD thing is sick. It's a USB display adapter protocol - exactly what I need! It was originally designed to send video from a computer to a Pi Zero for use as a secondary display. It consists of an upstreamed (!!!) kernel module that runs on the host, and separate gadget software that runs on the Pi Zero. I decided I would just write my own gadget implementation to run on the RP2040.

As a protocol, GUD seems decent. It supports compression over the wire, and only sends the deltas of what's changed in the host's framebuffer. It's also pretty robust in terms of allowing the gadget to advertise what features it supports - compression is optional, and there's flexibility in colour depth and resolution. And again, it's upstreamed into the kernel, so anyone on modern Linux could use my display adapter with no software tweaks.

Unfortunately, GUD has almost no documentation. I figured out what I needed to do by reverse engineering the kernel module, which involved recompiling it to add some debugging statements. The protocol is simple enough that is wasn't too much of a hassle, and it didn't take long before I had developed a gadget implementation in Rust for the RP2040.

And with that, we saw our first Linux images on the CRT:

I know, I know, it looks terrible. Several years ago, I had built a board that implements the R/G/B DACs out of resistors, and I reused that for this project. It can only do 12 bits of colour maximum, and for this test I only bothered to wire up ~2 bits per channel, which is basically unusable. But it proves the concept works!

[![](https://www.scd31.com/thumb/rcade/vga-dac.webp)](https://www.scd31.com/img/rcade/vga-dac.webp)

The board I built several years ago. It was originally designed to fit an STM32 development board.

To be honest, it's pretty lucky that this board came with me to New York. I'm surprised I didn't either throw it out or move it to my parent's place. It was probably in some other box of things I deemed worth keeping around.

[![](https://www.scd31.com/thumb/rcade/rev0-board.webp)](https://www.scd31.com/img/rcade/rev0-board.webp)

The VGA board connected to the RP2040.

You can see from the above picture that I really connected the bare minimum for a proof-of-concept. I find perfboard soldering to be a bit tedious!

As an aside, you may notice in the video that the entire screen is shifted to the left. The left side has wrapped around and is now on the right side. On initial boot, it would look fine; over time it would gradually get worse and worse. This is a bug in my implementation - I suspect it's some kind of buffer underflow that's happening, such that each time it occurs, the PIO gets progressively more out of sync. But this is just a guess; I didn't look into it too much.

The colour depth issue is trivial to fix, but this next one isn't. The framerate sucks! You can even see it in the video above, where you can watch the new frame scroll down the screen. The RP2040 can only do USB FS (full-speed), which is capable of 11 Mbps. At the 320x240x16 bpp we were originally targeting, every frame is 153.6 kB. At our maximum USB FS speed, that's less than 10 FPS! Embarrasingly, I had originally done the math with a bandwidth of 11 M**B**ps, not 11 M**b**ps, so I was off by a factor of 8. I was hoping to get something at least temporarily usable but had to go back to the drawing board.

Going on a GUD gadget side quest
--------------------------------

Who even needs microcontrollers anyway? My next idea was to use the normal GUD gadget implementation, running on a Pi Zero, but outputting to VGA over GPIO. Conceptually this is pretty simple, although in practice it was anything but. The canonical GUD gadget software was based on a 2021 version of [Buildroot](https://buildroot.org/), which was too old to output VGA. I tried, and failed, to update the Buildroot version, as well as to backport the VGA overlay. Neither of those really worked, but I didn't really know what I was doing.

I also played around with generating a custom NixOS image that had a modern kernel and the GUD gadget kernel module. When that didn't work I prepared to run a user space GUD gadget implementation on Raspberry Pi OS. But like, isn't that boring? And then I'll still be stuck at 18 bit colour! And sometimes a girl just wants to tickle her electrons :3

Attempt... 2? 3? 1+i? Returning to MCU land
-------------------------------------------

Okay, so my beloved RP2040 doesn't support USB HS (high-speed). My beloved RP2350 (the newer version of the same chip) doesn't either. But some of my beloved STM32s do!

Initially I was planning to go computer -> USB HS -> STM32 -> SPI bus -> RP2040 -> VGA. But like, that's complicated, and there are 2 microcontrollers to program, and there is so much to go wrong, and the SPI bus protocol is going to need to be robust against lost/extra bits, and AAAAAAAAAA I don't wanna!

But! STM32! I learned through research that some of the nicer ones have an LTDC peripheral, which, among other things, can drive an LCD display. And guess what? Many LCDs take in an R, G, B, HSYNC, and VSYNC signal. That's right - they pretend they're a CRT, and they pretend they have a cute little electron gun inside of them, and the STM32 is like "ok I got u" and can just like, do this natively. And I realize that this is what VGA is, but it's so, so funny to me that the protocol is literally just the manifestation of a physical design that is largely obsolete.

Okay so at this point I'm like, is this even a real project anymore? I'm just connecting the USB peripheral to the LTDC peripheral. What part of this is supposed to take effort? I had already written the GUD gadget implementation. Wasn't I basically already done?

OH BOY.

Anyway, by now it's Christmas time and I fly back to Canada to hang out with my family, as you would expect. I had none of my hardware with me, so now felt like a good time to design the actual board.

[![](https://www.scd31.com/thumb/rcade/rev1-top.webp)](https://www.scd31.com/img/rcade/rev1-top.webp)
[![](https://www.scd31.com/thumb/rcade/rev1-bottom.webp)](https://www.scd31.com/img/rcade/rev1-bottom.webp)

By Christmas Eve, this is what I had. Conceptually, it's a pretty basic board - there's the USB HS input, the VGA output, 3 8-bit DACs, some RAM for the framebuffer, and supporting components. At the heart of it is the STM32H723, which is a microcontroller that's advertised as supporting USB HS and LTDC.

It's worth talking about the DACs a bit. They have a few requirements. They need to map the 8-bit binary space uniformly to the analog domain. They also need to act as a resistor divider - my I/O is at 3.3V, but VGA expects a maximum of 0.7 volts for R/G/B. And finally, they need to be impedance-matched to the 75 ohms of the VGA cable, to prevent reflections and ringing that show up in the image. I am... pretty doubtful we need this at our resolution, but it doesn't hurt, and it increases nerd cred (^:

I encoded all of these requirements into a system of equations, threw it into a SAT solver, and computed all of my resistor values. I checked the output manually and it made sense, so I used these values in my DAC.

Also worth noting is the length-matched traces between the STM32 and the HyperRAM. Length-matching ensures that all the signals arrive at the same time; if some arrive too early or late it can cause issues. The traces aren't impedance-matched, but I did a bit of math and determined they were short enough that I didn't have to worry about it.

Also, I want to talk about the USB port. I used Mini-USB. Alright look. I know I know, I should have used USB-C. But I don't like USB-C! It's a dumb standard. We spent decades teaching non-technical users to plug the square wire into the square hole and the round wire into the round hole. And then we made every hole the same shape!! But they don't all support the same things!! Not even every **cable** supports the same things!! I hate it!! And Mini-USB is so cute. It's not reversible, but who cares? It's more robust than micro USB, while still being small. And it's my board, my rules. So yes, I will keep sending pictures of this board to people, and they will keep complaining it doesn't use USB-C. And I will continue to not care! Mini-USB is CUTE. And by the way, if you read this entire article and **this** is the section you choose to engage with, then you are boring!!! You will never live up to Mini-USB!!

Okay okay sorry about that. I am calm now. With all of that out of the way, I placed the order for the boards. I bought 5 of them, 2 of which were partially assembled. I would complete the rest of the assembly myself, but I didn't want to worry about the more finicky stuff. Between taxes, tariffs, and shipping, it came to a little over a hundred dollars USD.

Disaster strikes
----------------

About a week later, I was back home in NYC. My boards hadn't arrived yet, although I did have access to an STM32H723 development board at this point. To prepare for my boards, I started porting my RP2040 firmware to the STM32H723.

Things were going well until I tried getting USB set up. For some reason, I could only get it working at USB FS speeds. I figured I was just initializing something wrong - maybe a register I was forgetting about, or that wasn't in the HAL? I did a lot of digging, before finding this hidden in the datasheet (emphasis mine):

> The devices embed a USB OTG high-speed (up to 480 Mbit/s) device/host/OTG peripheral
> that supports both full-speed and high-speed operations. It integrates the transceivers for
> full-speed operation (12 Mbit/s) and a UTMI low-pin interface (ULPI) for high-speed
> operation (480 Mbit/s). **When using the USB OTG\_HS interface in HS mode, an external
> PHY device connected to the ULPI is required.**

My heart sank. Yes, despite this chip very clearly advertising support for USB HS, it can't actually do that without an external PHY. This is super easy to miss - I actually told other people about the problem, and often they would tell me I was incorrect until I showed it to them in the datasheet. I've also found many posts on the ST Community forums from people running into the same thing. So yeah, I need a new board.

But because boards are expensive, I figure I'll still use the rev 1 board to validate as much as I can.

Disaster strikes, again
-----------------------

Once the boards come, I complete assembly of one, plug it into my computer, and nothing happens. I find out that the 3.3V rail is shorted to ground. This is the same on all of my boards, even the 3 that are disassembled. Some debugging later, it turns out I moved a via in KiCad and didn't do a re-pour. My ground plane was connected to my power plane.

I have a full CI/CD pipeline set up for my PCBs, so I was surprised it didn't catch this. It turns out it has a bit of wiggle-room, and the re-pour was small enough it didn't get picked up. I now know I need to be disciplined and run DRC locally, ensuring there are literally no differences (and if there are, commit them and push them up to my Git forge).

Although annoying, and quite embarrassing, this wasn't a huge deal. I used a drill bit and very carefully drilled out the offending via by hand. It made a bit of a mess - make sure you use breathing protection - but I got a board that worked.

[![](https://www.scd31.com/thumb/rcade/rev1-drilled.webp)](https://www.scd31.com/img/rcade/rev1-drilled.webp)

The drilled-out via. You can see it directly under the text, near the center-bottom of the image.

At this point I wrote some code that exercised the HyperRAM and VGA. Everything worked great, so I began work on the new board. Here's what my development setup looked like while I was testing:

[![](https://www.scd31.com/thumb/rcade/rev1-ltdc-testing.webp)](https://www.scd31.com/img/rcade/rev1-ltdc-testing.webp)

Even though the rev 1 board didn't work out, Frank pointed out that the difference between it and the previous revision was stark:

[![](https://www.scd31.com/thumb/rcade/rev0-rev1.webp)](https://www.scd31.com/img/rcade/rev0-rev1.webp)

Not a bad pace of development!

Attempt 4 - Rev 2
-----------------

I needed an STM32 that supported ULPI (used for talking to the USB PHY), LTDC, and some kind of external RAM. I looked at dozens of chips and found all sorts of blockers. Chips that actually supported both (but they had overlapping pins), chips that were advertised as supporting both (but in actuality, could only do one or the other, depending on the specific model number), and chips that actually could do both, with unconflicting pins, but only in a BGA package. I did not particularly want to deal with that, mainly because the tiny vias and traces would balloon the board cost even more.

I ended up settling on the STM32H750IBT, a massive, 176 pin, LQFP chip. This thing is larger than some New York apartments, and at over $10 USD, it costs about the same! I have bought entire dev boards for a fraction of this.

Once I picked out the chip, I basically redesigned the entire board from scratch. Sure, I could reuse the DACs, but I needed completely new RAM (the new chip has no HyperBus), as well as the USB PHY and supporting components. Now that my Christmas vacation was over, it took me a solid week to get everything designed. This isn't my most complicated board, but it's certainly my most complex routing:

[![](https://www.scd31.com/thumb/rcade/rev2-routing.webp)](https://www.scd31.com/img/rcade/rev2-routing.webp)

I mean, look at those traces. I'm using basically all available space just to get them to be the same length. ST famously has bad pinouts, and because one of the memory controller pins is located on the complete opposite side of the chip, literally all of the rest of the RAM traces had to be lengthened. And the RAM has a 16-bit data bus. I had to route 38 length-matched traces for the memory alone!

The USB PHY also had a decent number of traces to route, although far less than the RAM. This is probably the part where I'm supposed to say that like, crosstalk is bad and stuff, but we're just gonna ignore that. I had like no space; leave me alone!

Here's what the board looked like:

[![](https://www.scd31.com/thumb/rcade/rev2-top.webp)](https://www.scd31.com/img/rcade/rev2-top.webp)
[![](https://www.scd31.com/thumb/rcade/rev2-bottom.webp)](https://www.scd31.com/img/rcade/rev2-bottom.webp)

And with that, I ordered the board. Waiting for it to arrive just about killed me, but when it finally did, I got to work.

Board bring-up
--------------

Board bring-up is a magical thing. One-by-one, you enable each part of the board, and you make sure that everything works the way you expect. Given that USB burned me before, I decided to start there.

Right out of the gate, I was off to a bumpy start. I got the USB technically working, and I even got it to show up on my computer as USB HS (yay!), but it was super, super flaky. Eventually I worked out that its crystal oscillator was unstable. Going back to the datasheet, I realized I missed a 1M ohm resistor, which was meant to be put in parallel with the crystal. I didn't have one handy, but I know the human body is around that resistance. I put one finger on each terminal of the crystal. It immediately stabilized. I was pretty ecstatic!

The next day I went to the Recurse Center and stole a 1M ohm resistor to affix to the board. (Faculty, if you're reading this, I owe you about a tenth of a cent. Sorry!)

With that over, the rest of the bring-up process was pretty smooth. I got the LTDC running and ported over the rest of the code that implemented the GUD protocol. I had written things pretty naively but, to my surprise, it didn't need any optimization for high-speed USB. I guess that's what a microcontroller with a 480 MHz core will get you!

Running it in the RCade cabinet
-------------------------------

I was already at the Recurse Center at this point, so I popped the back off the RCade, unplugged the VGA from the Pi, and plugged it into my board. It started up immediately - the colours looked great and I got the full 60 Hz framerate. To be honest, I was shocked at how good it looked, and the crowd that had formed was shocked too. I wasn't really a believer that 24 bit colour would be noticeable, but I was totally wrong. The lack of colour banding was striking.

Next, I plugged the board into the Pi, and Frank reconfigured it to make my display adapter the primary display. We launched the normal RCade software and played some games. They looked truly amazing; nothing like before. [Rose](https://rose.hall.ly/), one of the main people who developed the software, joked that it looked so good that some of the graphical shortcuts she took were no longer sufficient.

[![](https://www.scd31.com/thumb/rcade/image-before.webp)](https://www.scd31.com/img/rcade/image-before.webp)
[![](https://www.scd31.com/thumb/rcade/image-after.webp)](https://www.scd31.com/img/rcade/image-after.webp)

It's hard to tell in the pictures but the difference in person was striking. Where it's most obvious is in the lack of banding around the mountains.

This felt amazing, but I wasn't quite ready to leave the board installed. It was fragile - especially with the resistor I bodged on - and it was expensive. I took my board back out and Frank reverted the RCade to how it was before.

Designing a case
----------------

I'll be honest. I don't get that much joy out of 3D modeling. I find it frustrating, tedious, and generally unfulfilling. To get around this, I decided to use [YAPP](https://github.com/mrWheel/YAPP_Box) to design the case. YAPP is a parametric box generator written in OpenSCAD. I wrote a few dozen lines of code and ended up with this beauty:

[![](https://www.scd31.com/thumb/rcade/case-top.webp)](https://www.scd31.com/img/rcade/case-top.webp)
[![](https://www.scd31.com/thumb/rcade/case-bottom.webp)](https://www.scd31.com/img/rcade/case-bottom.webp)

It took barely any time at all and only took 2 physical revisions before I was happy with it. I added the OpenSCAD code to my board repository and CI/CD pipeline. Now, it builds all the files I need to order the boards, as well as the STL files for the case.

[![](https://www.scd31.com/thumb/rcade/case-printing.webp)](https://www.scd31.com/img/rcade/case-printing.webp)

HE'S BEGINNING TO TAKE FORM

And now, with the board in the case:

[![](https://www.scd31.com/thumb/rcade/physical-case-top.webp)](https://www.scd31.com/img/rcade/physical-case-top.webp)
[![](https://www.scd31.com/thumb/rcade/physical-case-bottom.webp)](https://www.scd31.com/img/rcade/physical-case-bottom.webp)

At this point I was starting to prepare myself to install it in the RCade.

Disaster strikes, again??
-------------------------

Everything was done, so I expected I'd just plug it in and be good to go. When I did this, though, nothing happened. After some debugging I realized the USB had completely died on my board. It wasn't showing up on any computer I connected it to, although the STM32 was still chugging along happily (and outputting to VGA).

I still haven't figured out exactly what happened here. I was having a bit of flakiness with the USB already. I vaguely suspect ESD to either the STM32 or the USB PHY, but am not super confident this is the cause. I'm going to keep looking into this. (inb4: wow maybe you shouldn't have touched the crystal without grounding yourself first!)

In the meantime, I assembled a second board and got that installed instead. I'm slightly nervous because I don't have a third board to use if this one also dies, and I don't want to order any more until I can figure out what's killing them. That said, it has been a few days now since I installed it, and despite running 24/7, there's no signs of it dying yet.

[![](https://www.scd31.com/thumb/rcade/in-cabinet.webp)](https://www.scd31.com/img/rcade/in-cabinet.webp)

Here's the board in its case, installed in the RCade. We're still running it off the Raspberry Pi for now, but soon we'll have that switched out with a laptop. I can't wait!

Future improvements
-------------------

There are all sorts of things I want to change. I want the board to also support audio, with an integrated amp. Perhaps even a tube amp? I just think it would be funny. And being able to read input from the controls would be cool too.

On the software side, I want double or triple buffering. I actually got them both working, although they didn't play nice with the deltas that GUD sends over the wire. There are workarounds to this that I haven't implemented yet. It would also be nice to give GUD the ability to disable these deltas; perhaps that would be a good feature for me to add to the kernel module. Writing some documentation on the GUD protocol could be good too!

This was a really fun project, and it's not over yet, but I think all the hard stuff is pretty much done (although - I've thought that before!). I really wasn't expecting this to take as long as it did, but I learned so much, and I'm a stronger engineer for it.

Source code
-----------

There's a few repositories of interest:

The hardware lives [here](https://gitlab.scd31.com/sophie/stm32-usb-vga-adapter-hardware).

The software lives [here](https://gitlab.scd31.com/sophie/stm32-usb-vga-rcade-adapter).

If you're interested, the original software for the RP2040 lives [here](https://gitlab.scd31.com/sophie/rp2040-rcade-crt-driver).

My very messy DAC equations live [here](https://gitlab.scd31.com/sophie/vga-dac-formula-sage).

My Nix GUD gadget attempt lives [here](https://gitlab.scd31.com/sophie/rcade-gud-os).

I also wrote a fair bit of scratch code while learning (such as for my kernel module), but I don't think any of it was worth putting it in my Git forge.