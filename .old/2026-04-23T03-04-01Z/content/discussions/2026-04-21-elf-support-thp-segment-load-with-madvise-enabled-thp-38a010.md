---
project: glibc
subsystem: elf
patch_id: null
tags:
- THP
- madvise
- elf
- glibc
- performance
discussion_id: CAMe9rOpuLjOmaFDiXVf+LOx54H5Nss95RBziKk91LyceH4Dibg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v5] elf: Support THP segment load with madvise enabled THP'
headline: 'Elf: Support THP segment load with madvise enabled THP'
tldr: Enable THP segment loading when THP is enabled with madvise in the kernel by
  calling madvise with MADV_HUGEPAGE on THP-eligible segments.
stakes: This patch improves performance by enabling Transparent Huge Pages (THP) for
  applications when THP is enabled with madvise in the kernel.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Potential for increased memory usage if THP is not used efficiently.
- Possible latency spikes due to background THP consolidation.
- May introduce compatibility issues with applications that are not designed to use
  THP.
- Requires careful consideration of THP eligibility criteria to avoid performance
  regressions.
- Impacts the ELF loader and requires thorough testing.
exchanges: []
primer_expert: This patch modifies the ELF loader in glibc to support THP when THP
  is enabled with madvise. It involves changes to ``_dl_map_segment_align``, ``rtld_setup_main_map``,
  ``LIBC_START_MAIN``, and ``_dl_postprocess_loadcmd`` to call ``madvise`` with ``MADV_HUGEPAGE``
  on THP-eligible segments. This affects how segments are mapped into memory during
  program loading.
primer_general: Transparent Huge Pages (THP) can improve performance by using larger
  memory pages. This patch enables THP segment loading when THP is enabled with ``madvise``
  in the kernel. It works by calling ``madvise`` with ``MADV_HUGEPAGE`` on all THP
  eligible segments, which informs the kernel that these segments are suitable for
  THP. This can lead to performance improvements for applications that benefit from
  THP.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOpuLjOmaFDiXVf+LOx54H5Nss95RBziKk91LyceH4Dibg@mail.gmail.com
bugzilla_url: null
date: '2026-04-21'
---

This patch enables THP segment loading when THP is enabled with madvise in the kernel. To enable THP segment load in an application, ``madvise`` should be called with ``MADV_HUGEPAGE`` on all THP eligible ``PT_LOAD`` segments. This patch addresses bugs #34079 and #34080.
