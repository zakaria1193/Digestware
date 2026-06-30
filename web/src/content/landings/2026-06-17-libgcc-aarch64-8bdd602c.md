---
project: gcc
subsystem: libgcc/aarch64
patch_id: null
tags:
- aarch64
- libgcc
- sme
commit_hash: 8bdd602c6dc534aa482653ad7e99f3332599c671
source_type: github
author: Claudio Bantaloukas
headline: 'AArch64: Implement streaming-compatible memory operations in libgcc'
tldr: Adds implementations for ARM's streaming-compatible memcpy, memmove, memset,
  and memchr to libgcc.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Arm C Language Extensions (ACLE) specify `__arm_sc_*` functions
  for memory operations within SME streaming modes. This change adds scalar implementations
  in libgcc for these functions, ensuring they can be used in streaming contexts without
  affecting SME state. The change involves new assembly files and updates to the version
  and target configuration files. `libgcc-sme.ver` exports the functions, while `t-aarch64`
  and `aarch64-asm.h` hook them into the build and assembly process.
primer_general: The ARM Scalable Matrix Extension (SME) is a feature for improving
  the performance of matrix computations. It includes a "streaming mode" that allows
  certain operations to execute more efficiently without affecting the processor's
  general state. This commit adds special versions of standard memory functions like
  `memcpy` and `memset` to the GCC library (libgcc) for ARM processors that support
  SME. These functions are designed to be used within SME's streaming mode, ensuring
  they don't disrupt the performance benefits of streaming operations. Basic tests
  are included to verify their functionality.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8bdd602c6dc534aa482653ad7e99f3332599c671
date: '2026-06-17'
is_stub: false
stub_reason: ''
---

ARM's Scalable Matrix Extension (SME) defines streaming-compatible versions of common memory routines.
This patch adds scalar implementations for `__arm_sc_memcpy`, `__arm_sc_memmove`, `__arm_sc_memset`, and `__arm_sc_memchr` to libgcc.
These functions are intended to behave identically to their standard C counterparts but are designed to work within streaming regions, ensuring predictable performance and avoiding unexpected state changes.
