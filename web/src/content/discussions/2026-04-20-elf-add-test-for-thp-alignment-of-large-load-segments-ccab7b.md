---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- thp
- alignment
- performance
discussion_id: PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v10] elf: Add test for THP alignment of large load segments'
headline: 'elf: Add test for THP alignment of large load segments'
tldr: A test for THP alignment of large load segments has been committed after a review.
stakes: Ensuring proper THP alignment improves performance by reducing TLB misses
  and improving memory access efficiency. This is especially important for large applications
  that benefit from THP.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Committed
outcome: committed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Reviewed and committed the patch, noting that it now says UNSUPPORTED
    if THP is not [always].
  quote: LGTM - it now says UNSUPPORTED if THP is not [always]. Committed.
primer_expert: This patch adds a test to the glibc ELF loader to verify that large
  executable segments are aligned to the THP size when THP is enabled. PT_LOAD segments
  in ELF files specify regions of the file that should be loaded into memory. THP
  (Transparent Huge Pages) are large memory pages that can improve performance. The
  test checks if the mapping address is aligned to the THP page size, which can be
  obtained from the kernel.
primer_general: In Linux, Transparent Huge Pages (THP) is a memory management feature
  that allows the system to use larger memory pages (typically 2MB) instead of the
  standard 4KB pages. This can improve performance by reducing the overhead of managing
  memory and improving TLB (Translation Lookaside Buffer) hit rates. This patch adds
  a test to glibc (the GNU C Library) to ensure that when a program loads a large
  executable segment, it is aligned to the THP size. This alignment is important for
  THP to work effectively and improve the program's performance.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982457B2EA5506F61A4A333832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

Wilco Dijkstra reviewed and committed a patch that adds a test to verify that large executable PT_LOAD segments are mapped at addresses aligned to the THP size when the glibc tunable glibc.elf.thp=1 is enabled and the system is configured to use THP in "always" mode. The commit includes a change to mark the test as UNSUPPORTED if THP is not in "always" mode.
