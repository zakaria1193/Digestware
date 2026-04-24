---
project: glibc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- memcpy
- optimization
- IFUNC
- RVV
discussion_id: 69b471a8-3e1f-449e-99f0-ba380e4f2e6e@oss.qualcomm.com
source_type: public_inbox
title: 'Re: [PATCH v2] RISC-V: add multiarch RVV support for memcpy using FMV IFUNC'
headline: 'RISC-V: add multiarch RVV support for memcpy using FMV IFUNC'
tldr: A proposed RISC-V memcpy optimization using FMV IFUNC is already implemented,
  making this patch obsolete.
proposer: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
  role: other
  position: Notes that the patch is obsolete because a functionally equivalent version
    has already been installed.
  quote: Note Peter installed Yow Zihong's version which is functionally equivalent.  So
    this patch is obsolete.
primer_expert: This patch concerns glibc's architecture-specific optimized memcpy
  implementations, selectable at runtime via IFUNC. The RISC-V vector extension (RVV)
  is a relatively new addition, and glibc needs to provide optimized versions that
  take advantage of it when available. The interaction with the dynamic linker (IFUNC)
  and CPU feature detection makes this non-trivial.
primer_general: memcpy is a fundamental function for copying blocks of memory.  To
  maximize performance, glibc provides optimized versions of memcpy that are selected
  at runtime based on CPU features. CPU feature detection is handled by the dynamic
  linker using IFUNCs. This patch aims to add an optimized memcpy implementation for
  RISC-V processors that support the Vector extension (RVV).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/69b471a8-3e1f-449e-99f0-ba380e4f2e6e@oss.qualcomm.com
bugzilla_url: null
date: '2026-04-23'
---

This patch proposed to use RISC-V's Vector extension (RVV) to speed up memcpy using Function Multi-Versioning (FMV) with an Indirect Function (IFUNC). However, a functionally equivalent version has already been installed, rendering this patch obsolete.
