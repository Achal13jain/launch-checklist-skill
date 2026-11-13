# Launch runbook

## Contents

- Items with outside lead time
- Launch styles
- Timeline
- Go or no-go meeting
- Launch day
- Rollback triggers
- After launch

## Items with outside lead time

These wait on another organisation, so their duration is outside the team's control. Identify the ones that apply during selection, put them at the top of the plan, and check the current waiting time at the provider's own page instead of quoting one from memory.

| Item | Why it takes time |
|---|---|
| Payment provider account activation and live mode | Business verification and document checks. |
| App store developer account enrolment | Identity or organisation verification before anything can be submitted. |
| App store and extension store review | Review queues, and rejections that need a resubmission. |
| Store pre-release testing requirements | Some stores require a testing period before production access. |
| OAuth consent screen or API scope verification | Provider review of sensitive scopes, sometimes with a security assessment. |
| Email sending domain reputation | New domains and addresses need gradual volume increase. |
| SMS or messaging sender registration | Telecom regulators or carriers approve sender identities and templates. |
| Code signing certificates | Identity validation by the certificate authority. |
| Trademark search and filing | Legal work, and official processing after filing. |
| Tax registration | Government processing. |
| Legal review of policies and contracts | Lawyer availability and revisions. |
| Security testing by an outside firm | Scheduling, testing and a retest after fixes. |
| Enterprise customer security questionnaires and agreements | Customer procurement cycles. |
| DNS changes and certificate issuance | Propagation and validation time. |
| Cloud quota increases | Provider approval. |
| Hardware certification (IoT) | Laboratory testing and regulatory approval. |

## Launch styles

| Style | Use it when | Effect on the checklist |
|---|---|---|
| Private beta | Invited users, feedback wanted | Legal, security and data items stay. Marketing, SEO and scale items move to After launch. |
| Soft launch | Public but unannounced | Everything user-facing is ready; announcement items wait. |
| Staged rollout | A percentage of users or regions first | Needs feature flags or store staged release, and a metric that decides when to widen. |
| Public launch | Announced on a date | Capacity, support staffing and rollback readiness become Blockers. |

Recommend a soft launch or staged rollout before any announced date when the release channel is irreversible or the risk profile is High.

## Timeline

Adapt the dates to the real launch date. Compress it for small projects, but keep the order.

**Four weeks or more before**
- Start every item with outside lead time.
- Decide the launch style, date, owner and success metrics.
- Complete the data map and decide which laws apply.

**Two weeks before**
- Feature freeze for launch scope. Only fixes from here.
- Full test pass on a production-like environment.
- Backups configured and one restore completed.
- Monitoring, alerts and error tracking live in production.
- Drafts of policies, announcement and support replies ready for review.

**One week before**
- Security and inspection findings fixed or accepted in writing.
- Load test at the expected peak.
- Production configuration reviewed: live keys, debug off, test data removed.
- Rollback rehearsed once.
- Go or no-go meeting scheduled.

**The day before**
- Go or no-go decision recorded.
- Final pre-launch check run from the checklist.
- On-call names, contact details and the rollback decision-maker confirmed.
- Avoid launching before a weekend or holiday unless people are available to respond.

## Go or no-go meeting

Decide with the checklist open. Go requires all of these:

- Every Blocker is Done with Verified evidence.
- Every open Before launch item has an owner, a date and an explicit acceptance of the risk.
- Rollback has been rehearsed and someone is named to call it.
- Monitoring shows a healthy baseline.
- Support and on-call cover is confirmed for launch day and the day after.

Record the decision, who made it and the date in section 12 of the checklist.

## Launch day

1. Confirm the baseline: error rate, latency and uptime before any change.
2. Take a fresh backup or confirm the latest one.
3. Deploy the release, or release the store build, or publish the package.
4. Run the production smoke test (item F10).
5. Complete one real end-to-end journey, including one real payment where payments exist.
6. Remove any launch gate: waitlist, maintenance page, `noindex`, feature flag.
7. Watch dashboards for the first hour before announcing.
8. Announce. Send email in batches where the list is large.
9. Keep one person watching errors, support and social channels, and one person free to fix.
10. Log every incident and decision with the time.

## Rollback triggers

Agree these before launch, with numbers, so nobody debates them under pressure. Typical triggers:

- A core journey (sign up, log in, pay, the main action) fails for real users.
- Error rate or latency stays above the agreed threshold for the agreed number of minutes.
- Any sign of data loss, data exposure or one user seeing another user's data.
- A payment or billing fault that charges users wrongly.
- Costs rising faster than the agreed ceiling.

For each trigger, write the response: roll back, turn off a feature flag, or fix forward. Name the person who decides. For irreversible channels, write what replaces rollback: halting a staged rollout, an expedited store update, a patch release, deprecating a package version, or a server-side kill switch.

## After launch

**First hour:** smoke test passes, errors and latency normal, signups and payments arriving, email delivering.

**First day:** review errors and support messages, check costs against forecast, confirm backups ran, confirm analytics events are arriving.

**First week:** triage feedback daily, fix high-severity bugs, check search indexing, check email deliverability and store reviews, review third-party quota use.

**Two weeks:** hold a review. What went well, what failed, which checklist items were missing, and which After launch items remain. Update the checklist file and close the launch.

**First month:** complete the After launch items, review costs and capacity, rotate any credentials shared during launch, and schedule the first restore test and dependency update.
