---
project: glibc
subsystem: io
patch_id: null
tags:
- glibc
- io
- fts
- gnulib
- compatibility
discussion_id: lhuy0iit5cy.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
headline: 'io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
tldr: Discussion about how to handle potential breakage from switching to gnulib's
  `fts` implementation, specifically regarding the use of `FTS_NOSTAT`.
stakes: Affects programs relying on the behavior of `fts` functions, potentially breaking
  compatibility.  Developers using `fts` need to be aware of changes to avoid unexpected
  behavior.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using gnulib's implementation provides potentially better code quality and maintainability.
- May introduce compatibility issues with existing code relying on specific behaviors
  of the old implementation.
- Adding compatibility symbols can mitigate compatibility issues but increases code
  complexity.
exchanges:
- author: Florian Weimer <fweimer@redhat.com>
  role: proposer
  position: Expresses concern about potential breakage due to changes in `FTS_NOSTAT`
    behavior when switching to the gnulib implementation.
  quote: I'm worried that more than just dracut is impacted.  The old behavior had
    been around for a long time.
- author: Florian Weimer <fweimer@redhat.com>
  role: contributor
  position: Suggests adding compatibility symbols to maintain the old behavior of
    `fts_read` and `fts_children`.
  quote: Maybe we can add compatibility symbols that perform post-processing in fts_read
    and fts_children, calling the new implementation?
primer_expert: This patch concerns the `fts` (file tree walk) functions, specifically
  the `fts_read` and `fts_children` APIs in `io/fts.c`. Gnulib is the GNU portability
  library. The issue revolves around the `FTS_NOSTAT` flag and whether the underlying
  implementation should still perform `stat` calls. Versioning symbols lets the older
  implementation provide a compatibility layer.
primer_general: The `fts` functions in glibc provide a way to traverse directory trees.
  Gnulib is a library providing implementations of functions commonly found on POSIX
  systems. The problem is that different implementations of `fts` might behave differently,
  potentially breaking programs that rely on the older behavior (specifically related
  to how file metadata is fetched). The discussion explores ways to maintain backward
  compatibility while updating the underlying implementation.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This discussion revolves around the transition to the gnulib `fts` implementation within glibc.  A concern is raised about potential breakage due to the `FTS_NOSTAT` flag behaving differently.  One suggestion involves adding compatibility symbols that perform post-processing to maintain the old behavior.
