---
project: glibc
subsystem: io
patch_id: null
tags:
- fts
- gnulib
- glibc
- file system
- compatibility
discussion_id: lhuy0iit5cy.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
headline: 'io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
tldr: The patch replaces glibc's fts implementation with the one from gnulib, and
  the discussion concerns compatibility issues related to stat'ing behavior.
stakes: The fts functions are used for file system traversal. Changes can affect programs
  like `find` and `du`. Compatibility issues can break existing applications. Performance
  of file system operations can be impacted.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Replacing the existing implementation with gnulib's may introduce subtle behavioral
  changes.
- Adding compatibility symbols increases the complexity of the code base.
- Not addressing the compatibility issue may break existing applications relying on
  the old behavior.
primer: The `fts` functions (fts_open, fts_read, fts_children, fts_close) provide
  a standardized way to traverse file system hierarchies. gnulib is a collection of
  portable implementations of standard library functions. The `stat` function retrieves
  information about a file, such as its size, permissions, and modification time.
  `FTS_NOSTAT` is a flag that tells `fts_open` not to `stat` files, presumably for
  performance reasons.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch replaces the glibc's implementation of the `fts` (file tree traversal) functions with the implementation from gnulib. The discussion revolves around a potential compatibility issue where the old behavior of `fts` performed stat'ing even with `FTS_NOSTAT` specified. The author suggests adding compatibility symbols to mitigate the impact on existing applications.
