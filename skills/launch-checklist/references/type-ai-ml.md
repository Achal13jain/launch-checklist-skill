# AI applications, AI agents and machine learning projects

Model providers change their data retention, training use, regional availability, pricing and model retirement dates. Read the provider's current official page for each of these and record the URL and date; the sources reference lists where to start. AI regulation is also changing, so check the jurisdictions reference.

## Contents

- Applications built on language models
- AI agents
- Trained and fine-tuned models

## Applications built on language models

- [ ] **AI1 [CRITICAL] Build an evaluation set and pass it before launch.** Collect realistic inputs with expected outcomes, including hard and adversarial cases, and score the product against them. Why: without a fixed test set, nobody knows whether a prompt or model change made things better or worse. Verify: the evaluation runs with one command, the scores are recorded with the model and prompt version, and they meet a written threshold.
- [ ] **AI2 [CRITICAL] Test for prompt injection and treat model output as untrusted.** Try instructions hidden in user input, uploaded files, web pages and retrieved documents. Never let model output directly run code, build queries, render as HTML or call tools without validation. Why: text the model reads can redirect it, and its output can carry an attack onward. Verify: a documented set of injection attempts fails to leak the system prompt, other users' data or unintended actions.
- [ ] **AI3 [CRITICAL] Confirm what the provider does with the data sent to it.** Check retention, use for training, who can access it, the processing region and the terms available for your plan. Why: this decides what may be sent and what the privacy policy must say. Verify: the provider's current data usage page and your account settings are recorded with the date, and the privacy policy matches. Needs: A1.
- [ ] **AI4 [CRITICAL] Limit usage and cost per user.** Set per-user and global limits on requests and tokens, cap output length, and alert on unusual spend. Why: an AI feature without limits can be drained by one script. Verify: exceed the limit with a test account and confirm refusal, and confirm the provider-side spending limit. Needs: N1.
- [ ] **AI5 [HIGH] Measure and reduce wrong answers.** Test factual accuracy on questions with known answers, ground answers in supplied sources where possible, show sources, and state the limits to users. Why: confident wrong answers are the main trust and liability problem. Verify: the evaluation set includes factual checks and unanswerable questions, with a recorded error rate.
- [ ] **AI6 [HIGH] Filter harmful input and output.** Decide what content the product must refuse or route to a person, and test it. Why: users will try, and some content brings legal or reputational harm. Verify: a set of harmful prompts produces refusals or safe responses.
- [ ] **AI7 [HIGH] Tell users they are dealing with AI and label generated content.** Why: users expect it, and several jurisdictions and stores require transparency. Verify: the disclosure is visible at the point of interaction. Needs: A2.
- [ ] **AI8 [HIGH] Keep personal data and secrets out of prompts and logs unless needed.** Minimise what is sent, redact where possible, and apply the retention schedule to stored conversations. Why: prompts and logs become a second copy of sensitive data. Verify: inspect logged prompts for a test conversation containing personal data.
- [ ] **AI9 [HIGH] Handle provider failure.** Set timeouts, retries with backoff, a fallback model or a clear message, and handle rate limit responses. Why: provider outages and rate limits are routine. Verify: block the provider in staging and observe the behaviour.
- [ ] **AI10 [HIGH] Pin model versions and plan for retirement.** Use a dated model version, record the provider's retirement date and re-run the evaluation before moving. Why: providers retire models, and an alias can change behaviour without notice. Verify: the configuration names an exact version, and the provider's deprecation page is recorded with the date.
- [ ] **AI11 [HIGH] Version prompts and configuration.** Keep prompts in version control and tie each release to a prompt and model version. Why: a prompt change is a behaviour change and needs the same care as code. Verify: the running prompt version can be identified and rolled back.
- [ ] **AI12 [HIGH] Measure latency and stream where it helps.** Why: slow answers feel broken. Verify: record the time to first output and total time at the 95th percentile.
- [ ] **AI13 [HIGH] Test retrieval quality and access control.** If: the product retrieves documents to answer questions. Check that retrieval returns relevant passages and only documents the current user may see. Why: retrieval can leak one customer's documents into another's answer. Verify: a user without access to a document cannot get an answer drawn from it.
- [ ] **AI14 [MEDIUM] Collect feedback and review real conversations within the privacy rules.** Why: real use differs from the test set. Verify: a feedback control exists and a review routine is scheduled.
- [ ] **AI15 [MEDIUM] Check the provider's usage policies and your right to the output.** Why: some uses are restricted, and terms differ on output ownership. Verify: the use case is checked against the provider's current usage policy.

