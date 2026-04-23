---
project: glibc
subsystem: elf
patch_id: null
tags:
- elf
- THP
- alignment
- testing
- PT_LOAD
discussion_id: 20260417035556.1778246-1-wangrui@loongson.cn
source_type: public_inbox
title: '[PATCH v10] elf: Add test for THP alignment of large load segments'
headline: Add test for THP alignment of large load segments
tldr: This patch adds a test to verify that large executable PT_LOAD segments are
  THP-aligned when glibc.elf.thp=1 and THP is in 'always' mode.
stakes: Ensures correct THP alignment for large executable segments, which can improve
  performance by reducing TLB misses.
proposer: WANG Rui <wangrui@loongson.cn>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch adds a test, improving code quality. Version 10 suggests
  refinement and heading towards consensus.
  in "always" mode.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260417035556.1778246-1-wangrui@loongson.cn
bugzilla_url: null
date: '2026-04-17'
---

This patch adds a new test to verify that large executable PT_LOAD segments are mapped at addresses aligned to the THP size when the glibc tunable glibc.elf.thp=1 is enabled and the system is configured to use THP in "always" mode. The test loads a shared object and checks /proc/self/maps for THP alignment. The test skips if THP size is unavailable or not in "always" mode.
