---
project: glibc
subsystem: glibc
patch_id: null
tags:
- thp
- performance
- memory management
- dynamic linker
- elf
discussion_id: CAMe9rOonJkGpOVzJDTmcy5Zg1AzUwaPrvByhG1PWE+TsbnongQ@mail.gmail.com
source_type: public_inbox
title: ''
headline: Support THP segment load with madvise enabled THP
tldr: This patch series enables Transparent Huge Page (THP) segment loading when THP
  is enabled with madvise in the kernel, fixing bugs related to dynamic and static…
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increased complexity in the dynamic linker.
- Potential for increased memory fragmentation if THP is not used effectively.
- The performance benefits are workload-dependent.
exchanges: []
primer_expert: This series modifies the dynamic linker to support THP when enabled
  via `madvise`. It changes `_dl_map_segment_align` to update alignments of PT_LOAD
  segments and calls `madvise` with `MADV_HUGEPAGE`. It's relevant for ELF loading
  and memory management within glibc.
primer_general: Transparent Huge Pages (THP) is a Linux kernel feature that can improve
  performance by using larger memory pages. This patch modifies glibc, the GNU C Library,
  to better support THP when THP is enabled with `madvise`. `madvise` is a system
  call that allows programs to give hints to the kernel about how they intend to use
  memory.  The patch makes changes to the dynamic linker, which is responsible for
  loading shared libraries at runtime, to ensure that THP is used effectively.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOonJkGpOVzJDTmcy5Zg1AzUwaPrvByhG1PWE+TsbnongQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-22'
---

This patch series enables Transparent Huge Page (THP) segment loading when THP is enabled with `madvise` in the kernel, addressing bugs #34079 and #34080 for both dynamic and static executables. It aligns PT_LOAD segments to THP page size, calls `madvise` with `MADV_HUGEPAGE` on THP-eligible segments, and sets the maximum page alignment on THP. This approach works when THP is enabled with 'always' in the kernel.
