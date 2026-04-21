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
tldr: Questions whether compatibility symbols are needed for the gnulib `fts` implementation
  due to potential impact on existing programs relying on the old behavior.
stakes: This impacts the compatibility of glibc with existing software that uses the
  `fts` functions, particularly concerning the expected behavior of `FTS_NOSTAT`.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using gnulib's implementation may offer improvements but carries the risk of breaking
  existing code.
- Adding compatibility symbols can reduce the risk of breakage but increases code
  complexity.
- Fixing the programs that rely on broken behavior is the ideal long-term solution
  but may be difficult or impossible in some cases.
exchanges:
- author: Florian Weimer <fweimer@redhat.com>
  role: proposer
  position: Expresses concern about the impact on existing programs and suggests adding
    compatibility symbols that perform post-processing to maintain the old behavior.
  quote: 'I''m worried that more than just dracut is impacted.  The old behavior

    had been around for a long time.


    Maybe we can add compatibility symbols that perform post-processing in

    fts_read and fts_children, calling the new implementation?  This way,

    the necessary changes would be confined to glibc, without complicating

    maintenance on the gnulib side.'
primer_expert: This patch replaces glibc's file tree traversal (`fts`) implementation
  with the one from gnulib. The key point of contention is the behavior of `FTS_NOSTAT`.
  Old code may have relied on `fts` stat'ing files even with `FTS_NOSTAT` set, which
  the new gnulib implementation does not do. Compatibility symbols are being considered
  as a way to preserve the old behavior.
primer_general: glibc, the GNU C Library, provides functions for interacting with
  the operating system, including traversing file systems. The `fts` (file tree walk)
  functions allow programs to recursively visit directories and files. `FTS_NOSTAT`
  is a flag that, in theory, tells `fts` not to retrieve file metadata (using `stat`).
  The discussion centers around whether a change to the `fts` implementation will
  break compatibility with existing programs that relied on a non-standard behavior
  of `FTS_NOSTAT`.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch aims to replace the glibc's `fts` implementation with the one from gnulib. The discussion revolves around the potential breakage introduced by the change, particularly regarding the behavior of `FTS_NOSTAT`. The reviewer suggests adding compatibility symbols to mitigate the impact on existing programs.
