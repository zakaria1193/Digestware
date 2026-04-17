---
project: glibc
subsystem: io
patch_id: null
tags:
- io
- fts
- gnulib
- FTS_NOSTAT
discussion_id: 102b9fbd-4894-4cb4-a72c-e8014685d0dc@cs.ucla.edu
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
headline: 'io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
tldr: Upstream suggests closing a bug report as WONTFIX, regarding programs relying
  on FTS_NOSTAT to stat files, which has always been broken.
stakes: Clarifies the intended behavior of FTS_NOSTAT and its impact on applications.
proposer: Paul Eggert <eggert@cs.ucla.edu>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The discussion is about resolving a bug report with a clear justification,
  suggesting a consensus towards the proposed action.
technical_tradeoffs:
- Fixing dracut and similar programs is preferred over versioning the symbol.
- Maintaining the current behavior avoids breaking existing (mis-)usages.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/102b9fbd-4894-4cb4-a72c-e8014685d0dc@cs.ucla.edu
bugzilla_url: null
date: '2026-04-17'
---

A discussion clarifies that programs relying on FTS_NOSTAT to stat files are inherently broken.  Upstream suggests closing bug report #34078 as WONTFIX, as the behavior is not going to be changed.
