# Core checklist

Items common to most launches. Each line holds an ID, a default priority, the task, an optional "If:" condition, a description, the reason and a verification step. Priorities are defaults; adjust them for the project as SKILL.md describes. Expand each selected line into the full item format from the output format reference.

## Contents

- A. Legal, Compliance and Policies
- B. Domain, Infrastructure and Deployment
- C. Security
- D. SEO and Search Visibility
- E. UI, UX and Accessibility
- F. Functionality and Quality Assurance
- G. Analytics, Tracking and Monitoring
- H. Performance and Optimization
- I. Communication and Transactional Email
- J. Documentation and Support
- K. Launch and Marketing Preparation
- L. Backup, Recovery and Business Continuity
- M. Accounts and Ownership
- N. Cost and Capacity
- O. Production Hygiene

## A. Legal, Compliance and Policies

Nothing in this category makes a product compliant by being published. Compliance comes from what the product actually does with data and money. Which laws apply depends on the business location, the users' locations, the data and the business model; use the jurisdictions reference and verify at the source.

- [ ] **A1 [CRITICAL] Map the personal data the product handles.** If: any personal data is collected, including emails, IP addresses and analytics identifiers. List each data field, its purpose, where it is stored, which vendors receive it and how long it is kept. Why: every policy, consent and deletion decision depends on this map. Verify: the map exists and matches the database schema, the forms and the third-party requests seen in inspection.
- [ ] **A2 [CRITICAL] Decide in writing which laws apply.** Record the business location, user locations, data types and business model, then list each law considered and why it applies or does not. Why: legal duties follow these facts, and guessing leads to both gaps and wasted work. Verify: a short note exists, cites official sources with dates, and has had legal review when the risk profile is High or Critical. Needs: A1.
- [ ] **A3 [CRITICAL] Publish a privacy policy that matches the data map.** If: personal data is collected. Describe what is collected, why, who receives it, retention, user rights and a contact. Why: required by most privacy laws and by app and extension stores; an inaccurate policy is itself a liability. Verify: every flow in A1 appears in the policy, and it is linked from the footer, sign-up screens and store listings. Needs: A1, A2.
- [ ] **A4 [HIGH] Publish terms of service.** If: users create accounts, pay or post content. Cover acceptable use, liability, termination, governing law and changes to the terms. Why: sets the contract with users and supports enforcement against abuse. Verify: the terms are linked at sign-up and checkout, and acceptance is recorded with a timestamp and version.
- [ ] **A5 [HIGH] Inventory cookies and trackers, and gate them on consent where the law requires.** If: the product sets non-essential cookies or loads third-party trackers. List each cookie and tracker with its purpose, and block the non-essential ones until the user agrees where consent is required. Why: consent rules vary by jurisdiction and regulators check this on a first visit. Verify: load the site in a clean browser profile and confirm that no non-essential cookie or tracker request appears before consent. Needs: A2.
- [ ] **A6 [CRITICAL] Provide working flows for user data rights.** If: a privacy law identified in A2 grants them. Let users access, correct, export and delete their data and withdraw consent, through the product or a monitored contact. Why: these are enforceable rights under several laws, with response deadlines. Verify: perform each request with a test account and confirm the data changes or is removed in the database and in vendor systems. Needs: A1, A2.
- [ ] **A7 [HIGH] Record consent.** If: any processing relies on consent. Store what the user agreed to, the wording version and the time, and honour withdrawal. Why: consent that cannot be shown is hard to rely on. Verify: a consent record exists for a new test user and changes when consent is withdrawn.
- [ ] **A8 [HIGH] Set and implement a retention and deletion schedule.** If: personal data is stored. Decide how long each data type is kept, including logs and backups, and automate deletion. Why: keeping data without a purpose increases breach impact and breaks minimisation rules. Verify: the schedule is written down and a job or procedure enforces it.
- [ ] **A9 [HIGH] Put agreements in place with vendors that process personal data.** If: personal data is sent to hosting, email, analytics, AI or support vendors. Sign each vendor's data processing terms and keep a list of sub-processors. Why: required under several privacy laws and requested by business customers. Verify: a vendor list exists with a link to each signed or accepted agreement.
- [ ] **A10 [HIGH] Write the breach notification procedure.** If: personal data is stored. Name who assesses an incident, who must be notified and within what time under each applicable law. Why: deadlines are short and differ by jurisdiction. Verify: the procedure names people and cites the official source and date for each deadline. Needs: A2.
- [ ] **A11 [CRITICAL] Publish refund and cancellation terms.** If: the product takes payment. State when refunds are given, how to cancel and how renewals work. Why: consumer law and payment providers expect clear terms, and unclear terms cause disputes. Verify: the policy is linked at checkout and matches how the billing system behaves in a test cancellation and refund.
- [ ] **A12 [HIGH] Confirm ownership or licence of everything shipped.** Check code, fonts, images, icons, music, datasets and copy, including work done by contractors. Why: unlicensed assets lead to takedowns and claims. Verify: an asset list records the licence or assignment for each third-party item.
- [ ] **A13 [HIGH] Comply with open-source licences.** If: the product includes third-party open-source code. Generate a dependency licence report, resolve licences that conflict with the distribution model and include required notices. Why: some licences impose conditions on distribution. Verify: a licence report exists and a notices file ships with the product.
- [ ] **A14 [MEDIUM] Check the product name and secure the identifiers.** Search trademark registers in the main markets, and confirm the domain, store name and social handles are held. Why: a name conflict after launch forces a rebrand. Verify: the search results are saved and the accounts are registered to the business.
- [ ] **A15 [HIGH] Handle tax registration and invoicing.** If: the product sells anything. Confirm the registration, tax collection and invoice requirements for each market sold into. Why: tax duties can begin with the first sale in a market. Verify: an accountant or the tax authority's page confirms the position, and a test purchase produces a correct invoice.
- [ ] **A16 [HIGH] Decide how children are handled.** If: children could plausibly use the product. Set a minimum age, add age checks or parental consent as the applicable laws require, and avoid tracking or targeting children. Why: children's data carries stricter rules in most jurisdictions and in store policies. Verify: the sign-up flow enforces the decision, and the decision cites the official sources. Needs: A2.
- [ ] **A17 [MEDIUM] Check accessibility obligations and publish a statement.** If: the product serves the public, government or education. Find out whether an accessibility law applies and state the conformance target and a contact for problems. Why: accessibility is a legal requirement for some products and markets. Verify: the statement is published and matches the result of item E8. Needs: A2.
- [ ] **A18 [HIGH] Set rules and a takedown route for user content.** If: users can post or upload content. Publish acceptable use rules, a way to report content, a takedown process and any grievance contact the law requires. Why: platforms carry duties for content they host, and abuse arrives early. Verify: submit a test report and confirm it reaches a person who can act.
- [ ] **A19 [MEDIUM] Add the disclaimers the product needs.** If: the product gives health, financial or legal information, uses affiliate links, or shows AI-generated output. Place each disclaimer where the user meets the content. Why: reduces the chance that users rely on content in ways it was not built for. Verify: each disclaimer is visible in the relevant screen.
- [ ] **A20 [HIGH] Get professional legal review.** If: the risk profile is High or Critical, or the product handles regulated data, children's data or cross-border transfers. Have a qualified lawyer review A2 and the published policies. Why: this skill and generic templates cannot give legal advice. Verify: the review is dated and its findings are tracked as items.

