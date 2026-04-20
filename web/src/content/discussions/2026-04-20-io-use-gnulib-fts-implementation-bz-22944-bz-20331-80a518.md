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
tldr: glibc's fts (file tree walk) implementation is being replaced with the gnulib
  version, but there are concerns about compatibility with existing programs relyin…
stakes: Potential breakage of existing programs if the change in fts behavior is not
  handled carefully.  This could affect programs that rely on specific stat'ing behavior.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using the gnulib implementation may improve maintainability and potentially performance.
- May break existing programs which rely on the current behavior.
- Versioning the symbol adds complexity but maintains backward compatibility.
- Fixing impacted programs directly is a cleaner solution in the long run but may
  take more time and effort.
primer_expert: glibc's `fts` (file tree walk) is being updated to use the gnulib version.
  The core issue revolves around symbol versioning and compatibility, specifically
  how `FTS_NOSTAT` interacts with existing code. The discussion focuses on whether
  to version the symbol or fix the impacted programs.
primer_general: The `fts` functions in glibc provide a way to traverse file system
  directory trees. This functionality is used by programs that need to explore directory
  structures, such as `find`. The `FTS_NOSTAT` flag controls whether `stat` is called
  for each file, which impacts performance and the availability of file metadata.
  Gnulib is a library of portable code often used to provide consistent functionality
  across different systems.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch switches glibc to use the gnulib implementation of the fts (file tree walk) functions.  A previous concern was that the gnulib implementation of `FTS_NOSTAT` might break programs like dracut.  The submitter now suggests adding compatibility symbols to perform post-processing to avoid complicating maintenance on the gnulib side.
