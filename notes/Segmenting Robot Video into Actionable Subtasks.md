---
title: "Segmenting Robot Video into Actionable Subtasks"
url: https://macrodata.co/blog/annotating-robot-video-subtasks
clipped: 2026-08-31 12:17:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Segmenting Robot Video into Actionable Subtasks](https://macrodata.co/blog/annotating-robot-video-subtasks)

## Digest Summary
The post presents WGO‑Bench, a new benchmark for robotic subtask annotation comprising 100 egocentric and robot‑video episodes with 743 human‑annotated segments across 62 high‑level instructions. Over 60 experiments identified the most effective pipeline: subtask boundary detection (0.306 F1), subtask labeling (61.0 % accuracy), and end‑to‑end annotation (0.168 F1). Gemini models, especially Gemini 3.5 Flash, outperform the best non‑Gemini model (GPT‑5.5) by 24.5 %. The optimal method uses visual “contact sheets” that pack 20 frames with embedded timestamps, achieving 0.263 F1 for segmentation while reducing inference cost to $2.64 per video hour (≈19× cheaper than human labeling). Direct frame‑by‑frame prompting reaches only 0.193 F1 and is far more expensive. Experiments show visual timestamps on contact sheets markedly improve boundary detection, whereas higher resolution, denser sampling, or larger sheets do not. The complete open‑source pipeline is available in Refiner for users to apply to their own robot videos.

---

## Full Article

[<- More blog posts](https://macrodata.co/blog)

## TL;DR

- We introduce [WGO‑Bench](https://huggingface.co/datasets/macrodata/WGO-Bench), a new benchmark for testing robotics subtask annotation performance across 100 egocentric and robot-video episodes with 743 annotated segments spanning 62 unique high-level task instructions.

- We ran over 60 experiments to find the best subtask annotation pipeline: the best subtask segmentation method reaches 0.306 F1, subtask labeling reaches 61.0% accuracy, and the best end-to-end pipeline reaches 0.168 F1.

- Gemini models are undisputed best for this task, with the best model (Gemini 3.5 Flash) outperforming the best non-Gemini model (GPT-5.5) by 24.5%.

- Our best end-to-end method uses contact sheets to keep inference cheap, costing $2.64 per hour of video (batch pricing), or roughly 19x less than human annotation.

- The full pipeline is open source and implemented in [Refiner](https://github.com/macrodata-labs/refiner); see the [ready-to-use subtask annotation example](https://macrodata.co/docs/examples/annotations/subtask-annotations) to run it on your own videos.

- Since completing this work, we have continued developing a proprietary subtask-annotation pipeline that delivers better performance. If you need stronger results on your robot-video dataset, [contact us to evaluate it on your data](https://macrodata.co/contact?subject=Robot%20video%20subtask%20annotation).

## Why annotate subtasks?

Imagine walking into a kitchen you have never seen before with an instruction: "Make me goulash." If you have never cooked it, you will need to learn it. To do so, you need more than the final instruction; you need the steps, the objects, and where to find them: open the left-most shelf, take out the cutting board, place it on the counter, pick up an onion, peel it, put it on the board, chop it, and so on.

Robot learning has a similar problem. To teach robots new long-horizon tasks, we need more than weak high-level instructions. For a robotics demonstration video, the useful signal is which subtask is happening at each moment, and where one subtask ends and the next begins.

Subtasks are becoming a central learning signal in recent robotics work. [Zawalski et al. (2025)](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-zawalski2025roboticcontrolembodiedchainofthought) uses subtasks together with chain-of-thought reasoning between plans and actions. The recent π series (⁠[Physical Intelligence et al., 2025](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-intelligence2025pi05visionlanguageactionmodelopenworld)⁠) and RT‑H (⁠[Belkhale et al., 2024](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-belkhale2024rthactionhierarchiesusing)⁠) use semantic subtask prediction alongside low-level action learning, with both showing substantial gains from this extra supervision. Subtasks are also useful beyond direct policy training: SARM (⁠[Kim et al., 2025](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-kim2025subtaskawarevisualrewardlearning)⁠) uses them for reward modeling.In π0.5, the VLA first predicts a semantic subtask from the observation and overall prompt, then predicts a low-level action chunk conditioned on that subtask through the flow-matching action expert.

As robotics data collection continues to scale, we need annotation pipelines that can keep up. Paying human annotators to watch every hour of video quickly stops being feasible. Despite the promising results, there is little public material on how to mine subtask annotations at scale. The closest public writeup we found is Scale's [dense video captioning post](https://labs.scale.com/blog/path-to-large-scale-dense-video-captioning) (⁠[Choghari et al., 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-scale2026densecaptioning)⁠), but it focuses on hand/egocentric manipulation videos only and starts from already separated clips. For robotics, that skips two harder problems: taking a raw episode and deciding where one subtask ends and the next begins, and testing whether the same methods transfer from egocentric video to robot-camera settings.
To fill this gap, we created a scalable pipeline to have models annotate subtasks without any human intervention, costing $2.64 per hour of video (batch pricing), making it roughly 19x cheaper than humans. This post shares the lessons we learned from this effort, including the best end-to-end method we found for mining subtasks from both egocentric and robot videos, as well as our new benchmark for robotics subtask annotation: [WGO‑Bench (What's Going On Bench)](https://huggingface.co/datasets/macrodata/WGO-Bench).

The full pipeline is open-sourced in [Refiner](https://github.com/macrodata-labs/refiner), our robotics data processing framework. To run it on your own data, see the [ready-to-use example code](https://macrodata.co/docs/examples/annotations/subtask-annotations).

## Measuring Progress: WGO‑Bench

To iterate and choose the best approach, we needed a benchmark. Instead of directly training and evaluating robot policies on every candidate method, which would be very slow and expensive, we built a new benchmark, [WGO‑Bench](https://huggingface.co/datasets/macrodata/WGO-Bench), to directly measure how close VLMs can get to human annotator performance, which are still employed for most of the current industrial efforts.

### Benchmark composition

We collected and manually annotated 100 episodes spanning head-camera recordings from Galaxea World (⁠[Jiang et al., 2025](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-jiang2025galaxeaopenworlddatasetg0)⁠), third-person camera views of station-arm manipulation from DROID (⁠[Khazatsky et al., 2025](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-khazatsky2025droidlargescaleinthewildrobot)⁠), and egocentric videos from HomER (⁠[Toloka, 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-homer_v2_2026)⁠) to create WGO‑Bench, a diverse subtask annotation benchmark. In total, it contains 743 annotated segments across 62 unique high-level task instructions.SectionTypeViewpointSamplesUnique tasksTotal durationAvg ep lenResolutionSegmentsHomERHumanEgocentric251739.2 min94.0sMixed, mostly 1920x1080 / 848x480470DROIDRobotExternal robot camera502624.9 min29.9s320x180150GalaxeaRobotRobot head camera25197.4 min17.7s1280x720123TotalMixedMixed1006271.5 min42.9sMixed743WGO-Bench sample breakdown

### Manually annotating subtasks

We manually annotated WGO‑Bench demonstrations following a strict annotation protocol: segments are atomic manipulation events, boundaries follow object-state changes, and labels must be self-contained enough to train policies without relying on previous actions.

Atomic event

#### One subtask should describe one completed manipulation event.

1/3clip002.805.708.1WrongPick, move, placeCorrectPickPlacenow

Subtasks should be atomic: one completed pick, one completed place, not a combined pick-move-place motion.Annotation policy examples from galaxea_069Annotation protocol details+

The episodes were segmented into atomic manipulation events rather than motion fragments. A subtask ends when the event is complete, not when the robot hand returns to a neutral pose. Unless there is a clear pause, the next subtask starts immediately after the previous one.

Boundaries are placed at object-manipulation changes: when an object becomes held, is released, reaches a new location, or a door or lid changes state. Camera motion, hesitation, and tiny hand adjustments are not separate subtasks.

Labels are self-contained. They do not refer to previous human or robot actions, and they describe the manipulated object and target location as precisely as possible: not "put the cup on the table", but "put the cup on the table next to the bowl." This prevents ambiguity because most robotic policies do not take past frames or actions as input.

#### Annotation interface

For the annotations themselves, we first tried existing tools like CVAT and Labelbox, but found them too inflexible. Instead, we built a simple API for manipulating datasets and calling generative models on our platform, then connected it to Codex. Annotators can point it at a dataset, describe what needs to be labeled, and generate a custom interface on demand, with model calls wired in for pre-segmentation or pre-labeling. All edits go through the same data layer, allowing parallel work, while keeping the data consistent. This interface is currently in closed beta; if you would like access, [request it here](https://macrodata.co/contact?subject=Annotations%20beta%20access&message=I%20would%20like%20access%20to%20Macrodata%20Annotations,%20my%20use-case%20is:).
WGO-Bench annotation interface in Macrodata Annotations.

#### Lessons from the annotation trenches

Even with a clear annotation protocol and a purpose-built UI, subtask annotation is difficult and slow for humans. The most obvious issue is time: without prefilled model suggestions, one minute of video easily takes more than ten minutes to annotate carefully.

Egocentric videos are usually the most time-consuming. Hands move quickly, subtasks are often much shorter than in robot videos, and both hands can act at once. For example, picking up a knife with the left hand while moving a tomato with the right. Even deciding where one action ends and the next begins can become ambiguous, such as whether sliding a container across a table should be split into pick -> slide or treated as one slide action.

The labels themselves are also hard to write precisely. Locations can be difficult to describe when there is no clear object to anchor them to, and manipulated objects are not always easy to recognize, especially in lower-resolution video. Fast egocentric motion makes this worse because a pick can happen in only a few frames, leaving little visual evidence for where the pick ends and the next action begins.

Hard localization

#### Locations are difficult to describe when there is no stable anchor.

1/5

Example

How would you describe which glass is being placed and where it's being placed?

Good labels need enough spatial detail to stand alone, even when the scene does not provide clear names for every location.Annotation difficulty examples

### Grading

For grading, we define three related tasks: segmentation, labeling, and end-to-end annotation. Segmentation tests whether a model can find the right time boundaries. Labeling tests whether a model can name a segment when the correct time window is already given. End‑to‑end annotation tests the full setting: the model must both find the segment and label it correctly.

For segmentation, the model predicts timestamped subtask boundaries. Labels can be included, but they are ignored for this score. We use Segment F1 and count a predicted segment as matching a gold (human annotated) segment when  `IoU >= 0.75` . Before scoring, we snap the first predicted start time and the last predicted end time to the human annotation boundaries, since the outer edges of an episode are often ambiguous (it is not always clear whether the first action starts at the beginning of the video, when the robot first appears, or when the robot starts moving; the same issue applies at the end).

For labeling, the model receives the gold segment boundaries and predicts one label per segment. We use a Scale‑style LLM‑as‑judge rubric, adapted for subtask labels, with  `gemini-3.5-flash`  as the judge.Prompt: Label judge rubric+12345678910111213141516171819202122232425262728293031323334 ` `You are judging whether a predicted subtask label matches a gold subtask label.

Gold label:
{gt_label}

Predicted label:
{pred_label}

Episode instruction:
{instruction}

Accept if:
- It describes the same manipulation event or world-state change.
- The main action is correct.
- The main manipulated object is correct.
- Source, destination, direction, or spatial relation is correct when central to the event.
- Wording can differ; synonyms are fine.
- It may be slightly less detailed than the gold label if it is still useful.

Reject if:
- The action is wrong.
- The main object is wrong.
- Source, destination, or direction is flipped or wrong.
- It describes a different event.
- It is too vague to identify the subtask.
- It hallucinates an important object or action.

Ignore:
- Grammar.
- Minor wording differences.
- Timing; timing is evaluated separately.

Return only JSON:
{"match": true}` ` 

Finally, we evaluate the end-to-end setting. It uses the same setup as segmentation, but a predicted segment also has to pass the labeling test in order to be considered a match.

## Part I: Finding subtask boundaries

Since we split annotation into boundary detection and labeling, the first question is how to find the subtask boundaries. Some methods can use extra robot state, such as gripper position, joint state, or end-effector motion. We intentionally do not assume access to that signal, because egocentric video and many scraped robot-video datasets only provide pixels.

### Fixed‑length baseline

As a sanity-check baseline, we ignore the video content and task instruction entirely. We simply split each episode into consecutive segments that are exactly  `5.77s`  long, the mean gold segment duration in WGO‑Bench, and score the resulting boundaries against the human subtask boundaries. This reaches  `0.070`  Segment F1 on the full 100-episode benchmark.

### Splitting Videos by Similarity

Our first non-trivial approach follows prior work on VLM captioning for subtask segmentation (⁠[Suzuki et al., 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-suzuki2026proprioceptionenhancesvisionlanguage)⁠). We ask a VLM (Gemini 3.5 Flash) to caption frames from the video, embed those captions, then split segments when the cosine similarity between neighboring caption embeddings drops far enough. Unfortunately, the threshold suggested in the paper heavily over-segments, and even after sweeping many similarity thresholds this method only barely beats the fixed-length baseline, reaching  `0.081`  F1.One frame through the pipelineframe > caption > vectorsampled framecaption from VLMtwist open the pitcher lidcaption embedding0.18-0.420.770.09-0.310.56dense high-dimensional vectorSimilarity to previous captionpaper cutoff 0.65keepcut, sim < 0.65Caption embedding0.108Segment F1Direct frame embeddings0.109Segment F1Fixed-length baseline0.070Segment F1The caption-embedding method converts frames into text, compares neighboring caption embeddings, then cuts whenever adjacent-caption similarity drops below the paper's 0.65 threshold. In our benchmark this over-segmented the episode and reached 0.108 Segment F1.

One possible issue is the unnecessary conversion through text: image -> caption -> embedding. In the hope that this was the bottleneck, we skipped captioning and embedded the frames directly with [Gemini Embedding 2](https://deepmind.google/models/gemini/embedding/). Unfortunately, this made things much worse, resulting in  `0.007`  F1.Prompt: Gemini embedding+1 ` `Represent this robot video frame based on the current sub-goal the robot or human is pursuing. Focus on what object is being manipulated, what state change is underway, where the object is moving, and whether the current sub-goal appears different from nearby moments. Do not describe the image; produce an embedding useful for grouping frames that belong to the same ongoing sub-goal.` ` 

### Asking the Model Directly

#### Per‑frame timestamped images

Instead of relying on embedding heuristics, we next fed frames directly into the model and asked it to segment the video. The key representation problem was how to represent time, as the model needed to know which frame corresponded to which timestamp.

Most approaches give the model time information through special temporal tokens (⁠[Li et al., 2025](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-li2025universalvideotemporalgrounding)⁠) or text. We used the simplest text-based version: interleave each sampled frame with its timestamp, use an instruction close to the one given to human annotators, and pack all frames into one prompt.

Because the model is already generating a structured segment list, we also ask it to include a short subtask label for each segment. That adds no meaningful extra cost and makes the outputs easier to inspect, but the experiments in this section are scored on boundary quality.

In this setup, the model receives a long sequence of separate images. Each frame is paired with timestamp text, and the prompt asks the model to use those timestamps when choosing subtask boundaries.Part 1: prompt textTotal parts647Input tokens361,186Reconstruct the sequence of manipulation events in this robot video from chronological frame images.Return only JSON with this shape: `{"segments":[{"start_sec":0.0,"end_sec":1.0,"subtask":"short action description"}]}` How to read the images+
- The images are individual video frames sampled in chronological order.
- There are no timestamps drawn on the images.
- The first image is at 0.0 seconds.
- Each next image is 0.5 seconds later than the previous image.
- Therefore image number N is at time_sec = (N - 1) * 0.5.
- Use this image-number-to-time mapping for start_sec and end_sec.
- Boundaries should normally land on or near one of those sampled times.Rules+
- Treat each segment as one world-state change.
- Good boundaries happen when objects become held, are released, reach new locations, change open/closed state, or contents visibly move.
- Choose start_sec at the first frame where causal motion is underway, and end_sec at the first frame where the resulting world state is achieved.
- Keep continuous gradual actions as one event.
- Output separate repeated events for the same action on different objects or target locations.
- Skip idle time, camera motion, hesitation, and tiny hand adjustments.Task instructionuse pitcher to pour water into tall glass and wine glassRepeated frame text + image pairs4 pairs shown / 323 pairs sentPart 2 ( `text` )Frame 000 at time_sec=0.000Part 3 ( `inline_data` )Part 4 ( `text` )Frame 001 at time_sec=0.500Part 5 ( `inline_data` )Part 6 ( `text` )Frame 002 at time_sec=1.000Part 7 ( `inline_data` )Part 8 ( `text` )Frame 003 at time_sec=1.500Part 9 ( `inline_data` )The frame-sequence setup sends one instruction text part, then one frame-index timestamp text part before each separate image input. The frames themselves have no timestamp overlay, which makes the request easy to build but expensive for Gemini's visual token accounting.

This resulted in a score of  `0.193`  F1, easily clearing the fixed-length baseline.

#### Contact Sheets: Better and Cheaper

The frame-based approach has two problems: it is expensive, and the performance is still weak. In our setup the Gemini API cost is  `$0.188`  per minute of video while only reaching  `0.193`  F1.

We take inspiration from Scale's contact sheets and pack multiple frames into one large image. In our case, each sheet contains 20 frames in a 4-row by 5-column layout, sampled every 0.5 seconds, such that one sheet spans 10 seconds of video.

To encode timestamps, we use the same basic strategy as the frame setup, but describe the contact-sheet map instead of attaching one timestamp to each separate frame.
This contact-sheet setup compresses 10 seconds of video into one image, with timestamps supplied separately in the prompt text.

This only gives a small quality bump to  `0.201`  F1. The bigger win is cost: roughly 12x cheaper, dropping to  `$0.0158`  per minute of video.

The cost drop from contact sheets mostly comes from how Gemini counts image inputs. Images up to 384 pixels in both dimensions count as  `258`  tokens, and larger images are split into  `768x768`  tiles, with each tile also counted as  `258`  tokens. Sending frames one by one pays that image cost for every sampled frame. Packing frames into one contact sheet pays for the sheet tiles instead, which amortizes the visual token cost across many frames. We also suspect contact sheets can be slightly better for quality because they reduce the number of separate images in the prompt; most models are trained with only a few images at a time, so a single composed image may be closer to the training distribution than a long list of individual frames.Input budgetsampled frames22040360frames per sheet20630Contact sheets12.5xcheaperImage reduction20.0x220 -> 11Scaled from measured HomER runs: 323 frame inputs vs 17 sheets. Token ratio for this setting: 16.2x.Per-frame images220 separate image inputs246,009input tokens$0.1280per minuteTimestamped contact sheets11 sheet images, 20 frames each15,154input tokens$0.0102per minuteContact sheets reduce the image count by packing many sampled frames into one timestamped image. Move the controls to see how the image count changes the token and price multiplier.

#### Timestamp Cues

The auxiliary labels made the failure mode easy to inspect. Even though label quality is not the metric here, the generated labels are usually reasonable: the model knows that an object was picked up, placed, opened, or moved. The weak point is boundary placement. It can describe the broad event, but still misses finer subtasks and struggles to place the start and end times in the right place.Boundary comparison / homer_1now 0s / 42sInstruction: use pitcher to pour water into tall glass and wine glassHomER clip used for boundary comparison0s / 42snowMethodGoldFrame sequenceContact sheet0s10s20s30s40sGold0twist open the pitcher lid0twist open the pitcher lid1pick up the pitcher1pick up the pitcher2pour water from the pitcher into the wine glass2pour water from the pitcher into the wine glass334twist the pitcher lid to close it4twist the pitcher lid to close it556pour water from the pitcher into the wine glass6pour water from the pitcher into the wine glassFrame sequence0adjust the lid0adjust the lid1lift the pitcher1lift the pitcher2pour water into the wine glass2pour water into the wine glassContact sheet0rotate lid open0rotate lid open1pour into wine glass1pour into wine glass2adjust pitcher lid2adjust pitcher lid3pour into wine glass3pour into wine glassThe model can often name the broad event while missing finer subtask boundaries. This compares the same HomER clip against the human labels, per-frame inputs, and the simple contact-sheet setup.

We initially avoided engraving timestamps directly into the frames because several works (⁠[Singh et al., 2019](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-singh2019textvqa); [Liu et al., 2024](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-liu2024ocrbench)⁠), as well as the Scale blog (⁠[Choghari et al., 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-scale2026densecaptioning)⁠), warn against relying on visual text. Still, we decided to try it. Beyond plain timestamps, we also tried different encodings: replacing timestamps with IDs like  `{A-Z}_{1-20}` , where the letter marks the sheet and the number marks the tile inside the sheet, combining textual and visual cues, and changing where the timestamp is rendered.Timestamp cue renderingTimestamp cue renderingText timestamp map - F1 0.201Visual timestamps - F1 0.263Visual + text map - F1 0.212Tile IDs - F1 0.231Tile IDs + text map - F1 0.229No visual cueText timestamp mapF1 0.201Best F1Visual timestampsF1 0.263Extra timestamp textVisual + text mapF1 0.212Contact sheet onlyTile IDsF1 0.231Extra timestamp textTile IDs + text mapF1 0.229Text timestamp maptile 01 -> 10.0stile 02 -> 10.5stile 03 -> 11.0s...Prompt payloadNo in-image cue; timing only appears in text.A contact sheet with no visual cue relies on the prompt text to map tile order back to timestamps. This reached F1 0.201.

Visual cues worked surprisingly well, pushing segmentation to  `0.263`  F1. Unfortunately, replacing timestamps with ID codes did not help, and combining visual cues with a text timestamp map made the result worse. So we kept the simple version: visual timestamps directly on the contact sheet.

Because visual cues worked so well, we also tried a few timestamp renderings: a yellow box in the top-right of each frame with black timestamp text, a white side strip with the frame time, and a large black box at the bottom-center with white timestamp text. None of them beat the original in-tile timestamp.Timestamp rendering styleStyle sweepTimestamp rendering styleYellow top-right - F1 0.249Side caption - F1 0.261Large bottom-center - F1 0.233Yellow top-rightF1 0.249Side captionF1 0.261Large bottom-centerF1 0.233A yellow top-right timestamp box remained readable but did not beat the original in-tile timestamp style.

#### Contact Sheet Sweeps

After the timestamp sweep, the obvious next question was whether the rest of the contact-sheet design mattered too. We therefore swept resolution, sampling rate, and the number of frames per sheet.Contact sheet design sweepResolutionSampling rateSheet size0.00.51.01.52.02.53.03.54.04.55.05.56.06.57.07.58.08.59.09.5Best setup224pxF10.290160pxsmall0.264224pxbest0.290320pxlarger0.231448pxlarger0.237640pxlargest0.259The contact-sheet sweep keeps converging on the same compact setting: 224px tiles, 0.5s sampling, and 20 frames per sheet.

Resolution

Surprisingly, scaling up the resolution did not help. It is not obvious why. When we resize benchmark videos down to 224px, even humans start to have more trouble annotating them, so we would expect normal-resolution sheets to help much more than they do. One possible explanation is that very large contact sheets hit practical limits in the model image pipeline, such as resizing, cropping, or less reliable attention over huge tiled images.

Sampling rate and sheet size

Again, the sweep did not improve over the original contact-sheet setting. Sampling more densely seemed to add noise or make the prompt harder to parse, while larger sheets did not provide enough extra context to justify the added visual complexity.

#### Input Decomposition Experiments

One reason we suspected the model might struggle was input size. For the longest episodes in our benchmark, a single full-episode call would send roughly 343 frames across 18 contact sheets, totaling around 20k input tokens. Since increasing context size and the number of separate input images typically degrades performance, we expected splitting segmentation into multiple smaller calls might help.

In each call, we sent one contact sheet with visual cues and additionally asked Gemini to emit whether the first segment was a continuation. We then postprocessed the results by merging continuations if either Gemini emitted the continuation flag or the segments matched exactly. We tried this both with a 2-frame overlap, to improve continuity matching, and with no overlap. To improve continuity further, we also tried adding textual information about the last unfinished segment from the previous call.

The main failure mode was that the model treated those artificial split points as real boundaries, ending segments there far more often than the gold annotations do:Sheet 1Sheet 2splitSheet 3splitSheet 4splitNo overlapPredicted boundary ends85 / 383 (22.2%)Gold boundary ends66 / 743 (8.9%)Overlap 2Predicted boundary ends135 / 410 (32.9%)Gold boundary ends92 / 743 (12.4%)Overlap 2 + last segmentPredicted boundary ends162 / 417 (38.8%)Gold boundary ends92 / 743 (12.4%)Sequential contact-sheet calls tend to invent boundaries at sheet edges, especially when extra continuity context is added.

Unfortunately, none of these methods beat the simple strategy of sending all contact sheets in one call. Still, some form of decomposition will likely matter when scaling to much longer episodes.

The results were fairly surprising: we thought adding overlap or last-segment context would reduce this split-boundary bias, but the opposite happened.Prompt: Input decomposition+123456789101112131415161718192021 ` `Segment the current timestamped contact sheet from one continuous robot video.

Return only JSON with this shape:
{"segments":[{"start_sec":0.0,"end_sec":1.0,"subtask":"short action description","continues_previous":false}],"end_state":"short description of what may continue after this sheet"}

Context:
- This is sheet {sheet_index} of {sheet_count}.
- Current sheet visible time range: {start_sec:.2f}s to {end_sec:.2f}s.
- Only output segments that overlap emit range: {emit_start_sec:.2f}s to {emit_end_sec:.2f}s.
- Frames before emit_start_sec are overlap context only.
- Each sheet has 4 rows and 5 columns. Time runs left-to-right, then top-to-bottom.
- Every tile has a timestamp in the top-left corner. Use those visible timestamps.
- Episode instruction: {instruction}
- Previous accepted segments: {previous_segments_json}

Rules:
- Treat each segment as one manipulation event that changes the world state.
- Good boundaries happen when an object becomes held, is released, reaches a new location, a lid/door changes state, a tool starts/stops affecting a surface, or contents visibly move.
- If the first visible event continues the final previous accepted segment, set continues_previous=true on that first segment and use the same subtask wording if possible.
- Do not create a boundary just because this contact sheet starts.
- Avoid idle time, camera motion, hesitation, and tiny hand adjustments.` ` 

#### The Model Matters

Given that we had converged on image inputs, we next checked whether the bottleneck was the model itself. We benchmarked Google models alongside other proprietary and open-source models.Model sweepF1Gemini 3.5 Flash baseline645 predictedfixed-window0.290Gemini Robotics ER 1.6556 predicted0.245GPT-5.5 low602 predicted0.233GPT-5.4 low529 predicted0.233Gemini 3.1 Pro Preview586 predicted0.232Gemini 3 Flash Preview685 predicted0.210Claude Opus 4.8733 predicted0.168Claude Sonnet 4.6698 predicted0.146Gemini 2.5 Pro662 predicted0.145Qwen 3.5 Plus763 predicted0.141Claude Haiku 4.5570 predicted0.128Gemini 3.1 Flash Lite757 predicted0.119Qwen 3.6 Flash715 predicted0.110GPT-5.4 mini317 predicted0.106Gemini 2.5 Flash855 predicted0.059Gemma 4 26B1,080 predicted0.057The model sweep shows Gemini 3.5 Flash as the strongest setting, while several models either under-segment or produce many extra segments.

Gemini was clearly ahead of the other frontier labs in this setup. We were also surprised that Gemini Robotics ER did not do better, given that it should be tuned for spatial and robotics tasks. The open-source models were weaker here and often over-predicted segments.

#### Prompt Search with GEPA

At this point, the failures had a pattern. The model could often see the manipulation, but it applied the wrong granularity. It treated approach, grasp adjustment, hesitation, retreat, and tiny repositioning as separate events, while our annotations only count completed manipulation events.

Instead of continuing to hand-tune prompts, we used GEPA (⁠[Agrawal et al., 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-agrawal2026gepareflectivepromptevolution)⁠) on a separately annotated 15-episode validation set. The goal was to search for prompts that make the model follow the annotation protocol described above: segment atomic manipulation events, ignore incidental motion, and place boundaries at completed world-state changes.

The base prompt,  `event_reconstruct_contact_sheets_v1` , already described the right kind of boundaries: objects becoming held, released, moved, opened, closed, affected by tools, or visibly changing state. What it did not do strongly enough was constrain granularity. The best GEPA‑found prompt,  `completed_events_duration_prior_v1` , keeps the same event vocabulary but adds stricter counting rules: only completed manipulation events, no separate approach/grasp-adjustment/retreat segments unless the world state changes, no merging of distinct pick/place/open/close/pour/wipe events, and a light duration prior for the expected segment length.Prompt search trajectoryF1Duration priorcompleted_events_duration_prior_v1 · 550 predictedbase prompt0.306State machinecompleted_events_state_machine_v1 · 530 predicted0.302Cleanupcompleted_events_cleanup_v1 · 541 predicted0.293Base promptevent_reconstruct_contact_sheets_v1 · 645 predicted0.290No durationcompleted_events_no_duration_v1 · 520 predicted0.279Clear statesclear_state_changes_v1 · 710 predicted0.259Recover repeatsrecover_repeated_events_v1 · 742 predicted0.249Prompt: GEPA variantscompleted_events_duration_prior_v1+1 ` `Reconstruct the sequence of manipulation events in this robot video from the timestamped contact sheets.` ` 2 3 ` `Return only JSON with this shape:` ` 4 ` `{"segments":[{"start_sec":0.0,"end_sec":1.0,"subtask":"short action description"}]}` ` 5 6 ` `Rules:` ` 7 ` `- Segment only completed robot manipulation events, not every visible movement.` ` 8 ` `- Good boundaries happen when a held object changes, an object is placed or released, a tool starts/stops changing a surface, a container/door/lid opens or closes, or contents move between containers.` ` 9 ` `- Do not split approach, grasp adjustment, small repositioning, and retreat unless the world state changes.` ` 10 ` `- Do not merge separate pick/place/open/close/pour/wipe events when they complete different states.` ` 11 ` `- Most segments should be 2-10 seconds. Shorter segments are okay only for fast pick, place, open, close, or release events.` ` 12 ` `- Use the visible timestamps for start_sec and end_sec.` ` 13 ` `- Ignore label wording quality; prioritize temporally correct boundaries.` ` GEPA improves the prompt by tightening the event granularity: fewer incidental segments and better F1.

The best prompt predicted fewer segments than the base prompt ( `550`  vs.  `645` ) and improved overall F1 by removing many incidental-motion boundaries without losing too many real subtasks.

### Final segmentation recipe

After running 54 segmentation experiments, spanning everything from  `0.007`  F1 to  `0.306`  F1, we converged on the following recipe:

- sample frames every  `0.5s` 

- render them as  `224px`  tiles

- pack  `20`  frames per contact sheet in a  `5` -column layout

- draw visual timestamps directly on the frames

- use Gemini 3.5 Flash with a completed-events prompt

The prompt itself was less about describing the image and more about enforcing the annotation protocol. It asked for completed manipulation events, not every visible movement; it split when objects were picked up, released, moved, opened, closed, affected by tools, or transferred; and it explicitly told the model not to split approach, grasp adjustment, retreat, hesitation, or tiny repositioning unless the world state changed.

## Part II: Turning Segments Into Subtasks

The second part of subtask annotation is labeling: given a fixed segment, describe the subtask happening inside it. This is considerably easier than boundary discovery because the model no longer has to reason over the whole episode at once; most subtasks are shorter than  `10s` .

As described in [Measuring Progress: WGO‑Bench](https://macrodata.co/blog/annotating-robot-video-subtasks#measuring-progress-wgo-bench), we evaluate labels with an LLM judge rather than exact string matching. A predicted label is correct if it describes the same manipulation event as the human annotation. Unlike boundary detection, this task does not have an obvious trivial baseline: there is no simple way to generate meaningful subtask labels without looking at the video.

We start from what worked best in our boundary experiments, with Scale's dense video captioning post (⁠[Choghari et al., 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-scale2026densecaptioning)⁠) as a useful reference point for compact video inputs. Once the segment boundaries are fixed, we only need to figure out how much visual evidence and surrounding context the model needs to name the event correctly.

### Input Formatting

As with segmentation, the first question is how to represent the video to the model. Labeling is easier because the input is already a short fixed segment, not a full episode, but it was still worth checking whether the same input-format lessons hold.

For most labeling experiments, we used the following prompt, based on what worked in segmentation.Prompt: Labeling+123456789101112131415161718 ` `Annotate the fixed robot video segment shown in the contact sheet.

Return only JSON:
{"label":"short descriptive subtask label"}

Focus on the state change caused by the segment.

Rules:
- The frames are chronological and timestamped.
- The segment boundaries are fixed; do not create, split, merge, or move segments.
- Compare the beginning and end of the segment, then describe the completed visible change.
- Use one concise imperative phrase.
- Name the manipulated object and the action/state change.
- Include source, destination, side, direction, final placement, opened/closed state, filled/cleaned/cut/drawn/folded part when visible.
- If the segment is a continuous process, describe the process and its target, e.g. "wipe the wooden table with the cloth" or "dice the onion on the cutting board".
- Do not mention timestamps, frame numbers, uncertainty, or invisible intent.

Episode instruction: {instruction}` ` 

We treat labeling as a state-change question: given a fixed time window, compare the beginning and end, then name the completed manipulation event. The prompt stayed the same across these runs; only the visual input changed.

We tried different ways to feed visual information to the model: an MP4 video clip of the complete target segment, a single contact sheet made from three sampled frames, and the same three frames sent as separate image inputs.MP4 clipOne short video file covering the target window.Accuracy40.4%300/7433-frame contact sheetThree sampled frames packed into one image.Accuracy52.9%393/7433 separate framesThe same three frames sent as individual image inputs.Accuracy54.1%402/743We kept the labeling prompt fixed and changed only the visual payload: video clip, composed contact sheet, or separate image inputs.

Surprisingly, separate frame inputs were slightly better than contact sheets for labeling. We still continued with contact sheets because they are about 12x cheaper, and the gap was small enough that cost mattered more.

### More Frames Are Not Always Better

The next question was how many frames to put inside the contact sheet. Unlike segmentation, labeling starts from well-bounded segments, so we can sample only a few frames uniformly and still capture most actions. In many cases, the start and end state already carry the useful signal.

We therefore ablated the number of frames per target sheet.Target sheet frame countAccuracy3 framesTarget sheet only - 393 / 74352.9%5 framesTarget sheet only - 417 / 74356.1%8 framesTarget sheet only - 396 / 74353.3%16 framesTarget sheet only - 389 / 74352.4%For fixed gold segments, adding more target frames did not improve label accuracy. Five uniformly sampled frames was the best target-only setting.

The best target-only setting uses only 5 frames. Beyond that, adding more frames does not meaningfully improve accuracy. However, this depends on how well the segments are split: with noisier or less precise boundaries, the model might need more frames to recover what happened.

### Before and After Helps

The third ablation asks whether the model benefits from context beyond the target segment itself. Many actions are easier to name when you see what came immediately before or after: after picking up a cup, the next state often tells you where it was placed; after opening a door, the following segment can clarify whether the action was entering, closing, or repositioning.

We tested the following context variants:

- whole-episode overview (one contact sheet sampled uniformly across the full episode)

- local +/-1s context around the target segment

- local +/-2s context around the target segment

- previous/current/next fixed-segment context

- previous/current/next fixed-segment context plus episode overview
Context ablationTarget sheet (baseline, no context)56.1%Episode overview54.1%+/-1s context56.7%+/-2s context54.4%Prev / current / next61.0%Prev/current/next + overview60.8%Inserted visual informationtargetVisual payloadJust the target-segment contact sheet, without any extra visual context.For labeling, the strongest representation is not a denser target sheet; it is structured context from the previous, current, and next segment.

Adding context helps, but only when it is structured as whole neighboring segments. A local  `+/-1s`  or  `+/-2s`  window is often too narrow: boundaries frequently sit near grasp or release events, so the padding does not show enough of the previous or next state. Whole‑episode overview also does not help much, likely because the global instruction already provides most of that high-level context.

### Final recipe

For labeling, the final recipe is simple:

- use the fixed segment boundaries

- render three small contact sheets: previous segment, current segment, next segment

- sample up to  `5`  frames per segment uniformly

- ask Gemini 3.5 Flash to label only the current segment

- use the neighboring segments only to disambiguate what changed

This gave our best raw-labeling result:  `453/743 = 61.0%`  accuracy. This is broadly consistent with Scale's finding that past/current/future visual context is the strongest representation for clip-level labeling (⁠[Choghari et al., 2026](https://macrodata.co/blog/annotating-robot-video-subtasks#ref-scale2026densecaptioning)⁠). The main difference is that we use compact contact sheets instead of their hand-collage setup, which keeps the same temporal contrast while making the pipeline substantially cheaper to run.

## End‑to‑End Evaluation

After finding the best segmentation and labeling recipes, the final question is whether the full task should be done in one pass or split into two steps: segment first, then relabel the predicted segments.

Our first experiments were just combining the best segmentation setup with the best labeling setup, but to our surprise this performed worse than taking the labels directly from segmentation. Thus we ran one more experiment: use the original segment label as a strong prior, then ask the model to verify and minimally correct it using the previous, current, and next segment images.MethodSegment F1Sort by Segment F1 ascendingLabel accuracy on temporal matchesSort by Label accuracy on temporal matches ascendingSemantic precisionSort by Semantic precision ascendingSemantic recallSort by Semantic recall ascendingSemantic E2E F1Sort by Semantic E2E F1 ascendingbest segment -> label `0.302`  `71.5%`  `0.184`  `0.132`  `0.154` one-pass segmentation labels `0.302`  `73.7%`  `0.190`  `0.136`  `0.158` segment -> seeded relabeling `0.302`  `78.1%`  `0.201`  `0.144`  `0.168` End-to-end segmentation and labeling resultsPrompt: Seeded relabeling+1 ` `Annotate one fixed segment from a longer video.` ` 2 3 ` `Return only JSON:` ` 4 ` `{"label":"short descriptive subtask label"}` ` 5 6 ` `Inputs:` ` 7 ` `- The first image is the previous fixed segment, if it exists; otherwise it is blank/context only.` ` 8 ` `- The second image is the current target segment.` ` 9 ` `- The third image is the next fixed segment, if it exists; otherwise it is blank/context only.` ` 10 ` `- Each image is timestamped with absolute video time.` ` 11 12 ` `Episode instruction:` ` 13 ` `{instruction}` ` 14 15 ` `Target segment:` ` 16 ` `{segment_index} of {segment_count}` ` 17 18 ` `Target time:` ` 19 ` `{start_sec:.2f}s to {end_sec:.2f}s` ` 20 21 ` `Original predicted label for this exact segment:` ` 22 ` `{seed_label}` ` 23 24 ` `Rules:` ` 25 ` `- Label only the current target segment.` ` 26 ` `- Use previous/next images only to disambiguate what changed during the current segment.` ` 27 ` `- Treat the original predicted label as a strong prior, not as ground truth.` ` 28 ` `- Verify and minimally correct the original label using the current target segment.` ` 29 ` `- If the original label describes the same action and main object, keep it, only improving grammar or adding clearly visible essential details.` ` 30 ` `- If it is too vague but directionally correct, make it more specific.` ` 31 ` `- If it describes the previous/next segment, the wrong action, wrong object, wrong destination, or wrong state change, replace it.` ` 32 ` `- Do not describe the previous or next segment.` ` 33 ` `- Do not split or merge the fixed segment.` ` 34 ` `- Do not introduce a new action unless it is clearly visible in the current target segment.` ` 35 ` `- Do not make the label broader than the fixed segment.` ` 36 ` `- Use one concise imperative phrase.` ` 37 ` `- Include the exact action and manipulated object.` ` 38 ` `- Include source, destination, side, direction, final location, opened/closed/filled/cleaned state, or affected part when visible and central.` ` 39 ` `- Do not mention timestamps, frame numbers, uncertainty, candidates, or invisible intent.` ` 

That finally beat the one-pass segmentation method and raised label accuracy on temporal matches to  `78.1%`  and semantic E2E F1 to  `0.168` .

The tradeoff is cost. Seeded relabeling improves semantic accuracy, but it can get expensive because each predicted segment triggers another model call and the relabeling prompt often incurs a lot of thinking tokens. Batch pricing cuts this roughly in half, but segmentation-only is still the cheaper default when cost is the priority. If label quality matters more and the budget allows it, running segmentation followed by seeded relabeling gives the best end-to-end result.StageCallsCost / hourBatch cost / hoursegmentation `100`  `$0.86/h`  `$0.43/h` seeded relabeling `532`  `$4.41/h`  `$2.21/h` total end-to-end `632`  `$5.27/h`  `$2.64/h` End-to-end cost breakdown for the seeded relabeling pipeline

### Failure Mode Breakdown

[Table 2](https://macrodata.co/blog/annotating-robot-video-subtasks#tab:end-to-end-results) separates the two failure modes: label accuracy on temporal matches reaches  `78.1%` , while Segment F1 is still only  `0.302` . Clearly the main bottleneck is segmentation.

The largest segmentation failure mode is short subtasks. This mirrors the human annotation problem described in the [manual labeling section](https://macrodata.co/blog/annotating-robot-video-subtasks#lessons-from-the-annotation-trenches): quick pick, place, and adjustment events can span only a few frames or seconds, making their boundaries hard to place. The same issue shows up in the pipeline. Segments shorter than  `2s`  have by far the lowest recall, only  `0.074` . This is most pronounced in HomER, the egocentric subset with the lowest F1, both because it has the highest concentration of short segments and because it contains the concurrent-subtask issues described in the labeling section.Temporal bottleneckSegmentation errorsRecall by durationRecall<2s7.4%13/176 matched2-5s23.7%68/287 matched5-10s45.8%82/179 matched10-20s35.3%24/68 matched>=20s33.3%11/33 matchedPer dataset F1F1 / matchedGalaxea0.58966 matchesDROID / RoboInter0.29248 matchesHomER0.22784 matchesSegmentation failures are dominated by ego-centric HomER and short events.

Once the model lands on the correct temporal segment, labeling is much less broken than segmentation. Interestingly, segments with correctly predicted boundaries are easier to label than all gold segments, with label accuracy increasing from  `61%`  to  `70.8%` . When it comes to errors, the action itself is mostly correct ( `92.0%`  slot accuracy), but the problem is grounding. Most error cases come from underspecification of state ( `pour water into glass`  vs  `pour water into glass until it's full` ) or initial/final location ( `pick up the plate below the table`  vs  `pick up a plate` ).Semantic groundingLabeling errorsFailure mode shareShareWrong target or direction42.5%failure shareRight verb, wrong object25.0%failure shareComplete miss15.0%failure shareWrong verb12.5%failure shareToo vague2.5%failure shareHallucinated detail2.5%failure shareSlot accuracyAccuracyVerb92.0%slot accuracyTool / surface94.2%slot accuracyObject89.1%slot accuracyTarget / direction76.6%slot accuracyState change73.0%slot accuracyMatched-label failures are mostly grounding errors: object identity, target location, and resulting state.

### Final end-to-end recipe

Both the segmentation only and segmentation + seed relabeling are open-sourced in [Refiner](https://github.com/macrodata-labs/refiner), our robotics data processing framework. To run it on your own videos, see the [ready-to-use subtask annotation example](https://macrodata.co/docs/examples/annotations/subtask-annotations).Refiner end-to-end pipelineSampling0.5sSheet layout4 x 5Tile width224pxDefaultone pass1: episodeVideoRaw robot or egocentric demonstration.2: sampled inputTimestamped sheets0s2.5s5s7.5sContact sheets carry visual evidence and timing.3: one callGemini promptinstruction+ timestamped sheets+ JSON schemaBoundaries and labels are predicted together.4: normalized outputSubtask rows0.000-7.709twist open the pitcher lid7.709-21.712pour water into the wine glass21.712-26.514twist the lid to close itRefiner sorts, validates, and writes the rows.The default end-to-end pipeline sends timestamped contact sheets to Gemini in one pass, then normalizes the returned segments into start, end, and label rows.

## Conclusion

We have shown that VLMs can pull useful subtask annotations out of raw robot videos, but the way we show the video to the model matters more than we expected. The best setup was also the simplest one. Timestamped contact sheets were cheaper and worked better than long sequences of individual frames. Prompt wording and model choice still changed the results a lot, and labeling worked best when the model could see what happened just before and just after the segment.

[WGO‑Bench](https://huggingface.co/datasets/macrodata/WGO-Bench) is still a small benchmark, but it gives us concrete tools to measure this problem end-to-end, including boundary discovery, segment labeling, and the combined semantic score. We are releasing it because subtask annotations are becoming an important training signal for long-horizon robot learning, and the community needs public evaluation targets for how to produce them at scale.

This is also the broader reason we are building Macrodata Labs: better data for better robots. Robotics teams should be able to turn raw physical-world experience into inspectable, enriched, reusable training signal without rebuilding the same data plumbing for every project or relying on hard-to-scale human annotation. Subtask annotation is one example of that larger problem, and we will keep tackling common robotics-data bottlenecks so more teams can turn real-world demonstrations into real-world progress.

The full open-source pipeline is available in Refiner for teams that want to run it themselves. Since this study, we have continued developing a proprietary subtask-annotation pipeline that delivers better performance on real-world robot video.

[Send us a small video sample](https://macrodata.co/contact?subject=Robot%20video%20subtask%20annotation) and we’ll run subtask annotation on it for free, so your team can evaluate the results.[Join our Discord](https://discord.gg/S8kZtmBR2x)[Contact us](https://macrodata.co/contact?subject=Physical%20AI%20data%20pipelines)[<- More blog posts](https://macrodata.co/blog)