## B. Domain, Infrastructure and Deployment

- [ ] **B1 [CRITICAL] Configure and document DNS for the production domain.** Set the records for the site, API, email and verification, and note what each is for. Why: a wrong or forgotten record takes the product or its email offline. Verify: each record resolves as documented from an outside network.
- [ ] **B2 [CRITICAL] Serve a valid TLS certificate that renews automatically.** Cover every production host, including API and asset subdomains. Why: an expired certificate blocks all users. Verify: inspect the certificate for each host and confirm the renewal mechanism and expiry date.
- [ ] **B3 [CRITICAL] Force HTTPS on every production host.** Redirect HTTP to HTTPS and send an HSTS header. Why: protects data in transit. Verify: request the http address and confirm a redirect, then read the response headers. Needs: B2.
- [ ] **B4 [HIGH] Redirect to one canonical host.** Choose www or the bare domain and redirect the other with a permanent redirect. Why: duplicate hosts split search ranking and break cookies. Verify: request both hosts and confirm one redirects to the other.
- [ ] **B5 [CRITICAL] Run production as a separate environment with its own configuration.** Use separate databases, keys and storage from development and staging. Why: shared resources let test activity damage real data. Verify: production configuration points to no development or staging resource.
- [ ] **B6 [CRITICAL] Keep secrets in a secret store, outside the repository and the client bundle.** Load them from the platform's secret manager or environment at runtime. Why: leaked secrets are a common cause of breaches. Verify: the repository, build output and browser bundle contain no secret values.
- [ ] **B7 [CRITICAL] Provision the production database with restricted access.** Apply all migrations, limit network access to the application, and use a least-privilege database user. Why: an open or drifted database risks exposure and failed deploys. Verify: the schema matches the migrations and the database refuses connections from outside the allowed network.
- [ ] **B8 [HIGH] Make deployment repeatable.** Deploy through a script or pipeline from a tagged commit, with no manual steps on the server. Why: manual deploys fail in ways nobody can reproduce. Verify: a second person can deploy by following the written steps.
- [ ] **B9 [CRITICAL] Write and rehearse the rollback procedure.** Define how to return to the previous version, including what happens to database changes. Why: a rollback tried for the first time during an incident often fails. Verify: perform one rollback in staging or production and record how long it took. Needs: B8.
- [ ] **B10 [HIGH] Keep database migrations compatible with the previous version.** Add before removing, in separate releases. Why: an incompatible migration makes rollback impossible. Verify: the previous application version runs against the migrated schema.
- [ ] **B11 [MEDIUM] Configure the CDN and cache headers.** If: the product serves static assets or cacheable pages. Cache static files with versioned names and keep private responses uncached. Why: improves speed and prevents private pages from being cached publicly. Verify: read the cache headers on an asset and on a logged-in page.
- [ ] **B12 [MEDIUM] Provide custom error and maintenance pages.** Cover not found, server error and planned maintenance. Why: raw server errors leak details and leave users stuck. Verify: trigger each page in production.
- [ ] **B13 [HIGH] Monitor uptime from outside.** Check the main page and a health endpoint from an external service that alerts a person. Why: the team should know about an outage before users report it. Verify: stop a staging instance and confirm the alert arrives. Needs: B14.
- [ ] **B14 [HIGH] Expose a health check that tests real dependencies.** Report whether the application can reach its database and critical services. Why: a process can be running while the product is broken. Verify: the endpoint fails when the database is unreachable.
- [ ] **B15 [HIGH] Confirm background jobs, queues and schedules run in production.** If: the product uses them. Check that workers start, schedules fire once, and failures are retried and reported. Why: background work fails silently. Verify: trigger each job in production and see it complete and log.

