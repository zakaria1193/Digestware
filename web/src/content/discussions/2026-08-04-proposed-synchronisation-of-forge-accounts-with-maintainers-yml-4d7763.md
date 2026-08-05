---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- maintenance
- attribution
- MAINTAINERS.yml
- forge
discussion_id: 010c2e55-7f21-4819-8657-f2ad9eccd616@foss.arm.com
source_type: public_inbox
title: '[RFC] Proposed synchronisation of forge accounts with MAINTAINERS.yml'
headline: Proposed synchronisation of forge accounts with MAINTAINERS.yml
tldr: Script to sync forge accounts with MAINTAINERS.yml and add historical email
  addresses.
proposer: Claudio Bantaloukas <claudio.bantaloukas@foss.arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Automating account synchronization improves accuracy but requires administrative
  access and a script.
- Adding historical emails enhances attribution completeness but might raise privacy
  or opt-out concerns.
- Manual updates by users are more privacy-preserving but less efficient and prone
  to incomplete data.
exchanges:
- author: Claudio Bantaloukas <claudio.bantaloukas@foss.arm.com>
  role: proposer
  position: Proposes a script to sync forge accounts with MAINTAINERS.yml and suggests
    adding historical email addresses to improve contribution attribution.
  quote: 'This should ensure that contributions are correctly attributed in the Forge
    user interface.


    Why use a script rather than ask people to add the addresses themselves? Some
    people previously contributed using addresses they can no longer access. Forgejo
    does not allow users to add an address without verifying it, whereas an administrator
    can associate an address through the REST API.'
primer_expert: This RFC proposes to automate the synchronization of user account details
  on forge.sourceware.org with the project's MAINTAINERS.yml file. It also seeks feedback
  on retroactively adding historical email addresses found in git logs to the MAINTAINERS.yml
  file. The goal is to ensure accurate attribution of contributions within the platform's
  UI and historical records.
primer_glossary:
- term: MAINTAINERS.yml
  definition: A file that lists maintainers for different parts of a software project,
    often used to determine who should review patches.
- term: forge.sourceware.org
  definition: The platform hosting the Sourceware project's code repositories and
    issue tracking.
- term: RFC
  definition: Request For Comments. A document or email requesting feedback on a proposed
    change or idea before implementation.
- term: inactive_email
  definition: A field within MAINTAINERS.yml that can list historical email addresses
    associated with a maintainer, for attribution purposes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/010c2e55-7f21-4819-8657-f2ad9eccd616@foss.arm.com
bugzilla_url: null
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

Claudio Bantaloukas proposes a script to synchronize user accounts on forge.sourceware.org with the MAINTAINERS.yml file. The script aims to ensure proper display of names and association of email addresses, affecting only existing forge accounts. Additionally, it suggests adding approximately 600 historical email addresses to MAINTAINERS.yml under inactive_email entries to improve contribution attribution. Feedback is requested on adding these historical addresses and the overall approach.
