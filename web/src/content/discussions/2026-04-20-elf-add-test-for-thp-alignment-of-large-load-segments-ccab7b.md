---
project: glibc
subsystem: elf
patch_id: null
tags:
- elf
- thp
- glibc
- test
- memory management
discussion_id: PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v10] elf: Add test for THP alignment of large load segments'
headline: 'Elf: Add test for THP alignment of large load segments'
tldr: A new test verifies that large executable segments are mapped at THP-aligned
  addresses when THP is enabled in "always" mode.
stakes: Ensures correct memory mapping behavior when using Transparent Huge Pages,
  which can impact performance.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a new test case, increasing the test suite size but improving confidence in
  THP alignment.
- The test is skipped if THP is not enabled in "always" mode, so it might not be executed
  on all systems.
primer_expert: This patch adds a test for THP alignment. glibc's ELF loader can use
  THP for large segments. This interacts with the kernel's memory management and can
  affect performance.
primer_general: Transparent Huge Pages (THP) is a memory management feature where
  the system uses larger memory pages (e.g., 2MB) instead of the standard size (e.g.,
  4KB). This can improve performance by reducing TLB misses. Glibc's ELF loader is
  responsible for loading shared objects and executables into memory, and it can be
  configured to use THP for larger segments if the underlying system supports it.
  This involves mapping regions of memory to take advantage of the larger page size.
  Correct alignment is crucial for THP to function properly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

This patch adds a test to verify that large executable PT_LOAD segments are mapped at addresses aligned to the THP size when the glibc tunable glibc.elf.thp=1 is enabled and the system is configured to use THP in "always" mode. The test loads a shared object with a large executable segment and checks /proc/self/maps. The patch has been committed.
