# Jurisdictions

This file lists what to check and which questions decide whether a law applies. It deliberately states few rules, thresholds or deadlines, because those change and because whether a law applies to a given product is a legal judgment. For each law that looks relevant, open the official page from the sources reference, read the scope and the current text, and record the URL and date in the checklist item. Present conclusions as questions for the user or their lawyer, and recommend legal review when the risk profile is High or Critical.

## Contents

- How to decide which sections apply
- India
- European Union
- United Kingdom
- United States
- Other countries
- Topics that cut across jurisdictions

## How to decide which sections apply

Ask these, then read the matching sections:

1. Where is the business established?
2. Where are the users or customers, and does the product target them (language, currency, marketing, shipping)?
3. What data is handled: personal, sensitive, children's, health, financial, location, biometric?
4. Does the product take payment, hold funds or move money between parties?
5. Does it host content from users, sell goods, or ship hardware?
6. Does it use AI in ways that affect people?
7. Are the customers businesses that will pass their own obligations on through contracts?

A law of one country can apply to a business in another when it serves people there. Check the territorial scope section of each law instead of assuming.

## India

Read this section when the business is in India or the product serves people in India.

| Topic | What to check | Where |
|---|---|---|
| Personal data | Whether and how the Digital Personal Data Protection Act, 2023 and the Digital Personal Data Protection Rules apply: notice, consent, children's data, user rights, breach notification, grievance contact, data retention and transfers. The rules were notified in November 2025 with provisions starting in phases, according to secondary sources. Confirm which provisions are in force today. | Ministry of Electronics and Information Technology |
| Security incidents | The incident reporting directions issued by CERT-In: which incidents are reportable, the reporting time, and log retention duties. | CERT-In |
| Intermediaries and user content | The Information Technology Act and the intermediary rules: due diligence, grievance officer and takedown duties, for products that host user content. | Ministry of Electronics and Information Technology, India Code |
| E-commerce and consumers | The Consumer Protection Act and the e-commerce rules: seller information, pricing, returns, grievance handling. Check the amendment history. | Department of Consumer Affairs |
| Tax | GST registration, invoicing and rules for online services and for foreign suppliers. | GST portal, a chartered accountant |
| Payments | Reserve Bank of India rules on payment aggregation, card storage and recurring payments, usually met through a licensed payment provider. | Reserve Bank of India, the payment provider's documentation |
| Messaging | Telecom regulator rules on commercial SMS and calls: sender and template registration, consent. | The telecom regulator and the SMS provider |
| Hardware | Product standards and registration for electronic devices. | Bureau of Indian Standards |

## European Union

Read this section when the business is in the EU or the product offers goods or services to people in the EU or monitors their behaviour.

| Topic | What to check | Where |
|---|---|---|
| Personal data | The General Data Protection Regulation: territorial scope, legal basis for each purpose, transparency, user rights, processor contracts, transfers outside the EU, breach notification, records of processing, impact assessments, and whether a representative or a data protection officer is needed. | EUR-Lex, the European Data Protection Board, the national regulator |
| Cookies and trackers | The ePrivacy rules as implemented in each member state: consent before non-essential storage or access on a device. | The national regulator |
| Consumers | Pre-contract information, withdrawal rights, pricing display, subscription cancellation and unfair terms. | EUR-Lex, national consumer authority |
| Accessibility | The European Accessibility Act: whether the product or service type is in scope, and the exemptions. | EUR-Lex, national authority |
| Online platforms | The Digital Services Act: duties for hosting services, platforms and marketplaces, scaled by size. | EUR-Lex, European Commission |
| AI | The AI Act: whether the use is prohibited, high-risk, subject to transparency duties or general-purpose, and which provisions already apply. | EUR-Lex, European Commission |
| Products with digital elements | The Cyber Resilience Act: security and vulnerability handling duties for software and connected products, and the dates from which they apply. | EUR-Lex |
| Tax | VAT on digital services and goods sold to consumers in the EU. | European Commission, a tax adviser |

## United Kingdom

Read this section when the business is in the UK or serves people there.

| Topic | What to check | Where |
|---|---|---|
| Personal data | UK GDPR and the Data Protection Act: the same topics as the EU list, registration with the regulator and the fee, and transfer rules. | Information Commissioner's Office |
| Cookies and marketing | The Privacy and Electronic Communications Regulations: cookies, email and SMS marketing consent. | Information Commissioner's Office |
| Children | The Age Appropriate Design Code for services likely to be accessed by children. | Information Commissioner's Office |
| Online safety | Duties for services with user-generated content or search. | Ofcom |
| Connected products | The product security regime for consumer connectable products. | GOV.UK |
| Consumers and tax | Consumer rights, subscription rules and VAT. | GOV.UK |

## United States

There is no single federal privacy law. Read this section when the business is in the US or serves people there, and check each state where the product has many users.

| Topic | What to check | Where |
|---|---|---|
| Unfair or deceptive practices | Whether the product does what its privacy policy and marketing say. | Federal Trade Commission |
| Children | The Children's Online Privacy Protection Rule, for services directed to children or that knowingly collect their data. | Federal Trade Commission |
| State privacy laws | California's consumer privacy law and the growing set of other state laws: applicability thresholds, notices, opt-out rights, sensitive data. | California Attorney General, California Privacy Protection Agency, each state's attorney general |
| Commercial email | The CAN-SPAM Act: sender identification, honest subject lines, unsubscribe handling. | Federal Trade Commission |
| SMS and calls | The Telephone Consumer Protection Act and carrier registration for business messaging. | Federal Communications Commission, the messaging provider |
| Accessibility | The Americans with Disabilities Act as applied to websites and apps, and procurement rules for government customers. | ADA.gov |
| Sector rules | Health data (HIPAA), financial data (GLBA), student data (FERPA) and payment cards (PCI DSS, an industry standard). | The relevant regulator, the PCI Security Standards Council |
| Subscriptions | Federal and state rules on automatic renewal and cancellation. | Federal Trade Commission, state law |
| Sales tax | Economic nexus rules by state. | A tax adviser |

## Other countries

For any other market with meaningful users, look for the national data protection law and regulator, consumer protection rules for online sales, tax on digital services, rules on commercial messages, and any data localisation requirement. Start from the national regulator's own website. If the checklist cannot cover a market, say so in the Assumptions section.

## Topics that cut across jurisdictions

- **Accessibility standard.** The Web Content Accessibility Guidelines are the common technical reference that laws point to. Check which version and level the applicable law names.
- **App and extension stores.** Store policies apply worldwide on top of local law and are often stricter.
- **Payment providers.** Their terms list prohibited and restricted businesses; check before building.
- **Business customers.** Contracts pass obligations down: data processing agreements, security questionnaires, audit rights and standards such as ISO 27001 or SOC 2. These are commercial requirements, not laws.
- **Export controls and sanctions.** Encryption, certain technologies and certain countries are restricted; app stores ask about encryption at submission.
- **Cross-border data transfers.** Several laws restrict sending personal data to other countries; map where each vendor stores and processes data.
