#!/usr/bin/env python3
"""Checks every push and every release. Exit code 0 means everything passed.

What it checks:
 1. Banned characters (em dashes, en dashes, curly quotes) in every text file people or agents read.
 2. SKILL.md frontmatter: name, description (under 1,024 characters, with the repo marker), version.
 3. Size limits: SKILL.md under 150 lines, each mode file and shared file under its limit.
 4. Every file path the skill names exists.
 5. No Airtable, Slack, or automation IDs, no tokens, no OAuth client files, and no names of a real company.
 6. Every JSON file parses.
 7. The rules inventory: every kept rule's anchor phrase is found word for word in its file.
 8. The two copies of the skill folder match byte for byte.
 9. The version is the same in SKILL.md and both plugin manifests.
"""
import csv
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "plugins", "content-machine", "skills", "content-machine")
MARKER = "github.com/arupc-alt/content-machine"

errors = []


def err(msg):
    errors.append(msg)


def rel(p):
    return os.path.relpath(p, ROOT)


def text_files():
    out = []
    for pattern in ("**/*.md", "**/*.json", "**/*.py", "**/*.yml", "**/*.csv", "LICENSE"):
        out += glob.glob(os.path.join(ROOT, pattern), recursive=True)
    skip = (os.sep + "dist" + os.sep, os.sep + ".git" + os.sep, os.sep + "skills" + os.sep + "content-machine" + os.sep)
    keep = []
    for p in sorted(set(out)):
        r = os.sep + rel(p)
        if any(s in r for s in skip[:2]):
            continue
        if r.startswith(os.sep + "skills" + os.sep):
            continue  # the synced copy is checked by comparison instead
        keep.append(p)
    return keep


# 1. Banned characters
BANNED = {chr(0x2014): "em dash", chr(0x2013): "en dash", chr(0x201C): "curly quote", chr(0x201D): "curly quote",
          chr(0x2018): "curly quote", chr(0x2019): "curly quote"}
for p in text_files():
    if p.endswith(".csv"):
        continue
    with open(p, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            for ch, name in BANNED.items():
                if ch in line:
                    err(f"{rel(p)}:{n}: {name} found")

# 2. Frontmatter
skill_md = open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8").read()
m = re.match(r"^---\n(.*?)\n---\n", skill_md, re.S)
version = None
if not m:
    err("SKILL.md: no frontmatter")
else:
    fm = m.group(1)
    name = re.search(r"(?m)^name:\s*(.+)$", fm)
    desc = re.search(r'(?m)^description:\s*"(.*)"\s*$', fm)
    ver = re.search(r'(?m)^\s+version:\s*"([^"]+)"', fm)
    if not name or name.group(1).strip() != "content-machine":
        err("SKILL.md: name must be content-machine")
    if not desc:
        err("SKILL.md: description missing or not on one quoted line")
    else:
        if len(desc.group(1)) >= 1024:
            err(f"SKILL.md: description is {len(desc.group(1))} characters (limit 1,023)")
        if MARKER not in desc.group(1):
            err("SKILL.md: description lacks the repo marker")
    if not ver:
        err("SKILL.md: metadata.version missing")
    else:
        version = ver.group(1)

# 3. Size limits
LIMITS = {"SKILL.md": 150}
if skill_md.count("\n") >= LIMITS["SKILL.md"]:
    err(f"SKILL.md has {skill_md.count(chr(10))} lines (limit {LIMITS['SKILL.md']})")
for p in glob.glob(os.path.join(SKILL, "modes", "*.md")) + glob.glob(os.path.join(SKILL, "shared", "**", "*.md"), recursive=True):
    size = os.path.getsize(p)
    if size > 120_000:
        err(f"{rel(p)} is {size} bytes (limit 120,000)")

# 4. Every named path exists
PATH_RE = re.compile(r"\b((?:modes|shared|templates|scripts|products)/[A-Za-z0-9_./-]+\.(?:md|json|py))\b")
for p in glob.glob(os.path.join(SKILL, "**", "*.md"), recursive=True):
    for target in set(PATH_RE.findall(open(p, encoding="utf-8").read())):
        if not os.path.exists(os.path.join(SKILL, target)):
            err(f"{rel(p)}: names {target}, which doesn't exist")

# 5. IDs, tokens, company names
ID_RE = re.compile(r"\b(?:app|tbl|fld|sel|wfl|eac|wsp|viw|rec)[A-Za-z0-9]{14}\b")
SLACK_RE = re.compile(r"\b[UCDG]0[A-Z0-9]{8,10}\b")
TOKEN_RE = re.compile(r"xox[abposr]-|client_secret|-----BEGIN|AIza[0-9A-Za-z_-]{20}|ghp_[0-9A-Za-z]{20}")
NAMES_RE = re.compile(r"surecart|brainstorm ?force|bsf\.io|\bCMP-\d|\bAST-\d|\barup\b|\bharsh\b|\bchetan\b|\bsheen\b", re.I)
for p in text_files():
    t = open(p, encoding="utf-8").read()
    for regex, what in ((ID_RE, "an Airtable or automation ID"), (SLACK_RE, "a Slack ID"),
                        (TOKEN_RE, "a token or secret"), (NAMES_RE, "a real company or person's name")):
        if p.endswith("check.py"):
            continue
        for hit in set(regex.findall(t)):
            err(f"{rel(p)}: looks like {what}: {hit!r}")
for p in glob.glob(os.path.join(ROOT, "**", "client_secret*.json"), recursive=True):
    err(f"{rel(p)}: OAuth client file in the repo")

# 6. JSON parses
for p in glob.glob(os.path.join(ROOT, "**", "*.json"), recursive=True) + glob.glob(os.path.join(ROOT, ".*", "**", "*.json"), recursive=True):
    if os.sep + ".git" + os.sep in p:
        continue
    try:
        json.load(open(p, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(f"{rel(p)}: invalid JSON: {e}")

# 7. Rules inventory
inv_files = glob.glob(os.path.join(ROOT, "tests", "rules-inventory", "*.csv"))
if not inv_files:
    err("tests/rules-inventory/ has no CSV files")
kept = dropped = 0
for p in inv_files:
    with open(p, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            target = (row.get("new_file") or "").strip()
            if target == "DROPPED":
                dropped += 1
                continue
            kept += 1
            path = os.path.join(SKILL, target)
            if not os.path.exists(path):
                err(f"{rel(p)} {row.get('rule_id')}: file {target} doesn't exist")
                continue
            anchor = (row.get("anchor") or "").strip()
            body = open(path, encoding="utf-8").read()
            if anchor and anchor not in body and anchor not in " ".join(body.split()):
                err(f"{rel(p)} {row.get('rule_id')}: anchor not found in {target}: {anchor!r}")

# 8. Two copies match
r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "sync.py"), "--check"], capture_output=True, text=True)
if r.returncode != 0:
    err(r.stdout.strip())

# 9. Versions match
for mf in ("plugins/content-machine/.claude-plugin/plugin.json", "plugins/content-machine/.codex-plugin/plugin.json"):
    v = json.load(open(os.path.join(ROOT, mf))).get("version")
    if v != version:
        err(f"{mf}: version {v} doesn't match SKILL.md {version}")

if errors:
    print(f"{len(errors)} problem(s):")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print(f"All checks passed. Version {version}. Rules inventory: {kept} kept, {dropped} dropped.")
