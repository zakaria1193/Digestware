---
project: glibc
subsystem: io
patch_id: null
tags:
- glibc
- io
- fts
- gnulib
- FTS_NOSTAT
discussion_id: lhuy0iit5cy.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
headline: 'io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
tldr: Discussion about potential regressions from using the gnulib `fts` implementation
  in glibc, specifically concerning `FTS_NOSTAT` behavior.
stakes: Potential breakage of existing applications relying on specific `fts` behavior,
  particularly those using `FTS_NOSTAT`.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Correctness of `FTS_NOSTAT` vs. compatibility with existing applications.
- Maintenance burden of compatibility symbols vs. forcing application updates.
- Complexity of integrating gnulib code into glibc.
primer_expert: The thread discusses integrating gnulib's `fts` implementation into
  glibc. The core issue is a behavioral change regarding `FTS_NOSTAT`. The older implementation
  performed implicit `stat` calls even with `FTS_NOSTAT`, a behavior some applications
  relied upon. The discussion centers on whether to maintain compatibility via compatibility
  symbols or force applications to adapt to the new, stricter `FTS_NOSTAT` semantics.
primer_general: The `fts` functions in glibc provide a way to traverse directory hierarchies.  The
  `FTS_NOSTAT` flag is intended to prevent the `fts` functions from calling `stat`
  on each file, which can improve performance.  However, older implementations of
  `fts` in glibc may have ignored this flag and still called `stat`.  This discussion
  concerns a change in glibc to use a new `fts` implementation from gnulib, which
  correctly honors `FTS_NOSTAT`.  This change could break applications that relied
  on the old, incorrect behavior.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This discussion concerns a patch to use the gnulib `fts` implementation in glibc.  Adhemerval Zanella Netto asks if bug 34078 should be closed as WONTFIX, which relates to the `FTS_NOSTAT` flag. Florian Weimer expresses concern that more than just dracut might be affected by the change in behavior and suggests adding compatibility symbols to perform post-processing, confining the changes to glibc.
