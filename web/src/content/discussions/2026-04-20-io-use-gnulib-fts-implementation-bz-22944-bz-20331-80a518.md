---
project: glibc
subsystem: io
patch_id: null
tags:
- glibc
- gnulib
- fts
- file system
- compatibility
discussion_id: lhuy0iit5cy.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
headline: 'io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
tldr: Discussion about integrating gnulib's fts implementation into glibc, and the
  potential impact on applications relying on the previous behavior.
stakes: Addresses issues related to file traversal in glibc by integrating gnulib's
  fts implementation, potentially impacting applications that rely on the previous
  fts behavior.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 5
sentiment_rationale: The discussion expresses concern about potential breakage and
  proposes solutions to maintain compatibility.
technical_tradeoffs:
- Potential compatibility issues with existing applications.
- Increased maintenance complexity if compatibility symbols are added.
primer: Glibc is the GNU C Library. gnulib is a project providing implementations
  of standard functions for different platforms. `fts` (file tree traversal) is a
  set of functions for traversing file system hierarchies. `stat` is a system call
  that returns file metadata. This discussion centers around updating glibc's file
  system traversal functions with a gnulib implementation and handling potential compatibility
  issues.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This thread discusses the integration of the gnulib `fts` implementation into glibc. A concern is raised about the impact on applications, like dracut, that might rely on the old behavior of performing more stat'ing than specified by `FTS_NOSTAT`. The suggestion is to add compatibility symbols that perform post-processing, confining the changes to glibc and avoiding complications on the gnulib side.
