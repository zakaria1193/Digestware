---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- dev-process
- attribution
discussion_id: d7d9c81f-e058-4052-82de-8fc050fd9c78@foss.arm.com
source_type: public_inbox
title: 'Re: [RFC] Proposed synchronisation of forge accounts with MAINTAINERS.yml'
headline: Proposed synchronisation of forge accounts with MAINTAINERS.yml
tldr: A script is proposed to synchronize forge.sourceware.org accounts with MAINTAINERS.yml
  to ensure accurate contributor attribution.
proposer: Claudio Bantaloukas <claudio.bantaloukas@foss.arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Claudio Bantaloukas <claudio.bantaloukas@foss.arm.com>
  role: proposer
  position: Proposes a script to synchronize forge accounts with MAINTAINERS.yml for
    accurate contributor attribution and provides the script for review.
  quote: null
primer_expert: MAINTAINERS.yml is a crucial file in GCC that lists maintainers and
  reviewers for various subsystems. Forge.sourceware.org is the project's development
  platform. Synchronizing these ensures that contributor information is consistent
  across the project's infrastructure, aiding in proper attribution and communication.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/d7d9c81f-e058-4052-82de-8fc050fd9c78@foss.arm.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

Claudio Bantaloukas has developed a script to synchronize forge.sourceware.org accounts with the MAINTAINERS.yml file. The script aims to ensure names appear correctly in profiles and bot emails, and associates all email addresses from MAINTAINERS.yml with their respective forge accounts. This is an additive operation affecting only existing forge accounts and will be run periodically based on feedback. Claudio also shares the script's current form and discusses historical email addresses found in git logs.
