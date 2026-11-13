# Launch Checklist

**Home page:** [launch-checklist-skill.pages.dev](https://launch-checklist-skill.pages.dev/)

Get a launch checklist written for your project, not for every project. This open skill inspects your repository and live site, asks only what it cannot see, and writes a tracked checklist of what blocks launch, what can wait and what does not apply to you.

## What it does

- Inspects an available repository and live site read-only, and sets each status from what it finds.
- Classifies the project by type, risk, jurisdiction and whether a bad release can be undone.
- Selects the items a project fact calls for, and lists the rest as not applicable with a reason.
- Opens the official page before stating any legal, store or provider rule, and records the address and date.
- Writes `LAUNCH_CHECKLIST.md` with priorities, launch blockers, dependencies, verification steps and evidence, and updates the same file when run again.

The library holds 439 items. Fifteen core categories cover legal and compliance, infrastructure, security, SEO, accessibility, quality assurance, monitoring, performance, email, documentation, marketing, backups, account ownership, cost and production hygiene. Fifteen project-type files cover websites and web apps, SaaS, e-commerce, APIs, mobile apps, desktop apps, browser extensions, AI and machine learning, data projects, open-source projects, developer tools, internal software, self-hosted software, cloud infrastructure and IoT. A launch runbook adds lead times, a timeline, launch-day steps and rollback triggers.

## Install

In Claude Code, use either the plugin or a copied skill folder, not both, or the skill is listed twice.

### Claude Code

Add the repository marketplace and install the plugin:

```text
/plugin marketplace add Achal13jain/launch-checklist-skill
/plugin install launch-checklist@launch-checklist
```

Invoke it directly with `/launch-checklist:launch-checklist`, or ask Claude Code a launch question. To use a copied folder instead, put `skills/launch-checklist` in `~/.claude/skills/` for all your projects, or in a repository's `.claude/skills/`.

### Skills CLI

One command installs the skill into the agents you choose:

```bash
npx skills add Achal13jain/launch-checklist-skill
```

Choose an agent with `-a`, for example `-a claude-code`, and add `-g` to install it for all your projects.

### Codex

Codex reads personal skills from `~/.agents/skills` and a repository's skills from `.agents/skills`:

```bash
git clone https://github.com/Achal13jain/launch-checklist-skill.git
mkdir -p ~/.agents/skills
cp -r launch-checklist/skills/launch-checklist ~/.agents/skills/
```

Mention it with `$launch-checklist`, or run `/skills` to pick it.

### Gemini CLI

```bash
gemini skills install https://github.com/Achal13jain/launch-checklist-skill.git --path skills/launch-checklist
```

Add `--scope workspace` to install it for the current project only, and enter `/skills reload` in a running session.

### GitHub Copilot CLI

Copilot reads personal skills from `~/.copilot/skills` and a repository's skills from `.github/skills`:

```bash
git clone https://github.com/Achal13jain/launch-checklist-skill.git
mkdir -p ~/.copilot/skills
cp -r launch-checklist/skills/launch-checklist ~/.copilot/skills/
```

## Try it

- "I am launching my SaaS next month. What have I missed?"
- "Run a launch readiness check on this repository. Do not change anything."
- "We submit our app to the stores in two weeks. Give me only the launch blockers."
- "Update the launch checklist and export it to CSV for our tracker."

## Project contents

- `skills/launch-checklist/` is the portable skill: `SKILL.md`, twenty-one reference files, a checklist template and a script that converts a finished checklist to CSV.
- `.claude-plugin/` contains the Claude Code plugin and marketplace manifests.
- `docs/` contains the project home page and its local assets.
- `evals/evals.json` holds three test prompts.
- `tools/check_skill.py` runs the structural checks in CI. `tools/build_site.py` copies the item library into the home page. `tools/build_pdf.py` builds a printable PDF of the full library, or a two-page version with `--short`.

## Status

Version 0.1.0 is a first release for real-world use and feedback. It has passed structural checks only, and the three test prompts in `evals/` have not been run yet. The repository does not claim a reliability score. The skill has been written for Claude Code and has not yet been tried in other agents.

The official pages the skill verifies against are listed in `skills/launch-checklist/references/sources.md`, with the date each was last reached. A few could not be reached by an automated request and are marked as such.

## Safety

The skill inspects read-only by default. It does not change your repository, cloud accounts, DNS, store listings or production without explicit approval of that specific change. It probes only sites you own or are authorised to test, with ordinary single requests. It never prints secrets. It is not a lawyer or an auditor, and a finished checklist does not prove compliance.

## Privacy

The skill is Markdown plus one small script, `scripts/export_csv.py`, which reads a checklist file and writes a CSV file on your machine. It collects nothing and sends nothing anywhere by itself. What you share while using it goes to the AI tool you use it in, under that tool's terms. When it checks a law, a store policy or a provider's terms, it asks your AI tool to open that organisation's public page. The home page loads nothing from other sites and uses no analytics scripts; it remembers your light or dark choice in your browser.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) to report a wrong or missing item or to propose a change. Report security issues privately as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). Created and maintained by [Achal Jain](https://github.com/Achal13jain).
