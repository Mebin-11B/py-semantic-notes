---
title: "How to sequence your own DNA at home"
url: https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home
clipped: 2026-08-31 12:22:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How to sequence your own DNA at home](https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home)

## Digest Summary
The author describes an end‑to‑end workflow for personal whole‑genome sequencing using an Oxford Nanopore MinION. After collecting cheek cells with sterile swabs, DNA is extracted with the NEB Monarch HMW kit, bound to magnetic beads, washed, and eluted. Quantification is performed on a Qubit fluorometer before a low‑input (≈14 ng) repair/end‑prep using FFPE DNA Repair Buffer, FFPE DNA Repair Mix, and N‑Prep Enzyme Mix, followed by AMPure XP bead cleanup. Adapter ligation employs ONT LNB, LA, and Salt‑T4 DNA ligase, with a second bead‑based cleanup using Long Fragment Buffer. The final library is mixed with sequencing buffer and library beads, primed, and loaded onto a FLO‑MIN114 flow cell. Basecalling is done with Dorado (HAC or SUP), reads are aligned to GRCh38 via minimap2, and variants are called with Clair3. Annotation uses Ensembl VEP, ClinVar, gnomAD, and PharmGKB to generate a VCF with gene, consequence, clinical significance, population frequency, and depth metrics. The pipeline provides a queryable genome for pharmacogenomic insights and variant interpretation, though it is not a diagnostic test.

---

## Full Article

# How to sequence your own DNA at home

