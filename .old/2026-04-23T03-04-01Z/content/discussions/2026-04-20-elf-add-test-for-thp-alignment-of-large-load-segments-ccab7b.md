---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- THP
- memory alignment
- performance
discussion_id: PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v10] elf: Add test for THP alignment of large load segments'
headline: 'elf: Add test for THP alignment of large load segments'
tldr: Test added and committed to verify THP alignment of large executable PT_LOAD
  segments when glibc tunable is enabled and THP is in "always" mode.
stakes: Ensures proper memory alignment for performance when using Transparent Huge
  Pages (THP).
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The test increases the overall test suite size.
- Proper alignment can improve performance, but might introduce constraints on memory
  layout.
- THP can improve performance in some cases, but can also cause performance regressions
  if not used appropriately.
exchanges:
- author: Wilco Dijkstra
  role: reviewer
  position: Reviews and commits the patch after verifying that it reports UNSUPPORTED
    if THP is not in 'always' mode.
  quote: LGTM - it now says UNSUPPORTED if THP is not [always]. Committed.
primer_expert: This patch adds a test for THP alignment of `PT_LOAD` segments. `PT_LOAD`
  specifies how to load segments from the ELF file into memory. THP is enabled via
  the `glibc.elf.thp` tunable. The test checks alignment in `/proc/self/maps`, it
  checks the address where it's loaded is a multiple of THP size when the tunable
  is enabled.
primer_general: In computing, memory is often divided into pages.  Transparent Huge
  Pages (THP) is a Linux kernel feature that attempts to use larger memory pages (huge
  pages) to improve performance.  The ELF format is a common file format for executables
  and shared libraries. `PT_LOAD` segments within an ELF file specify how parts of
  the file should be loaded into memory. This test verifies the memory mapped is aligned
  to the page size and hence improves performance and reduces TLB misses.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

A test has been added to verify that large executable `PT_LOAD` segments are mapped at addresses aligned to the Transparent Huge Page (THP) size. This is done when the `glibc.elf.thp=1` tunable is enabled and the system is configured to use THP in "always" mode. The test uses `dlopen` to load a shared object and checks `/proc/self/maps`.
