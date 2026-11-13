# Changelog

All notable changes to this project are recorded here. Versions follow semantic versioning: a major version for changes that alter the skill's stance or remove guidance, a minor version for new items or project types, and a patch version for corrections.

## 0.1.0 - 2026-11-13

- First version. `SKILL.md` runs seven steps: intake, classify, inspect, select, verify, write and hand over. It writes `LAUNCH_CHECKLIST.md` and updates the same file on later runs.
- A library of 439 items: fifteen core categories and fifteen project-type files, each item with an ID, a default priority, a reason and a verification step.
- Reference files for jurisdictions (India, the European Union, the United Kingdom and the United States), official sources with the date each was last reached, read-only inspection, the output format and a launch runbook.
- `scripts/export_csv.py` converts a finished checklist to CSV for task trackers.
- Packaged as a Claude Code plugin with its own marketplace, and installable with the skills CLI or by copying the folder. The README and home page also give install steps for Codex, Gemini CLI and GitHub Copilot CLI.
- A one-page home page in `docs/index.html` for Cloudflare Pages, with light and dark themes, three worked examples, a picker that filters the real item library, and copyable install commands and prompts. It loads nothing from other sites; its IBM Plex fonts are hosted in `docs/fonts/` under the SIL Open Font License.
- `tools/check_skill.py` for structural checks in CI, `tools/build_site.py` to copy the library into the home page, and `tools/build_pdf.py` to build a full PDF and a two-page short version.
