"""Build a printable PDF of the full launch checklist reference.

Usage: python tools/build_pdf.py [output.pdf]            the full reference, about 60 pages
       python tools/build_pdf.py --short [output.pdf]    only the Critical items, a few pages

Joins the reference files into one HTML document and prints it to PDF with headless
Chrome or Edge. The default outputs are Launch-Checklist.pdf and Launch-Checklist-Short.pdf. Needs Python 3, the "markdown" package (pip install markdown) and
Chrome or Edge installed.
"""
import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile

try:
    import markdown
except ImportError:
    sys.exit('The "markdown" package is missing. Install it with: pip install markdown')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(ROOT, "skills", "launch-checklist", "references")
ORDER = [
    "core-checklist.md", "type-web.md", "type-saas.md", "type-ecommerce.md", "type-api.md",
    "type-mobile.md", "type-desktop.md", "type-browser-extension.md", "type-ai-ml.md",
    "type-data.md", "type-open-source.md", "type-developer-tools.md", "type-internal.md",
    "type-self-hosted.md", "type-cloud-infra.md", "type-iot.md", "jurisdictions.md",
    "launch-runbook.md", "sources.md",
]
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

INTRO = """
# Launch Checklist

<p class="sub">A complete pre-launch and post-launch reference for digital products. Built on {date}.</p>

## How to use this document

This is the full library: every item for every project type. No single project needs all of it.

1. Read the **Core checklist** (categories A to O). Most launches need most of it.
2. Add the section for each **project type** your product combines, for example web application plus SaaS plus AI.
3. Cross out the items whose "Applies if" condition is not true for your project, and write down why.
4. Use the **Jurisdictions** section to decide which laws to check, and the **Sources** section to find the official page for each. Read the official page on the day; this document deliberately states few legal or platform rules, because they change.
5. Start the items with outside lead time first. The **Launch runbook** lists them and gives a timeline, launch-day steps and rollback triggers.

Each item shows an ID, a default priority, the task, why it matters and how to verify it. The priorities are defaults:

- **CRITICAL:** must be complete before a public launch when the item applies.
- **HIGH:** strongly recommended before launch.
- **MEDIUM:** important, and can be completed around launch.
- **LOW:** worth doing later.

Raise a priority when the product handles money, sensitive data or cannot be rolled back after release. Lower it for a prototype, a private beta or an internal tool with few users.

This document supports planning. It is not legal, security or compliance advice, and completing it does not prove compliance. Get professional review where the stakes call for it.

## Sections

{toc}
"""

CSS = """
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif; font-size: 9.6pt; line-height: 1.42; color: #1c2430; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 6pt; color: #10233f; border-bottom: 2pt solid #10233f; padding-bottom: 5pt; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; font-size: 28pt; border: 0; margin-top: 60mm; }
h2 { font-size: 13pt; margin: 16pt 0 6pt; color: #10233f; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; page-break-after: avoid; }
p { margin: 0 0 6pt; }
p.sub { font-size: 12pt; color: #4a5568; margin-bottom: 30mm; }
ul, ol { margin: 0 0 6pt; padding-left: 16pt; }
ul.items { list-style: none; padding-left: 0; }
ul.items > li { padding: 5pt 0 5pt 17pt; border-bottom: 0.5pt solid #d9dee6; position: relative; page-break-inside: avoid; }
.cb { position: absolute; left: 0; top: 7pt; width: 9pt; height: 9pt; border: 1pt solid #4a5568; border-radius: 1.5pt; }
.id { font-family: Consolas, "Courier New", monospace; font-size: 8.4pt; color: #4a5568; margin-right: 3pt; }
.pr { font-size: 7.2pt; font-weight: 700; letter-spacing: 0.4pt; padding: 1pt 4pt; border-radius: 2pt; margin-right: 4pt; vertical-align: 1pt; }
.CRITICAL { background: #fbe3e1; color: #9b1c12; }
.HIGH { background: #fdecd2; color: #8a4b00; }
.MEDIUM { background: #e1ecfb; color: #174a8c; }
.LOW { background: #e6ebe7; color: #3c5245; }
.f { color: #4a5568; font-weight: 600; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 8pt; font-size: 8.6pt; }
th, td { border: 0.5pt solid #c5ccd6; padding: 3pt 5pt; text-align: left; vertical-align: top; word-break: break-word; }
th { background: #eef1f5; }
tr { page-break-inside: avoid; }
code { font-family: Consolas, "Courier New", monospace; font-size: 8.6pt; background: #eef1f5; padding: 0 2pt; border-radius: 2pt; }
a { color: #174a8c; text-decoration: none; }
"""