## C. Security

- [ ] **C1 [CRITICAL] Require authentication on every non-public route and API endpoint.** Apply the check centrally so new routes are protected by default. Why: one unprotected endpoint exposes data. Verify: request each private route without a session and confirm it is refused.
- [ ] **C2 [CRITICAL] Enforce authorisation on every object.** Check on the server that the current user or tenant owns each record read or changed. Why: changing an identifier in a request is one of the most common ways to reach other users' data. Verify: with two test accounts, try to read and modify the other account's records by ID and confirm refusal.
- [ ] **C3 [CRITICAL] Store passwords with a current password hashing algorithm, or delegate login to an identity provider.** If: the product has its own passwords. Why: weak hashing turns a database leak into account takeovers. Verify: inspect the stored hash format and the library used.
- [ ] **C4 [HIGH] Require multi-factor authentication for administrators, and offer it to users where accounts hold value.** Why: stolen passwords are common. Verify: an administrator account cannot sign in without the second factor.
- [ ] **C5 [CRITICAL] Rate-limit authentication and expensive endpoints.** Cover login, sign-up, password reset, verification codes, search, uploads and anything that costs money per call. Why: stops credential guessing, abuse and runaway bills. Verify: exceed the limit from one client and confirm requests are refused.
- [ ] **C6 [HIGH] Protect public forms from bots and spam.** If: the product has public sign-up, contact or comment forms. Why: spam sign-ups damage email reputation and data quality. Verify: an automated submission is blocked or flagged.
- [ ] **C7 [CRITICAL] Validate input on the server and use parameterised queries.** Why: prevents injection and corrupt data; client-side checks can be bypassed. Verify: send malformed and hostile input directly to the API and confirm it is rejected, and confirm no query is built by joining strings.
- [ ] **C8 [CRITICAL] Protect against cross-site scripting and request forgery.** Encode output, sanitise any rendered user HTML, and use anti-forgery tokens or same-site cookies for state-changing requests. Why: these attacks let others act as the user. Verify: stored script input is rendered as text, and a forged cross-site request is refused.
- [ ] **C9 [HIGH] Restrict cross-origin access to known origins.** Why: a wildcard with credentials lets any site call the API as the user. Verify: a request from an unlisted origin receives no permissive header.
- [ ] **C10 [HIGH] Send security headers.** Set a content security policy, HSTS, content type options, frame restrictions and a referrer policy. Why: they limit the damage of other flaws. Verify: read the response headers and run a header scanner.
- [ ] **C11 [CRITICAL] Secure sessions and cookies.** Mark session cookies Secure, HttpOnly and SameSite, expire them, rotate the session on login, and invalidate it on logout and password change. Why: weak sessions allow account takeover. Verify: inspect the cookie flags, and confirm an old session stops working after logout and after a password change.
- [ ] **C12 [CRITICAL] Scan the repository and its history for secrets, and rotate any found.** Why: a secret that was ever committed must be treated as leaked. Verify: a secret scan of the full history is clean, and rotated keys are confirmed as revoked.
- [ ] **C13 [HIGH] Scan dependencies and fix known serious vulnerabilities.** Why: vulnerable packages are exploited automatically. Verify: the audit report shows no unaddressed critical or high finding, and automated update alerts are on.
- [ ] **C14 [HIGH] Secure file uploads.** If: users upload files. Limit type and size, store outside the web root or in object storage, serve from a separate domain or with a download header, and scan where the risk warrants it. Why: uploads are a route to code execution and malware hosting. Verify: uploading a script or oversized file is refused, and uploaded files cannot execute.
- [ ] **C15 [HIGH] Make password reset and verification tokens single-use and short-lived.** Why: reusable tokens allow takeover through old emails. Verify: a used or expired link is refused.
- [ ] **C16 [MEDIUM] Publish a security contact.** Provide a `security.txt` file and a monitored address for vulnerability reports. Why: researchers need a route to report problems privately. Verify: the file is served and a test message is answered.
- [ ] **C17 [HIGH] Log administrative and sensitive actions.** Record who did what and when for logins, permission changes, exports and deletions, without logging secrets. Why: needed to investigate incidents and required by some customers. Verify: perform an admin action and find it in the log.
- [ ] **C18 [CRITICAL] Remove default credentials and close administrative interfaces to the public internet.** Cover database consoles, dashboards, debug tools and storage buckets. Why: exposed admin tools are found by scanners within hours. Verify: each interface is unreachable without the private network or login, and no default password works.
- [ ] **C19 [HIGH] Return safe error messages.** Show users a generic message and keep stack traces and query details in the logs. Why: detailed errors help attackers. Verify: force an error in production and read the response.
- [ ] **C20 [HIGH] Encrypt sensitive data at rest and limit who can read it.** If: the product stores sensitive data such as identity documents, health or financial data, or tokens for other services. Why: reduces the impact of a storage breach. Verify: the storage encryption setting is on and access is limited to named roles.
- [ ] **C21 [HIGH] Give CI and deployment credentials the least privilege they need.** Scope tokens to one repository and environment, and prefer short-lived credentials. Why: build systems are a common path into production. Verify: review the token scopes and confirm none has organisation-wide or administrator rights.
- [ ] **C22 [HIGH] Commission an independent security test.** If: the product handles payments, sensitive data or enterprise customers. Why: an outside tester finds what the builders overlook. Verify: a dated report exists and its findings are fixed or accepted in writing.

