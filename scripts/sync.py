#!/usr/bin/env python3
"""Copy the skill from plugins/content-machine/skills/content-machine/ to skills/content-machine/.

People edit only the copy under plugins/. This script makes the top-level copy that
Codex's $skill-installer reads. Run it before every commit. `--check` only compares.
"""
import filecmp
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "plugins", "content-machine", "skills", "content-machine")
DST = os.path.join(ROOT, "skills", "content-machine")


def differences(a, b):
    out = []
    cmp = filecmp.dircmp(a, b, ignore=["__pycache__", ".DS_Store"])
    out += [os.path.join(a, x) for x in cmp.left_only]
    out += [os.path.join(b, x) for x in cmp.right_only]
    for name in cmp.common_files:
        if not filecmp.cmp(os.path.join(a, name), os.path.join(b, name), shallow=False):
            out.append(os.path.join(a, name))
    for sub in cmp.common_dirs:
        out += differences(os.path.join(a, sub), os.path.join(b, sub))
    return out


def main():
    if "--check" in sys.argv:
        if not os.path.isdir(DST):
            print("skills/content-machine/ is missing. Run scripts/sync.py.")
            return 1
        diff = differences(SRC, DST)
        if diff:
            print("The two skill folders differ. Run scripts/sync.py. Differences:")
            for d in diff:
                print("  " + os.path.relpath(d, ROOT))
            return 1
        print("Skill folders match.")
        return 0
    if os.path.isdir(DST):
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
    print("Copied the skill to skills/content-machine/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
