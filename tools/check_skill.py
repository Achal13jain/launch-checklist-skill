"""Structural checks for the launch-checklist skill. Run: python tools/check_skill.py

Checks the frontmatter, description and SKILL.md length, links between SKILL.md and the
reference files, a Contents section in long reference files, the checklist item format,
unique item IDs, references to item IDs that do not exist, the house style (no em dashes,
en dashes or double hyphens in prose), and the JSON files. Exit code 1 if anything fails.
Needs Python 3 and PyYAML.
"""
import glob
import json
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "launch-checklist"
SKILL = os.path.join(ROOT, "skills", NAME)
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL", msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# 1. Frontmatter
text = read(os.path.join(SKILL, "SKILL.md"))
fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", text, re.S).group(1))
name, desc = fm.get("name", ""), fm.get("description", "")
if set(fm) != {"name", "description"}:
    fail(f"frontmatter should hold only name and description, found {sorted(fm)}")
if name != NAME or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
    fail(f"name {name!r} breaks the naming rules or does not match the folder")
if not desc or re.search(r"[<>]", desc) or len(desc) > 1024:
    fail("description is empty, has angle brackets or is over 1024 characters")
lines = text.count("\n")
print(f"description: {len(desc)} of 1024 characters; SKILL.md: {lines} of 500 lines")
if lines >= 500:
    fail("SKILL.md is too long")

# 2. Links and reference files
refs = sorted(glob.glob(os.path.join(SKILL, "references", "*.md")))
linked = set(re.findall(r"\((?:references|assets)/([\w.-]+)\)", text))
for path in refs:
    ref, body = os.path.basename(path), read(path)
    if ref not in linked:
        fail(f"{ref} is not linked from SKILL.md")
    if body.count("\n") > 100 and "## Contents" not in body:
        fail(f"{ref} is over 100 lines without a Contents section")
for ref in linked:
    if not any(os.path.exists(os.path.join(SKILL, d, ref)) for d in ("references", "assets")):
        fail(f"SKILL.md links to a missing file: {ref}")
print(f"references: {len(refs)} files")

# 3. Checklist items
ITEM = re.compile(r"^- \[ \] \*\*([A-Z]+\d+) \[(CRITICAL|HIGH|MEDIUM|LOW)\] [A-Z].+?\.\*\* ")
ids, counts = {}, {}
for path in refs:
    ref = os.path.basename(path)
    in_code = False
    for n, line in enumerate(read(path).splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
        if in_code or not line.startswith("- [ ]"):
            continue
        m = ITEM.match(line)
        if not m:
            fail(f"{ref}:{n} item does not match the format")
            continue
        if " Why: " not in line or " Verify: " not in line:
            fail(f"{ref}:{n} item {m.group(1)} lacks Why or Verify")
        if m.group(1) in ids:
            fail(f"{ref}:{n} duplicate ID {m.group(1)}, first used in {ids[m.group(1)]}")
        ids[m.group(1)] = ref
        counts[m.group(2)] = counts.get(m.group(2), 0) + 1
print(f"items: {len(ids)} ({', '.join(f'{k} {v}' for k, v in sorted(counts.items()))})")
for path in refs:
    for n, line in enumerate(read(path).splitlines(), 1):
        for needs in re.findall(r" Needs: ([A-Z0-9, ]+)\.", line):
            for ref_id in re.findall(r"[A-Z]+\d+", needs):
                if ref_id not in ids:
                    fail(f"{os.path.basename(path)}:{n} depends on unknown ID {ref_id}")

# 4. House style: no em dashes, en dashes or double hyphens in prose
prose = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
for path in prose:
    in_code = False
    for n, line in enumerate(read(path).splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or re.fullmatch(r"\s*-{3,}\s*", line) or re.fullmatch(r"[|\-: ]+", line):
            continue
        if "—" in line or "–" in line or re.search(r"(?<!-)--(?!-)", re.sub(r"`[^`]*`", "", line)):
            fail(f"{os.path.relpath(path, ROOT)}:{n} has an em dash, en dash or double hyphen")
print(f"house style: {len(prose)} Markdown files checked")

# 5. JSON files
for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "evals/evals.json"):
    try:
        json.loads(read(os.path.join(ROOT, rel)))
    except (OSError, ValueError) as e:
        fail(f"{rel}: {e}")

# 6. Home page: the item data matches the reference files, and the prose has no long dashes
page = os.path.join(ROOT, "docs", "index.html")
if os.path.exists(page):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_site.py"), "--check"],
                       capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())
    if r.returncode:
        fail("docs/index.html is out of date; run python tools/build_site.py")
    for n, line in enumerate(read(page).splitlines(), 1):
        if "—" in line or "–" in line:
            fail(f"docs/index.html:{n} has an em dash or en dash")

print("\nFAILED" if failures else "\nAll checks passed")
sys.exit(1 if failures else 0)
