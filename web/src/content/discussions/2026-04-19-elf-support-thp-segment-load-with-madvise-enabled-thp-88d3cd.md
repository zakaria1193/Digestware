---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- THP
- madvise
- performance
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: 'Elf: Support THP segment load with madvise enabled THP'
tldr: This patch series enables Transparent Huge Page (THP) support for segment loading
  when THP is enabled with madvise in the kernel.
stakes: Enables THP when using madvise, which can improve performance by reducing
  TLB misses and improving memory locality. This benefits applications that use large
  amounts of memory.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The patch series is on its 4th version, indicating ongoing refinement
  and discussion.
technical_tradeoffs:
- Requires kernel support for THP with madvise.
- Adds complexity to the segment loading process.
- May increase memory fragmentation in some cases.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

This patch series enables THP support for segment loading when THP is enabled with madvise in the kernel. It involves updating segment alignments, calling `madvise` with `MADV_HUGEPAGE` on THP-eligible segments, and adding tests to verify correct alignment. This addresses issues where THP was not being utilized effectively in dynamic and static executables, as well as shared objects.
