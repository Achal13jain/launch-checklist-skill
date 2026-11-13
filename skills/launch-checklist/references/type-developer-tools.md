# Developer platforms, SDKs, libraries and CLI tools

A published package version is permanent in practice. Registries restrict or forbid removing versions, and other people's builds depend on them, so a release needs the care of an irreversible change. Read the open-source file as well when the code is public, and the API file when the tool wraps a service.

## Libraries and SDKs

- [ ] **DEV1 [CRITICAL] Define the public API surface and mark the rest as internal.** Why: anything exported becomes something users depend on. Verify: the documented surface matches the exports, and internal modules are clearly marked or hidden.
- [ ] **DEV2 [CRITICAL] Follow semantic versioning and decide when to release the first stable version.** Why: users set their dependency ranges from the version number. Verify: the versioning policy is written, and the release matches it.
- [ ] **DEV3 [CRITICAL] Inspect the package contents before publishing.** Build the package and list what it contains. Why: packages often ship secrets, tests, source maps or miss the built files. Verify: install the built package into an empty project and use it, and confirm no secret or unwanted file is inside.
- [ ] **DEV4 [CRITICAL] Secure the registry account and publish from CI.** Use two-factor login and the registry's trusted publishing or scoped tokens. Why: a stolen publishing token lets an attacker ship malware to every user. Verify: publishing works only from the release pipeline. Needs: OSS12.
- [ ] **DEV5 [HIGH] Test against the supported runtime and platform matrix.** Cover language versions, operating systems and module formats. Why: users run combinations the author never did. Verify: CI runs the matrix and the supported versions are documented.
- [ ] **DEV6 [HIGH] Keep dependencies few and ranges sensible.** Why: every dependency is passed on to users as size, risk and conflict. Verify: review the dependency list and its licences.
- [ ] **DEV7 [HIGH] Provide types, examples and reference documentation.** Why: developers judge a library by how fast they reach a working call. Verify: each public function has documentation and a tested example.
- [ ] **DEV8 [HIGH] Write errors that say what went wrong and what to do.** Why: clear errors reduce support requests. Verify: trigger the common mistakes and read the messages.
- [ ] **DEV9 [HIGH] Publish a deprecation policy and migration guides.** Why: users need a path through breaking changes. Verify: the policy is in the documentation.
- [ ] **DEV10 [MEDIUM] Keep SDKs for several languages consistent.** If: the platform ships more than one SDK. Why: differing behaviour between SDKs confuses teams. Verify: the same test scenarios pass in each SDK.
- [ ] **DEV11 [MEDIUM] Disclose any telemetry and make it opt-out or opt-in.** Why: developers react strongly to undisclosed data collection in their tools. Verify: the documentation states what is sent and how to disable it.

## CLI tools

- [ ] **CLI1 [HIGH] Follow command-line conventions.** Provide help and version output, meaningful exit codes, errors on the error stream, and no prompts when input is not a terminal. Why: scripts and pipelines depend on these. Verify: run the tool in a script and check the exit codes for success and failure.
- [ ] **CLI2 [HIGH] Offer machine-readable output and a quiet mode.** Why: people automate CLI tools. Verify: the structured output parses, and colour is disabled when output is piped.
- [ ] **CLI3 [CRITICAL] Protect users from destructive commands.** Ask for confirmation, offer a dry run and require an explicit flag for irreversible actions. Why: a mistyped command should not destroy data. Verify: run each destructive command without the flag.
- [ ] **CLI4 [CRITICAL] Store credentials safely.** Use the operating system credential store or a file with restricted permissions, and keep tokens out of logs and shell history. Why: CLI tokens often carry wide access. Verify: inspect where the token is stored and its permissions.
- [ ] **CLI5 [HIGH] Test installation by each supported method on each operating system.** Cover package managers, install scripts and direct downloads, with checksums or signatures. Why: installation is the first point of failure. Verify: install on clean machines for each method.
- [ ] **CLI6 [MEDIUM] Provide an update path and an update notice.** Why: users keep old versions for years. Verify: an old version reports that a newer one exists.
- [ ] **CLI7 [MEDIUM] Add shell completion and a clear configuration order.** Document how flags, environment variables and configuration files override each other. Why: reduces friction and confusion. Verify: completion works in the main shells.

## Developer platforms

- [ ] **PLAT1 [HIGH] Build self-service onboarding.** Sign-up, key creation, a quick start and a first successful call without contacting anyone. Why: developers leave when blocked. Verify: time a new developer from sign-up to first call.
- [ ] **PLAT2 [HIGH] Provide a sandbox, sample applications and a console.** Why: developers want to try before integrating. Verify: the samples run against the sandbox.
- [ ] **PLAT3 [HIGH] Publish status, changelog and support channels.** Why: integrators need to know about incidents and changes. Verify: each is linked from the documentation.
- [ ] **PLAT4 [HIGH] Publish the terms for developers.** Acceptable use, limits, pricing, data handling and what happens on suspension. Why: businesses assess these before building on a platform. Verify: the terms are linked at sign-up.
