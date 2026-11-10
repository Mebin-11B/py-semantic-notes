---
title: "Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting"
url: https://github.com/moongate-community/moongatev2
clipped: 2026-06-17 01:36:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Game Emulation
  - .NET 10
  - C#
  - Lua Scripting
  - MessagePack
  - Spatial World Database
related:
  - "[[Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc]]"
  - "[[LÖVE 2D Game Framework for Lua]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Moongate v2 is a modern Ultima Online server emulator written in C# targeting .NET 10, featuring Native AOT, snapshot journaling, and Lua scripting.
>
> **Key points:**
> - Implements a modular architecture with a deterministic game-loop and source-generated packet processing.
> - Uses Lua scripting to dynamically manage commands, dialogues, speech, and user interface gumps.
> - Persists world data using MessagePack-serialized snapshotting and append-only journaling.
> - Employs a chunk/sector-based spatial model for lazy loading and optimized map entity updates.
>
> **Concept links:** [[Game Emulation]], [[.NET 10]], [[C#]], [[Lua Scripting]], [[MessagePack]], [[Spatial World Database]]
>
> **Suggested connections:**
> - [[Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc]] — related performance runtime migrations.
> - [[LÖVE 2D Game Framework for Lua]] — related Lua-based game development.
<!-- ai-summary:end -->

# [Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting](https://github.com/moongate-community/moongatev2)

## Digest Summary
Moongate v2 is a modern Ultima Online server written in C# targeting .NET 10 with Native AOT support. It emphasizes a clean, modular architecture, deterministic timestamp‑driven game‑loop, strong packet tooling, and unit‑tested core services. The server provides TCP connection handling, attribute‑based packet registration (source‑generated), inbound/outbound message buses, domain event dispatch, and a Lua scripting runtime for commands, speech, and gumps. Persistence uses a snapshot + append‑only journal serialized via MessagePack‑CSharp source‑generated contracts, with file‑locking and Z‑Linq query support. World data are streamed by 16×16 sector chunks, lazily loaded and synchronized on player login or sector changes, offering predictable memory growth and cache‑friendly entity queries. A lightweight HTTP host exposes health, metrics and OpenAPI docs; minimal SMTP email delivery uses Scriban templates. Recent work migrated persistence to MessagePack for AOT stability, split outbound packet sending to a dedicated thread, optimized hot paths, and added Lua GM commands. Missing features include full combat, skill progression, NPC AI, economy systems, and complete UO protocol coverage. Configuration is fully overridable via MOONGATE_ environment variables.

## Discussion Summary
The comments express strong enthusiasm for the Ultima Online emulator project, recalling nostalgia for the original game and praising the clean architecture, sector‑based syncing, and use of .NET, Lua, and NativeAOT. Contributors note related experiences with other emulators, offer technical suggestions such as AI integration, and ask about client compatibility and packet handling. Minor concerns appear about legal exposure and the appropriateness of the term “server emulator,” but overall the tone is supportive and interested in collaborative development.

---

## Full Article

[![Moongate logo](https://github.com/moongate-community/moongate/raw/main/images/moongate_logo.png)](https://github.com/moongate-community/moongate/blob/main/images/moongate_logo.png)

[![.NET 10](https://camo.githubusercontent.com/7d4a6208fe54f84175e09badaa00dd99f4acc25a28143a515a4ddfeb07ad5790/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d2e4e455425323031302d626c756576696f6c6574)](https://camo.githubusercontent.com/7d4a6208fe54f84175e09badaa00dd99f4acc25a28143a515a4ddfeb07ad5790/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d2e4e455425323031302d626c756576696f6c6574)
[![Lua Scripting](https://camo.githubusercontent.com/e03d91ded1a254505ccbcce8efded7dceeb34f3f65f3ef91e820161c0ad74406/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f736372697074696e672d4c75612d79656c6c6f77)](https://camo.githubusercontent.com/e03d91ded1a254505ccbcce8efded7dceeb34f3f65f3ef91e820161c0ad74406/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f736372697074696e672d4c75612d79656c6c6f77)
[![GPL-3.0 License](https://camo.githubusercontent.com/a8f839e5e0d6bc584a8c8bd13dedd9134b8ec7897907d51f7741182d744f3b81/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d47504c2d2d332e302d626c7565)](https://camo.githubusercontent.com/a8f839e5e0d6bc584a8c8bd13dedd9134b8ec7897907d51f7741182d744f3b81/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d47504c2d2d332e302d626c7565)

[![CI](https://github.com/moongate-community/moongate/actions/workflows/ci.yml/badge.svg)](https://github.com/moongate-community/moongate/actions/workflows/ci.yml)
[![Tests](https://camo.githubusercontent.com/bb97396c66feeeb164ad8e9f2111e44f4b9aa2c70ae10254df1ddeca1477d330/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6d6f6f6e676174652d636f6d6d756e6974792f6d6f6f6e676174652f67682d70616765732f6261646765732f74657374732e6a736f6e)](https://github.com/moongate-community/moongate/actions/workflows/ci.yml)
[![Coverage](https://camo.githubusercontent.com/1379df7c848ac27dbaa79a58c238a7198d926fda1de90d93175bbb630048ffdf/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6d6f6f6e676174652d636f6d6d756e6974792f6d6f6f6e676174652f67682d70616765732f6261646765732f636f7665726167652e6a736f6e)](https://github.com/moongate-community/moongate/actions/workflows/coverage.yml)
[![FOSSA Status](https://camo.githubusercontent.com/1e450c5e0969b7e464d8f7a601a0534cd5bbe119575e980e05cf484c6373efea/68747470733a2f2f6170702e666f7373612e636f6d2f6170692f70726f6a656374732f6769742532426769746875622e636f6d2532466d6f6f6e676174652d636f6d6d756e6974792532466d6f6f6e676174652e7376673f747970653d736d616c6c)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmoongate-community%2Fmoongate?ref=badge_small)
[![Docker Image](https://camo.githubusercontent.com/df8b156d242b7b090d0a678387dab2cd97ec5e10d1d416771d25249f11f8bd10/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f762f746769616368692f6d6f6f6e676174653f736f72743d73656d766572)](https://hub.docker.com/r/tgiachi/moongate)

Moongate v2 is a modern Ultima Online server built with .NET 10, deterministic game-loop processing, Lua scripting, and a
chunk/sector-based spatial world model.

[![FOSSA Status](https://camo.githubusercontent.com/537e205df79e819faa3271b0b21ca45a14f05fafec913a135352ac25ebc62f28/68747470733a2f2f6170702e666f7373612e636f6d2f6170692f70726f6a656374732f6769742532426769746875622e636f6d2532466d6f6f6e676174652d636f6d6d756e6974792532466d6f6f6e676174652e7376673f747970653d6c61726765)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmoongate-community%2Fmoongate?ref=badge_large)

Looking for Collaborators
-------------------------

I am actively looking for contributors and reviewers.

* Pull requests run the `CI` workflow only, to keep feedback fast.
* Coverage, security audit, and third-party notices run on `main`, with scheduled/manual execution for the heavier audits.
* GitHub releases are mirrored to Discord via the `GitHub Release Assets` workflow.
* Configure the repository secret `DISCORD_CHANGELOG_WEBHOOK_URL` to enable changelog posting.
* Release notes are sourced from `CHANGELOG.md`, include a generated contributors section, and are posted to Discord after
  the GitHub release is created.
* NuGet packages are published by the `NuGet Publish` workflow.
* Configure the repository secret `NUGET_KEY` to enable publishing to `nuget.org`.
* The NuGet publish flow also ships `Moongate.Templates`, which provides `dotnet new moongate-plugin`, and
  `Moongate.TemplateValidator`, which provides `moongate-template`.

* .NET SDK 10.0+
* Ultima Online data files (client)

```
git clone https://github.com/moongate-community/moongate.git
cd moongate
dotnet run --project src/Moongate.Server -- --root-directory ~/moongate --uo-directory ~/uo
```

Run this every time you change shard template data under your Moongate root, especially `~/moongate/templates/items`,
`~/moongate/templates/mobiles`, `~/moongate/templates/loot`, `~/moongate/templates/factions`,
`~/moongate/templates/sell_profiles`, or `~/moongate/data/containers`.

Install the validator tool from `nuget.org`:

```
dotnet tool install --global Moongate.TemplateValidator
```

Run the validator:

```
moongate-template validate --root-directory ~/moongate
```

Each validation run prints the validator version and the target root directory before the validation summary.

Update an existing global installation:

```
dotnet tool update --global Moongate.TemplateValidator
```

If you are developing inside this repository and want to install from a locally packed artifact instead:

```
dotnet pack tools/Moongate.TemplateValidator/Moongate.TemplateValidator.csproj -o ./tools/Moongate.TemplateValidator/nupkg
dotnet tool install --tool-path ./artifacts/template-tool --add-source ./tools/Moongate.TemplateValidator/nupkg Moongate.TemplateValidator
```

Run the local installation:

```
./artifacts/template-tool/moongate-template validate --root-directory ~/moongate
```

Published docs: `docs/articles/operations/template-validation.md`

### Run Server (Docker quick start)

```
git clone https://github.com/moongate-community/moongate.git
cd moongate
docker build -t moongate:local .
docker run --rm -it \
  -p 2593:2593 \
  -p 8088:8088 \
  -v "$HOME/moongate:/app/moongate" \
  -v "$HOME/uo:/app/uo" \
  moongate:local
```

Server port: `2593`
UDP ping port: `12000`
HTTP/UI API port: `8088`

Transport encryption:

* Moongate supports both plain and encrypted UO clients.
* Recommended default: `game.encryptionMode = "Both"` in `moongate.json`.
* Operational details and handshake behavior: `docs/articles/networking/client-encryption.md`

Default credentials: `admin` / `password`
Change them immediately from the server console with `.password`.

Player portal routes:

* Dev UI: `http://localhost:5173/portal/login`
* Embedded UI: `http://localhost:8088/portal/login`
* Authenticated profile: `http://localhost:8088/portal/profile`

```
cd ui
npm install
npm run dev
```

UI default URL: `http://localhost:8088/`

* UO TCP server + packet pipeline
* Deterministic single game-loop with separate network inbound/outbound workers
* Source-generated packet/command/listener registration
* Sector/chunk spatial system with lazy warmup and broadcast radius
* Registry-driven snapshot buckets + journal persistence over MemoryPackable runtime entities
* Lua scripting runtime for commands, gumps, item/mobile behavior
* Startup-loaded C# plugins from the runtime `plugins/<plugin-id>/` directory
* Classic books rendered from `moongate_data/templates/books/*.txt`, with support for both read-only content and writable
  books (`0x93` header saves, `0x66` page saves)
* HTTP admin API + OpenAPI for tooling/UI
* Web admin UI (`ui/`) for item templates and server/admin workflows
* Player portal for authenticated account overview, profile editing, and password change (`/portal/login`, `/portal/profile`,
  `/api/portal/me`, `/api/portal/me/password`)

* Spatial model is sector-first (chunk-style), not pure repeated range scans.
* World generation pipeline uses named generators (`IWorldGenerator`) and command-triggered runs (example: doors).
* Doors support runtime open/close behavior and network updates.
* Persistence uses MemoryPack with registry-driven snapshot buckets and generic journal entries.
* Mobile domain model was refactored to remove `Level` and `Experience` from `UOMobileEntity` (they are not part of the base
  UO mobile model).

* **UI Screen 1**: login and initial admin entry point.
  [![UI Screen 1](https://github.com/moongate-community/moongate/raw/main/images/ui/ui_screen1.png)](https://github.com/moongate-community/moongate/blob/main/images/ui/ui_screen1.png)
* **UI Screen 2**: authenticated dashboard and main navigation.
  [![UI Screen 2](https://github.com/moongate-community/moongate/raw/main/images/ui/ui_screen2.png)](https://github.com/moongate-community/moongate/blob/main/images/ui/ui_screen2.png)
* **UI Screen 3**: item templates search with image previews.
  [![UI Screen 3](https://github.com/moongate-community/moongate/raw/main/images/ui/ui_screen_3.png)](https://github.com/moongate-community/moongate/blob/main/images/ui/ui_screen_3.png)

* **Character Creator at Docks**: character creation flow and initial spawn area.
  [![Character Creator at Docks](https://github.com/moongate-community/moongate/raw/main/images/screenshots/screen_creator_at_docks.png)](https://github.com/moongate-community/moongate/blob/main/images/screenshots/screen_creator_at_docks.png)
* **Door Open/Close Fix**: the bug is still there (damn doors).
  [![Door Open/Close Fix](https://github.com/moongate-community/moongate/raw/main/images/screenshots/screen_door_bug.png)](https://github.com/moongate-community/moongate/blob/main/images/screenshots/screen_door_bug.png)
* **Orion Lua Brain**: scripted NPC behavior example (`orion.lua`) with speech loop (my cat is always hungry and always
  looking for food).
  [![Orion Lua Brain](https://github.com/moongate-community/moongate/raw/main/images/screenshots/screen_orione_hungry_cat.png)](https://github.com/moongate-community/moongate/blob/main/images/screenshots/screen_orione_hungry_cat.png)
* **Teleport Gump**: Lua-driven teleport UI and location workflow.
  [![Teleport Gump](https://github.com/moongate-community/moongate/raw/main/images/screenshots/screen_teleport_gump.png)](https://github.com/moongate-community/moongate/blob/main/images/screenshots/screen_teleport_gump.png)

* Docs home: `docs/index.md`
* Getting started: `docs/articles/getting-started/`
* Architecture: `docs/articles/architecture/`
* Beginner content authoring: `docs/articles/scripting/create-your-first-content.md`
* Beginner systems path: `docs/articles/scripting/create-your-first-systems.md`
* Scripting: `docs/articles/scripting/` including authored dialogues, quests, public moongates, scheduled events, starting loadout, and loot containers
* Persistence: `docs/articles/persistence/`
* Networking/protocol: `docs/articles/networking/` including client encryption and the UDP ping server
* Operations: `docs/articles/operations/` including template validation, in-game item admin commands, and help ticket workflow

Published docs: <https://moongate-community.github.io/moongate/>

* Benchmarks project: `benchmarks/Moongate.Benchmarks`
* Cross-map teleport cold-destination benchmark: `TeleportMapChangeBenchmark.HandleCrossMapTeleport_ColdDestination`
* Same-map teleport cold-destination benchmark with self refresh:
  `TeleportMapChangeBenchmark.HandleSameMapTeleport_ColdDestination_WithSelfRefresh`
  + Dry run on Apple M4 Max / .NET 10:
    - cross-map median `2.850 ms`, mean `4.284 ms`, first cold outlier `19.939 ms`, allocated `1.85 MB`
    - same-map median `1.947 ms`, mean `2.908 ms`, first cold outlier `13.514 ms`, allocated `1.22 MB`
* Intelligent NPC dialogue scheduling benchmark: `NpcDialogueSchedulingBenchmark`
  + Dry run on Apple M4 Max / .NET 10:
    - queue listener median `2.729 us`, mean `183.0 us`, first cold outlier `2.133 ms`, allocated `592 B`
    - schedule and complete median `1.170 ms`, mean `1.258 ms`, first cold outlier `2.169 ms`, allocated `1552 B`
    - reject duplicate in-flight median `1.270 ms`, mean `1.073 ms`, first cold outlier `2.696 ms`, allocated `1288 B`
* Black-box socket stress tool: `tools/Moongate.Stress`
* Guide: `docs/articles/operations/stress-test.md`
* Packet handler performance guide: `docs/articles/networking/packet-handler-performance.md`

Moongate v2 is inspired by the UO emulator ecosystem.

Special thanks:

Data imported/adapted from ModernUO distribution is used in selected world datasets (decoration, locations, signs).

[![Star History Chart](https://camo.githubusercontent.com/445330f2703dd5eeb0c784ff3396c3cb996153e4b178c37f1e110f52ac57a570/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f696d6167653f7265706f733d6d6f6f6e676174652d636f6d6d756e6974792f6d6f6f6e6761746526747970653d64617465266c6567656e643d746f702d6c656674)](https://www.star-history.com/?repos=moongate-community%2Fmoongate&type=date&legend=top-left)
[![FOSSA Status](https://camo.githubusercontent.com/474491091fa59f4c5020de8b971dd14cca63556dcbb7b1ca49b8c5542c9434b2/68747470733a2f2f6170702e666f7373612e636f6d2f6170692f70726f6a656374732f6769742532426769746875622e636f6d2532466d6f6f6e676174652d636f6d6d756e6974792532466d6f6f6e676174652e7376673f747970653d736869656c64)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmoongate-community%2Fmoongate?ref=badge_shield)

Contributions are welcome. Please open an issue/discussion first for non-trivial changes.

* Follow `CODE_CONVENTION.md`
* Keep tests green
* Keep docs aligned with runtime behavior

GPL-3.0. See `LICENSE`.