## AI agents

- [ ] **AGT1 [CRITICAL] Give the agent the least access it needs.** Scope each tool, credential and data source narrowly, and separate read from write. Why: an agent with broad access turns one bad instruction into broad damage. Verify: list every tool and credential with its scope, and confirm none is wider than its task.
- [ ] **AGT2 [CRITICAL] Require human approval for irreversible or outward-facing actions.** Cover sending messages, spending money, deleting data and changing production. Why: agents make mistakes and can be manipulated. Verify: attempt each such action and confirm it waits for approval.
- [ ] **AGT3 [CRITICAL] Bound every run.** Limit steps, time, spend and retries, and stop on repeated failure. Why: a looping agent burns money and can repeat a harmful action. Verify: force a loop and confirm it stops at the limit.
- [ ] **AGT4 [HIGH] Log every action with enough detail to audit and undo.** Why: when an agent does something unexpected, the record is the only way to understand and reverse it. Verify: reconstruct a full run from the logs.
- [ ] **AGT5 [HIGH] Isolate code execution and browsing.** If: the agent runs code or browses. Use a sandbox with no access to secrets or the internal network. Why: executed code and web pages are untrusted input. Verify: from inside the sandbox, attempts to reach internal addresses and credentials fail.
- [ ] **AGT6 [HIGH] Test the agent on realistic multi-step tasks, including failure.** Why: single-step tests do not show how errors compound. Verify: a task suite with recorded success rates, including tool errors and misleading content.
- [ ] **AGT7 [HIGH] Provide a way to stop and take over.** Why: the operator needs an immediate stop. Verify: stop a running agent and confirm no further actions occur.

## Trained and fine-tuned models

- [ ] **ML1 [CRITICAL] Evaluate on held-out data that reflects production.** Keep test data separate from training data and check for leakage between them. Why: leaked or unrepresentative test data gives scores that collapse in production. Verify: the split method is documented and the metrics are reproducible.
- [ ] **ML2 [CRITICAL] Confirm the right to use the training data and the base model.** Check dataset licences, consent for personal data and the base model's licence terms for the intended use. Why: data and model licences restrict commercial use more often than expected. Verify: a record lists each dataset and model with its licence and source. Needs: A12.
- [ ] **ML3 [HIGH] Check data quality.** Validate schema, ranges, missing values, duplicates and label quality, and document known gaps. Why: data faults become model faults that are hard to trace. Verify: automated data checks run before training and their report is saved.
- [ ] **ML4 [HIGH] Evaluate fairness across relevant groups.** If: the model affects people. Compare performance across groups and document the findings and mitigations. Why: uneven performance causes harm and, in some uses, legal exposure. Verify: a report shows the metrics by group.
- [ ] **ML5 [HIGH] Make training reproducible.** Version the code, data, configuration, random seeds and environment. Why: a model that cannot be rebuilt cannot be fixed or audited. Verify: retraining from the recorded versions gives comparable metrics.
- [ ] **ML6 [HIGH] Version and register models, with a rollback path.** Why: production needs to return to the previous model quickly. Verify: the serving system can switch to the prior version, and that switch has been tested.
- [ ] **ML7 [HIGH] Benchmark inference latency, throughput and resource needs.** Test on the production hardware at expected load. Why: a model that is accurate but too slow or costly cannot ship. Verify: a benchmark report gives latency percentiles and cost per thousand predictions.
- [ ] **ML8 [HIGH] Monitor the model in production.** Track input drift, prediction distribution, quality against delayed labels where available, and data pipeline health. Why: model quality decays as the world changes, without any error being raised. Verify: drift and quality dashboards exist with alerts.
- [ ] **ML9 [HIGH] Define the fallback when the model is unavailable or unsure.** Use a rule, a simpler model, a default or a human. Why: the product must still work. Verify: disable the model in staging and observe the result.
- [ ] **ML10 [MEDIUM] Document the model.** Intended use, limits, training data summary, metrics and known failure cases. Why: users and reviewers need to know what the model is for. Verify: a model card or equivalent is published or available.
- [ ] **ML11 [MEDIUM] Track training and inference cost.** Why: compute cost grows quietly. Verify: cost per training run and per month of inference is recorded with a budget alert.
- [ ] **ML12 [HIGH] Test robustness.** Feed malformed, out-of-range and adversarial inputs. Why: production inputs are messier than test data. Verify: the service returns a controlled error or a flagged low-confidence result.
