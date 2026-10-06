#!/usr/bin/env python3
"""Runs the QA measurement script on planted drafts and checks it catches each planted problem.

This is the automatic part of the release checks. The full checks, which need a real Claude or
Codex session with connected tools, are in tests/release-checklist.md.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MEASURE = os.path.join(ROOT, "plugins", "content-machine", "skills", "content-machine", "scripts", "measure.py")
DRAFTS = os.path.join(HERE, "fixtures", "drafts")


def measure(path):
    out = subprocess.run([sys.executable, MEASURE, path, "--spelling", "US"], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def main():
    expected = json.load(open(os.path.join(DRAFTS, "expected.json")))
    failures = []
    for name, want in expected.items():
        r = measure(os.path.join(DRAFTS, name))
        got = {
            "em_dashes": r["banned_characters"]["em_dash_count"],
            "raw_markup": r["raw_markup_in_text"]["count"],
            "other_spelling": len(r["spelling"]["other_spelling_hits"]),
            "ai_tells": r["ai_tells_words_and_phrases"]["hit_count"],
        }
        for key, value in want.items():
            if key.endswith("_min"):
                field = key[:-4]
                if got[field] < value:
                    failures.append(f"{name}: expected at least {value} {field}, got {got[field]}")
            elif got[key] != value:
                failures.append(f"{name}: expected {key} = {value}, got {got[key]}")
    if failures:
        print("Fixture checks failed:")
        for f in failures:
            print("  " + f)
        return 1
    print(f"Fixture checks passed ({len(expected)} drafts).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
