# Output format

## Contents

- Item format
- Fields
- Launch gates
- Evidence labels
- Output structure
- Rules that keep the output usable

## Item format

Write every item in the checklist file exactly like this, so the export script and task trackers can read it:

```markdown
- [ ] **B3 [CRITICAL] Force HTTPS on every production host**
  - Description: Redirect all HTTP requests to HTTPS and send an HSTS header.
  - Why: Protects data in transit and stops browsers from using an insecure connection.
  - Verification: Request the http address and confirm a redirect to https; inspect the response headers.
  - Category: Domain, Infrastructure and Deployment
  - Gate: Blocker
  - Depends on: B1, B2
  - Status: Not Started
  - Owner:
  - Due:
  - Evidence: Checked 2026-11-10, http://example.com returned 200 with no redirect.
```

The reference files store each item on one line in a shorter form: title, an optional "If:" condition, a description, "Why:" and "Verify:". Expand that line into the fields above and rewrite the wording to name this project's real hosts, vendors and flows.

## Fields

| Field | Rule |
|---|---|
| Checkbox | Unchecked unless the status is Done. |
| ID | Keep the ID from the reference file. Use the prefix `X` for items you add. IDs never change between runs. |
| Priority | CRITICAL, HIGH, MEDIUM or LOW, adjusted for this project. |
| Task | Starts with a verb and names the specific thing. "Improve security" is not a task. |
| Description | What needs to be done, in one or two sentences. |
| Why | The consequence of skipping it, for this project. |
| Verification | An observable check another person could repeat. |
| Category | The category name from the core file, or the project type. |
| Gate | Blocker, Before launch, After launch or Not Applicable. |
| Depends on | IDs that must be done first. Leave empty when none. |
| Status | Not Started, In Progress, Done or Not Applicable. |
| Owner, Due | Leave empty unless the user gave them. |
| Evidence | What was observed, where and on what date. For facts about laws, stores and providers, the official URL and the date it was opened. |

## Launch gates

- **Blocker.** The product should not go live without it. Reserve this for legal obligations that apply, security and data integrity failures, broken core functionality, and anything that cannot be fixed after release.
- **Before launch.** Strongly recommended before launch. Skipping it is a decision the user should make knowingly.
- **After launch.** Safe to complete in the first days or weeks. Give a target such as "within two weeks".
- **Not Applicable.** Considered and ruled out. Always give the reason in one line.

Priority and gate are related but separate. A HIGH item can be After launch for a private beta, and a MEDIUM item can be a Blocker when the release channel cannot be reversed.

## Evidence labels

Label every project fact and every status so the user knows how far to trust it:

- **Verified:** seen in the repository, on the live site or at an official source during this run.
- **Stated:** the user said so.
- **Assumed:** a reasonable default that nobody has confirmed.

Set a status to Done only on Verified evidence. A user statement moves an item to In Progress with "confirm" in the Evidence field, unless the item can only ever be confirmed by the user.

## Output structure

Use these sections, in this order:

1. **Project Overview.** A table: product, project types, audience, business model, stack, hosting and distribution, data handled, accounts and payments, third-party services, team, launch date and style. Each row labelled Verified, Stated or Assumed.
2. **Assumptions and Missing Information.** What was assumed, and what answer would change the checklist.
3. **Launch Readiness Summary.** Risk profile, reversibility, counts per gate and per status, a one-paragraph verdict, and the items with outside lead time.
4. **Critical Launch Blockers.** The Blocker items in dependency order, in full format.
5. **Complete Categorized Checklist.** Core categories A to O.
6. **Project-Specific Technical Checklist.** The items from each type file, grouped by type.
7. **Security and Privacy Audit.** A summary table that points to item IDs, plus findings from inspection.
8. **Testing and Quality Assurance Plan.** What to test, in which environment, in what order, pointing to item IDs.
9. **Deployment and Rollback Plan.** The steps for this project's release channel, the rollback trigger and who can call it.
10. **Post-Launch Monitoring Checklist.** First hour, first day, first week, first month.
11. **Recommended Tools and Services.** Only where a tool removes real work for this project. Prefer what the project already uses. Say when no tool is needed.
12. **Final Go-Live Approval Checklist.** Sign-off lines for the people who must agree.

End with **Final pre-launch check**: a compact list of at most twenty items to verify immediately before launch, each one line with its ID.

For a large project, split sections 5 and 6 into phases: Foundation (legal decisions, accounts, long lead time), Build (implementation), Verify (testing and inspection), Launch (launch day), Stabilise (after launch).

## Rules that keep the output usable

- State each item once. Sections 7 to 10 refer to IDs; they do not restate items.
- Put the Not Applicable list at the end of section 5, one line per item with its reason.
- Keep legal obligations and good practice visibly separate. Use "Legal obligation where (condition)" or "Good practice" in the Why field for category A items.
- Name real things: the actual domain, the actual payment provider, the actual store. Generic wording is a sign that inspection was skipped.
- Write for copying. Plain Markdown, no nested tables inside list items, no HTML.
