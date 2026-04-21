---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- thp
- memory management
- dynamic linking
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: 'Elf: Support THP Segment Load With Madvise Enabled THP'
tldr: This patch enables Transparent Huge Page (THP) support for segment loading in
  glibc when THP is enabled with madvise in the kernel.
stakes: Enabling THP with madvise can improve application performance by using larger
  memory pages, but requires careful management to avoid performance regressions or
  memory waste.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Enabling THP can improve performance for some applications but may degrade performance
  for others due to latency spikes and memory waste.
- Using madvise provides applications with control over THP usage, but requires developers
  to understand the performance implications.
- The patch adds complexity to the dynamic linking process.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes enabling Transparent Huge Page (THP) support for segment loading
    in glibc when THP is enabled with madvise in the kernel.
  quote: 'to enable THP segment load in an application, madvise should

    be called with MADV_HUGEPAGE on all THP eligible PT_LOAD segments'
- author: Carlos O'Donell <carlos@redhat.com>
  role: reviewer
  position: Acknowledges the patch and lists the changes from the previous version.
  quote: null
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Replies to Carlos O'Donell, seemingly in agreement.
  quote: null
primer_expert: This patch modifies glibc's dynamic linker to support THP when enabled
  with `madvise`. It involves changes to `_dl_map_segment_align`, `rtld_setup_main_map`,
  and `_dl_postprocess_loadcmd` to call `madvise` with `MADV_HUGEPAGE` on THP-eligible
  `PT_LOAD` segments. The patch also introduces `DL_MAP_DEFAULT_THP_PAGESIZE` in `hugepages.h`.
  This is relevant for understanding how glibc interacts with the kernel's memory
  management and dynamic linking, specifically the ELF loading process.
primer_general: Transparent Huge Pages (THP) is a Linux kernel feature that attempts
  to improve performance by using larger memory pages (typically 2MB) instead of the
  standard 4KB pages. This patch modifies glibc, the GNU C Library, to support THP
  when THP is enabled in "madvise" mode. In this mode, applications can advise the
  kernel to use THP for specific memory regions. The patch ensures that when a program
  or library is loaded, the appropriate memory segments are marked for THP if the
  system is configured to use it. This can improve performance for applications that
  benefit from larger pages, but also introduces potential drawbacks like increased
  memory usage or memory fragmentation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

H.J. Lu proposes enabling Transparent Huge Page (THP) support for segment loading in glibc when THP is enabled with madvise in the kernel. The patch modifies how segments are aligned and mapped during dynamic linking, and calls `madvise` with `MADV_HUGEPAGE` on THP-eligible segments. The patch also adds tests to verify that large executable PT_LOAD segments are mapped at addresses aligned to THP page size.
