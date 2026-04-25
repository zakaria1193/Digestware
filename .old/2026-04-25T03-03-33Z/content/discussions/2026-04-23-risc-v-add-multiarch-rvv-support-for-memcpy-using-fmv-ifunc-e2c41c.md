---
project: glibc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- memcpy
- vectorization
- ifunc
- fmv
discussion_id: 69b471a8-3e1f-449e-99f0-ba380e4f2e6e@oss.qualcomm.com
source_type: public_inbox
title: 'Re: [PATCH v2] RISC-V: add multiarch RVV support for memcpy using FMV IFUNC'
headline: 'RISC-V: Add multiarch RVV support for memcpy using FMV IFUNC'
tldr: A patch adding RISC-V vector support for memcpy is obsolete because a functionally
  equivalent version has already been installed.
proposer: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adding RVV support increases code complexity.
- IFUNC resolvers add runtime overhead.
- The performance benefits depend on the availability of RVV and the size of the memory
  being copied.
exchanges: []
primer_expert: This patch adds a multiarch implementation of `memcpy` for RISC-V,
  leveraging FMV IFUNC to select a vector-optimized version at runtime if the CPU
  supports RVV. It interacts with the dynamic linker and CPU feature detection. This
  is relevant to ABI and performance for RISC-V systems.
primer_general: The `memcpy` function copies a block of memory from one location to
  another.  This patch uses RISC-V vector instructions (RVV) to potentially speed
  up `memcpy` on RISC-V processors that support these instructions.  The Function
  Multi-Versioning (FMV) and IFUNC (indirect function) mechanisms allow the system
  to choose the best `memcpy` implementation at runtime based on the CPU's capabilities,
  providing optimized performance where possible.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/69b471a8-3e1f-449e-99f0-ba380e4f2e6e@oss.qualcomm.com
bugzilla_url: null
date: '2026-04-23'
---

A patch adding RISC-V vector support for `memcpy` using Function Multi-Versioning (FMV) and IFUNC is now obsolete. Jeffrey Law notes that a functionally equivalent version has already been installed. The original patch aimed to utilize new RISC-V CPUs with vector extensions to speed up functions like `memcpy`.