## D. SEO and Search Visibility

Applies to public web surfaces: marketing sites, documentation, landing pages and public application pages. Skip for internal tools and for products with no public pages.

- [ ] **D1 [HIGH] Give each public page a unique title and description.** Why: these are what search results and shared links show. Verify: read the page source of the main pages, or crawl the site and list duplicates.
- [ ] **D2 [HIGH] Set a canonical URL on each public page.** Why: prevents duplicate versions competing with each other. Verify: each page's canonical tag points to its preferred address.
- [ ] **D3 [HIGH] Publish an XML sitemap.** List the indexable pages and reference the sitemap from robots.txt. Why: helps search engines find pages. Verify: fetch the sitemap and confirm the URLs return success.
- [ ] **D4 [CRITICAL] Confirm robots.txt and indexing directives are correct for production.** Allow the pages that should be found and remove any leftover `noindex` or site-wide disallow from development. Why: a leftover block keeps the whole site out of search. Verify: fetch robots.txt and check the headers and source of the main pages.
- [ ] **D5 [MEDIUM] Add Open Graph and social card metadata with a preview image.** Why: controls how links look when shared. Verify: test a link in a social preview tool or by pasting it into a chat application.
- [ ] **D6 [MEDIUM] Provide a favicon and application icons.** Why: missing icons look unfinished in tabs, bookmarks and home screens. Verify: the icon appears in a browser tab and when saved to a phone home screen.
- [ ] **D7 [MEDIUM] Add structured data where it fits.** If: pages describe products, articles, organisations, events or similar. Why: enables richer search results. Verify: run the pages through a structured data testing tool with no errors.
- [ ] **D8 [MEDIUM] Use one main heading per page, a logical heading order and descriptive image alt text.** Why: helps both search engines and screen reader users. Verify: inspect the heading outline and images on the main pages.
- [ ] **D9 [HIGH] Verify the site in search engine webmaster tools and submit the sitemap.** Why: shows indexing problems and search performance. Verify: the property is verified and the sitemap is accepted. Needs: D3.
- [ ] **D10 [MEDIUM] Check for broken links and redirect old URLs.** If: replacing an existing site, map each old URL to its new one with a permanent redirect. Why: broken links lose visitors and ranking. Verify: a link crawl reports no broken internal links, and old URLs redirect.
- [ ] **D11 [HIGH] Confirm that crawlers can see the content.** If: pages are rendered in the browser by script. Why: content that needs script execution may be indexed late or incompletely. Verify: fetch a page without running script and confirm the main content is present, or use the search engine's URL inspection.
- [ ] **D12 [LOW] Use readable, stable URLs and add language annotations for multilingual sites.** Why: stable addresses keep links working. Verify: URLs are lowercase, descriptive and free of session parameters.

## E. UI, UX and Accessibility

- [ ] **E1 [HIGH] Test the layout at phone, tablet and desktop widths.** Why: most traffic for many products is on phones. Verify: complete the main journeys at each width with no horizontal scrolling or overlapping elements.
- [ ] **E2 [HIGH] Test in the browsers and operating systems the audience uses.** Why: rendering and feature support differ. Verify: the main journeys pass in each supported browser, and the supported list is written down.
- [ ] **E3 [HIGH] Design the loading, empty, error and success states.** Why: these states are what users see when things are slow or go wrong. Verify: trigger each state on the main screens.
- [ ] **E4 [HIGH] Make forms easy to complete.** Use visible labels, clear inline errors, the right keyboard types, autofill hints, and keep entered data after an error. Why: forms are where sign-ups and purchases are lost. Verify: complete each form by keyboard and on a phone, including an error path.
- [ ] **E5 [HIGH] Support keyboard navigation with a visible focus indicator.** Why: required for many users and by accessibility standards. Verify: reach and operate every control with the keyboard alone.
- [ ] **E6 [HIGH] Test with a screen reader.** Why: automated tools find only part of the problems. Verify: complete the main journey with a screen reader and hear a meaningful name for every control.
- [ ] **E7 [HIGH] Meet colour contrast requirements.** Why: low contrast makes text unreadable for many people. Verify: a contrast checker passes for text and controls at the chosen conformance level.
- [ ] **E8 [HIGH] Run an automated accessibility scan and fix serious findings.** Why: catches missing labels, roles and alt text quickly. Verify: the scan report for the main pages shows no critical or serious issue.
- [ ] **E9 [MEDIUM] Provide a helpful not-found page.** Include navigation back to the main areas. Why: keeps visitors who follow a bad link. Verify: request a missing page.
- [ ] **E10 [MEDIUM] Ask for confirmation, or allow undo, on destructive actions.** Why: prevents accidental data loss. Verify: try to delete something important.
- [ ] **E11 [MEDIUM] Keep typography, spacing and components consistent.** Why: inconsistency reads as low quality. Verify: review the main screens side by side.
- [ ] **E12 [MEDIUM] Respect user settings for zoom, text size and reduced motion.** Why: required by accessibility standards. Verify: zoom to 200 percent and enable reduced motion.
- [ ] **E13 [MEDIUM] Check dark mode.** If: the product offers it. Why: unreadable text and invisible icons are common. Verify: review every main screen in dark mode.
- [ ] **E14 [MEDIUM] Check language, date, number, currency and time zone handling.** If: users are in more than one country or language. Include right-to-left layout where relevant. Why: wrong formats cause real errors in dates and money. Verify: use the product with a different locale and time zone.

