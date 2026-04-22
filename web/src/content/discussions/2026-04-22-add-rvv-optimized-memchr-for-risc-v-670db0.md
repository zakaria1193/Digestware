---
project: glibc
subsystem: riscv
patch_id: null
tags:
- riscv
- RVV
- glibc
- memchr
- optimization
discussion_id: dfc87507-e63d-422a-9e8c-96a438ff7427@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH] riscv: add RVV-optimized memchr'
headline: Add RVV-optimized memchr for RISC-V
tldr: This patch adds a RISC-V RVV-optimized implementation of the memchr function
  to glibc.
stakes: RVV-optimized memchr can improve performance on RISC-V processors with vector
  extensions, benefiting applications that rely heavily on memory searching.
proposer: daichengrong <daichengrong@iscas.ac.cn>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- RVV optimization increases code complexity but improves performance on supported
  hardware.
- Requires RVV-enabled RISC-V processors to realize performance gains.
exchanges: []
primer_expert: This patch introduces an RVV-optimized `memchr` for RISC-V in glibc.
  RVV (RISC-V Vector Extension) allows for SIMD-style operations on RISC-V, potentially
  speeding up memory operations. `memchr` searches for the first occurrence of a character
  within a block of memory. Toolchain developers working on RISC-V can use this as
  a reference for RVV optimization techniques.
primer_general: '`memchr` is a standard C library function that searches for the first
  occurrence of a specific character within a given block of memory. This patch optimizes
  `memchr` for RISC-V processors that have the RVV (RISC-V Vector Extension). RVV
  allows the processor to perform the same operation on multiple data elements simultaneously
  (SIMD), leading to faster execution. This optimization improves the performance
  of programs that frequently use `memchr` on RISC-V systems.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/dfc87507-e63d-422a-9e8c-96a438ff7427@iscas.ac.cn
bugzilla_url: null
date: '2026-04-22'
---

Kito Cheng proposed adding a RISC-V RVV (vector extension) optimized implementation of the `memchr` function to glibc. The patch provides a new implementation of `memchr` specifically designed to leverage the RVV instructions for improved performance on RISC-V processors.
