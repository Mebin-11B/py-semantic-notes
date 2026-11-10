---
title: "Minecraft: Java Edition now uses SDL3"
url: https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4
clipped: 2026-08-31 12:23:00
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Minecraft: Java Edition now uses SDL3](https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4)

## Digest Summary
Minecraft 26.3 Snapshot 4 introduces several core updates:

- **Platform integration:** Window management, input, and platform handling have moved from GLFW to SDL 3. Keyboard input now uses SDL scancodes and keycodes; raw mouse input is removed, and relative mouse mode is always active.
- **UI adjustments:** Borderless fullscreen becomes the default, can toggle without restart, and exclusive fullscreen is dropped on macOS. Minimum window size is 320×240, and Wayland is preferred on Linux. Debug overlay gains a separate GUI scale, player‑speed readout, and refresh‑rate display.
- **Gameplay additions:** Spectator mode can interact with portals. New item components include `minecraft:cooking_fuel`, `minecraft:brewing_fuel`, `minecraft:sign_text_front/back`, `minecraft:waxed`, `minecraft:cushion/color`, `minecraft:villager_food`, and `minecraft:mob_visibility`. Armadillos no longer roll up in liquids.
- **Technical changes:** Data pack version → 111.0, resource pack version → 92.0. Loot‑table fields now accept registry elements, tags, and inline values; numerous advancement, trigger, and slot‑source schemas were tightened. Signs no longer auto‑execute click events; a boolean `allow_op_features` restores previous behavior.
- **World‑gen & environment:** Added `minecraft:gameplay/natural_mob_spawns` and `minecraft:gameplay/creature_world_gen_spawn_probability` attributes. Known issues include crashes in exclusive fullscreen on Windows (multi‑monitor) and Wayland.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
> You can view the original article page directly [here](https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4).