def prepare(text):
    """Turn the one-line reference items into styled HTML list items."""
    text = re.sub(r"\n## Contents\n.*?(?=\n## )", "\n", text, flags=re.S)
    # Two sentences in the core file are instructions for the agent, not for a reader.
    text = text.replace(" Priorities are defaults; adjust them for the project as SKILL.md describes.", "")
    text = text.replace(" Expand each selected line into the full item format from the output format reference.", "")
    out = []
    for line in text.splitlines():
        m = re.match(r"^- \[ \] \*\*(\S+) \[(CRITICAL|HIGH|MEDIUM|LOW)\] (.+?)\*\* (.*)$", line)
        if m:
            item_id, pr, title, rest = m.groups()
            rest = re.sub(r"^If: ", '<span class="f">Applies if:</span> ', rest)
            for label in ("Why", "Verify", "Needs"):
                rest = rest.replace(f" {label}: ", f'<br><span class="f">{label}:</span> ')
            line = (f'- <span class="cb"></span><span class="id">{item_id}</span>'
                    f'<span class="pr {pr}">{pr}</span><strong>{title}</strong><br>{rest}')
        out.append(line)
    return "\n".join(out)


SHORT_CSS = """
@page { size: A4; margin: 10mm 11mm 10mm 11mm; }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif; font-size: 7.9pt; line-height: 1.27; color: #1c2430; margin: 0; }
h1 { font-size: 17pt; margin: 0; color: #10233f; letter-spacing: -0.3pt; }
h1 span { font-weight: 400; color: #4a5568; }
.sub { margin: 2pt 0 5pt; padding-bottom: 4pt; border-bottom: 1.5pt solid #10233f; color: #2d3748; }
h2 { font-size: 10pt; margin: 6pt 0 3pt; padding: 1.5pt 5pt; background: #10233f; color: #fff; break-after: avoid; }
h2 small { font-weight: 400; font-size: 8pt; opacity: 0.85; }
h3 { font-size: 8.2pt; margin: 4.5pt 0 1pt; color: #10233f; border-bottom: 0.5pt solid #9aa5b5; break-after: avoid; }
.cols { column-count: 2; column-gap: 7mm; }
.newpage { break-before: page; margin-top: 0; }
.cols h3:first-child { margin-top: 0; }
ul, ol { margin: 0; padding: 0; list-style: none; }
li { position: relative; padding: 0.7pt 0 0.7pt 37pt; break-inside: avoid; }
.core li { padding-left: 27pt; }
.noid li { padding-left: 10pt; }
li .cb { position: absolute; left: 0; top: 2pt; width: 6.4pt; height: 6.4pt; border: 0.8pt solid #4a5568; border-radius: 1pt; }
li .id { position: absolute; left: 9.5pt; top: 1.2pt; font-family: Consolas, "Courier New", monospace; font-size: 6.4pt; color: #5a6578; }
.plain li { padding-left: 10pt; }
ol.plain { counter-reset: n; }
ol.plain li { counter-increment: n; padding-left: 12pt; }
ol.plain li::before { content: counter(n) "."; position: absolute; left: 0; color: #5a6578; }
ul.plain li::before { content: ""; position: absolute; left: 1pt; top: 4pt; width: 3pt; height: 3pt; border-radius: 50%; background: #5a6578; }
p { margin: 0 0 3pt; }
.group { break-inside: avoid; padding-top: 4.5pt; }
.group:first-child { padding-top: 0; }
.group h3 { margin-top: 0; }
.foot { margin-top: 5pt; padding-top: 3pt; border-top: 0.5pt solid #9aa5b5; color: #4a5568; font-size: 7.4pt; }
"""

SHORT_RUNBOOK = """
<div class="group"><h3>Start early, because these wait on other people</h3>
<p>Payment provider activation. App store enrolment and review. Sign-in or API scope verification. Warming up a new email domain. SMS sender registration. Code signing certificates. Trademark and tax registration. Legal review. Outside security testing. Cloud quota increases. Hardware certification.</p></div>
<div class="group"><h3>Go only if</h3><ul class="noid">
<li><span class="cb"></span>Every blocker is done, with evidence.</li>
<li><span class="cb"></span>Every open item has an owner, a date and an accepted risk.</li>
<li><span class="cb"></span>Rollback has been rehearsed, and one person is named to call it.</li>
<li><span class="cb"></span>Monitoring shows a healthy baseline, and alerts reach a person.</li>
<li><span class="cb"></span>Support and on-call cover is confirmed for launch day and the day after.</li>
</ul></div>
<div class="group"><h3>Launch day, in order</h3><ol class="plain">
<li>Note the baseline: errors, response times, uptime.</li>
<li>Take a fresh backup, or confirm the latest one.</li>
<li>Release.</li>
<li>Run the smoke test.</li>
<li>Complete one real journey, including one real payment.</li>
<li>Remove launch gates: waitlist, maintenance page, noindex, feature flags.</li>
<li>Watch for an hour, then announce.</li>
<li>Log every incident and decision with the time.</li>
</ol></div>
<div class="group"><h3>Roll back if</h3><ul class="plain">
<li>A core journey fails for real users.</li>
<li>Errors or response times stay above the agreed threshold.</li>
<li>There is any sign of data loss, or of one user seeing another's data.</li>
<li>Users are charged wrongly.</li>
<li>Costs rise faster than the agreed ceiling.</li>
</ul><p>Agree the numbers before launch, and name who decides.</p></div>
<div class="group"><h3>After launch</h3><ul class="plain">
<li>First hour: smoke test, errors, sign-ups, payments, email delivery.</li>
<li>First day: errors, support messages, costs against forecast, backups ran.</li>
<li>First week: daily triage, search indexing, email deliverability, store reviews.</li>
<li>Two weeks: review what failed and what was missing, then close the checklist.</li>
</ul></div>
"""


