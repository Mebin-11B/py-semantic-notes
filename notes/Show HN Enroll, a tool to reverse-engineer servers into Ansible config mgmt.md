---
title: "Show HN: Enroll, a tool to reverse-engineer servers into Ansible config mgmt"
url: https://enroll.sh
clipped: 2026-06-17 02:05:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Enroll, a tool to reverse-engineer servers into Ansible config mgmt](https://enroll.sh)

## Digest Summary
Enroll is a tool for reverse‑engineering server configurations into Ansible playbooks. It employs a “safe‑by‑default” harvesting approach: it blocks likely secret files using a path denylist, inspects file contents to avoid sensitive data, and enforces size limits on collected items. Users can later enable more aggressive data collection if needed. The system focuses on minimizing accidental exposure of credentials while facilitating automated configuration extraction.

## Discussion Summary
The comments convey strong enthusiasm for the JinjaTurtle tool and its integration with Enroll, highlighting its potential to simplify learning and applying Ansible by converting existing configurations into templates and variables. Users appreciate its pragmatic approach for automating server setup, see value in reverse‑engineering existing Ansible‑managed machines, and note the possibility of comparing actual system state with IaC definitions. Some express curiosity about the accuracy of generated output and how it compares to alternatives such as cloud‑init, but overall the sentiment is positive and supportive.

---

## Full Article

Copy

```
# Harvest â Manifest in one go
enroll single-shot --harvest ./harvest --out ./ansible

# Then run Ansible locally
ansible-playbook -i "localhost," -c local ./ansible/playbook.yml
```

Good for

Disaster recovery snapshots, "make this one host reproducible", and carving a golden role set you'll refine over time.

---

Want templates for structured configs? Install

[JinjaTurtle](https://git.mig5.net/mig5/jinjaturtle)

and use

`--jinjaturtle`

(or let it auto-detect).

Copy

```
# Remote harvest over SSH, then manifest locally
enroll single-shot \
  --remote-host myhost.example.com \
  --remote-user myuser \
  --harvest /tmp/enroll-harvest \
  --out ./ansible \
  --fqdn myhost.example.com
```

If you don't want/need sudo on the remote host, add `--no-sudo` (expect a less complete harvest). For remote sudo prompts use `--ask-become-pass`/`-K`. If your SSH private key is encrypted, use `--ask-key-passphrase` (interactive) or `--ssh-key-passphrase-env ENV_VAR` (non-interactive/CI).

Copy

```
# Multi-site mode: shared roles, host-specific state in inventory
enroll harvest --out /tmp/enroll-harvest
enroll manifest --harvest /tmp/enroll-harvest --out ./ansible --fqdn "$(hostname -f)"

# Run the per-host playbook
ansible-playbook ./ansible/playbooks/"$(hostname -f)".yml
```

Rule of thumb: single-site for "one server, easy-to-read roles"; `--fqdn` for "many servers, high abstraction, fast adoption".

Copy

```
# Compare two harvests and get a human-friendly report (ignoring noise)
enroll diff --old /path/to/harvestA --new /path/to/harvestB --format markdown \
  --exclude-path /var/anacron \
  --ignore-package-versions

# Send a webhook when differences are detected
enroll diff \
  --old /path/to/harvestA \
  --new /path/to/harvestB \
  --webhook https://example.net/webhook \
  --webhook-format json \
  --webhook-header 'X-Enroll-Secret: ...' \
  --ignore-package-versions \
  --exit-code

# Ignore a path and changes to package versions, and optionally
# enforce the old state locally (requires ansible-playbook)
enroll diff --old /path/to/harvestA --new /path/to/harvestB \
  --exclude-path /var/anacron \
  --ignore-package-versions \
  --enforce
```

E-mail notifications are also supported. Run it on a systemd timer to alert to drift!

Copy

```
# Explain what's in a harvest
enroll explain /path/to/harvest

# JSON format, and using a SOPS-encrypted harvest
enroll explain /path/to/harvest.sops \
  --sops \
  --format json
```

'explain' tells you why something was included, but also why something was *excluded*.

Copy

```
# Validate a harvest is correct.
enroll validate /path/to/harvest

# Check against the latest published version of the state schema specification
enroll validate /path/to/harvest --schema https://enroll.sh/schema/state.schema.json
```

'validate' makes sure the harvest's state confirms to Enroll's

[state schema](https://enroll.sh/schema.html)

, doesn't contain orphaned artifacts and isn't missing any artifacts needed by the state. By default, it checks against the schema packaged with Enroll, but you can also check against the latest version on this site.