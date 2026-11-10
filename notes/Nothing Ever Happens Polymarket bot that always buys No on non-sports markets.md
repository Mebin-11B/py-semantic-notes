---
title: "Nothing Ever Happens: Polymarket bot that always buys No on non-sports markets"
url: https://github.com/sterlingcrispin/nothing-ever-happens
clipped: 2026-06-17 01:17:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Nothing Ever Happens: Polymarket bot that always buys No on non-sports markets](https://github.com/sterlingcrispin/nothing-ever-happens)

## Digest Summary
The repository implements an asynchronous Python bot for Polymarket that automatically buys “No” on standalone yes/no markets for entertainment purposes.  

**Structure**  
- `bot/`: runtime, exchange clients (live or `PaperExchangeClient`), dashboard, recovery logic, and the `nothing_happens` strategy.  
- `scripts/`: helpers for deployed instances and local inspection (e.g., DB stats, export, wallet history, log parsing).  
- `tests/`: unit and regression tests.  

**Operation**  
- Scans markets, selects “No” entries below a configurable price cap, tracks open positions, provides a web dashboard, and persists state for recovery.  
- Live trading requires `BOT_MODE=live`, `LIVE_TRADING_ENABLED=true`, `DRY_RUN=false`, plus `PRIVATE_KEY`, `FUNDER_ADDRESS`, `DATABASE_URL`, and `POLYGON_RPC_URL`. Missing variables default to the paper client.  

**Setup & Deployment**  
- Install with `pip install -r requirements.txt`; copy `config.example.json` → `config.json` and `.env.example` → `.env`.  
- Runtime reads `config.json` (non‑secret) and `.env` (secrets); alternative config via `CONFIG_PATH`.  
- Dashboard binds `$PORT` or `DASHBOARD_PORT`.  
- Heroku deployment uses environment variables and runs only a web dyno; a worker dyno exists solely to fail fast.  

Local configuration, ledgers, and export artifacts are ignored by default.

## Discussion Summary
Comments show a mixed view of the “always‑no” prediction‑market bot. Many describe it as an amusing meme or academic experiment rather than a reliable profit source, noting that frequent small wins can be offset by occasional large losses and that the implied edge may already be priced in. Skepticism centers on the lack of transparent performance data, the risk of long‑tail events, and the idea that widespread use would erode any advantage. A few users point to similar bots on non‑real‑money platforms as modestly successful, while others highlight the broader informational value of prediction markets despite these concerns.

---

## Full Article

Nothing Ever Happens Polymarket Bot
===================================

Focused async Python bot for Polymarket that buys No on standalone non-sports yes/no markets.

*FOR ENTERTAINMENT ONLY. PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USE AT YOUR OWN RISK. THE AUTHORS ARE NOT LIABLE FOR ANY CLAIMS, LOSSES, OR DAMAGES.*

[![Dashboard screenshot](https://github.com/sterlingcrispin/nothing-ever-happens/raw/main/docs/dashboard.jpg)](https://github.com/sterlingcrispin/nothing-ever-happens/blob/main/docs/dashboard.jpg)

* `bot/`: runtime, exchange clients, dashboard, recovery, and the `nothing_happens` strategy
* `scripts/`: operational helpers for deployed instances and local inspection
* `tests/`: focused unit and regression coverage

The bot scans standalone markets, looks for NO entries below a configured price cap, tracks open positions, exposes a dashboard, and persists live recovery state when order transmission is enabled.

The runtime is `nothing_happens`.

Real order transmission requires all three environment variables:

* `BOT_MODE=live`
* `LIVE_TRADING_ENABLED=true`
* `DRY_RUN=false`

If any of those are missing, the bot uses `PaperExchangeClient`.

Additional live-mode requirements:

* `PRIVATE_KEY`
* `FUNDER_ADDRESS` for signature types `1` and `2`
* `DATABASE_URL`
* `POLYGON_RPC_URL` for proxy-wallet approvals and redemption

```
pip install -r requirements.txt
cp config.example.json config.json
cp .env.example .env
```

`config.json` is intentionally local and ignored by git.

The runtime reads:

* `config.json` for non-secret runtime settings
* `.env` for secrets and runtime flags

The runtime config lives under `strategies.nothing_happens`. See [config.example.json](https://github.com/sterlingcrispin/nothing-ever-happens/blob/main/config.example.json) and [.env.example](https://github.com/sterlingcrispin/nothing-ever-happens/blob/main/.env.example).

You can point the runtime at a different config file with `CONFIG_PATH=/path/to/config.json`.

The dashboard binds `$PORT` or `DASHBOARD_PORT` when one is set.

The shell helpers use either an explicit app name argument or `HEROKU_APP_NAME`.

```
export HEROKU_APP_NAME=<your-app>
./alive.sh
./logs.sh
./live_enabled.sh
./live_disabled.sh
./kill.sh
```

Generic deployment flow:

```
heroku config:set BOT_MODE=live DRY_RUN=false LIVE_TRADING_ENABLED=true -a "$HEROKU_APP_NAME"
heroku config:set PRIVATE_KEY=<key> FUNDER_ADDRESS=<addr> POLYGON_RPC_URL=<url> DATABASE_URL=<url> -a "$HEROKU_APP_NAME"
git push heroku <branch>:main
heroku ps:scale web=1 worker=0 -a "$HEROKU_APP_NAME"
```

Only run the `web` dyno. The `worker` entry exists only to fail fast if it is started accidentally.

| Script | Purpose |
| --- | --- |
| `scripts/db_stats.py` | Inspect live database table counts and recent activity |
| `scripts/export_db.py` | Export live tables from `DATABASE_URL` or a Heroku app |
| `scripts/wallet_history.py` | Pull positions, trades, and balances for the configured wallet |
| `scripts/parse_logs.py` | Convert Heroku JSON logs into readable terminal or HTML output |

Local config, ledgers, exports, reports, and deployment artifacts are ignored by default.