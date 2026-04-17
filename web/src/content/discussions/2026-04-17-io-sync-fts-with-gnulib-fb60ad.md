---
project: glibc
subsystem: io
patch_id: null
tags:
- fts
- gnulib
- synchronization
- FTS_NOSTAT
discussion_id: 5fdbda76-438c-4f14-a4f3-b6b774f997fa@linaro.org
source_type: public_inbox
title: 'Re: [PATCH 3/3] io: Sync fts with gnulib'
headline: 'io: Sync fts with gnulib'
tldr: The patch syncs the fts implementation with gnulib, including fixes and documentation
  for FTS_NOSTAT.
stakes: Synchronization with gnulib ensures glibc's fts implementation remains up-to-date
  with bug fixes and feature enhancements.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch addresses feedback and incorporates suggestions, indicating
  a positive reception.
technical_tradeoffs:
- Synchronization with external libraries can introduce dependencies and require ongoing
  maintenance.
- Adopting changes from gnulib may require adapting glibc-specific code.
- May need to resolve conflicts that arise during the synchronization process.
series_id: 'glibc:io: sync fts with gnulib'
series_role: reply
series_parts:
- title: 'io: Sync fts with gnulib'
  url: https://inbox.sourceware.org/libc-alpha/c06b6f0d-1acf-482e-b2c1-098c92dcd467@cs.ucla.edu
  n: 3
  total: 3
- title: 'io: Sync fts with gnulib'
  url: https://inbox.sourceware.org/libc-alpha/20260417132808.235562-4-adhemerval.zanella@linaro.org
  n: 3
  total: 3
url: https://inbox.sourceware.org/libc-alpha/5fdbda76-438c-4f14-a4f3-b6b774f997fa@linaro.org
bugzilla_url: null
date: '2026-04-17'
---

This patch updates the fts implementation in glibc by syncing it with the gnulib version. Paul Eggert suggested using a FIFO instead of a directory in the example for FTS_NSOK. The patch addresses this suggestion.
