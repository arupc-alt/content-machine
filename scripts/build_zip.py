#!/usr/bin/env python3
"""Build the upload zips for Claude: dist/content-machine.zip and dist/content-machine-pipeline.zip.

The second zip is the same skill under the name content-machine-pipeline, for accounts that
already have a different skill called content-machine.
"""
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "plugins", "content-machine", "skills", "content-machine")
DIST = os.path.join(ROOT, "dist")


def build(name):
    os.makedirs(DIST, exist_ok=True)
    path = os.path.join(DIST, name + ".zip")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for folder, dirs, files in os.walk(SRC):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in sorted(files):
                if f == ".DS_Store":
                    continue
                full = os.path.join(folder, f)
                rel = os.path.relpath(full, SRC)
                arc = os.path.join(name, rel)
                data = open(full, "rb").read()
                if rel == "SKILL.md" and name != "content-machine":
                    text = data.decode("utf-8")
                    text = re.sub(r"(?m)^name: content-machine$", "name: " + name, text, count=1)
                    data = text.encode("utf-8")
                z.writestr(arc, data)
    print("Built " + os.path.relpath(path, ROOT))


if __name__ == "__main__":
    build("content-machine")
    build("content-machine-pipeline")
    sys.exit(0)
