---
project: glibc
subsystem: io
patch_id: null
tags:
- fts
- ftw
- gnulib
- consolidation
- synchronization
discussion_id: 20260417132808.235562-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: '[PATCH 0/3] Consolidate and sync fts/ftw'
headline: Consolidate and sync fts/ftw
tldr: This series consolidates the fts/ftw implementation and syncs fts with gnulib,
  including fixes for FTS_NOSTAT.
stakes: Consolidating implementations reduces code duplication and improves maintainability,
  while syncing with gnulib ensures access to the latest features and bug fixes.
proposer: Adhemerval Zanella <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch series aims to improve code maintainability and incorporates
  external updates, suggesting a positive direction.
  handled carefully.
series_id: glibc:consolidate and sync fts/ftw
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260417132808.235562-1-adhemerval.zanella@linaro.org
bugzilla_url: null
date: '2026-04-17'
---

This patch series consolidates the fts/ftw implementations on generic code, aliasing FTS from __OFF_T_MATCHES_OFF64_T. It also includes a sync of the fts implementation from gnulib, incorporating fixes and documentation for FTS_NOSTAT. The consolidation simplifies the code and helps in adding new versioning symbols if needed.
