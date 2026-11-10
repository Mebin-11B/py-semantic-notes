---
title: "Memory Prices | DAM"
url: https://dam.stanford.edu/memory-prices.html
clipped: 2026-08-31 12:26:38
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Memory Prices | DAM](https://dam.stanford.edu/memory-prices.html)

## Full Article

[Stanford University](https://stanford.edu)
      
    
    
    

    
      
        Memory Prices 
      
    
    
      

  Historic and current memory and storage prices, collected in the spirit of
  John C. McCallum's classic memory-price dataset â interactive, with the raw data downloadable.
  Hover for details, click the legend to toggle series, drag or use the slider to zoom, and use the
  camera icon to export an image.

  [â¬ Download CSV](https://dam.stanford.edu/assets/memory-prices/memory-prices.csv)
  Loadingâ¦

  

## Price per gigabyte over time

  Historical lowest $/GB on a log scale â one line per memory type:
    DRAM, NAND flash, and HBM.
    Toggle nominal vs inflation-adjusted dollars (constant 2024 $, US CPI-U).
  
    Nominal USDReal USD (2024$)
  
  

  

## DRAM price by generation

  The DRAM line above, broken out by generation across the full history â
    Pre-DDR (SDRAM/core), DDR, DDR2, DDR3, DDR4, DDR5. (Generation is inferred from product
    descriptions, so older points are approximate.)
  
    Nominal USDReal USD (2024$)
  
  

  

## Accelerator cost breakdown

  
    Modeled estimates from Epoch AI: quarterly accelerator cost across the four
    largest AI-accelerator designers â Nvidia, AMD, Google (TPU) and Amazon (Trainium)
    â stacked by component (HBM, logic die, packaging/CoWoS, auxiliary), a
    production-volume-weighted average.
  
  
    Absolute ($B/quarter)Share (%)
  
  

  

## HBM price by generation

  By HBM generation (HBM2e â HBM3 â HBM3e â HBM4). HBM is sold only to accelerator
    makers on confidential contracts â there is no public spot market â so these are
    sparse industry-analyst estimates (TrendForce / SemiAnalysis), not transaction
    prices. HBM4 is projected (launches Q3 2026). $/TBps is cost per unit of memory bandwidth
    (stack price Ã· per-stack bandwidth).
  
    $/GB$/TBps
  
  

  Methodology note. $/GB is the cheapest listed retail price in nominal
  USD â not contract, average, inflation-adjusted, or a confirmed sale price. DRAM history is
  the McCallum dataset (extended from mid-2024 by Keepa Amazon prices); NAND is Keepa's cheapest
  consumer-NVMe price from 2016 (approximate anchors before); HBM figures are modeled estimates.
  Sources are listed below and in the downloadable dataset; please check before citing.

  Methodology, sources and caveats

  

### Sources and method

  
    CategoryWhat we trackSource and methodReliability
    
      DRAM $/GB
          cheapest retail $/GB, overall and by generation (DDR3/DDR4/DDR5)
          Deep history (1957â2024): the McCallum memory-price dataset
              ([jcmit.net,
              via the Internet Archive](https://web.archive.org/web/20250716092935/https://jcmit.net/memoryprice.htm)). Mid-2024 onward: the cheapest new
              consumer DIMM each month from [Keepa](https://keepa.com) (Amazon retail
              price history), refreshed monthly.
          Reference + live
      NAND $/GB
          cheapest retail SSD $/GB, 2010âpresent
          2016 onward: the cheapest consumer NVMe SSD each month
              from [Keepa](https://keepa.com) (Amazon retail price history), refreshed monthly;
              SATA and enterprise/datacenter drives are excluded, and per-drive posting glitches are
              filtered (see caveats). 2010â2016: four approximate pre-NVMe
              anchor points (no McCallum-equivalent flash dataset exists).
          Live + approximate
      HBM spend and cost breakdown
          quarterly HBM spend ($B) and each component's share (%) of the accelerator bill of
              materials (HBM, logic, packaging, auxiliary)
          [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)
              (CC-BY): a modeled estimate, production-volume-weighted across the four largest
              accelerator designers (Nvidia, AMD, Google, Amazon); aggregate only, no per-company split.
          External estimate
      HBM $/GB by generation
          HBM price per GB and per TB/s of bandwidth, by generation
          Industry-analyst estimates â
              [TrendForce](https://www.trendforce.com) and
              [SemiAnalysis](https://www.semianalysis.com) (HBM has no public spot market);
              bandwidth from [JEDEC/Rambus](https://en.wikipedia.org/wiki/High_Bandwidth_Memory).
              HBM4 is projected.
          Sparse estimate
    
  

  

### Caveats

  
    
- $/GB defaults to the cheapest retail price in nominal USD (not contract or
        average; retail lags contract). Use the Real USD toggle for inflation-adjusted
        values â constant 2024 dollars via US CPI-U annual averages (BLS).
    
- The cheapest listing often tracks an end-of-life generation being cleared out,
        not the leading edge â the per-generation chart shows this.
    
- These are cheapest listed prices over time (via Keepa), not confirmed
        sales. For the SSD data, obvious posting errors are removed â any month a drive is listed
        more than 60% below its own typical price (e.g. a $130 SSD shown at $4) is dropped.
    
- The DRAM line splices two sources at mid-2024 (McCallum â Keepa); a small step
        there is expected, since Amazon's cheapest clearance can sit below McCallum's representative low.
    
- HBM figures are modeled estimates (cost share and spend), not measured prices.
  

  

### Updates

  

DRAM and NAND $/GB refresh monthly from Keepa; HBM updates quarterly (Epoch AI).
     The McCallum backbone and HBM estimates are fixed. The downloadable
     [CSV](https://dam.stanford.edu/assets/memory-prices/memory-prices.csv) lists every point with its source.

  

### About

  

Compiled and maintained by David Shim, Stanford DAM project. Questions or corrections:
     [hsshim@stanford.edu](mailto:hsshim@stanford.edu).