## F. Functionality and Quality Assurance

- [ ] **F1 [CRITICAL] Test the core user journeys end to end in a production-like environment.** Write down the journeys that define the product and run each from start to finish. Why: a launch with a broken core journey fails regardless of everything else. Verify: each journey passes, with the date and build recorded.
- [ ] **F2 [CRITICAL] Test every account flow.** If: the product has accounts. Cover sign-up, email verification, login, logout, password reset, social login, lockout, email change and account deletion. Why: account problems block users entirely. Verify: each flow passes with a fresh account, including the emails.
- [ ] **F3 [CRITICAL] Test payment flows in live mode.** If: the product takes payment. Cover success, decline, authentication challenge, refund, cancellation, renewal and webhook delivery, and make one real low-value purchase. Why: test mode does not prove that live keys, webhooks and bank flows work. Verify: a real charge appears in the provider dashboard, the product grants access, and the refund completes.
- [ ] **F4 [HIGH] Test validation on the client and the server.** Why: the server must reject what the client would have blocked. Verify: submit invalid data through the interface and directly to the API.
- [ ] **F5 [HIGH] Test behaviour when third-party services fail.** Simulate timeouts and errors from each integration. Why: outside services fail, and the product should degrade without losing data. Verify: with a dependency unavailable, the user sees a clear message and no data is corrupted.
- [ ] **F6 [HIGH] Test edge cases.** Cover empty input, very long input, special characters and other scripts, double submission, the back button, expired sessions, slow networks and two users acting at once. Why: real users reach these within days. Verify: each case is handled without an error page or duplicate records.
- [ ] **F7 [HIGH] Run the automated tests on the release commit.** Why: confirms that late fixes did not break earlier work. Verify: the pipeline is green for the exact commit being released.
- [ ] **F8 [HIGH] Test on real devices.** If: the product is used on phones or tablets. Why: emulators miss touch, keyboard, performance and browser differences. Verify: the main journeys pass on at least one real Android and one real iOS device, where both are supported.
- [ ] **F9 [HIGH] Test roles and permissions.** If: the product has more than one role. Why: permission errors expose data or block work. Verify: for each role, confirm what it can and cannot do against a written matrix.
- [ ] **F10 [CRITICAL] Prepare a production smoke test and run it after every deploy.** A short script or list that checks the main page, login, the main action and one integration. Why: finds a broken deploy within minutes. Verify: the smoke test runs against production and passes.
- [ ] **F11 [HIGH] Verify migrated or imported data.** If: launch involves moving existing data. Why: migration errors are hard to repair after users start writing new data. Verify: record counts and sampled records match the source.
- [ ] **F12 [HIGH] Triage the open bugs and publish known issues.** Why: launching with an unknown bug list is a gamble. Verify: no open bug is rated critical or high, and the remaining ones are listed.

## G. Analytics, Tracking and Monitoring

Analytics and third-party tracking are optional. Install them only for a question the team will act on, and prefer the least data that answers it.

