---
project: glibc
subsystem: advisories
patch_id: null
tags:
- glibc
- security
- advisory
- vulnerability
discussion_id: 20260420203837.3439057-1-carlos@redhat.com
source_type: public_inbox
title: '[COMMITTED] advisories: Fix spelling mistake in GLIBC-SA-2026-0009.'
headline: 'Advisories: Fix Spelling Mistake In GLIBC-SA-2026-0009'
tldr: A spelling mistake in the GLIBC-SA-2026-0009 advisory has been corrected.
stakes: Correcting advisory text ensures accurate communication regarding security
  vulnerabilities and their potential impact.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges: []
primer_expert: This commit fixes a spelling error in a GLIBC security advisory. GLIBC
  security advisories provide information about security vulnerabilities in the GNU
  C Library, their impact, and how to mitigate them. The advisory in question, GLIBC-SA-2026-0009,
  relates to a `scanf` vulnerability.
primer_general: GLIBC, the GNU C Library, is a fundamental part of the Linux operating
  system. It provides the standard functions that programs use to interact with the
  system. When security vulnerabilities are discovered in GLIBC, advisories are issued
  to inform users about the issue and how to address it. This commit simply corrects
  a spelling error in one of those advisories, ensuring clear communication about
  the vulnerability.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420203837.3439057-1-carlos@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Carlos O'Donell committed a change to fix a spelling mistake in the GLIBC-SA-2026-0009 advisory. The correction changes "format specififer" to "format specifier".
