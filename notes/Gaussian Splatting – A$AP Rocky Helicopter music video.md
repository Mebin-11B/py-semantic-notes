---
title: "Gaussian Splatting – A$AP Rocky \"Helicopter\" music video"
url: https://radiancefields.com/a-ap-rocky-releases-helicopter-music-video-featuring-gaussian-splatting
clipped: 2026-06-17 01:56:32
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - gaussian splatting
  - volumetric capture
  - music video vfx
  - radiance fields
  - houdini simulations
  - octanerender
related:
  - "[[Gaussian Splatting]]"
  - "[[Volumetric Capture]]"
  - "[[Radiance Fields]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An industry report on the creation of A$AP Rocky's "Helicopter" music video, highlighting the massive use of 56-camera volumetric capture and dynamic Gaussian splatting.
>
> **Key points:**
> - The music video utilizes volumetric capture for human performances to allow post-production cameras to move freely in three-dimensional space.
> - A 56-camera RGB-D array captured over 10 TB of raw spatial data, resulting in 30 minutes of splatted footage (1 TB of PLY point sequence files).
> - The pipeline processed the splats inside Houdini and rendered them via OctaneRender, enabling realistic relighting and shadowing of the virtual actors.
> - Unlike AI-generated animations, every frame represents real physical stunt capture data (wire work, props) preserved spatially and composed digitally.
>
> **Concept links:** [[Gaussian Splatting]], [[Volumetric Capture]], [[Music Video VFX]], [[Radiance Fields]], [[Houdini Simulations]], [[OctaneRender]]
>
> **Suggested connections:**
> - [[Gaussian Splatting]] — The primary technique representing 3D spatial points as rasterized ellipsoids.
> - [[Volumetric Capture]] — The physical recording infrastructure required to capture 360-degree performance data.
> - [[Radiance Fields]] — The category of spatial representation methods (e.g., NeRFs, splats) adopted in artistic video editing.
<!-- ai-summary:end -->


# [Gaussian Splatting – A$AP Rocky "Helicopter" music video](https://radiancefields.com/a-ap-rocky-releases-helicopter-music-video-featuring-gaussian-splatting)

## Digest Summary
A$AP Rocky’s “Helicopter” music video was created using full‑body volumetric capture and dynamic Gaussian splatting. Director Dan Strait selected the technique to give unrestricted post‑production freedom that conventional filming could not provide. Evercoast recorded all performers, including Rocky, with a 56‑camera RGB‑D array in Los Angeles (August), capturing over 10 TB of raw data and producing roughly 30 minutes of splatted footage (≈1 TB of PLY sequences). The raw captures were processed in Houdini using CG Nomads GSOPs and rendered with OTOY’s OctaneRender, which allowed relighting and shadowing of the splats. Blender was used for layout and preview, while WildCapture’s tools supplied primitive pose estimations for motion transfer and simulation of rigid/soft bodies. The workflow enabled live on‑set previews, rapid creative decisions, and extensive recomposition of physically performed stunts (wire rigs, props) without additional filming. The final aesthetic appears synthetic, but all motion is captured from real performances rather than AI‑generated content.

## Discussion Summary
The comments express strong interest in the music video’s use of Gaussian splatting, highlighting its technical novelty and artistic impact while noting the complexity of the underlying workflow. Readers seek clearer explanations of the method, compare it to traditional VFX and AI‑generated visuals, and discuss its potential for faster, more flexible compositing. Opinions diverge on visual quality, with some finding the texture off or causing motion sickness, and others praising the surreal aesthetic; cost and practicality are also debated. Overall sentiment is curious and cautiously optimistic.

---

## Full Article

Believe it or not, A$AP Rocky is a huge fan of radiance fields.

Yesterday, when A$AP Rocky released the music video for *Helicopter*, many viewers focused on the chaos, the motion, and the unmistakable early MTV energy of the piece. Whatâs easier to miss, unless you know what youâre looking at, is that nearly every human performance in the video was captured volumetrically and rendered as dynamic splats.