- [ ] **G1 [HIGH] Define the launch success metrics.** Choose a few numbers, such as activation, conversion and retention, with targets. Why: without them nobody can say whether the launch worked. Verify: the metrics and targets are written down and each can be measured.
- [ ] **G2 [MEDIUM] Install product or web analytics that fit the privacy position.** If: G1 needs data the product does not already have. Gate it on consent where required and disclose it in the privacy policy. Why: analytics added without thought create legal exposure. Verify: events arrive, and no analytics request is sent before consent where consent is required. Needs: A5.
- [ ] **G3 [MEDIUM] Verify conversion and funnel events.** If: analytics is installed. Why: untested tracking gives wrong numbers that drive wrong decisions. Verify: perform each tracked action once and find exactly one matching event.
- [ ] **G4 [CRITICAL] Track errors in production.** Capture server and client errors with the release version and enough context to reproduce them, without personal data or secrets. Why: users rarely report errors; they leave. Verify: trigger a test error in production and find it in the tracker.
- [ ] **G5 [HIGH] Monitor performance and resource use.** Track response times, error rates and the saturation of servers, databases and queues. Why: slowdowns come before outages. Verify: a dashboard shows the last hour for each.
- [ ] **G6 [HIGH] Collect logs centrally with a retention period.** Keep secrets and unnecessary personal data out of them. Why: logs on a lost server are gone, and logs holding secrets are a liability. Verify: search for a recent request in the log system, and search the logs for a known secret pattern and find nothing.
- [ ] **G7 [CRITICAL] Route alerts to a person and test them.** Alert on downtime, error spikes, failed payments, failed jobs and certificate expiry. Why: an alert nobody receives protects nothing. Verify: fire a test alert and confirm the on-call person receives it.
- [ ] **G8 [MEDIUM] Prepare a launch-day dashboard.** Put traffic, sign-ups, errors, latency, payments and costs on one screen. Why: speeds up decisions on launch day. Verify: the dashboard loads and each panel has data.
- [ ] **G9 [MEDIUM] Disclose and mask session recording.** If: the product records sessions or heatmaps. Mask form fields and personal data. Why: recordings easily capture sensitive data. Verify: review a recording and confirm inputs are masked.

## H. Performance and Optimization

- [ ] **H1 [MEDIUM] Compress images and serve them in modern formats at the right size.** Why: images are usually the largest part of a page. Verify: no image on the main pages is larger than its display size requires.
- [ ] **H2 [MEDIUM] Lazy-load content below the first screen.** Why: speeds up the first view. Verify: off-screen images and embeds load only when scrolled to.
- [ ] **H3 [MEDIUM] Reduce the script and style bundle.** Split by route, remove unused code and avoid heavy libraries for small tasks. Why: large bundles slow down phones. Verify: review the bundle report and the size of the first load.
- [ ] **H4 [MEDIUM] Minify and compress text assets.** Why: reduces transfer size at no cost. Verify: responses for scripts, styles and pages carry a compression header.
- [ ] **H5 [HIGH] Index and review the database queries on the main paths.** If: the product has a database. Remove repeated queries in loops and add indexes for common filters. Why: slow queries become outages as data grows. Verify: the slow query log is clean for the main journeys at realistic data volume.
- [ ] **H6 [HIGH] Measure Core Web Vitals on the key pages.** If: the product has public web pages. Why: affects user experience and search ranking. Verify: record the lab scores for each key page, and check field data once traffic exists.
- [ ] **H7 [HIGH] Set and meet a response time target for the API.** If: the product has an API or server-rendered pages. Why: gives a threshold for alerts and load testing. Verify: the 95th percentile response time for the main endpoints is within the target.
- [ ] **H8 [MEDIUM] Audit fonts and third-party scripts.** Subset and preload fonts, and remove or defer third-party scripts. Why: third-party scripts are a common cause of slow pages. Verify: list every third-party request on the main page and justify each.
- [ ] **H9 [MEDIUM] Record a baseline performance audit.** Why: gives a reference to compare against after launch. Verify: a dated audit report for the main pages is saved.

## I. Communication and Transactional Email

Applies when the product sends any email or message.

- [ ] **I1 [CRITICAL] Confirm every transactional email is sent from production and arrives.** Cover verification, password reset, receipts, invitations and alerts. Why: a missing verification or reset email locks users out. Verify: trigger each email in production and receive it in an outside mailbox.
- [ ] **I2 [CRITICAL] Authenticate the sending domain with SPF, DKIM and DMARC.** Why: unauthenticated mail is rejected or marked as spam by the main mailbox providers. Verify: look up the DNS records, and read the authentication results in the headers of a received message.
- [ ] **I3 [HIGH] Check the current bulk sender requirements of the main mailbox providers.** If: the product will send more than a small volume. Why: providers set authentication, unsubscribe and complaint rate rules that change. Verify: read the providers' current pages listed in the sources reference and record what applies. Needs: I2.
- [ ] **I4 [HIGH] Test deliverability to the main mailbox providers.** Why: mail can pass authentication and still land in spam. Verify: send each template to test mailboxes at the main providers and confirm inbox placement.
- [ ] **I5 [HIGH] Separate transactional and marketing mail, and honour unsubscribes.** If: the product sends marketing mail. Use separate streams or subdomains, include an unsubscribe link and one-click unsubscribe header, and send only to people who agreed. Why: marketing complaints should not block password resets, and marketing email is regulated. Verify: unsubscribe with a test address and confirm no further marketing mail arrives.
- [ ] **I6 [HIGH] Process bounces and complaints.** Stop sending to addresses that bounce or complain. Why: continuing to send damages the domain's reputation. Verify: a simulated bounce suppresses the address.
- [ ] **I7 [HIGH] Set up monitored support and contact addresses on the product's domain.** Use a real reply address. Why: users reply to emails, and unanswered replies lose trust. Verify: send a message to each address and confirm a person receives it.
- [ ] **I8 [MEDIUM] Test templates in the main mail clients.** Include a plain text version, working links and correct names. Why: broken layouts and wrong merge fields look careless. Verify: review each template on desktop and mobile clients, in light and dark modes.
- [ ] **I9 [MEDIUM] Confirm contact form submissions reach a person.** If: the site has a contact form. Why: forms that post nowhere lose leads silently. Verify: submit the production form and receive the notification.
- [ ] **I10 [HIGH] Meet consent and registration rules for SMS, messaging apps and push notifications.** If: the product uses them. Check sender registration and consent rules for each country. Why: these channels are regulated and carriers block unregistered senders. Verify: the registration is approved and a test message arrives. Needs: A2.

