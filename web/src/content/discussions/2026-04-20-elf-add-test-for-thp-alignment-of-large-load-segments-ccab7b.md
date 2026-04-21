---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- THP
- alignment
- performance
discussion_id: PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v10] elf: Add test for THP alignment of large load segments'
headline: 'elf: Add test for THP alignment of large load segments'
tldr: A test for THP alignment of large load segments has been approved and committed.
stakes: Ensuring proper THP alignment can improve application performance by reducing
  TLB misses.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Enabling THP can improve performance but may also increase memory usage.
- Proper alignment requires coordination between the kernel, glibc, and the application.
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Approved the patch and committed it, noting that the test now reports
    UNSUPPORTED if THP is not in "always" mode.
  quote: LGTM - it now says UNSUPPORTED if THP is not [always]. Committed.
primer_expert: This patch adds a test for THP alignment of ELF load segments.  THP
  (Transparent Huge Pages) can improve performance by reducing TLB overhead. The glibc
  tunable `glibc.elf.thp` controls whether glibc attempts to align large load segments
  to THP boundaries. This test verifies that alignment.  A general toolchain dev might
  not be aware of the specific glibc tunables affecting THP behavior.
primer_general: Transparent Huge Pages (THP) is a Linux kernel feature that uses larger
  memory pages (typically 2MB) to improve performance by reducing the overhead of
  managing memory translations. This patch adds a test to glibc to ensure that large
  executable sections of programs are properly aligned in memory when THP is enabled.
  Proper alignment can further improve performance by reducing the number of TLB (Translation
  Lookaside Buffer) misses, which occur when the system has to look up the physical
  address of a memory location.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

A patch adding a test to verify that large executable PT_LOAD segments are mapped at addresses aligned to the THP size when the glibc tunable glibc.elf.thp=1 is enabled and the system is configured to use THP in "always" mode has been reviewed and committed. The test is skipped if THP size cannot be determined or if THP is not enabled in "always" mode.
