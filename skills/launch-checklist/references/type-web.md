# Websites and web applications

The core checklist is written with web products in mind, so this file mostly adjusts it.

## Static and content sites

For business sites, portfolios, landing pages, blogs and documentation with no accounts and no payments, these core items usually become Not Applicable: C1 to C5, C11, C14, C15, C17, F2, F3, F9, most of L, and N2 to N5. Categories D, E and H rise in importance because search and first impressions are the product.

- [ ] **WEB1 [HIGH] Secure the content management system.** If: the site runs on a CMS. Update the core, themes and plugins, remove unused ones, protect the admin login and change default paths where supported. Why: outdated CMS plugins are a leading cause of hacked sites. Verify: the update screen shows nothing pending, and the admin login is protected by two-factor login or an access restriction.
- [ ] **WEB2 [HIGH] Confirm who can publish and how content is backed up.** Why: content lives outside the code repository on many platforms. Verify: an export or backup of the content exists and the editor list is current.
- [ ] **WEB3 [MEDIUM] Test every form and embedded widget.** Cover contact forms, newsletter sign-up, booking widgets and maps. Why: these are often the only conversion on the site. Verify: each submission arrives at its destination.
- [ ] **WEB4 [MEDIUM] Publish the business details the law or the audience expects.** Company name, registered address, contact details and any registration numbers the jurisdiction requires. Why: several jurisdictions require business identification on commercial sites. Verify: the details are on the contact or legal page. Needs: A2.
- [ ] **WEB5 [MEDIUM] Check documentation search, versioning and code samples.** If: the site is documentation. Why: wrong samples and broken search are the main documentation complaints. Verify: run each code sample, and search for the main terms.
- [ ] **WEB6 [LOW] Add a feed and sharing metadata for articles.** If: the site is a blog. Why: helps readers and aggregators follow new posts. Verify: the feed validates.

## Web applications

- [ ] **WEB7 [HIGH] Decide the browser support policy and show a message to unsupported browsers.** Why: silent failure on an old browser looks like a broken product. Verify: open the application in an unsupported browser.
- [ ] **WEB8 [HIGH] Handle session expiry and lost connections without losing work.** Why: users leave tabs open for days. Verify: let a session expire with a form half filled, and disconnect the network during a save.
- [ ] **WEB9 [HIGH] Make deploys safe for users who have the old version open.** Version the assets and prompt or reload when the client is out of date. Why: old tabs calling a new API cause confusing errors. Verify: deploy while a session is open and continue using it.
- [ ] **WEB10 [MEDIUM] Test installed and offline behaviour.** If: the application is a progressive web app. Check the manifest, the service worker update path and offline pages. Why: a faulty service worker can pin users to an old version. Verify: install the app, deploy an update and confirm the client updates.
- [ ] **WEB11 [MEDIUM] Check deep links, refresh and the back button on every route.** If: the application uses client-side routing. Why: a refresh that returns a not-found page is a common single-page application fault. Verify: load each main route directly by URL.
- [ ] **WEB12 [HIGH] Test real-time features under reconnection and across multiple instances.** If: the application uses websockets or live updates. Why: these fail on mobile networks and when the server scales out. Verify: drop the connection and confirm it recovers with no lost or duplicate messages.