## J. Documentation and Support

- [ ] **J1 [HIGH] Write a getting started guide.** Take a new user from nothing to first success. Why: most users decide in the first minutes. Verify: someone unfamiliar with the product completes the guide without help.
- [ ] **J2 [MEDIUM] Document the main tasks.** Why: reduces support load. Verify: each main feature has a page or in-product help.
- [ ] **J3 [MEDIUM] Publish FAQs and troubleshooting for the known problems.** Why: answers the repeated questions once. Verify: the questions raised during testing are covered.
- [ ] **J4 [HIGH] Show how to get support and what response time to expect.** Why: users with no route to help leave or complain publicly. Verify: the contact route is reachable from every page or screen.
- [ ] **J5 [HIGH] Prepare support for launch day.** Decide who answers, during which hours, with prepared replies for the expected questions and an escalation route to engineering. Why: support volume peaks at launch. Verify: a test request receives a reply through the planned process.
- [ ] **J6 [MEDIUM] Start a changelog or release notes.** Why: tells users what changed and shows the product is alive. Verify: the launch version has an entry.
- [ ] **J7 [MEDIUM] Publish known limitations.** Why: sets expectations and reduces support. Verify: the list matches the open issues in F12.
- [ ] **J8 [HIGH] Write the internal runbook.** Cover how to deploy, roll back, restore a backup and handle the likely incidents, with where the credentials are kept. Why: the person who built it will not always be the person on call. Verify: a second person follows it to perform a deploy.
- [ ] **J9 [MEDIUM] Set up a status page.** If: other people or businesses depend on the product's availability. Why: gives one place to communicate incidents. Verify: post and resolve a test incident.
- [ ] **J10 [MEDIUM] Set up feedback collection and a triage routine.** Why: launch feedback is most useful when it is captured and reviewed on a schedule. Verify: a feedback item submitted through the product appears in the tracker.

## K. Launch and Marketing Preparation

- [ ] **K1 [HIGH] Write the positioning in one or two sentences.** Say who the product is for, what it does and why it is different. Why: every page and announcement is built from this. Verify: someone outside the team can repeat it after one reading.
- [ ] **K2 [HIGH] Finish the landing page and test its call to action.** If: the product is offered to the public. Why: this is where launch traffic lands. Verify: follow the call to action from the landing page through to a completed sign-up or purchase.
- [ ] **K3 [HIGH] Publish pricing that matches the billing system.** If: the product is paid. Why: a mismatch between the page and the charge causes disputes. Verify: each plan, price, currency and limit on the page matches the billing configuration.
- [ ] **K4 [MEDIUM] Prepare screenshots and a short demo video.** Why: people judge the product before trying it. Verify: the assets show the current interface.
- [ ] **K5 [MEDIUM] Prepare the announcement drafts and assets.** Cover email, social posts, a blog post and images in the sizes each channel needs. Why: launch day leaves no time for writing. Verify: every draft is reviewed and scheduled or ready to send.
- [ ] **K6 [MEDIUM] Prepare launch platform and directory listings.** If: relevant to the audience. Why: listings need assets and timing that are easy to miss. Verify: each listing is drafted according to the platform's current guidelines.
- [ ] **K7 [MEDIUM] Use only real testimonials and case studies, with permission.** Why: invented or unapproved endorsements are a legal and reputational risk. Verify: written permission exists for each one shown.
- [ ] **K8 [MEDIUM] Tell the waitlist and beta users first.** If: one exists. Why: early supporters are the most likely first customers. Verify: the message is drafted and the list is clean and consented.
- [ ] **K9 [HIGH] Decide the launch date, style and owner.** Use the launch runbook reference. Why: a launch without an owner and a date drifts. Verify: the decision is recorded in the checklist.
- [ ] **K10 [LOW] Set up campaign links for attribution.** Why: shows which channels worked. Verify: a tagged link appears correctly in analytics.

## L. Backup, Recovery and Business Continuity

- [ ] **L1 [CRITICAL] Back up the database and user files automatically, to a separate location.** If: the product stores data that cannot be recreated. Why: without backups, one mistake or failure ends the product. Verify: the latest backup exists, is recent and is stored outside the primary system.
- [ ] **L2 [CRITICAL] Restore a backup and record how long it takes.** Why: a backup that has never been restored is unproven. Verify: restore into a separate environment and confirm the data is complete and usable. Needs: L1.
- [ ] **L3 [HIGH] State how much data loss and downtime are acceptable.** Why: these two numbers decide backup frequency and recovery design. Verify: the numbers are written down and the backup schedule meets them.
- [ ] **L4 [HIGH] Write an incident response plan.** Define severity levels, who leads, who communicates, where the team gathers and how users are told. Why: confusion in the first minutes makes incidents longer. Verify: walk through one imagined incident with the plan.
- [ ] **L5 [HIGH] List the services the product depends on and what happens when each fails.** Why: shows single points of failure before they fail. Verify: each dependency has an owner, a status page link and a fallback or accepted impact.
- [ ] **L6 [HIGH] Make sure a second person can operate everything.** Why: one person holding all access and knowledge is a single point of failure. Verify: a second person can sign in to each critical system and follow the runbook. Needs: J8.
- [ ] **L7 [MEDIUM] Plan for the loss of a region or provider.** If: the risk profile is High or Critical. Why: large outages are rare but long. Verify: the plan states what is rebuilt, from what, and in what order.
- [ ] **L8 [LOW] Keep the ability to export data and move providers.** Why: reduces dependence on one vendor's pricing and survival. Verify: a full data export can be produced in a standard format.