I spoke with [Evercoast](https://evercoast.com/), the team responsible for capturing the performances, as well as Chris Rutledge, the projectâs CG Supervisor at [Grin Machine](https://vimeo.com/grinmachine), and Wilfred Driscoll of WildCapture and [FitsÅ«.ai](https://fitsu.ai/), to understand how *Helicopter* came together and why this project represents one of the most ambitious real world deployments of dynamic gaussian splatting in a major music release to date. Wild Capture was responsible for initiating the project and bringing together the team.

The decision to shoot *Helicopter* volumetrically wasnât driven by technology for technologyâs sake. According to the team, the director Dan Strait approached the project in July with a clear creative goal to capture human performance in a way that would allow radical freedom in post-production. This would have been either impractical or prohibitively expensive using conventional filming and VFX pipelines.

Chris told me heâd been tracking volumetric performance capture for years, fascinated by emerging techniques that could enable visuals that simply werenât possible before. Two years ago, he began pitching the idea to directors in his circle, including Dan, as a âsomedayâ workflow. When Dan came back this summer and said he wanted to use volumetric capture for the entire video, the proliferation of gaussian splatting enabled them to take it on.

![](https://i.ytimg.com/vi_webp/g1-46Nu3HxQ/sddefault.webp)VIDEO

The aesthetic leans heavily into kinetic motion. Dancers colliding, bodies suspended in midair, chaotic fight scenes, and performers interacting with props that later dissolve into something else entirely. Every punch, slam, pull-up, and fall you see was physically performed and captured in 3D.

Almost every human figure in the video, including Rocky himself, was recorded volumetrically using Evercoastâs system. Itâs all real performance, preserved spatially.

This is not the first time that A$AP Rocky has featured a radiance field in one of his music videos. The 2023 music video for *Shittinâ Me* featured several NeRFs and even the GUI for Instant-NGP, which you can spot throughout the piece.

![](https://i.ytimg.com/vi_webp/Oh8b_P7_AuA/sddefault.webp)VIDEO

The primary shoot for *Helicopter* took place in August in Los Angeles. Wild Captured hired Evercoast and they deployed a 56 camera RGB-D array, synchronized across two Dell workstations. Performers were suspended from wires, hanging upside down, doing pull-ups on ceiling-mounted bars, swinging props, and performing stunts, all inside the capture volume.

Scenes that appear surreal in the final video were, in reality, grounded in very physical setups, such as wooden planks standing in for helicopter blades, real wire rigs, and real props. The volumetric data allowed those elements to be removed, recomposed, or entirely recontextualized later without losing the authenticity of the human motion.

Over the course of the shoot, Evercoast recorded more than 10 terabytes of raw data, ultimately rendering roughly 30 minutes of final splatted footage, exported as PLY sequences totaling around one terabyte.

That data was then brought into Houdini, where the post production team used CG Nomads GSOPs for manipulation and sequencing, and OTOYâs OctaneRender for final rendering. Thanks to this combination, the production team was also able to relight the splats.

One of the more powerful aspects of the workflow was Evercoastâs ability to preview volumetric captures at multiple stages. The director could see live spatial feedback on set, generate quick mesh based previews seconds after a take, and later review fully rendered splats through Evercoastâs web player before downloading massive PLY sequences for Houdini.

In practice, this meant creative decisions could be made rapidly and cheaply, without committing to heavy downstream processing until the team knew exactly what they wanted. Itâs a workflow that more closely resembles simulation than traditional filming.

Chris also discovered that Octaneâs Houdini integration had matured, and that Octaneâs early splat support was far enough along to enable relighting. According to the team, the ability to relight splats, introduce shadowing, and achieve a more dimensional â3D videoâ look was a major reason the final aesthetic lands the way it does.

The team also used Blender heavily for layout and previs, converting splat sequences into lightweight proxy caches for scene planning. Wilfred described how WildCaptureâs internal tooling was used selectively to introduce temporal consistency. In his words, the team derived primitive pose estimation skeletons that could be used to transfer motion, support collision setups, and allow Houdiniâs simulation toolset to handle rigid body, soft body, and more physically grounded interactions.

One recurring reaction to the video has been confusion. Viewers assume the imagery is AI-generated. According to Evercoast, that couldnât be further from the truth. Every stunt, every swing, every fall was physically performed and captured in real space. What makes it feel synthetic is the freedom volumetric capture affords. You arenât limited by the cameraâs composition. You have free rein to explore, reposition cameras after the fact, break spatial continuity, and recombine performances in ways that 2D simply canât.

In other words, radiance field technology isnât replacing reality. Itâs preserving everything.