---
title: "Math-to-Manim"
url: https://github.com/HarleyCoops/Math-To-Manim
clipped: 2026-06-17 00:55:37
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Math-to-Manim](https://github.com/HarleyCoops/Math-To-Manim)

## Digest Summary
Math‑To‑Manim (M2M2) is a pipeline that converts math‑or physics prompts into fully inspectable Manim explainer videos and accompanying artifacts. Each run follows a fixed stage chain—IntentAgent → PrerequisiteGraphAgent → CurriculumAgent → MathAgent → StoryboardAgent → SceneSpecAgent → ManimCodeAgent → StaticReviewAgent → RenderAgent → VideoReviewAgent → PublisherAgent—producing JSON contracts, a knowledge graph, curriculum, math packet, storyboard, scene spec, generated Python code, validation reports, render results, and review notes. The system supports audience‑aware requests, reverse‑reasoning from final concepts to prerequisites, and typed Pydantic artifacts between stages. A reinforcement‑learning “Prime Intellect” environment uses the generated scene spec, code, and validation evidence to train models to repair failing Manim code; rewards check parseability, safety, expected terms, and layout. The repository includes CLI commands for smoke tests, model‑driven generation (OpenAI or Codex), and rendering (Manim, FFmpeg, LaTeX). Artifacts are stored under runs// bundles, enabling traceability, debugging, and recursive editing via agents such as Hermes. MIT‑licensed.

## Discussion Summary
The discussion characterizes the “RL repair loop” as simply iterative prompting with error feedback rather than true reinforcement learning, noting the absence of training code, a reward function, or an environment in the repository. It highlights that the process fixes only code while keeping the scene specification unchanged, which limits its ability to resolve fundamental design issues such as an over‑specified object layout that cannot physically fit, rendering multiple repair attempts ineffective.

---

## Full Article

This repo is also a live **Hermes Agent workspace**. Hermes is not imported by Math-To-Manim and is not a runtime dependency; it is the contributor/operator layer that uses the repo the way a developer would: read files, search code, patch docs and code, run terminal checks, inspect generated artifacts, review media with vision, delegate larger work, track todos, and preserve useful context through skills and memory.

| Hermes-native capability | How it is used in Math-To-Manim |
| --- | --- |
| File + search tools | Read `README.md`, `AGENTS.md`, `pyproject.toml`, schemas, tests, docs, and generated run artifacts before making claims. |
| Patch tool | Make surgical edits to docs, schemas, tests, pipeline code, and launch copy while preserving repo style and typed contracts. |
| Terminal tool | Run `pytest`, CLI help, deterministic smoke generations, Codex checks, Manim, FFmpeg, link validators, git, and GitHub verification. |
| Vision/media review | Inspect screenshots, contact sheets, frames, and GIFs so showcase media is judged visually, not trusted because filenames exist. |
| Delegation + todos | Split larger work across focused agents, track acceptance criteria, and keep implementation/review/checklist state explicit. |
| Session search + memory | Recover prior repo decisions and preserve stable conventions without storing secrets or temporary run noise. |
| Skills | Load procedures such as `agents-md`, `codebase-inspection`, `manim-video`, `systematic-debugging`, `writing-plans`, `test-driven-development`, and `subagent-driven-development`. |

The Math-To-Manim side gives Hermes concrete things to operate: the `math-to-manim` CLI, deterministic helpers in `math_to_manim/tools/`, typed stages in `math_to_manim/agents/` and `math_to_manim/pipeline/`, schemas in `math_to_manim/schemas/`, render/review helpers, and reproducible `runs/<run_id>/` bundles containing JSON contracts, `generated_scene.py`, validation/render/review reports, contact sheets, frames, and `manifest.json`.

Start a repo-aware Hermes session:

```
# Install/configure Hermes if needed.
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes doctor

# From the repo root, preload skills for this repo.
hermes --skills agents-md,manim-video,codebase-inspection,systematic-debugging
```

See [`AGENTS.md`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/AGENTS.md) for the full operating contract and [`docs/HERMES_LEARNS_MANIM.md`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/HERMES_LEARNS_MANIM.md) for the launch/thread plan and new animation slate.

---



---

[![Mythos Learns Math-to-Manim](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/mythos-learns-math-to-manim.png)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/mythos-learns-math-to-manim.png)

**This repo is now built around Claude Mythos.** The six-agent reasoning chain has been rebuilt on Claude-native tooling: the agents are Claude Code subagents, a custom harness drives them headlessly through the Claude CLI, and a Mythos-class model writes every frame with the camera as narrator — plain-language headlines before symbols, flights into the exact term being explained, pull-backs to restore context, true-3D set pieces.

The chain: **intent → cartographer → curriculum → math-director → cinematographer → scene-composer**, then codegen → static checks → render → self-repair.

| Piece | Where | What it does |
| --- | --- | --- |
| Agent charters | [`mythos/agents/`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/mythos/agents) (mirrored in `.claude/agents/` for native Claude Code use) | The six minds of the chain, one markdown charter each |
| Custom harness | [`mythos/harness.py`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/mythos/harness.py) | Runs the whole chain via `claude -p`; artifacts land in `runs/mythos/<ts>/`; `--offline` rehearsal mode needs no login |
| Camera grammar | [`mythos/cinematography.py`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/mythos/cinematography.py) | `headline`, `zoom_to`, `pull_back`, `term_tour`, `tilt_to_3d`, glows — the Mythos house style, Anthropic palette |
| Provider seam | [`math_to_manim/providers/mythos_cli.py`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/math_to_manim/providers/mythos_cli.py) | Drops Mythos into the legacy typed pipeline: `M2M2_CODEGEN_PROVIDER=mythos-cli` |
| Flagship film | [`examples/mythos/qft_cinematic.py`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/examples/mythos/qft_cinematic.py) | QED in 8 acts: 200 s, ~160 animations, term-by-term Lagrangian camera tours |

```
uv sync --extra render

# the whole chain, one line
python -m mythos.harness "explain quantum field theory" --render -q m

# or render the flagship directly
manim -qh examples/mythos/qft_cinematic.py QFTCinematicJourney
```

[![Camera inside the QED Lagrangian: the Dirac term spotlit with a plain-language caption](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/mythos-qft-term-tour.png)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/mythos-qft-term-tour.png)
[![The electron-photon vertex with the fine-structure constant resolving to 1/137](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/mythos-qft-vertex.png)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/mythos-qft-vertex.png)

*Stills from the Mythos cut of the QED journey: the camera inside the Lagrangian (left); the e⁻e⁻γ vertex as α resolves to 1/137 (right).*

The original Codex/OpenAI chain remains available as a legacy provider — nothing was removed, Mythos is simply the way the films get made now.

---

**Math-To-Manim** started on the morning of Donald Trump's inauguration. I do not think it was an accident that the Chinese decided to release the R1 model on that day.

I was awake, saw the model hit Hugging Face, and quickly built a `.ipynb` to load the model and run it.

I created this repo at `2025-01-20T11:04:50Z` / `04:04:50 MST`.

Within a couple of minutes I realized what this meant. If the Chinese, via GRPO, had reasoning on a chip, recursive reasoning was not far behind. In my tweet I wrote "Wrap it up, its over" and I still believe it.

```
09a2f22  2025-01-20T04:24:50-07:00  updated
A        DeepSeek_R1_zero.ipynb
A        Readme.md
```

Three hours later, the first Manim file landed: `pythagorean.py` at `2025-01-20T07:18:12-07:00`.

[![The original R1 Pythagorean theorem Manim animation from the viral January 20, 2025 tweet](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/r1-pythagorean-tweet.gif)](https://x.com/christiancooper/status/1881335734256492605?s=20)

> "I asked #R1 to visually explain to me the Pythagorean theorem. This was done in one shot with no errors in less than 30 seconds. Wrap it up, its over: #DeepSeek #R1"
>
> — [Christian H. Cooper, January 20, 2025](https://x.com/christiancooper/status/1881335734256492605?s=20)

What I saw with R1 is that the model was already good with Manim code out of the box. What actually runs under the hood with Math-To-Manim is a series of six planning agents that recursively reason over the prompt you gave it before code generation, validation, rendering, and review. This all runs on Codex 5.5.

However, since Prime Intellect rolled out hosted evals, and since I understand Recursive Learning Models better now, I am using the reasoning traces for RL training.

But this will always just work. If you are a teacher or a parent, you can always ask for an explanation and just get an MP4 back. You never have to see or worry about the reasoning training.

For the curious, follow along here: [Prime Intellect M2M hub: `harleycooper/math-to-manim`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/PRIME_INTELLECT_RL.md).

-christian

---

"Hey man, I just want to see a demo, I don't need a calculus lecture"
---------------------------------------------------------------------

Fair. The whole point is that the pipeline should turn a one-sentence idea into something moving on screen before you have to read the architecture docs.

[![A generated Manim movie unwrapping circle annuli into a triangle](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/showcase/assets/circle-area-3d-unwrapped.gif)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/showcase/assets/circle-area-3d-unwrapped.gif)

WSL quickstart:

```
cd /mnt/c/Users/$USER

git clone https://github.com/HarleyCoops/Math-To-Manim.git
cd Math-To-Manim

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev,render]"
./scripts/bootstrap-render.sh  # Debian/Ubuntu/WSL system deps for real MP4 output

m2m2 generate \
  "Show why the quantum harmonic oscillator only allows discrete energies: start with a springy potential well, zoom into the wavefunctions, then reveal the ladder of allowed energy levels." \
  --codegen-provider codex-cli \
  --codex-full-auto \
  --style cinematic \
  --quality l \
  --runs-dir runs
```

Generated bundles and videos stay in repo-local `runs/<run_id>/` by default;
the `--runs-dir runs` flag above is intentionally explicit so agent-driven runs
do not disappear into `/tmp`.

If you want Hermes to run the harness like an operator instead of driving the CLI by hand:

```
hermes --skills manim-video,systematic-debugging,codebase-inspection \
  -z "Run the M2M2 pipeline on the quantum harmonic oscillator demo prompt with --runs-dir runs, inspect the repo-local run bundle, try a low-quality render, and report the generated movie path or the exact blocker. Do not put user-visible outputs in /tmp."
```

That gives you the practical loop: ask for the movie, inspect the run bundle, then tell the agent what to fix.

---

[![Hermes Learns Manim: an agent surrounded by equations, turning recursive reasoning into animation code](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/hermes-learns-manim.jpg)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/hermes-learns-manim.jpg)

Hermes is the contributor/operator agent around this repository. It is not imported by Math-To-Manim and is not a runtime dependency; it uses the repo the way a developer would: read files, search code, patch docs and code, run terminal checks, inspect generated artifacts, review frames or GIFs, track todos, delegate larger work, and preserve stable context through skills.

That makes Hermes useful for maintaining the reverse-reasoning pipeline without becoming part of it. A Hermes session can inspect `AGENTS.md`, `pyproject.toml`, schemas, tests, and `runs/<run_id>/` bundles; run `pytest`, CLI smoke commands, Manim, FFmpeg, and git checks; then verify that docs, code, and showcase media still match the artifact contracts.

Repo-local Hermes skills live under [`hermes/skills/`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/hermes/skills). The old Claude `./skill` path is historical; current contributor guidance is in [`AGENTS.md`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/AGENTS.md), with launch notes in [`docs/HERMES_LEARNS_MANIM.md`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/HERMES_LEARNS_MANIM.md).

---

Reverse reasoning pipeline
--------------------------

A normal text-to-code demo jumps from request to Python. Math-To-Manim takes the long way on purpose: it reasons backward from the final concept to the prerequisites, then walks forward through a teachable visual sequence.

The code path is explicit in [`math_to_manim/pipeline/runner.py`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/math_to_manim/pipeline/runner.py). `AnimationPipeline.generate()` runs a fixed stage chain: `IntentAgent`, `PrerequisiteGraphAgent`, `CurriculumAgent`, `MathAgent`, `StoryboardAgent`, `SceneSpecAgent`, `ManimCodeAgent`, `StaticReviewAgent`, `RenderAgent`, `VideoReviewAgent`, and `PublisherAgent`.

| Stage | Why it exists | Artifact |
| --- | --- | --- |
| Intent | Clarify what the learner is really asking. | `intent.json` |
| Reverse prerequisites | Build the knowledge graph needed before the target idea. | `knowledge_graph.json` |
| Curriculum | Turn the graph into a teachable order. | `curriculum.json` |
| Math packet | Select definitions, equations, assumptions, and examples. | `math_packet.json` |
| Storyboard | Decide the screen beats before code exists. | `storyboard.json` |
| Scene spec | Compile the visual plan into Manim objects, animations, timing, and camera notes. | `scene_spec.json` |
| Code, validation, render, review | Generate runnable Manim, gate it with static checks, render when allowed, and package the evidence. | `generated_scene.py`, reports, manifest |

[![Render validation and bounded repair loop diagram showing static review, render skip, Manim subprocess, repair from frozen scene spec, video review, and publisher package](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/render-repair-loop.svg)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/render-repair-loop.svg)

That gives every run a memory: JSON contracts, generated code, render results, review notes, and a manifest. The output is not just a video; it is an inspectable path from **question** to **understanding** to **animation**.

For current editable-video status and the planned prompt/spec/code edit loop, see the [roadmap](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/ROADMAP.md).

---

Prime Intellect RL repair loop
------------------------------

Math-To-Manim is also becoming a Prime Intellect reinforcement-learning environment. The first RL target is not "make the whole video in one shot." It is the edit move that matters after a base model produces a plausible but flawed scene: text overlaps formulas, equations are too small, the camera angle hides the point, or the zoom never lands on the symbol the learner needs to read.

A concrete target is the quantum-physics homepage-style failure mode: a beautiful Manim pass that still has text/formula collisions. The experiment is to give the model the typed scene plan, the generated Python, validation/render evidence, and a human request such as "fix the overlap," "change the POV angle," or "zoom into the formulas before the narration moves on." The policy should return a sparse code edit that preserves the scene while making the movie more readable.

[![Prime Intellect logo](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/prime-intellect/primeintellect-logo.svg)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/prime-intellect/primeintellect-logo.svg)

[![Diagram of the Math-To-Manim Prime Intellect RL repair loop from generated Manim code through static reward checks back to corrected renderable Manim Python](https://github.com/HarleyCoops/Math-To-Manim/raw/main/docs/assets/prime-intellect/m2m2-prime-rl-loop.svg)](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/prime-intellect/m2m2-prime-rl-loop.svg)

|  |  |  |
| --- | --- | --- |
| [Prime Intellect lab field visual, used here to represent the environment task space](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/prime-intellect/primeintellect-lab.png) | [Prime Intellect reward hacking visual, used here to represent reward design pressure](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/prime-intellect/primeintellect-reward-hacking-cover.png) | [Prime Intellect compute corridor visual, used here to represent hosted training and inference](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/assets/prime-intellect/primeintellect-compute-bg.png) |
| **Run bundle as environment** | **Reward function as critic** | **Policy update as repair engine** |

The current hub environment is `harleycooper/math-to-manim`. A repair task carries the original prompt, typed `scene_spec`, generated Manim Python, static-validation report, and render/recovery evidence when available. The model must return one strict `GeneratedCode` JSON block. The Verifiers reward checks whether the proposed code parses, defines the expected Manim scene, avoids unsafe imports and calls, preserves expected math terms, and reduces obvious text/layout crowding hazards.

```
generated_scene.py + scene_spec + validation/render evidence
  -> Prime Intellect Verifiers environment
  -> model proposes corrected GeneratedCode JSON
  -> static reward checks parseability, scene shape, safety, terms, layout
  -> hosted RL updates the repair policy
  -> corrected, renderable Manim Python flows back into M2M2 recovery
```

That keeps the fast RL loop text-and-AST based while the slower Manim renderer remains the audit gate. The intended result is a model that learns the house style of this repo: cinematic but readable scenes, sparse formulas, staged captions, safe Manim code, and edits that can respond to text or voice change requests without throwing away the whole movie.

Current hosted-training status: the environment action passes on Prime, the hub package is published as `harleycooper/math-to-manim@0.1.1`, a 1-step smoke completed, and a 25-step W&B-enabled pilot has been launched on `Qwen/Qwen3.5-35B-A3B`.

See the full integration notes in [`docs/PRIME_INTELLECT_RL.md`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/PRIME_INTELLECT_RL.md).

---

Windows PowerShell:

```
git clone https://github.com/HarleyCoops/Math-To-Manim.git
cd Math-To-Manim
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e ".[dev]"
python -m pytest
```

macOS / Linux / WSL:

```
git clone https://github.com/HarleyCoops/Math-To-Manim.git
cd Math-To-Manim
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
python -m pytest
```

### 2. Run a no-API smoke test

This proves the CLI, artifact contracts, and validators are wired before you spend model or render time:

```
math-to-manim generate "Explain why derivatives are slopes" --deterministic --no-render
```

Equivalent module form:

```
python -m math_to_manim.cli generate "Explain why derivatives are slopes" --deterministic --no-render
```

### 3. Generate with model calls

Set an OpenAI key and choose a model if desired:

```
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="gpt-4.1"
math-to-manim generate "Explain Fourier epicycles as rotating vectors" --no-render
```

PowerShell:

```
$env:OPENAI_API_KEY = "sk-..."
$env:OPENAI_MODEL = "gpt-4.1"
math-to-manim generate "Explain Fourier epicycles as rotating vectors" --no-render
```

### 4. Install render extras when you want MP4 output

Python render dependency:

```
python -m pip install -e ".[dev,render]"
```

System render dependencies are also needed for real Manim output, especially FFmpeg and LaTeX for `MathTex`. On Debian/Ubuntu/WSL:

```
./scripts/bootstrap-render.sh
```

The package list lives in [`requirements-system.txt`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/requirements-system.txt).

---

Math-To-Manim can keep the typed planning pipeline while sending the Manim codegen and repair loop through a locally authenticated Codex CLI session.

Check Codex first:

```
codex --version
codex exec "Say ready from inside this repo"
```

Then route codegen through Codex:

```
math-to-manim generate "Explain derivatives as slopes with a cinematic tangent-line reveal" \
  --codegen-provider codex-cli \
  --codex-full-auto \
  --style cinematic \
  --quality l
```

Earlier planning stages remain on the typed adapters; only the generated-code and repair stages move first. That makes the migration incremental instead of all-or-nothing.

---

A generation writes a self-contained run bundle:

```
runs/<run_id>/
  request.json
  intent.json
  knowledge_graph.json
  curriculum.json
  math_packet.json
  storyboard.json
  scene_spec.json
  generated_code.json
  generated_scene.py
  validation_report.json
  render_result.json
  review_report.json
  trace.jsonl  # stage-boundary events when tracing is enabled
  recovery_manifest.json  # after recover-render
  draft_review/
    draft_review.md
    contact_sheet.png
    frames/
  animation_package.json
  manifest.json
```

After editing `generated_scene.py` inside a run bundle, rerun the recovery path:

```
math-to-manim recover-render runs/<run_id> --quality l
```

That command refreshes validation, render, review, draft-review assets, and
`recovery_manifest.json` without regenerating upstream planning artifacts.

Package layout:

```
math_to_manim/
  agents/      # stage adapters
  schemas/     # versioned artifact contracts
  tools/       # graph, validation, rendering, video, artifact helpers
  pipeline/    # orchestration, tracing, repair loop
  rendering/   # Manim and FFmpeg wrappers
  review/      # static and visual review scoring
```

---

Sixteen curated GIFs are tracked under [`docs/showcase/assets/`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/showcase/assets) as the **art direction target** for Math-To-Manim's visual explanations.

|  |  |  |
| --- | --- | --- |
| [Rhombicosidodecahedron](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/showcase/README.md) | [Hopf fibration](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/showcase/README.md) | [Lorenz attractor](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/showcase/README.md) |
| **Geometry as spectacle** | **Topology as choreography** | **Chaos as intuition** |

See the full gallery with descriptions: **[`docs/showcase/README.md`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/showcase/README.md)**.

### Make a README-sized GIF from a render

```
MP4="media/videos/your_scene/480p15/YourScene.mp4"

ffmpeg -y -ss 95 -t 24 -i "$MP4" \
  -vf "fps=12,scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=96[p];[s1][p]paletteuse=dither=bayer:bayer_scale=5" \
  docs/showcase/assets/your-clip.gif
```

Adjust `-ss` and `-t` to capture the teaching beat you want.

---

MIT.