## M. Accounts and Ownership

- [ ] **M1 [CRITICAL] Hold the domain in an account the business controls, with automatic renewal and a transfer lock.** Why: an expired or hijacked domain takes the product and its email offline. Verify: the registrar account shows the business as owner, renewal on, lock on and a valid payment method.
- [ ] **M2 [CRITICAL] Turn on two-factor login for every critical account.** Cover the registrar, DNS, cloud, code host, payment provider, app stores, package registries and the email provider. Why: these accounts control the whole product. Verify: each account shows two-factor login as enabled for every member.
- [ ] **M3 [HIGH] Keep shared credentials and recovery codes in a password manager with a second administrator.** Why: access must survive one person being unavailable. Verify: a second person can retrieve each credential.
- [ ] **M4 [HIGH] Review who has access and remove those who no longer need it.** Cover former contractors and unused service accounts. Why: old access is a common way in. Verify: the member list of each critical system contains only current people with the least access they need.
- [ ] **M5 [HIGH] Confirm that plans and billing will hold through launch.** Check that payment cards are valid and that free or trial tiers will not stop the service at launch volume. Why: a lapsed card or a free tier limit can take the product down. Verify: review the plan, limits and next billing date for each service.

## N. Cost and Capacity

- [ ] **N1 [CRITICAL] Set billing alerts and spending limits on usage-priced services.** If: any cloud, AI, email, SMS or API service is billed by usage. Why: a bug, abuse or sudden attention can produce a very large bill overnight. Verify: each provider shows a budget alert going to a monitored address, and a hard limit where the provider offers one.
- [ ] **N2 [HIGH] Load test at the expected launch peak with a margin.** If: the launch will be announced or traffic may spike. Test a staging copy, or production with approval. Why: shows the breaking point before users find it. Verify: the test report shows response times and error rates at the target load.
- [ ] **N3 [HIGH] Check third-party quotas and rate limits at launch volume.** Cover email sends, API calls, AI tokens, SMS, storage and database connections. Why: default quotas are often set for development. Verify: for each service, compare the expected launch-day use with the current limit and request increases early.
- [ ] **N4 [HIGH] Confirm headroom or automatic scaling.** Why: capacity that cannot grow turns success into an outage. Verify: scaling rules and maximums are set, and the database connection limit covers the maximum number of application instances.
- [ ] **N5 [HIGH] Add switches to turn off expensive or risky features without a deploy.** Why: gives a fast response to abuse or cost spikes. Verify: turning the switch off in production disables the feature and leaves the rest working.
- [ ] **N6 [MEDIUM] Estimate the cost per user and per action.** Why: confirms the pricing covers the cost, especially where AI or media processing is involved. Verify: a short calculation exists using current provider prices from their official pages.

## O. Production Hygiene

- [ ] **O1 [CRITICAL] Turn off debug mode and development tools in production.** Why: debug output exposes internals and sometimes allows code execution. Verify: the production configuration and a forced error both show debug is off.
- [ ] **O2 [CRITICAL] Remove test data, seed accounts and default users from production.** Why: test accounts with known passwords are an open door, and test data confuses real users. Verify: query production for the known test accounts and records.
- [ ] **O3 [CRITICAL] Switch every integration to its live keys and endpoints.** Cover payments, email, SMS, analytics and webhooks, and make sure webhooks point to production. Why: a product running on test keys takes no real payments and sends no real mail. Verify: list each integration with its mode, and confirm a live event arrives.
- [ ] **O4 [HIGH] Decide whether source maps are public.** Why: public source maps reveal the original source code. Verify: request a source map for the main script and confirm the result matches the decision.
- [ ] **O5 [HIGH] Protect staging and preview environments.** Put them behind a login and mark them not to be indexed. Why: staging sites leak unreleased features and appear in search results. Verify: staging asks for credentials and carries a `noindex` directive.
- [ ] **O6 [MEDIUM] Remove placeholder content.** Search for filler text, TODO notes, example addresses and broken images. Why: placeholders in production look unfinished. Verify: a search of the built output finds none.
- [ ] **O7 [HIGH] Make the running version identifiable.** Expose the release version or commit in a header, endpoint or footer, and send it with error reports. Why: nobody can debug or roll back without knowing what is running. Verify: the version shown in production matches the release tag.
- [ ] **O8 [HIGH] Review the default state of every feature flag.** If: the product uses flags. Why: a flag left in its development state ships unfinished features or hides finished ones. Verify: list each flag with its intended and actual production state.
