---
project: glibc
subsystem: elf
patch_id: null
tags:
- elf
- THP
- testing
- performance
- memory management
discussion_id: PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v10] elf: Add test for THP alignment of large load segments'
headline: 'Elf: Add test for THP alignment of large load segments'
tldr: A new test verifies that large executable PT_LOAD segments are mapped at addresses
  aligned to the THP size when THP is enabled in "always" mode.
stakes: Ensures that glibc correctly utilizes Transparent Huge Pages (THP) for performance
  optimization when loading shared objects.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased test complexity.
- Dependency on THP kernel configuration.
primer_expert: This patch adds a test for `PT_LOAD` segments THP alignment. The test
  uses `dlopen` to load a shared object and checks `/proc/self/maps` to verify the
  mapping address alignment, which depends on `glibc.elf.thp` and the system's THP
  mode. Correct THP alignment can improve performance. Interaction with the dynamic
  linker (`ld-linux.so`) is key here.
primer_general: Transparent Huge Pages (THP) is a memory management feature that allows
  the system to use larger memory pages (typically 2MB) instead of the standard 4KB
  pages. This can improve performance by reducing TLB misses. The dynamic linker (`ld-linux.so`)
  maps program segments into memory, and glibc can influence this process to utilize
  THP for eligible segments, assuming the kernel supports it. This requires specific
  alignment. This patch adds a test to ensure that glibc correctly aligns large executable
  segments when THP is enabled.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

This patch adds a test to verify that large executable segments in shared objects are mapped at addresses aligned to the THP size when the glibc tunable `glibc.elf.thp=1` is enabled and the system is configured to use THP in "always" mode. The test loads a shared object with a large executable segment and checks `/proc/self/maps` for THP alignment. The patch has been reviewed and committed.
