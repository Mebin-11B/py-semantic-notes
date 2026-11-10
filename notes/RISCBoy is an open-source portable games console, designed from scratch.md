---
title: "RISCBoy is an open-source portable games console, designed from scratch"
url: https://github.com/Wren6991/RISCBoy
clipped: 2026-08-31 12:22:41
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [RISCBoy is an open-source portable games console, designed from scratch](https://github.com/Wren6991/RISCBoy)

## Digest Summary
RISCBoy is an open‑source, portable handheld console implemented entirely in synthesizable Verilog 2005 and designed for FPGA deployment. It features a RISC‑V‑compatible RV32IMC CPU that passes the official RISC‑V compliance suite and formal verification checks, along with M‑mode CSRs, exception handling, and vectored interrupts. The system includes a raster graphics pipeline, display controller, AHB‑lite/APB bus fabric, memory controllers, UART, GPIO, and other peripherals. The primary target hardware is a Lattice iCE40‑HX8k (7 680 LEs), though a reduced RV32I core can run on the iCE40‑UP5k, and experimental support exists for Lattice ECP5 boards using internal 256 KiB synchronous RAM. Build flow relies on the open‑source IceStorm toolchain, a custom RISC‑V GNU toolchain (RV32IMC/rv32i) and Xilinx ISIM for simulation. The repository is organized into submodules covering HDL, documentation, PCB KiCad files, and test suites. PCB Rev A is a 5 × 5 cm 4‑layer design compatible with iTead prototyping; Rev B is pending further gateware and bootloader maturation.

---

## Full Article

[Skip to content](https://github.com/Wren6991/RISCBoy#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [Wren6991](https://github.com/Wren6991)    
    /
    
      [RISCBoy](https://github.com/Wren6991/RISCBoy)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2FWren6991%2FRISCBoy)    You must be signed in to change notification settings

  

  
- 
          [Fork
    22](https://github.com/login?return_to=%2FWren6991%2FRISCBoy)
  

  
- 
        
        [Star
          505](https://github.com/login?return_to=%2FWren6991%2FRISCBoy)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     master[Branches](https://github.com/Wren6991/RISCBoy/branches)[Tags](https://github.com/Wren6991/RISCBoy/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[736 Commits](https://github.com/Wren6991/RISCBoy/commits/master/)736 Commits

## Folders and files

NameNameLast commit messageLast commit date[board](https://github.com/Wren6991/RISCBoy/tree/master/board)[board](https://github.com/Wren6991/RISCBoy/tree/master/board)  [doc](https://github.com/Wren6991/RISCBoy/tree/master/doc)[doc](https://github.com/Wren6991/RISCBoy/tree/master/doc)  [hdl](https://github.com/Wren6991/RISCBoy/tree/master/hdl)[hdl](https://github.com/Wren6991/RISCBoy/tree/master/hdl)  [reference](https://github.com/Wren6991/RISCBoy/tree/master/reference)[reference](https://github.com/Wren6991/RISCBoy/tree/master/reference)  [scripts @ 1784767](https://github.com/Wren6991/fpgascripts/tree/17847670571b3b6037730182ed0d6182ce2230a6)[scripts @ 1784767](https://github.com/Wren6991/fpgascripts/tree/17847670571b3b6037730182ed0d6182ce2230a6)  [software](https://github.com/Wren6991/RISCBoy/tree/master/software)[software](https://github.com/Wren6991/RISCBoy/tree/master/software)  [synth](https://github.com/Wren6991/RISCBoy/tree/master/synth)[synth](https://github.com/Wren6991/RISCBoy/tree/master/synth)  [test](https://github.com/Wren6991/RISCBoy/tree/master/test)[test](https://github.com/Wren6991/RISCBoy/tree/master/test)  [.gitattributes](https://github.com/Wren6991/RISCBoy/blob/master/.gitattributes)[.gitattributes](https://github.com/Wren6991/RISCBoy/blob/master/.gitattributes)  [.gitignore](https://github.com/Wren6991/RISCBoy/blob/master/.gitignore)[.gitignore](https://github.com/Wren6991/RISCBoy/blob/master/.gitignore)  [.gitmodules](https://github.com/Wren6991/RISCBoy/blob/master/.gitmodules)[.gitmodules](https://github.com/Wren6991/RISCBoy/blob/master/.gitmodules)  [Readme.md](https://github.com/Wren6991/RISCBoy/blob/master/Readme.md)[Readme.md](https://github.com/Wren6991/RISCBoy/blob/master/Readme.md)  [TODO.todo](https://github.com/Wren6991/RISCBoy/blob/master/TODO.todo)[TODO.todo](https://github.com/Wren6991/RISCBoy/blob/master/TODO.todo)  [sourceme](https://github.com/Wren6991/RISCBoy/blob/master/sourceme)[sourceme](https://github.com/Wren6991/RISCBoy/blob/master/sourceme)  View all files

## Repository files navigation

# RISCBoy

RISCBoy is an open-source portable games console, designed from scratch. This includes:

- A RISC-V compatible CPU

- A raster graphics pipeline and display controller

- Other chip infrastructure: busfabric, memory controllers, UART, GPIO etc.

- A PCB layout in KiCad

It is a Gameboy Advance from a parallel universe where RISC-V existed in 2001. A love letter to the handheld consoles from my childhood, and a 3AM drunk text to the technology that powered them.

The design is written in synthesisable Verilog 2005, and is intended to fit onto an iCE40-HX8k FPGA. This is a LUT4-based FPGA with 7680 logic elements, so fitting a 32 bit games console requires a crowbar and some vaseline, or perhaps just careful design. The HX8k was once the largest FPGA targeted by the open-source [Icestorm](http://www.clifford.at/icestorm/) FPGA toolchain, but that toolchain has since [moved on](https://github.com/SymbiFlow/prjtrellis) to [greater things](https://github.com/SymbiFlow/prjxray).

More detailed information can be found in the [documentation](https://github.com/Wren6991/RISCBoy/blob/master/doc/riscboy_doc.pdf).

The processor supports the RV32IMC instruction set, and passes the RISC-V compliance suite for these instructions, as well as the [riscv-formal](https://github.com/SymbioticEDA/riscv-formal) verification suite, and some of my own formal property checks for instruction frontend consistency and basic bus compliance. It also supports M-mode CSRs, exceptions, and a simple compliant extension for vectored external interrupts.

## Cloning

This repository uses submodules for HDL as well as tests
 `git clone --recursive https://github.com/Wren6991/RISCBoy.git riscboy` 

Alternatively
 `git clone https://github.com/Wren6991/RISCBoy.git riscboy
cd riscboy
git submodule update --init --recursive` 

Note a recursive submodule update is required to run the processor's standalone tests. This is not necessary for building RISCBoy gateware.

## Building RV32IMC Toolchain

The RV32IMC toolchain is required for compilation of software-based tests. Follow the instructions on the [RISC-V GNU Toolchain GitHub](https://github.com/riscv/riscv-gnu-toolchain), except for the configure line:
 `# Prerequisites for Ubuntu 20.04
sudo apt install -y autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev
cd /tmp
git clone --recursive https://github.com/riscv/riscv-gnu-toolchain
cd riscv-gnu-toolchain
# The ./configure arguments are the most important difference
./configure --prefix=/opt/riscv --with-arch=rv32imc --with-abi=ilp32 --with-multilib-generator="rv32i-ilp32--;rv32ic-ilp32--;rv32im-ilp32--;rv32imc-ilp32--"
sudo mkdir /opt/riscv
sudo chown $(whoami) /opt/riscv
make -j $(nproc)` 

On smaller FPGAs, like the iCE40 UP5k, RISCBoy may be configured to use a smaller RV32I variant of the processor, rather than the higher-performance RV32IMC version. The compiler will support any of the ISA variants available on RISCBoy, but we must also instruct the toolchain build scripts to produce standard libraries for these variants, via the  `--with-multilib`  arguments. Running a RV32I executable linked against an RV32IMC standard library on an RV32I-only processor will ruin your day!

## Simulation

The simulation flow is driven by Xilinx ISIM 14.x; makefiles are found in the scripts/ folder. This has only been tested with the Linux version of ISIM.

You will also need to checkout the RISC-V compliance suite in order to run these tests (note the  `-- test`  is required to stop git from looking in the KiCad directories and complaining about the library structure there).
 ` `$ git submodule update --init --recursive
` ` 

Once this is ready, you should be able to run the following:
 `. sourceme
cd test
./runtests` 

which will run all of the HDL-level tests. Software tests will require the RV32IC toolchain. You may need to adjust some of the paths in  `sourceme`  if ISIM is installed in a non-default location. To graphically debug a test, run its makefile directly:
 `cd system
make TEST=helloworld gui` 

## PCB

The image shows the Rev A PCB. It is compatible with iTead's 4-layer 5x5 cm prototyping service, which currently costs $65 for 10 boards.

The schematic can be viewed [here (pdf)](https://github.com/Wren6991/RISCBoy/blob/master/board/fpgaboy.pdf)

Rev B will look quite different; I am waiting for the gateware and bootloader to mature before proceeding. My current dev hardware looks a lot like my [Snowflake FPGA board](https://github.com/Wren6991/Snowflake-FPGA).

## Synthesis

FPGA synthesis for iCE40 uses an open-source toolchain. If you would like to build this project using the existing makefiles, you will first need to build the toolchain I used:

- [Yosys](https://github.com/yosyshq/yosys) for synthesis

- [nextpnr](https://github.com/YosysHQ/nextpnr) for place and route

- [Project Icestorm](http://www.clifford.at/icestorm/) for bitstream generation

Note that I have only built these on Linux. I've heard it is possible to build these on Windows, but haven't tried it. However, they can be built on a Raspberry Pi, which is neat.

Once the toolchain is in place, run
 `. sourceme
cd synth
make -f HX8k-EVN.mk bit` 

to generate an FPGA image suitable for Lattice HX8k evaluation board.

There is also highly experimental support (i.e. not my main dev platform) for ECP5, with board files for the Lattice LEF5UM5G-85F-EVN evaluation board:
 `make -f ECP5-EVN.mk BUILD=full bit` 

This build replaces the external, 512 kiB, 16 bit wide SRAM of RISCBoy development hardware with an internal, 256 kiB, 32 bit wide synchronous memory, which Trellis builds out of ECP5 sysmem blocks.

## Directory Structure

-  `board` : KiCad files for main RISCBoy PCB and other small boards used during development

-  `doc` : LaTeX source and diagrams for documentation, and the most recently built PDF

-  `hdl` : The Verilog source for RISCBoy gateware.

-  `busfabric` : AHB-lite crossbar and APB peripheral fabric

-  `graphics` : Source for the pixel processing unit

-  `hazard5` : Source for the RISC-V processor. This is completely self-contained.

-  `mem` : Memory controllers, and inference/injection wrappers and models for the memories themselves

-  `peris` : Small peripherals such as UART, SPI, PWM

-  `riscboy_core` : Structural module to instantiate and connect the components that comprise RISCBoy

-  `riscboy_fpga` : Top-level wrappers for a few different FPGAs and boards: connect up IOs, provide clock and reset

-  `reference` : a few PDFs for standards used in RISCBoy, e.g. the RISC-V instruction set

-  `scripts` : Junk that I can't put anywhere else

-  `software` : Loose collection of C files that are used for system-level tests. Not really a useful software tree yet.

-  `synth` : Working directory for running whole-system synthesis. Top-level makefiles, pin constraint files.

-  `test` : Regression tests. Some are Verilog testbenches, others are software testcases that run on simulations of the processor or the full system.

## About

Portable games console, designed from scratch: CPU, graphics, PCB, and the kitchen sink

### Topics

[cpu](https://github.com/topics/cpu)[fpga](https://github.com/topics/fpga)[gameboy](https://github.com/topics/gameboy)[pcb](https://github.com/topics/pcb)[risc](https://github.com/topics/risc)[risc-v](https://github.com/topics/risc-v)

### Resources

[Readme](https://github.com/Wren6991/RISCBoy#readme-ov-file)[Activity](https://github.com/Wren6991/RISCBoy/activity)

### Stars

505 stars

### Watchers

18 watching

### Forks

[22 forks](https://github.com/Wren6991/RISCBoy/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FWren6991%2FRISCBoy&report=Wren6991+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
