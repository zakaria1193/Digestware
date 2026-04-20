---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- thp
- performance
- memory management
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: Enable THP segment load with madvise in ELF
tldr: This patch enables Transparent Huge Page (THP) segment loading in glibc when
  THP is enabled with madvise in the kernel.
stakes: Improves application performance by utilizing THP when available, especially
  when THP is enabled with madvise.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Requires kernel support for THP.
- May increase memory usage if THP is not used efficiently.
- Adds complexity to the ELF loader.
primer_expert: This patch modifies glibc's ELF loader (`_dl_map_segment_align`, `_dl_executable_postprocess`,
  `_dl_postprocess_loadcmd`) to support THP when enabled with `madvise`. It addresses
  alignment of `PT_LOAD` segments and uses `madvise` to encourage THP usage. It also
  interacts with the `-z separate-code` linker option and `<hugepages.h>`.
primer_general: Transparent Huge Pages (THP) is a Linux kernel feature that automatically
  promotes the use of larger memory pages (2MB or 1GB instead of 4KB) to improve performance.  The
  ELF loader is responsible for loading executables and shared libraries into memory.  This
  patch modifies the ELF loader in glibc to take advantage of THP when THP is enabled
  with `madvise`, which requires programs to explicitly request THP using the `madvise`
  system call. By enabling this feature, applications can potentially improve performance
  without code changes, assuming the kernel is configured to use THP.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

This patch enables Transparent Huge Page (THP) segment loading in glibc when THP is enabled with madvise in the kernel. It includes changes to update alignments of PT_LOAD segments, call `madvise` with `MADV_HUGEPAGE` on THP eligible segments, and add tests to verify the alignment.  The patch also folds in a linker option and adjusts how THP page size is handled.