def critical_items(name):
    """Yield (heading, [(id, title), ...]) for the Critical items in one reference file."""
    with open(os.path.join(REFS, name), encoding="utf-8") as f:
        body = f.read()
    title = re.match(r"# (.+)", body).group(1)
    core = name == "core-checklist.md"
    heading, rows = title, []
    for line in body.splitlines():
        h = re.match(r"^## ([A-O]\. .+)$", line) if core else None
        if h:
            if rows:
                yield heading, rows
            heading, rows = h.group(1), []
        m = re.match(r"^- \[ \] \*\*(\S+) \[CRITICAL\] (.+?)\.\*\* ", line)
        if m:
            rows.append(m.groups())
    if rows:
        yield heading, rows


def short_page(date):
    def block(heading, rows):
        items = "".join(f'<li><span class="cb"></span><span class="id">{i}</span>{t}</li>' for i, t in rows)
        return f"<h3>{heading}</h3><ul>{items}</ul>"

    core = "".join(block(h, r) for h, r in critical_items("core-checklist.md"))
    types = "".join(block(h, r) for name in ORDER if name.startswith("type-") for h, r in critical_items(name))
    body = (
        "<h1>Launch Checklist <span>the short version</span></h1>"
        f'<p class="sub">Only the items marked Critical, which should be finished before a public launch. Skip any '
        "that plainly do not apply. The full version gives the reason and the check for each one, and lists "
        f"the High, Medium and Low items. Built on {date}.</p>"
        "<h2>Before any launch</h2>"
        f'<div class="cols core">{core}</div>'
        "<h2>Launch week</h2>"
        f'<div class="cols">{SHORT_RUNBOOK}</div>'
        '<h2 class="newpage">Add for what you are launching <small>use every section that fits</small></h2>'
        f'<div class="cols">{types}</div>'
        '<p class="foot">This supports planning. It is not legal, security or compliance advice. Laws, store policies '
        "and provider terms change, so read the official page on the day you rely on it.</p>"
    )
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Launch Checklist, short version</title><style>{SHORT_CSS}</style></head><body>{body}</body></html>'


def full_page(date):
    parts, titles = [], []
    for name in ORDER:
        with open(os.path.join(REFS, name), encoding="utf-8") as f:
            body = f.read()
        titles.append(re.match(r"# (.+)", body).group(1))
        parts.append(prepare(body))
    toc = "\n".join(f"{i}. {t}" for i, t in enumerate(titles, 1))
    source = INTRO.format(date=date, toc=toc) + "\n\n" + "\n\n".join(parts)
    html = markdown.markdown(source, extensions=["tables", "fenced_code", "sane_lists"])
    html = re.sub(r'<ul>\s*(?=<li><span class="cb">)', '<ul class="items">', html)
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Launch Checklist</title><style>{CSS}</style></head><body>{html}</body></html>'


def main():
    args = [a for a in sys.argv[1:] if a != "--short"]
    short = "--short" in sys.argv
    default = "Launch-Checklist-Short.pdf" if short else "Launch-Checklist.pdf"
    out_pdf = os.path.abspath(args[0] if args else os.path.join(ROOT, default))
    date = datetime.date.today().strftime("%d %B %Y").lstrip("0")
    page = short_page(date) if short else full_page(date)

    browser = next((b for b in BROWSERS if os.path.exists(b)), None) or shutil.which("chrome") or shutil.which("chromium")
    if not browser:
        sys.exit("Chrome or Edge was not found, so the PDF cannot be printed.")
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        html_path = os.path.join(tmp, "launch-checklist.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page)
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--user-data-dir={os.path.join(tmp, 'profile')}",
                        f"--print-to-pdf={out_pdf}", "file:///" + html_path.replace("\\", "/")],
                       check=True, capture_output=True, timeout=180)
    print(f"Wrote {out_pdf} ({os.path.getsize(out_pdf) // 1024} KB)")


if __name__ == "__main__":
    main()
