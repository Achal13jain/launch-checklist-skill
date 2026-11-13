"""Inject the checklist library into the home page. Run: python tools/build_site.py

The picker on docs/index.html filters the real library, so the page carries a compact
copy of every item (ID, priority, title and a condition). This script rebuilds that
copy from the reference files and writes it between the LIB markers in the page.

    python tools/build_site.py           rewrite the data block in docs/index.html
    python tools/build_site.py --check   exit 1 if the page is out of date

Needs Python 3 only.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(ROOT, "skills", "launch-checklist", "references")
PAGE = os.path.join(ROOT, "docs", "index.html")

# Facts the picker can switch on and off.
FACTS = [
    ["pub", "Public launch"],
    ["web", "Public web pages"],
    ["ui", "A user interface"],
    ["srv", "A backend or database"],
    ["acct", "User accounts"],
    ["data", "Personal data"],
    ["pay", "Payments"],
    ["mail", "Sends email"],
]

# Project types: key, chip label, reference file, ID prefix, ID number range, facts it implies.
# "app" is implied only and has no chip: it marks a product people operate, as opposed to a
# content site, so documentation, support and release-process items are not pushed onto a
# static site.
TYPES = [
    ("site", "Website or docs site", "type-web.md", "WEB", (1, 6), "pub web ui"),
    ("webapp", "Web app", "type-web.md", "WEB", (7, 99), "pub web ui srv acct data app"),
    ("saas", "SaaS", "type-saas.md", "SAAS", None, "pub web ui srv acct data pay mail app"),
    ("ecom", "Online store", "type-ecommerce.md", "ECOM", None, "pub web ui srv acct data pay mail app"),
    ("api", "API or backend", "type-api.md", "API", None, "pub srv app"),
    ("mobile", "Mobile app", "type-mobile.md", "MOB", None, "pub ui app"),
    ("desktop", "Desktop app", "type-desktop.md", "DESK", None, "pub ui app"),
    ("ext", "Browser extension", "type-browser-extension.md", "EXT", None, "pub ui app"),
    ("ai", "AI app", "type-ai-ml.md", "AI", None, "pub ui srv app"),
    ("agent", "AI agent", "type-ai-ml.md", "AGT", None, "pub srv app"),
    ("ml", "ML model", "type-ai-ml.md", "ML", None, "srv app"),
    ("data", "Data pipeline", "type-data.md", "DATA", None, "srv app"),
    ("oss", "Open source", "type-open-source.md", "OSS", None, "pub app"),
    ("lib", "Library or SDK", "type-developer-tools.md", "DEV", None, "pub app"),
    ("cli", "CLI tool", "type-developer-tools.md", "CLI", None, "pub app"),
    ("plat", "Developer platform", "type-developer-tools.md", "PLAT", None, "pub web ui srv acct data app"),
    ("internal", "Internal tool", "type-internal.md", "INT", None, "ui srv acct data app"),
    ("selfhosted", "Self-hosted", "type-self-hosted.md", "SH", None, "pub ui srv acct app"),
    ("infra", "Cloud infrastructure", "type-cloud-infra.md", "INF", None, "srv app"),
    ("iot", "IoT device", "type-iot.md", "IOT", None, "pub srv data app"),
]

# When each core item applies. Empty means always. "?" means it depends on a detail the
# skill asks about. Otherwise a list of facts joined by "|": the item applies when any is on.
# This is a simplification for the picker; the skill itself reads each item's "If:" clause.
CORE_COND = """
A1=data A2= A3=data A4=acct|pay A5=? A6=data A7=? A8=data A9=data A10=data A11=pay A12= A13=
A14=pub A15=pay A16=? A17=? A18=? A19=? A20=?
B1=web|srv B2=web|srv B3=web|srv B4=web B5=srv B6=srv B7=srv B8=web|srv B9=web|srv B10=srv
B11=web|srv B12=web|srv B13=web|srv B14=srv B15=?
C1=srv C2=srv C3=acct C4=acct C5=srv C6=? C7=srv C8=srv C9=srv C10=web|srv C11=acct C12= C13=app
C14=? C15=acct C16=app C17=srv C18=srv C19=srv C20=? C21=app C22=?
D1=web D2=web D3=web D4=web D5=web D6=web D7=? D8=web D9=web D10=web D11=? D12=web
E1=ui E2=ui E3=app E4=app E5=ui E6=ui E7=ui E8=ui E9=web E10=app E11=ui E12=ui E13=? E14=?
F1= F2=acct F3=pay F4=srv F5=srv F6=app F7=app F8=? F9=? F10=web|srv F11=? F12=app
G1=pub G2=? G3=? G4=srv G5=srv G6=srv G7=srv G8=srv G9=?
H1=ui H2=web H3=web H4=web H5=srv H6=web H7=srv H8=web H9=web
I1=mail I2=mail I3=? I4=mail I5=? I6=mail I7= I8=mail I9=? I10=?
J1=app J2=app J3=app J4=app J5=app J6=app J7=app J8=app J9=? J10=app
K1=pub K2=pub K3=pay K4=app K5=pub K6=? K7=pub K8=? K9= K10=pub
L1=srv L2=srv L3=srv L4=srv L5=srv L6=app L7=? L8=srv
M1=web|srv M2= M3= M4=app M5=
N1=srv N2=? N3=srv N4=srv N5=srv N6=srv
O1=srv O2=srv O3=srv O4=srv O5=srv O6=ui O7=srv O8=?
"""
ITEM = re.compile(r"^- \[ \] \*\*([A-Z]+)(\d+) \[(CRITICAL|HIGH|MEDIUM|LOW)\] (.+?)\.\*\* (If: )?")


def read(name):
    with open(os.path.join(REFS, name), encoding="utf-8") as f:
        return f.read()


def items_in(name):
    for line in read(name).splitlines():
        m = ITEM.match(line)
        if m:
            prefix, num, pri, title, cond = m.groups()
            yield prefix, int(num), pri[0], title, bool(cond)


def build():
    cond = dict(pair.split("=") for pair in CORE_COND.split())
    groups, core = [], {}
    names = dict(re.findall(r"^## ([A-O])\. (.+)$", read("core-checklist.md"), re.M))
    for prefix, num, pri, title, _ in items_in("core-checklist.md"):
        item_id = f"{prefix}{num}"
        if item_id not in cond:
            sys.exit(f"tools/build_site.py: add a condition for core item {item_id} to CORE_COND")
        core.setdefault(prefix, []).append([item_id, pri, title, cond.pop(item_id)])
    if cond:
        sys.exit(f"tools/build_site.py: CORE_COND names items that no longer exist: {sorted(cond)}")
    for letter in sorted(core):
        groups.append({"k": letter, "n": f"{letter}. {names[letter]}", "core": 1,
                       "f": "core-checklist.md", "items": core[letter]})
    types = []
    for key, label, ref, prefix, rng, facts in TYPES:
        rows = [[f"{p}{n}", pri, title, "?" if c else ""] for p, n, pri, title, c in items_in(ref)
                if p == prefix and (rng is None or rng[0] <= n <= rng[1])]
        if not rows:
            sys.exit(f"tools/build_site.py: no items found for type {key} in {ref}")
        groups.append({"k": key, "n": label, "core": 0, "f": ref, "items": rows})
        types.append([key, label, facts.split()])
    return {"facts": FACTS, "types": types, "groups": groups}


def main():
    lib = build()
    total = sum(len(g["items"]) for g in lib["groups"])
    block = "/*LIB:START*/var LIB=" + json.dumps(lib, separators=(",", ":"), ensure_ascii=False) + ";/*LIB:END*/"
    with open(PAGE, encoding="utf-8") as f:
        page = f.read()
    new, n = re.subn(r"/\*LIB:START\*/.*?/\*LIB:END\*/", lambda _: block, page, flags=re.S)
    if n != 1:
        sys.exit("tools/build_site.py: the LIB markers were not found exactly once in docs/index.html")
    if "--check" in sys.argv:
        if new != page:
            sys.exit("docs/index.html is out of date; run python tools/build_site.py")
        print(f"site data: in sync ({total} items)")
        return
    with open(PAGE, "w", encoding="utf-8", newline="\n") as f:
        f.write(new)
    print(f"Wrote {total} items into docs/index.html ({len(block) // 1024} KB of data)")


if __name__ == "__main__":
    main()
