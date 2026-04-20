---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- thp
- memory management
- testing
discussion_id: PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v10] elf: Add test for THP alignment of large load segments'
headline: 'Elf: Add test for THP alignment of large load segments'
tldr: A test for THP alignment of large load segments has been committed, ensuring
  segments are aligned to THP size when glibc.elf.thp=1 and THP is in always mode.
stakes: Ensures correct alignment of large load segments when using Transparent Huge
  Pages (THP), potentially improving performance.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
primer: Transparent Huge Pages (THP) is a memory management feature in the Linux kernel
  that uses large pages (e.g., 2MB) to reduce TLB pressure. The ELF format defines
  how executables and shared libraries are structured. This test ensures that large
  segments within these files are properly aligned in memory to take advantage of
  THP when enabled. Alignment is crucial for optimal performance when using THP.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

The patch adds a test to verify that large executable PT_LOAD segments are mapped at addresses aligned to the THP size when the glibc tunable `glibc.elf.thp=1` is enabled and the system is configured to use THP in 'always' mode. The test uses dlopen to load a shared object with a large executable segment and inspects /proc/self/maps to check alignment. Wilco Dijkstra reviewed and committed the patch, marking it UNSUPPORTED if THP is not in always mode.
