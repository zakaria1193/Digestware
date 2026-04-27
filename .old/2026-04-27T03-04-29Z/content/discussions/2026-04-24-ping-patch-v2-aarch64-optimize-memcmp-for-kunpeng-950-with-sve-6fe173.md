---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- aarch64
- memcmp
- optimization
- SVE
discussion_id: 20260424035025.574-1-yeweihong@huawei.com
source_type: public_inbox
title: 'Ping:[PATCH v2] aarch64: Optimize memcmp for Kunpeng 950 with SVE'
headline: 'Ping:[PATCH v2] aarch64: Optimize memcmp for Kunpeng 950 with SVE'
tldr: The patch optimizes memcmp for the Kunpeng 950 processor using Scalable Vector
  Extension (SVE).
proposer: Weihong Ye <yeweihong@huawei.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increased code complexity in `memcmp`.
- Potential for increased binary size.
- Optimization specific to Kunpeng 950, may not benefit other architectures.
exchanges: []
primer_expert: The patch focuses on optimizing `memcmp` in `string/memcmp.c` for the
  AArch64 architecture, utilizing SVE. This optimization is specific to the Kunpeng
  950 processor, which may not be widely known outside of hardware-specific glibc
  optimizations. The interaction with other parts of glibc is minimal, but the performance
  impact on workloads using `memcmp` on Kunpeng 950 systems could be significant.
primer_general: '`memcmp` is a fundamental C function used to compare two blocks of
  memory. Glibc, the standard C library, provides optimized implementations of `memcmp`
  for various architectures. This patch aims to improve `memcmp`''s performance on
  the Kunpeng 950 processor by leveraging its Scalable Vector Extension. SVE allows
  the processor to perform the same operation on multiple data elements simultaneously,
  speeding up the comparison process. This optimization sits within the runtime library
  and directly affects the performance of applications that rely heavily on `memcmp`.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260424035025.574-1-yeweihong@huawei.com
bugzilla_url: null
date: '2026-04-24'
---

This patch optimizes the `memcmp` function for AArch64 architecture, specifically targeting the Kunpeng 950 processor using Scalable Vector Extension (SVE). The patch is a re-ping of a previous submission, seeking feedback and comments.  The goal is to improve performance of memory comparison operations on this specific hardware.