I have now sequenced my own genome 5 times with an [Oxford Nanopore Technologies MinION](https://nanoporetech.com/products/sequence/minion). This means collecting them from a swab, prepping them for sequencing, running them through a sequencer, then doing analysis over them. 

Cheek cells are easily accessible and replenish pretty quickly. They are not used for cancer diagnosis, inflammation, or what genes are being activated in other parts of the body (like if you have hives on your chest and want to test what genes are being expressed in the cells that are inflamed), since you would want to collect the cells having problems and compare them against other normal versions of those cells. 

To sequence the cells, I bought lab materials and consumables to sequence my own genome at home. It took me about two months to get everything together to do a full end to end high quality run. Likewise, the costs are still out of reach for the average person but they are decreasing (exponentially!) and we will eventually have affordable technology, like a cell phone or AI, telling us about our DNA + RNA expression real-time.

# What can I even do with my own genome?

Before we actually spend all this time and money on sequencing, what can we actually do with our genome? 

The genome is not magic by itself- it is the reference layer. Once I have a VCF, I can run it through tools like [VEP](https://www.ensembl.org/Tools/VEP), [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/), [gnomAD](https://gnomad.broadinstitute.org/), [PharmGKB](https://www.clinpgx.org/) (highly recommend), [Gene Inspector](https://gene-inspector.pro/), or Claude, and start asking: 
- Which variants do I have?
- Which genes and pathways are affected?
- Which medicines might I metabolize differently?
- What rare variants should I take seriously?
- Where does the model know nothing yet? 

This last part matters- the information produced is not yet diagnosis-level, and it is definitely not “edit yourself with CRISPR because an AI said so.” The near-term value is turning a static genome into something queryable, but the “edit yourself with CRISPR” will most likely follow. DNA is the stable reference, RNA is the current state, and we will eventually integrate all biosensor data into one ‘model’ of yourself.

Here are a list of links and Twitter posts to help:
- Genetic variants from first principles: [Adib @ ICML 🇰🇷 Adib @ ICML 🇰🇷 on Twitter / X](https://x.com/adibvafa/status/1943172968374284608)
- TLDR these genes, and the combinations of them, compound into real physical diseases. We will probably map these in the next decade 
- Pass your genome + RNA to any of these models: [https://www.biotender.online/bio-model-install-guide/](https://www.biotender.online/bio-model-install-guide/) 
- Give your genome to Claude Code- message me if you want me to set this up for you 
- [Take it to a doctor](https://x.com/parmita/status/2024197362286231640) if you metabolize particular drugs differently 
- [Patrick Collison post](https://x.com/patrickc/status/2045164908912968060?lang=en) on using agents to talk to his genome

# Protocol Steps

This is dense- you are welcome read this, or feed it to your AI. Feel free to copy and paste the URL of this and have ChatGPT walk you through it. If you have AR glasses, even better, since the AI can walk you through the whole protocol.

### Hardware

- [Oxford Nanopore Technologies MinION](https://store.nanoporetech.com/us/minion.html) ($7.5k)
- Laptop/workstation for MinKNOW (any PC should be fine)
- 100GB+ storage for outputs
- GPU for Dorado basecalling
- [Vortex](https://www.premiumvials.com/intllab-lab-vortex-mixer-touch-function-lab-vortexer-tattoo-ink-gel-polish-eyelash-adhesives-acylic-paints-test-tubes-and-centrifuge-tubes/?setCurrencyId=1&sku=B08CR43XR3&gad_source=1&gad_campaignid=17182097677&gbraid=0AAAAADpaBkD8X3NHGME9qLpyX764qirew&gclid=Cj0KCQjwk_bPBhDXARIsACiq8R3NH7o4Itb-exPNJG6bpxF2Tcq-r-6r5qv467VZoP-dd-I64DOogK8aAoOqEALw_wcB) ($50)
- [Heat block](https://www.amazon.com/ONiLAB-Mini-Incubator-Aluminium-Calibration/dp/B09VDHS8Z1/ref=sr_1_4?c=ts&dib=eyJ2IjoiMSJ9.DxmMKmWh0Bx0gedZkoko5BEpl9GgEYm-mnndXVtgU_vkjNyUdZb3EOpONsMCc8lEeqeTd62z1zdZ6PLqyHIPJ84nGwhwAJTdaNwja0ciEjuGokdrHcpSKrlrH9LQuEERzNR9d9yjZVuzVIQSTad_id9dKyLBjVrfu_R9Tbexb7CFjdiY8amEbtcmW0EvB8JQpCujFEEuCymGw9aMbx6IBxWmoLCVGHvzHxsNqZOvldQXvblZc19u5Fg3LAog-F6vY6mO063kTaDoGYqLt2lFpL_fiFEs8qZeFawmWniN59E.KheuyTowfnORjWIMj8Z3GE8ZbxOJ3mvUPw2mzbgUolI&dib_tag=se&keywords=Lab%2BHeat%2BBlocks&qid=1779942886&s=industrial&sr=1-4&ts_id=317999011&th=1) ($250)
- [Centrifuge](https://www.ebay.com/p/1401686604?iid=257405680491) ($400 used on eBay)

### Consumables

- [SQK-LSK114 Ligation Sequencing Kit V14 for DNA](https://store.nanoporetech.com/us/ligation-sequencing-kit-v14.html)
- [EXP-WSH004 Flow Cell Wash Kit](https://store.nanoporetech.com/us/flow-cell-wash-kit-xl.html)
- [EXP-CTL001 Control material](https://store.nanoporetech.com/us/control-expansion.html)
- [PBS 1x](https://www.amazon.com/Phosphate-Buffered-Laboratory-Solution-Dilution/dp/B0F37JVYPM/ref=pd_lpo_d_sccl_1/141-3646762-1592425?pd_rd_w=Vio7Q&content-id=amzn1.sym.4c8c52db-06f8-4e42-8e56-912796f2ea6c&pf_rd_p=4c8c52db-06f8-4e42-8e56-912796f2ea6c&pf_rd_r=1RAYMT518CPA4P35Y3JR&pd_rd_wg=8y9gl&pd_rd_r=214b114f-b8e3-4f2a-b195-854c7ee5af81&pd_rd_i=B0F37JVYPM&psc=1)
- [Isohelix Buccal swabs](https://isohelix.com/isohelix-dna-rna-buccal-swabs/)

### Reagents

- DNA extraction kit
- [NEB Monarch HMW DNA Extraction Kit for Cells & Blood](https://www.neb.com/en-us/products/t3050-monarch-hmw-dna-extraction-kit-for-cells-and-blood?srsltid=AfmBOopwK2Ptt58Wnqc57Ap-fWeURP3IwAkTuURYQ2y8WJA1T0bRXPfm) ($87 for 5 runs)
- Nuclei Prep Buffer
- Nuclei Lysis Buffer
- RNase A
- Proteinase K
- Precipitation Enhancer
- DNA Capture Beads
- gDNA Wash Buffer
- Elution Buffer II
- Bead retainers / Monarch collection parts from kit
- DNA library-prep reagents
- [NEBNext Companion Module v2](https://www.neb.com/en-us/products/e7672-nebnext-companion-module-oxford-nanopore-technologies-ligation-sequencing) / repair-end prep reagents ($760 for 24 reactions)
- FFPE DNA Repair Buffer
- FFPE DNA Repair Mix
- Ultra II End-prep Reaction Buffer
- Ultra II End-prep Enzyme Mix
- NEBNext Quick T4 DNA Ligase
- [Oxford Nanopore SQK-LSK114](https://store.nanoporetech.com/ligation-sequencing-kit-v14.html) ($720 for 6 reactions)
- Long Fragment Buffer / LFB
- Elution Buffer / EB
- Ligation Adapter / LA
- Ligation Buffer / LNB
- Sequencing Buffer / SB
- Library Beads / LIB
- Flow cell priming reagents
- Flow Cell Flush / FCF
- Flow Cell Tether / FCT
- BSA
- AMPure XP beads
- 80% ethanol
- [Nuclease-free water](https://www.neb.com/en-us/products/b1500-nuclease-free-water) ($32 for 25mL)
- DNA quantity measurement
- Qubit fluorometer
- Qubit dsDNA BR or HS Assay Kit

### Bench equipment

- Microcentrifuge
- Vortex mixer
- Heat block / dry bath
- Magnetic rack for 1.5/2 mL tubes
- Tube racks
- Ice bucket / cold block
- Freezer at -20°C
- Fridge at 4°C
- Pipettes
- [P1000](https://www.celltreat.com/product/230310/?srsltid=AfmBOop7MuiqtVqRT8AACyVnfJUa00gGjI6vS3r-DmRRr42d-AIkpvL4) (100–1000 µL)
- [P200](https://www.celltreat.com/product/230305/?srsltid=AfmBOoocy9DW-W0XWDau5WS9ttg4giT7eHEe_KTqbuJsCfezbYkR_I_T) (0–200 µL)
- [P20](https://www.celltreat.com/product/230300/?srsltid=AfmBOor2Ua9Ksz2GSp2yiixRHjD7cQPZZps1lbH5M99LmytpdkBR9O_P) (2–20 µL)
- [P10](https://www.celltreat.com/product/230299/?srsltid=AfmBOooUG9IKlj51JFTqOAqxtzX46tKQp4vgfZM3U7ZO6Jl0lIeJWf2j) (1-10 µL)

## Plastics / Lab Pro-style consumables

- Sterile flocked cheek swabs
- 1.5 mL microcentrifuge tubes
- 2.0 mL microcentrifuge tubes
- DNA LoBind 1.5 mL tubes
- RNA LoBind tubes
- 0.2 mL PCR tubes
- Qubit assay tubes
- Pipette sterile filtered tips
- [P1000](https://www.celltreat.com/product/229021/?srsltid=AfmBOooMVUkpab8utFQDOJx9T7-Iecml2LwChJ8ouKGHCGOIRS_nGzU_) (100–1000 µL)
- [P200](https://www.celltreat.com/product/229019/?srsltid=AfmBOoq_AY6muqjDIEN4a3UqyzFJRQle3mttQdRq8tYVYV_XMVk_tNI_) (0–200 µL)
- [P20](https://www.celltreat.com/product/229017/?srsltid=AfmBOop_O0H8GcXsX9NCabN5mW28MXO6yzvZMRMn_ASZMLBnvKw2p9eD) (2–20 µL)
- [P10](https://www.celltreat.com/product/229015/?srsltid=AfmBOooIp9QLYVdz_j6wAbuGSSRNUZxfvzq0aWoSYm38Y2kt_EkpD2Yz) (1-10 µL)
- Wide-bore P200 tips
- Tube labels / lab marker
- [Gloves](https://labproinc.com/products/labclean-unicare-soft-blue-textured-lc-g-nb200-l)

## Software stack

- MinKNOW
- Dorado
- minimap2
- samtools
- mosdepth
- NanoPlot or pycoQC
- Clair3
- DeepVariant, optional
- Ensembl VEP
- ClinVar
- gnomAD
- PharmGKB
- dbSNP, optional
- Python/R
- SQLite/Postgres for query layer later

# End-to-end DNA sequencing protocol 

The goal is to go from 2 cheek-swab samples → MinION sequencing

# 0. Setup

- Gloves on.
- Clean bench.
- Label tubes:
-  `Cheek sample` 
-  `Extracted DNA` 
-  `End-prep` 
-  `Ligation` 
-  `Final library` 
-  `Priming mix` 
-  `Loading mix` 
- Bring AMPure XP beads to room temperature.
- Keep enzyme mixes cold.
- Set heat block to 56°C.
- Keep Nuclei Prep Buffer cold.
- Confirm gDNA Wash Buffer already has ethanol added.
- Confirm you have isopropanol for DNA binding.
- Confirm you have fresh 80% ethanol for AMPure cleanup.
- Confirm you have the corrected ONT reagents:
- FFPE DNA Repair Buffer v2
- FFPE DNA Repair Mix
- N-Prep Enzyme Mix
- Salt-T4 DNA Ligase
- LNB
- LA
- LFB
- EB
- SB
- LIB
- FCF
- FCT

# 1. Collect cheek cells

Goal: get as much cheek-cell material as possible into PBS.
- Rinse mouth with water.
- Wait 10 minutes.
- Do not brush teeth.
- Do not use mouthwash.
- Scrape inside cheek firmly for 60 seconds.
- Add 1 mL cold PBS to labeled tube.
- Put swab head into PBS.
- Vortex 10 seconds.
- Press swab against tube wall to squeeze liquid out.
- Remove and discard swab.

What good looks like:Copy ` `PBS may look slightly cloudy.` ` 

# 2. Pellet cheek cells

Goal: concentrate cells and remove excess PBS.
- Spin at 2,000 × g for 30 seconds.
- Look for a small white/off-white pellet or smear.
- Remove most PBS with P1000.
- Remove more PBS carefully with P200.
- Leave 50–100 µL above the pellet.
- Flick gently to resuspend the pellet.

Do not aspirate the pellet.

# 3. Prepare Monarch lysis solutions for one sample

## Nuclei Prep Solution

Copy ` `165 µL Nuclei Prep Buffer
5.5 µL RNase A` ` 

Mix gently. Keep cold.

You will use 150 µL.

## Nuclei Lysis Solution

Copy ` `165 µL Nuclei Lysis Buffer
11 µL Proteinase K` ` 

Mix gently. Keep at room temperature.

You will use 150 µL.

The extra volume is intentional so pipetting error does not leave you short.

# 4. Lyse cells

Goal: break open cells and digest proteins while preserving long genomic DNA.
- Add 150 µL Nuclei Prep Solution to the resuspended cheek-cell pellet.
- Pipette up/down gently 10 times.
- Incubate 2 minutes at room temperature.
- Add 150 µL Nuclei Lysis Solution.
- Invert tube gently 10 times.
- Do not vortex.
- Incubate at 56°C for 10 minutes.

What good looks like:Copy ` `The liquid may become more viscous.` ` 

Do not vortex after lysis. At this point, the priority is preserving high molecular weight DNA.

# 5. Bind DNA to Monarch capture beads

Goal: precipitate genomic DNA onto the large Monarch capture beads.
- Add 75 µL Precipitation Enhancer.
- Invert gently 8–10 times.
- Add 2 DNA Capture Beads.
- Add 275 µL isopropanol.
- Invert slowly 30 times.
- Do not vortex.

Important:Copy ` `The beads now carry the DNA.
Do not lose the beads.
Do not use ethanol here.` ` 

# 6. Wash DNA-bound beads

Goal: wash contaminants away while keeping DNA bound to the capture beads.
- Let beads settle briefly.
- Remove liquid carefully without removing beads.
- Add 500 µL gDNA Wash Buffer.
- Invert gently 2–3 times.
- Remove wash buffer carefully.
- Add another 500 µL gDNA Wash Buffer.
- Invert gently 2–3 times.
- Remove wash buffer carefully.
- Remove as much residual wash as practical without touching or removing beads.

Critical:Copy ` `gDNA Wash Buffer must already have ethanol added.` ` 

# 7. Elute genomic DNA

Goal: release purified genomic DNA from the Monarch capture beads.
- Put bead retainer into Monarch collection tube.
- Transfer/pour beads into the retainer.
- Pulse spin ≤1 second.
- Move beads to a clean Monarch tube.
- Add 100 µL Elution Buffer II.
- Incubate at 56°C for 5 minutes.
- Put bead retainer over a clean DNA LoBind tube labeled  `Extracted DNA` .
- Transfer eluate + beads into bead retainer.
- Spin at 12,000 × g for 30 seconds.
- Keep the eluate.

The eluate is the purified genomic DNA.

Do not discard the eluate.

# 8. Measure quantity of DNA with a Fluorometer

Goal: measure whether there is enough DNA to justify ONT library prep.

Use:Copy ` `1x dsDNA High Sensitivity` ` 

Do not select the older non-1X dsDNA HS workflow if using the premixed 1X reagent.

## Standards

Standard #1:Copy ` `190 µL 1X dsDNA HS working solution
10 µL Standard #1` ` 

Standard #2:Copy ` `190 µL 1X dsDNA HS working solution
10 µL Standard #2` ` 

## Sample, first attempt

Copy ` `198 µL 1X dsDNA HS working solution
2 µL DNA` ` 

On Qubit, enter:Copy ` `Sample volume = 2 µL` ` 

## If too low

Use more DNA in a fresh Qubit tube:Copy ` `190 µL 1X dsDNA HS working solution
10 µL DNA` ` 

On Qubit, enter:Copy ` `Sample volume = 10 µL` ` 

Do not just add 8 µL to the old 198 + 2 tube, because that makes 208 µL total and breaks the assay math.

Record:Copy ` `Genomic DNA concentration:
Remaining DNA volume:
Estimated total DNA:` ` 

Calculate:Copy ` `total DNA ng = Qubit concentration ng/µL × remaining volume µL` ` 

# Pause point

This is the best place to pause. For a same-day break:Copy ` `Store extracted DNA at 4°C / fridge.` ` 

Before storing:
- Make sure the DNA is in a clearly labeled DNA LoBind tube.
- Quick spin.
- Do not vortex.
- Close tube tightly.
- Put it in the fridge.

Resume at Step 10.

# 9. Prepare DNA input for repair/end-prep

Goal: prepare 47 µL DNA input.

Ideal target:Copy ` `1,000 ng DNA in 47 µL` ` 

Calculate:Copy ` `DNA volume needed = 1000 ng / Qubit concentration ng/µL` ` 

Then:Copy ` `water volume = 47 µL - DNA volume` ` 

If the DNA is too dilute and 1,000 ng cannot fit into 47 µL, use the maximum possible volume:Copy ` `47 µL extracted DNA
0 µL water` ` 

For the first low-input run:Copy ` `0.296 ng/µL × 47 µL = ~13.9 ng DNA` ` 

That was far below the recommended input, but useful as an end-to-end practice run.

# 10. Repair / end-prep

Goal: repair DNA and prepare the ends for adapter ligation.

Use the actual v2 reagents:Copy ` `FFPE DNA Repair Buffer v2
FFPE DNA Repair Mix
N-Prep Enzyme Mix / Ultra II End Prep Enzyme Mix` ` 

Do not use Salt-T4 DNA Ligase in this step. It is used later.

If not using DCS, replace the optional 1 µL DCS with 1 µL nuclease-free water.

## Reaction

Copy ` `47 µL DNA
1 µL nuclease-free water
7 µL FFPE DNA Repair Buffer v2
2 µL FFPE DNA Repair Mix
3 µL N-Prep Enzyme Mix

Total = 60 µL` ` 

## Steps

- Add 47 µL DNA to a 0.2 mL thin-walled PCR tube labeled  `End-prep` .
- Add 1 µL nuclease-free water.
- Add 7 µL FFPE DNA Repair Buffer v2.
- Pipette mix 10–20 times.
- Add 2 µL FFPE DNA Repair Mix.
- Pipette mix 10–20 times.
- Add 3 µL N-Prep Enzyme Mix.
- Pipette mix 10–20 times.
- Quick spin.

Incubate:Copy ` `20°C for 5 minutes
65°C for 5 minutes
Then place on ice` ` 

# 11. AMPure cleanup after repair/end-prep

Goal: clean the repaired/end-prepped DNA.

Input:Copy ` `60 µL repair/end-prep reaction` ` 
- Resuspend AMPure XP beads until uniformly brown.
- Add 60 µL AMPure XP beads to the 60 µL reaction.
- Mix gently by pipetting 10 times.
- Incubate 5 minutes at room temperature.
- Put tube on magnet.
- Wait until solution clears.
- Remove and discard supernatant without touching beads.

## Wash 1

- Keep tube on magnet.
- Add 200 µL fresh 80% ethanol.
- Remove ethanol.

## Wash 2

- Add another 200 µL fresh 80% ethanol.
- Remove ethanol.

## Dry

- Remove residual ethanol with P10/P20.
- Air dry briefly, about 30 seconds.
- Do not overdry.
- Do not let beads crack.

## Elute

- Remove tube from magnet.
- Add 61 µL nuclease-free water.
- Resuspend beads gently.
- Incubate 5–10 minutes at room temperature.
- Put tube back on magnet.
- Wait until clear.
- Transfer 60 µL clear eluate to a clean DNA LoBind tube labeled  `Ligation` .

Do not transfer beads.

# 12. Adapter ligation

Goal: attach ONT sequencing adapters.

Use the actual reagents:Copy ` `LNB
LA
Salt-T4 DNA Ligase` ` 

## Reaction

Copy ` `60 µL repaired/end-prepped DNA
25 µL LNB
10 µL Salt-T4 DNA Ligase
5 µL LA

Total = 100 µL` ` 

## Steps

- Use a clean DNA LoBind tube labeled  `Ligation` .
- Mix LNB slowly by pipetting before adding. It is viscous.
- Add 60 µL repaired/end-prepped DNA.
- Add 25 µL LNB.
- Add 10 µL Salt-T4 DNA Ligase.
- Add 5 µL LA.
- Mix gently by pipetting 10–15 times.
- Do not vortex.
- Quick spin.
- Incubate 10 minutes at room temperature.

Before incubation, say/check:Copy ` `DNA, LNB, Salt-T4 DNA Ligase, LA.` ` 

Failure points:Copy ` `Forgetting LA = no sequenceable library.
Forgetting Salt-T4 DNA Ligase = adapter ligation fails.
Poorly mixed LNB = bad ligation chemistry.
Vortexing = unnecessary DNA shearing.` ` 

# 13. Adapter-ligated library cleanup

Goal: remove free adapters, ligase, salts, and small fragments while keeping adapter-ligated DNA.

Important:Copy ` `This cleanup uses LFB, not ethanol.` ` 

Input:Copy ` `100 µL ligation reaction` ` 
- Resuspend AMPure XP beads fully.
- Add 40 µL AMPure XP beads to the 100 µL ligation reaction.
- Mix gently by pipetting 10 times.
- Incubate 5 minutes at room temperature.
- Place tube on magnet.
- Wait until solution clears.
- Keep tube on magnet.
- Remove and discard supernatant carefully.
- Do not touch bead pellet.

## Wash 1

- Add 250 µL LFB to beads.
- Remove tube from magnet.
- Gently resuspend beads by flicking or slow pipetting.
- Put tube back on magnet.
- Wait until clear.
- Remove and discard LFB.

## Wash 2

- Add another 250 µL LFB.
- Remove tube from magnet.
- Gently resuspend beads.
- Put tube back on magnet.
- Wait until clear.
- Remove and discard LFB.
- Remove residual LFB with P10/P20.
- Do not overdry.

## Elute

- Add 25 µL EB.
- Remove tube from magnet.
- Resuspend gently.
- Incubate 10 minutes at room temperature.
- Put tube back on magnet.
- Wait until eluate is clear.
- Transfer clear eluate to a clean DNA LoBind tube labeled  `Final library` .

This is the final sequencing library.

Practical rule:Copy ` `Liquid moves. Beads stay.` ` 

Do not transfer beads into the final library.

# 14. Check quantity of DNA one more time

Goal: measure final adapted library concentration.

Because low-input runs may produce very little final library, this may read low or fail.

Use:Copy ` `199 µL 1X dsDNA HS working solution
1 µL final library` ` 

On Qubit:Copy ` `Sample volume = 1 µL` ` 

Record:Copy ` `Final library concentration:
Final library volume:
Estimated mass loaded:` ` 

Calculate:Copy ` `mass loaded ng = final library concentration ng/µL × 12 µL` ` 

If the final library is too low, do not repeatedly burn more library on Qubit. For a practice run, proceed with 12 µL library in the loading mix.

# 15. Flow cell check with MinKNOW

Goal: verify the flow cell before loading the library.
- Take flow cell out of fridge.
- Let it sit at room temperature for 20 minutes.
- Keep it flat.
- Do not shake.
- Plug in MinION.
- Open MinKNOW.
- Insert flow cell.
- Run flow cell check.
- Record active pores.

Decision table:Copy ` `>1200 pores = great
800–1200 pores = usable
500–800 pores = marginal/practice
<500 pores = bad, but still possible for mechanical practice
<200 pores = essentially not worth it except loading practice` ` 

Record:Copy ` `Flow cell ID:
Starting active pores:
Flow cell age:
Previously used? yes/no:
Washed? yes/no:` ` 

# 16. Understand the final tubes and ports

At the end, there are three tubes:Copy ` `Tube 1: Final library
- This is the DNA library made after adapter cleanup.

Tube 2: Priming mix
- This prepares the flow cell.

Tube 3: Loading mix
- This contains final library + sequencing buffer + library beads.` ` 

There are two flow-cell ports:Copy ` `Port 1: Priming port
- This is under the sliding cover.
- Priming mix goes here.

Port 2: SpotON sample port
- This is the small sample well.
- Loading mix goes here drop by drop.` ` 

Important:Copy ` `Final library does not go directly onto the flow cell by itself.
Final library first goes into the loading mix tube.` ` 

# 17. Make priming mix for ONT Flow Cell

If BSA is available:Copy ` `1170 µL FCF
5 µL BSA
30 µL FCT

Total = 1205 µL` ` 

If BSA is not available and this is a practice run:Copy ` `1170 µL FCF
30 µL FCT

Total = 1200 µL` ` 

Do not substitute SFB, DCS, LIS, or LNB for BSA.

Mix gently. Avoid bubbles.

This is Tube 2:  `Priming mix` .

# 18. First prime

Do this only after flow cell check is complete. Make sure to watch this video: [https://www.youtube.com/watch?v=IknVaEnuDz0](https://www.youtube.com/watch?v=IknVaEnuDz0). It is how you load the actual flow cell!
- Keep flow cell plugged in and flat.
- Open the sliding cover to expose the priming port.
- Check for an air bubble near the port.

Draw back only 20–30 µL:Copy ` `Set P1000 to 200 µL.
Put tip into priming port.
Slowly dial to 220–230 µL.
Stop as soon as liquid enters the tip.
Do not pull more.` ` 

Then load into the priming port:Copy ` `800 µL priming mix` ` 

Go slowly. Avoid bubbles.

Wait:Copy ` `5 minutes` ` 

# 19. Make loading mix during the 5-minute wait

Tube 3:  `Loading mix` 

Use:Copy ` `37.5 µL SB
25.5 µL LIB
12 µL final library

Total = 75 µL` ` 

Important:Copy ` `LIB = Library Beads from the ONT kit.
LIB is not AMPure XP beads.
LIB settles fast.
Mix LIB immediately before pipetting.` ` 

Steps:
- Mix LIB immediately before pipetting.
- Add 37.5 µL SB to a clean tube.
- Add 25.5 µL LIB.
- Add 12 µL final library.
- Mix gently by pipetting.
- Do not vortex.

# 20. Second prime

After the 5-minute wait, load into the priming port:Copy ` `200 µL priming mix` ` 

Avoid bubbles.

# 21. Load library onto SpotON port

- Gently mix Tube 3 loading mix immediately before loading.
- Open the SpotON sample port.
- Load the full 75 µL loading mix into the SpotON port.
- Add it drop by drop.
- Let each drop disappear before adding the next.
- Do not force it.
- Do not jab the port.
- Avoid bubbles.

Then:Copy ` `Close SpotON cover.
Close priming port.
Add light shield.
Close MinION lid.
Start run in MinKNOW.` ` 

Final mental model:Copy ` `Priming mix → sliding priming port
Loading mix → SpotON sample port
Final library → only goes into loading mix first` ` 

# 22. Sequence DNA with MinKNOW 

Recommended basic settings:Copy ` `Flow cell type: FLO-MIN114
Kit: SQK-LSK114
Basecalling: ON
Model: High-accuracy / HAC
Barcoding: OFF
Alignment: OFF
Adaptive sampling: OFF
Raw reads / POD5: ON
Filtering: OFF for low-input practice runs` ` 

Then:Copy ` `Save configuration
Start` ` 

For a low-input practice run, keep raw POD5 on so the data can be analyzed later even if live output is poor.

# 23. Basecall after run if needed

- Find POD5 output directory.
- Install Dorado.
- Run basecalling:Copy ` `dorado basecaller sup pod5_directory/ > calls.bam` ` 
- Convert BAM to FASTQ if needed:Copy ` `samtools fastq calls.bam > reads.fastq` ` 
- For faster first pass, use HAC instead of SUP:Copy ` `dorado basecaller hac pod5_directory/ > calls.bam` ` 

# 24. Align reads to human reference

- Download GRCh38 FASTA.
- Index reference:Copy ` `minimap2-d GRCh38.mmi GRCh38.fa` ` 
- Align reads:Copy ` `minimap2-ax map-ont GRCh38.mmi reads.fastq | samtoolssort-o aligned.bam` ` 
- Index BAM:Copy ` `samtools index aligned.bam` ` 
- Check alignment summary:Copy ` `samtools flagstat aligned.bam > flagstat.txt` ` 
- Check coverage:Copy ` `mosdepth sample_cov aligned.bam` ` 

# 25. Variant calling

- Install Clair3.
- Use ONT model.
- Run Clair3 with GRCh38 reference, sorted BAM, and output directory.
- Output should include VCF.
- Do not overinterpret low-coverage variants.
- For a first MinION run, treat this as technical validation, not medical-grade interpretation.

# 26. Annotation

- Install VEP.
- Annotate VCF against GRCh38.
- Add ClinVar.
- Add gnomAD.
- Add PharmGKB later.
- Store final table with columns:
- chromosome
- position
- ref
- alt
- gene
- consequence
- ClinVar significance
- gnomAD frequency
- genotype
- read depth
- variant quality

# References

[Seth Howes protocol](https://iwantosequencemygenomeathome.com/#costs) (X profile)

[DNA Quantification with Qubit](https://www.youtube.com/watch?v=YXSaJQsIpFI)

[Molecular Biology of the Cell](https://www.amazon.com/Molecular-Biology-Sixth-Bruce-Alberts/dp/0815345240)

[Quantifying Life](https://www.amazon.com/Quantifying-Life-Symbiosis-Computation-Mathematics/dp/022637176X) (super underrated)

[Integrated Drug Discovery Technologies](https://www.amazon.com/Integrated-Drug-Discovery-Technologies-Houng-Yau-ebook/dp/B00SC81HWC/ref=sr_1_1?crid=1WQOFZZS77LE6&dib=eyJ2IjoiMSJ9.-1b9qnZYOTdD8F9n4EqjyU2xLAWmJwd14zom3XbYxoKZcdJ8J0qpIsZD_jz-DtzgbjsZufP2mK-DYvWTYH8OYzAqsoGHgCkkJ697picfAtb_tCD2aYhtMHof_cIcnZvI8p_cvEyzmsKfmvoc1nB2G925qblja1OGOO6n_DNn-A7ACBHw8ci2zY-iB4u0fTNhZlR5jQHFDz0grGrLzpEYMTpOAJKPNAGv6PWpPBJK6JY.ngjMGi_K9Q-HCSpN4u8nIWhq5LncwL2MB4JBvJYlObY&dib_tag=se&keywords=integrated+drug+discovery+technologies&qid=1781302527&sprefix=integrated+drug+d%2Caps%2C230&sr=8-1)

[Darkome](https://www.amazon.com/Darkome-Hannu-Rajaniemi-ebook/dp/B0C9GNJH1C) 

[Upgrade](https://www.amazon.com/Upgrade-Novel-Blake-Crouch/dp/0593157532)

[Sid’s cancer data](https://osteosarc.com/)

[DNA Whole Genome Sequencing - astrology for sigmas](https://vad1ms.substack.com/p/dna-whole-genome-sequencing-astrology?r=2xxyvi&utm_campaign=post&utm_medium=web&triedRedirect=true)

[DNA sequencing at home with the flongle](https://blog.booleanbiotech.com/sequencing-at-home-with-flongle)
