"""Convert a launch checklist Markdown file into CSV for Linear, Notion, Trello or Jira.

Usage: python export_csv.py LAUNCH_CHECKLIST.md launch-checklist.csv

Reads items written in the format from references/output-format.md:

    - [ ] **B3 [CRITICAL] Force HTTPS on every production host**
      - Description: ...
      - Status: Not Started

An item that appears more than once (for example in the blockers section and again
in its category) is written once, using the first occurrence. Needs Python 3 only.
"""
import csv
import re
import sys

FIELDS = ["ID", "Task", "Priority", "Category", "Gate", "Status", "Description", "Why",
          "Verification", "Depends on", "Owner", "Due", "Evidence"]
ITEM = re.compile(r"^- \[( |x|X)\] \*\*(\S+) \[(CRITICAL|HIGH|MEDIUM|LOW)\] (.+?)\*\*\s*$")
FIELD = re.compile(r"^\s+- ([A-Za-z ]+):\s*(.*)$")


def parse(text):
    items, seen, current = [], set(), None
    for line in text.splitlines():
        m = ITEM.match(line)
        if m:
            done, item_id, priority, task = m.groups()
            current = None
            if item_id not in seen:
                seen.add(item_id)
                current = dict.fromkeys(FIELDS, "")
                current.update({"ID": item_id, "Priority": priority.title(), "Task": task.rstrip(".")})
                if done.lower() == "x":
                    current["Status"] = "Done"
                items.append(current)
            continue
        f = FIELD.match(line)
        if f and current is not None:
            name, value = f.group(1).strip(), f.group(2).strip()
            if name in FIELDS and not (name == "Status" and current["Status"] == "Done"):
                current[name] = value
        elif line.strip() and not line.startswith(" "):
            current = None
    return items


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        items = parse(f.read())
    with open(sys.argv[2], "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(items)
    print(f"Wrote {len(items)} items to {sys.argv[2]}")


if __name__ == "__main__":
    main()
