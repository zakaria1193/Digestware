---
project: glibc
subsystem: localedata
patch_id: null
tags:
- localedata
- formatting
- consistency
discussion_id: 20260417221937.2881058-1-carlos@redhat.com
source_type: public_inbox
title: '[COMMITTED] localedata: Consistently use one space after ''category'''
headline: 'localedata: Correct spacing in hrx_BR locale'
tldr: Fixes inconsistent spacing in the hrx_BR locale file by ensuring there's one
  space after 'category'.
stakes: Ensures consistency in locale data formatting, which is important for maintainability
  and avoids potential parsing issues.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Committed
outcome: committed
sentiment_score: 10
sentiment_rationale: Trivial change, already committed.
technical_tradeoffs: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260417221937.2881058-1-carlos@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

Carlos O'Donell committed a change to make the category format in the hrx_BR locale consistent with other locales. This change adds a single space after the 'category' keyword.
