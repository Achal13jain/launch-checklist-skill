# Security policy

This project is a set of instructions for an AI assistant, plus one small script (`skills/launch-checklist/scripts/export_csv.py`) that reads a Markdown file and writes a CSV file. The script makes no network requests. The instructions can still cause harm if they are wrong. Examples of what counts as a security problem here:

- An instruction that could lead an assistant to change a repository, cloud account, DNS record, store listing or production system without the user's explicit approval.
- An instruction that could lead an assistant to probe, scan or load test a system the user does not own or is not authorised to test.
- An instruction that could make an assistant print, copy or commit a secret.
- A weakness that lets repository content or a fetched web page steer the skill against the user's interest (prompt injection).
- A real credential committed to this repository.

## Reporting a problem

Please do not open a public issue for a security problem. Report it privately through GitHub: open the repository's security tab and choose "Report a vulnerability". Include the prompt you used, what the assistant did, the surface you used (Claude Code or another agent) and the version of the skill.

The maintainer will acknowledge the report, keep you informed while it is being fixed, and credit you in the changelog unless you prefer otherwise.

## Supported versions

Only the latest release receives fixes.
