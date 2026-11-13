# Inspection

Gather evidence before asking questions. Everything here is read-only. Probe only systems the user owns or is authorised to test, with ordinary single requests.

## Contents

- Repository signals
- Live site probes
- DNS and email probes
- Store and registry listings
- What inspection cannot show

## Repository signals

Read these when a repository is available, and record the file and line as evidence.

| Look at | It tells you |
|---|---|
| README, docs folder | Purpose, audience, install steps, stated limitations. |
| Package manifests and lockfiles | Stack, frameworks, outdated or abandoned dependencies, licence field. |
| Deployment files (Dockerfile, platform config, infrastructure code, CI workflows) | Hosting, environments, how a release happens, whether rollback exists. |
| Environment examples (`.env.example`) and config loaders | Third-party services in use, which secrets exist, whether production differs from development. |
| Committed secrets | Search for `.env` files, private keys and tokens in the tree and in git history. Report the location, never the value. |
| Auth code and middleware | Session handling, password hashing, role checks, rate limiting. |
| Database schema and migrations | Personal data fields, tenant columns, soft deletes, migration safety. |
| Payment and webhook handlers | Signature verification, idempotency, test versus live keys. |
| Email and notification code | Providers, templates, unsubscribe handling. |
| Analytics and tracking snippets | Which trackers load, and whether they wait for consent. |
| AI calls | Providers, models, what user data is sent, limits, logging. |
| Tests and CI | What is covered, whether checks block merges, whether the release commit is green. |
| Public folder | `robots.txt`, sitemap, favicon, `security.txt`, source maps, leftover test pages. |
| LICENSE, NOTICE, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT | Open-source readiness. |
| App manifests (`AndroidManifest.xml`, `Info.plist`, extension `manifest.json`) | Permissions requested, versions, identifiers. |
| Placeholder text | Search for lorem ipsum, TODO, example.com, test accounts and debug flags. |

If dependency audit tooling is already installed (for example `npm audit` or `pip-audit`), run it in report mode. Install nothing without asking.

## Live site probes

Run these against the production URL, and against staging when it exists. Each is one ordinary request.

| Check | How | Supports |
|---|---|---|
| HTTP redirects to HTTPS | `curl -sI http://HOST` | B3 |
| One canonical host | `curl -sI https://www.HOST` and the bare host | B4 |
| Certificate validity and expiry | `curl -vI https://HOST` or the browser padlock | B2 |
| Security headers | `curl -sI https://HOST`, read the header list | C10 |
| Cookie flags | Response `Set-Cookie` headers | C11 |
| robots.txt and sitemap | Fetch `/robots.txt` and `/sitemap.xml` | D3, D4 |
| Indexing directives | Look for `noindex` in headers and page source, on production and staging | D4, O5 |
| Titles, descriptions, canonical, Open Graph | Read the page source of the main pages | D1, D2, D5 |
| Error pages | Request a path that does not exist | B11, E9 |
| Disclosure contact | Fetch `/.well-known/security.txt` | C16 |
| Exposed files | Request `/.env`, `/.git/config` and a `.map` file for a main script, once each | C12, O4 |
| Legal pages | Follow footer links to privacy, terms, refund and contact pages | A3, A4, A10 |
| Trackers before consent | Load the page in a clean browser profile and list cookies and third-party requests before interacting | A5, G2 |
| Health endpoint | Request the documented health path | B13 |

When browser tooling is available, also run an accessibility scan and a Lighthouse audit on the main pages and record the scores with the date.

## DNS and email probes

| Check | How | Supports |
|---|---|---|
| SPF | `nslookup -type=txt DOMAIN`, look for a record starting `v=spf1` | I2 |
| DMARC | `nslookup -type=txt _dmarc.DOMAIN` | I2 |
| DKIM | Needs the selector from the email provider; ask the user or read the provider setup | I2 |
| Mail routing | `nslookup -type=mx DOMAIN` | I6 |
| Certificate authority restriction | `nslookup -type=caa DOMAIN` | B2 |

## Store and registry listings

When the product is already listed, read the public listing: store page, package registry page, extension store page. Check the name, description, screenshots, privacy link, declared data use, permissions, version and last update against what the code does.

## What inspection cannot show

Ask the user about these, because no file or request reveals them:

- Where the business is registered and where users are.
- Whether backups have been restored successfully.
- Who has access to the registrar, cloud, code host, payment and store accounts, and whether two-factor login is on.
- Whether billing alerts and spending caps are set.
- Vendor agreements, tax registration and legal review.
- Who is on call on launch day and who can call a rollback.

Record each answer as Stated, with the date.
