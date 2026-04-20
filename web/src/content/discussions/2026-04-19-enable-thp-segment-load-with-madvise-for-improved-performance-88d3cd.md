---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- THP
- madvise
- performance
- elf
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: Enable THP segment load with madvise for improved performance
tldr: This patch enables Transparent Huge Page (THP) segment loading when THP is enabled
  with madvise, improving application performance.
stakes: Enabling THP when using madvise can improve performance, but requires careful
  handling to avoid potential issues.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: Patch aims to improve performance and includes tests, but also
  acknowledges potential risks.
technical_tradeoffs:
- Potential performance improvements with THP.
- Increased code complexity for handling THP with madvise.
- Risk of regressions or compatibility issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

This patch updates the THP segment load approach to work when THP is enabled with madvise in the kernel. It defines `DL_MAP_DEFAULT_THP_PAGESIZE` in `hugepages.h`, modifies `_dl_map_segment_align` to update alignments of PT_LOAD segments, calls `_dl_executable_postprocess` and `_dl_postprocess_loadcmd_extra` to call `madvise` with `MADV_HUGEPAGE` on THP eligible segments, and adds tests to verify alignment to THP page size.
