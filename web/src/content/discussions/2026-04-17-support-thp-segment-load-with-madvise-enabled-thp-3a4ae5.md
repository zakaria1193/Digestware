---
project: glibc
subsystem: elf
patch_id: null
tags:
- elf
- THP
- madvise
- performance
- dynamic linker
discussion_id: CAMe9rOp-_96y0s=3yMi9_+8G_PsaagRAHrMqLqCHLY4QYK6XvQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2 2/2] elf: Support THP segment load with madvise enabled THP'
headline: Support THP segment load with madvise enabled THP
tldr: This patch enables THP segment loading when THP is enabled with madvise in the
  kernel.
stakes: Allows applications to take advantage of THP even when the kernel is configured
  to use madvise mode, potentially improving performance.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The patch addresses a limitation in THP support and builds upon
  previous work. The discussion suggests ongoing refinement.
series_id: 'glibc:elf: support thp segment load with madvise enabled thp'
series_role: reply
series_parts:
- title: 'elf: Support THP segment load with madvise enabled THP'
  url: https://inbox.sourceware.org/libc-alpha/CAHirt9hsXHVttvtkqkrF=WGn+K0h9_EeJpZnV5g1BpcJddYH2g@mail.gmail.com
  n: 2
  total: 2
- title: 'elf: Support THP segment load with madvise enabled THP'
  url: https://inbox.sourceware.org/libc-alpha/CAMe9rOryN0j-SZT_C4EYzEHt+B7kQTvC5t4GaQ3H8dPXG+aejg@mail.gmail.com
  n: 2
  total: 2
- title: 'elf: Support THP segment load with madvise enabled THP'
  url: https://inbox.sourceware.org/libc-alpha/CAMe9rOrVsKZz0MuqGwu1KX4MaFK=tc0idvk1kHy2+B8hOdLCVA@mail.gmail.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOp-_96y0s=3yMi9_+8G_PsaagRAHrMqLqCHLY4QYK6XvQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

This patch modifies the ELF loader to support Transparent Huge Pages (THP) when THP is enabled with madvise in the kernel. It removes `_dl_map_segment_align`, calls `_dl_map_segment_adjust` to align THP-eligible `PT_LOAD` segments, and calls `madvise` with `MADV_HUGEPAGE` on those segments.
