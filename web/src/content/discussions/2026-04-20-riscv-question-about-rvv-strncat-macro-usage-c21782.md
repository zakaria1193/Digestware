---
project: glibc
subsystem: riscv
patch_id: null
tags:
- glibc
- riscv
- RVV
- ifunc
- optimization
discussion_id: 0f654c95-3b36-4fdc-a598-102686601ac0@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [PATCH v5 14/18] riscv: Add RVV strncat for multiarch and non-multiarch'
headline: 'Riscv: Question about RVV strncat macro usage.'
tldr: Inquiry regarding the need for `riscv_libc_ifunc_redirected` macro versus `riscv_libc_ifunc`
  for RVV strncat implementation.
stakes: Ensuring proper ifunc usage for optimized RISC-V string functions contributes
  to performance and code maintainability.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Choosing the correct ifunc macro is crucial for proper runtime dispatch.
- Different macros may have different overhead or capabilities.
- Inconsistent macro usage can lead to code maintenance issues.
primer_expert: This patch series introduces optimized string functions for RISC-V
  with the RVV extension, using the ifunc mechanism for runtime dispatch.  `riscv_libc_ifunc`
  and `riscv_libc_ifunc_redirected` likely handle different ifunc resolution strategies.  Understanding
  their distinction is crucial for correct multiarch function selection. This involves
  `sysdeps/riscv/multiarch/*` and `sysdeps/riscv/rvv/*`.
primer_general: The glibc library provides standard C library functions. On RISC-V
  architectures, optimized versions of these functions can be implemented using the
  RVV (RISC-V Vector Extension) for improved performance.  Ifuncs (Indirect Functions)
  are used to select the appropriate implementation at runtime based on the CPU's
  capabilities. This discussion concerns the correct use of ifuncs when adding RVV-optimized
  `strncat` and other string functions.
series_id: 'glibc:riscv: add rvv strncat for multiarch and non-multiarch'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/0f654c95-3b36-4fdc-a598-102686601ac0@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-20'
---

This email questions the use of the `riscv_libc_ifunc_redirected` macro in the RVV strncat patch, asking why it differs from the `riscv_libc_ifunc` macro used in the memset and strcat implementations. The author requests justification for the new macro and its specific application in this context, also applying to strncpy, strnlen, memcmpeq and memrchr patches.
