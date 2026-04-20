---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- thp
- memory management
- performance
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: 'Elf: Support THP segment load with madvise enabled THP'
tldr: Enable glibc to load program segments using Transparent Huge Pages (THP) when
  THP is enabled with madvise, improving memory utilization.
stakes: This patch enables THP for program segments when THP is configured with madvise,
  which can reduce memory fragmentation and improve performance for applications using
  large memory regions.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Requires kernel support for THP with madvise.
- Adds complexity to glibc's ELF loading process.
- May increase memory usage if THP is not used efficiently.
primer: Transparent Huge Pages (THP) is a Linux kernel memory management feature that
  reduces TLB (Translation Lookaside Buffer) pressure by using larger page sizes (typically
  2MB) than the default 4KB.  glibc's dynamic linker (`ld-linux.so`) is responsible
  for loading shared libraries and executables into memory.  The ELF format describes
  how a program is structured in memory.  madvise is a system call that allows a program
  to advise the kernel about how it intends to use a region of memory. This patch
  modifies glibc's ELF loading routines to take advantage of THP when available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

This patch series enables THP support for program segments in glibc when the kernel uses madvise for THP. It aligns PT_LOAD segments to THP page sizes and calls `madvise` with `MADV_HUGEPAGE` on THP-eligible segments. The patch updates the `_dl_map_segment_align` function and adds calls to `_dl_executable_postprocess` and `_dl_postprocess_loadcmd_extra` to handle dynamic and static executables, as well as shared objects. The series includes tests to verify alignment.
