---
title: "Uv is fantastic, but its package management UX is a mess"
url: https://www.loopwerk.io/articles/2026/uv-ux-mess/
clipped: 2026-06-17 00:59:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Uv is fantastic, but its package management UX is a mess](https://www.loopwerk.io/articles/2026/uv-ux-mess/)

## Digest Summary
The article praises uv’s speed and unified toolchain handling but critiques its package‑management user experience. uv lacks a dedicated “outdated” command; users must run `uv tree --outdated --depth 1`, which prints the full dependency tree and forces manual scanning for updates. Unlike pnpm and Poetry, which add caret or range constraints (e.g., `^1.23.4` or `>=1.23.4,<2.0.0`) that limit upgrades to compatible minor versions, uv’s default adds only a lower bound (`>=2.13.4`), permitting unrestricted major‑version jumps and making bulk updates unsafe. The upgrade workflow is cumbersome: a full lockfile upgrade uses `uv lock --upgrade` (a “nuclear” operation), while updating specific packages requires repeatedly adding `--upgrade-package` flags. A recent `--bounds` option can enforce upper limits (e.g., `--bounds major`), but it is preview‑only and must be typed for each addition. The author calls for a true `uv outdated` command, a more ergonomic update syntax, and default version constraints that respect semantic versioning to make maintenance comparable to pnpm or Poetry.

## Discussion Summary
Comments show a mixed but generally appreciative view of uv: many acknowledge its speed, single‑resolution design and intentional omission of upper bounds as sensible trade‑offs for Python’s ecosystem, while also noting that this can cause friction for users accustomed to other tools. Several participants suggest clearer commands for upgrades, outdated checks, and automatic script handling, and some compare uv’s ergonomics unfavorably to pip, Poetry, or npm. Overall, the community values uv’s core benefits but calls for improved UX, documentation, and optional features to address the highlighted pain points.

---

## Full Article

uv is fantastic, but its package management UX is a mess
========================================================

![Hero image](https://www.loopwerk.io/articles/heroes/2026-05-21-uv-ux-mess-1480w.webp)

UPDATE

**May 22, 2026:** This article hit the Hacker News front page. Readers pointed out a couple of things Iâd missed and one bit of framing I should have been clearer about. See the [Corrections and clarifications](https://www.loopwerk.io/articles/2026/uv-ux-mess/#corrections-and-clarifications) section at the bottom.

Astralâs [uv](https://docs.astral.sh/uv/) has taken the Python world by storm, and for good reason. It is blisteringly fast, handles Python versions with ease, and replaces a half-dozen tools with a single binary. Iâve written [multiple articles](https://www.loopwerk.io/articles/tag/uv/) about it before.

Getting started with a new Python project using uv and adding your first dependencies is very easy. But once you move past the initial setup and into the maintenance phase of a project, i.e. checking for outdated packages and performing routine upgrades, the CLI starts to feel surprisingly clunky compared to its peers like pnpm or Poetry.

Finding outdated packages
-------------------------

In my JavaScript projects, if I want to see what needs an update, I run:

```
$ pnpm outdated
```

This gives a clean, concise list of outdated packages, their current version, the latest version, and the version allowed by your constraints.

In uv, there is no `uv outdated`. Instead, you have to memorize the following mouthful:

```
$ uv tree --outdated --depth 1
```

The output is also a problem. It doesnât just show you what is outdated; it shows you your entire top-level dependency tree, with a small annotation next to the ones that have updates available. If you have 50 dependencies and only two are outdated, you still have to scan a 50-line list.

Poetry isnât much better with its command `poetry show --outdated`, but at least it only shows actual outdated packages.

Unsafe version constraints by default
-------------------------------------

This is the most significant philosophical departure uv takes from pnpm and Poetry, and itâs a dangerous one for production stability.

### How pnpm/Poetry handle it

When you add a package using `pnpm add`, it writes it to `package.json` using the caret requirement (`^1.23.4`). The caret at the beginning means that any 1.x.x version is allowed, but it will not update to 2.0.0.

Poetry does the same by default, using a format like `>=1.23.4,<2.0.0`. I find this less readable than `^1.23.4`, but the effect is the same.

In both cases, **updates are safe by default**. You can run `pnpm update` or `poetry update` every morning and have high confidence that your build wonât break due to a major API change (assuming the packages you depend on respect SemVer).

### How uv handles it

When you run `uv add pydantic`, it inserts this into your `pyproject.toml`:

```
dependencies = [
    "pydantic>=2.13.4",
]
```

Note the lack of an upper bound. In the eyes of uv, pydantic version 2, 3, and 100 are all perfectly acceptable.

This means uv updates are **unsafe by default**. If you run a bulk update, you arenât just getting bug fixes; you are opting into every breaking change published by every maintainer in your dependency graph.

The bad UX of the upgrade command
---------------------------------

The commands to actually perform an update in uv feel like they were designed for machines rather than humans.

If you want to update everything in pnpm or Poetry, itâs a simple `pnpm update` or `poetry update` command. In uv, you use:

```
$ uv lock --upgrade
```

THOUGHTS

Why isnât this simply `uv update` or `uv upgrade`? Who designed this command line interface? Itâs not `uv lock --add` or `uv lock --remove` either!

Because of the âno upper boundsâ issue mentioned above, `uv lock --upgrade` is a nuclear option. It will upgrade every single package in your lockfile to their absolute latest versions, ignoring SemVer safety. And this includes deep, nested dependencies youâve never heard of! Good luck, better hope there are no breaking changes anywhere.

Once you realize this is too risky, youâll want to upgrade only specific packages. After scouring the subpar output of `uv tree --outdated --depth 1` to find them, the syntax becomes a repetitive chore.

How pnpm does it:

```
$ pnpm update pydantic httpx uvicorn
```

How uv does it:

```
$ uv lock --upgrade-package pydantic --upgrade-package httpx --upgrade-package uvicorn
```

Having to repeat the `--upgrade-package` flag for every single item is a huge hassle when you want to update a bunch of packages. I donât understand why the UX of uvâs commands is so poor.

There is hope: the bounds flag
------------------------------

Luckily uv has recently introduced a `--bounds` option for `uv add`:

```
$ uv add pydantic --bounds major
```

This produces the safer `pydantic>=2.13.4,<3.0.0` constraint weâve come to expect. However, this is currently an opt-in feature. You have to remember to type it every time, and as of now, it is considered a preview feature.

Until `--bounds major` (or a similar configuration) becomes the default behavior, uv users are essentially forced to choose between two bad options:

1. Manually edit `pyproject.toml` to add upper bounds for every single dependency.
2. Live in fear that `uv lock --upgrade` will accidentally pull in a breaking major version change.

What Iâd like to see
----------------------

I love uv. Its speed is transformative, and the way it manages Python toolchains is second to none. But as a package manager, the developer experience for maintaining a project is currently a step backward from the tools that came before it.

We need a dedicated `uv outdated` command that filters noise, a more ergonomic `update` command that doesnât require repeating flags, and default version constraints that respect the sanity of Semantic Versioning.

Until then, Iâll be double-checking every single line of my lockfile changes with a healthy dose of suspicion.

Corrections and clarifications
------------------------------

After this article hit Hacker News, readers pointed out two things Iâd missed and one bit of framing I should have been clearer about up front.

1. Use `uv pip list --outdated` instead of `uv tree --outdated --depth 1`. The `uv pip` command actually filters to only outdated packages, which makes the âFinding outdated packagesâ critique much weaker than I made it out to be. The remaining complaint is that this lives under the pip-compatibility namespace rather than as a first-class top-level command, which is a discoverability issue, not a noisy-output one.
2. You *can* set the `--bounds` default in `pyproject.toml`. You donât have to remember to type `--bounds major` on every `uv add`. You can set it once:

   ```
   [tool.uv]
   add-bounds = "major"
   ```

   This invalidates the âtwo bad optionsâ framing in the bounds-flag section. The actual situation is closer to: set this once in your config, and you get sensible defaults from then on. Itâs still a preview feature, and for applications it would be better as the default, but the ergonomics are not nearly as bad as I painted them.
3. Scope: applications vs. libraries. The standard Python packaging advice is that *libraries* published to PyPI should not pin upper bounds, and that advice is correct. If every library pins upper bounds, downstream consumers end up with dependency trees that canât resolve. But for *applications*, where you are the terminal node in the dependency graph and nobody resolves against your constraints, the calculus is reversed: upper bounds cost you nothing and protect you from surprise major version bumps. This article is about maintaining applications (websites, services, internal tools), not publishing libraries. I should have been explicit about that from the start, because the âno upper boundsâ default is indeed reasonable for the library case.