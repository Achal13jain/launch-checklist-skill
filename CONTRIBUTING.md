# Contributing

Thank you for helping improve Launch Checklist. The most useful contribution is a report of an item that was wrong, out of date, missing, or out of proportion for a real project, because the skill's whole purpose is a checklist that fits the project in front of it.

## Reporting a problem with the checklist

Open an issue. Include the prompt you used, the kind of project (what it does, who uses it, whether it handles money or personal data, how it is released), what the skill produced, and what you expected instead and why. A short excerpt of the checklist is enough.

For security problems, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Rules for changing the skill

The skill lives in `skills/launch-checklist/`. These rules keep it accurate and usable on every surface that loads skills.

1. **Specific first.** A new item should say when it applies, why it matters and how to verify it. If it only applies to some projects, give it an "If:" clause. Avoid items that restate another item.
2. **Verify rules at the source.** Anything about a law, a store policy, or a provider's terms, limits, defaults or prices must come from the current official page. Read the page, then add or update its row in `references/sources.md` with the date you reached it.
3. **Point to the rule instead of copying it.** Thresholds, deadlines and version requirements go stale. The item should tell the assistant what to check and where, so the assistant reads the current page when the skill is used.
4. **Keep law and good practice apart.** Say which one an item is, and present legal conclusions as questions for professional review.
5. **Keep the structure.** `SKILL.md` stays under 500 lines. Reference files are linked directly from `SKILL.md`. A reference file over 100 lines starts with a Contents section. Item IDs are never reused or renumbered, because existing checklists refer to them.
6. **Keep the frontmatter portable.** `SKILL.md` has only `name` and `description`. The description stays under 1,024 characters, in the third person, and says what the skill does and when to use it.
7. **House style.** Write in full sentences and plain words. Do not use em dashes, en dashes or double hyphens in prose; the check script enforces this for Markdown files.

## Making a change

1. Fork the repository and create a short-lived branch from `main`.
2. Make the change, and add a line describing it to the newest entry in `CHANGELOG.md`. The maintainer sets the version number when releasing.
3. If you added, removed or retitled an item, rebuild the home page data. A new core item also needs a condition in `tools/build_site.py`; the script tells you when one is missing.

   ```bash
   python tools/build_site.py
   ```

4. Run the checks. They need Python 3 and PyYAML (`pip install pyyaml`):

   ```bash
   python tools/check_skill.py
   ```

5. Open a pull request. CI runs the same check script.

The PDFs are optional. `python tools/build_pdf.py` builds the full reference and `python tools/build_pdf.py --short` builds the two-page version; both need the `markdown` package and Chrome or Edge.
