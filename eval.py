"""Score retrieval quality on eval/cases.json (recall@3 / recall@10).

    python eval.py                       # all modes of this app
    python eval.py --mode hybrid -v      # one mode, show misses
    python eval.py --original http://127.0.0.1:8090   # also score the original Go app

A case passes at k if EVERY title fragment in "expect" appears in the title of
some note among the top-k results.
"""
import argparse
import json

import requests

import config
import db
import search


def hit(expect, titles):
    return all(any(e.lower() in t.lower() for t in titles) for e in expect)


def score(name, fn, cases, verbose):
    r3 = r10 = 0
    for c in cases:
        titles = fn(c["q"])
        ok3, ok10 = hit(c["expect"], titles[:3]), hit(c["expect"], titles[:10])
        r3 += ok3
        r10 += ok10
        if verbose and not ok10:
            print(f"   MISS  {c['q']!r}\n         got: {titles[:4]}")
    n = len(cases)
    print(f"{name:<22} recall@3 = {r3}/{n} ({r3 / n:.0%})   recall@10 = {r10}/{n} ({r10 / n:.0%})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["keyword", "semantic", "hybrid"])
    ap.add_argument("--original")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    cases = json.load(open(config.ROOT / "eval" / "cases.json"))
    con = db.connect()
    for mode in [a.mode] if a.mode else ["keyword", "semantic", "hybrid"]:
        score(f"this app / {mode}", lambda q, m=mode: [r["title"] for r in search.run(con, q, m, log=False)],
              cases, a.verbose)
    if a.original:
        score("original (Go) app", lambda q: [n["title"] for n in requests.get(
            a.original + "/api/search", params={"q": q}, timeout=30).json()["notes"]], cases, a.verbose)


if __name__ == "__main__":
    main()
