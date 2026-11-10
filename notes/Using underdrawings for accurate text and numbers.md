---
title: "Using \"underdrawings\" for accurate text and numbers"
url: https://samcollins.blog/underdrawings/
clipped: 2026-06-17 01:07:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - AI image generation
  - underdrawings technique
  - multimodal AI workflows
  - deterministic layout tools
related:
  - "[[AI Image Generation]]"
  - "[[Underdrawings Technique]]"
  - "[[Multimodal AI Workflows]]"
  - "[[Deterministic Layout Tools]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The author explains the "underdrawing" technique, which combines deterministic layout tools (like SVGs) with generative AI image-to-image models to produce accurate text and numbers in images.
> 
> **Key points:**
> - State-of-the-art image generators (like Gemini 3 Pro and ChatGPT Images 2) struggle with precise text rendering and numbering tasks natively.
> - The underdrawing method uses SVG/HTML to create a precise outline with text and numbers positioned deterministically (Layer 1).
> - This outline is then passed into a multimodal AI model as an image-to-image input alongside a style prompt to render the final artistic image (Layer 2).
> - While not always 100% perfect, this multi-step approach significantly improves text rendering fidelity.
> 
> **Concept links:** [[AI Image Generation]], [[Underdrawings Technique]], [[Multimodal AI Workflows]], [[Deterministic Layout Tools]]
> 
> **Suggested connections:**
> - [[AI Image Generation]] — tools and techniques for generating graphics from prompts.
> - [[Underdrawings Technique]] — methods using structural frameworks as visual guidance in generative models.
> - [[Multimodal AI Workflows]] — chaining programmatic layout generators with machine learning models.
<!-- ai-summary:end -->

# [Using "underdrawings" for accurate text and numbers](https://samcollins.blog/underdrawings/)

## Digest Summary
The post describes a two‑stage “underdrawing” technique for producing AI‑generated images that contain precise text or numbers. First, a deterministic tool (e.g., SVG, HTML, Python, Mermaid) creates a layout containing the exact characters in the correct positions and orientations; this underdrawing is exported as a bitmap. Second, a multimodal image model such as Gemini 3.0 Pro receives the underdrawing together with a descriptive prompt and generates the final visual, effectively “painting over” the accurate text layer. The author demonstrates the method with a 50‑stone spiral board, showing that Gemini 3 Pro and ChatGPT‑Images‑2 fail to render correct numbering when used alone, while Gemini 3.0 Pro with the underdrawing produces correct numbers, ordering, and shape. The workflow can be scripted (e.g., with Claude Code or Codex) and is not guaranteed to succeed on every run, but it substantially improves numeric and textual fidelity in generated images.

## Discussion Summary
The comments express a generally positive view of recent advances, noting that using a structured img2img pipeline and a simple technique for embedding reliable text and numbers in generated images improves results. Participants highlight a gap in systematic knowledge about which tasks suit LLMs or diffusion models, calling for clearer taxonomies and studies. There is surprise that image models lack built‑in support for these tricks, alongside acknowledgment that in‑painting and guided sketches remain common practices for higher‑quality outputs. Overall, the discussion centers on practical workflow refinements and a desire for deeper understanding of model capabilities.

---

## Full Article

Using âunderdrawingsâ for accurate text and numbers
=======================================================

I discovered a technique for generating reliable text and numbers in AI generated images.

For example, the following image is considered impossible with state of the art image models. But I made this with Gemini 3.0 Pro (plus one extra step Iâm going to explain below).

![](https://samcollins.blog/_astro/grid-candy-transformed-v8.Bv9YI1JR_Z1z1E8B.webp)

The Underdrawing Method
-----------------------

Iâm totally naming it like itâs a thing but it does seem to be a thing. Hereâs a simple a/b test showing the results without and with this method.

```
Make an image of a game board with 50 stepping stones arranged in a spiral, winding counter-clockwise inward from start at the outside (1) to finish at the centre (50). Each stone is clearly numbered consecutively from 1 to 50. Style: claymation diorama, studio-lit, candy-bright, soft bokeh background.
```

### â Gemini 3 Pro (without underdrawing)

As expected. Impressive at first glance but falls apart once you start reading.

![](https://samcollins.blog/_astro/gemini-pro-fail.Dno56JYy_1iYsf7.webp)

### â ChatGPT Images 2 (without underdrawing)

I was so impressed with ChatGPT-Images-2 release I **expected it to get this**. Very surprising to see it fail similar to Gemini.

![](https://samcollins.blog/_astro/chatgpt-images-2-stones.CGYFRAUH_Tsjnp.webp)

### â Gemini 3.0 Pro **(with the underdrawing method)**

Bingo. Correct numbers, correct number and sequencing of buttons, correct spiral shape

![](https://samcollins.blog/_astro/gemini-pro-transformed-3d-concise-plus.CgYT-7hb_Z1MIux1.webp)

So how does it work?
--------------------

I came up with this pattern while trying to figure out how to generate an image of a 100-step adventure board for my kid.

### Use deterministic and generative machines for what theyâre good at

1. **SVG/HTML** makes dry visuals but with excellent math and precision
2. **Image Gen models** make stunning visuals but with unreliable math and text

**âGive it an outline. Ask it to paint on topâ**

1. **Layer 1: The âunderdrawingâ (deterministic)**: Layout the numbers and text in the correct positions and orientations in whatever language/format you prefer (svg, python, mermaid) â you just need to export an image of it with the pixels of the numbers/text.
2. **Layer 2: The âpaintingâ (generative):** Using a multi-modal image model like Gemini 3.0 Pro (you need image+text input â image output), pass your underdrawing image along with your text prompt.

### Example

#### Step 1 of 2: generate the numbers/text outline with SVG

```
Make an SVG of 50 stepping stones arranged in a spiral, winding counter-clockwise inward from start at the outside (1) to finish at the centre (50), each stone numbered consecutively from 1 to 50. Each stone is a different shape: circle, square, triangle, hexagon.
```

![](https://samcollins.blog/_astro/spiral-candy.CbV86oWQ_Z1tticf.webp)

#### Step 2 of 2: Use the underdrawing to do image-to-image generation

```
Transform this image into a photographed claymation diorama of assorted artisan chocolates and candies, arranged in a spiral path winding counter-clockwise inward from start (1) at the outside to finish (50) at the centre, viewed from a low-angle tilted perspective.
```

![](https://samcollins.blog/_astro/gemini-pro-transformed-candy.CVv4X6Xg_1Xyvip.webp)

Thatâs it
-----------

It isnât hard. By now claude code or codex can do every step of that for you.

Note: itâs good, but it wonât be perfect every time. Thank you for the reality check, 71.

![](https://samcollins.blog/_astro/grid-candy-transformed-v5.Vbd57dCU_Z8AS9e.webp)