---
project: glibc
subsystem: riscv
patch_id: null
tags:
- glibc
- riscv
- rvv
- strncat
- ifunc
discussion_id: 0f654c95-3b36-4fdc-a598-102686601ac0@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [PATCH v5 14/18] riscv: Add RVV strncat for multiarch and non-multiarch'
headline: 'riscv: Add RVV strncat for multiarch and non-multiarch'
tldr: Questions the need for a new macro `riscv_libc_ifunc_redirected` in the `strncat`
  implementation, when `riscv_libc_ifunc` is used elsewhere.
stakes: Ensuring consistent use of macros across the RISC-V architecture for optimized
  string functions in glibc.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Introducing a new macro may add complexity and potential inconsistency.
- Reusing the existing macro may simplify maintenance and improve code readability.
- The new macro may address specific requirements of `strncat` not covered by `riscv_libc_ifunc`.
exchanges:
- author: Peter Bergner <bergner@tenstorrent.com>
  role: proposer
  position: Asks why the patch introduces `riscv_libc_ifunc_redirected` macro, instead
    of reusing the existing `riscv_libc_ifunc` macro.
  quote: Can you explain why the need for this new riscv_libc_ifunc_redirected macro
    and its use here?  Ie, why doesn't this just use the same template as the memset
    and strcat files?
primer_expert: The patch series introduces optimized RISC-V vector (RVV) implementations
  of standard C string functions within glibc. The `strncat` patch utilizes a new
  macro, `riscv_libc_ifunc_redirected`, for ifunc resolution. This deviates from the
  pattern used in other RVV-optimized functions like `memset` and `strcat`, which
  employ `riscv_libc_ifunc`. The question arises whether this new macro is necessary
  or if the existing one could be reused to maintain consistency.
primer_general: glibc, the GNU C Library, provides standard functions for C programs.  Optimized
  implementations of these functions can leverage specific hardware features for performance.  This
  patch series adds optimized versions of string functions for RISC-V processors using
  vector instructions (RVV). `ifunc` is a glibc mechanism that allows resolving a
  function call at runtime to the most appropriate implementation based on the CPU's
  capabilities.  The discussion questions the introduction of a new macro for selecting
  the `strncat` implementation, rather than using the existing macro used in other
  similar functions.
series_id: 'glibc:riscv: add rvv strncat for multiarch and non-multiarch'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/0f654c95-3b36-4fdc-a598-102686601ac0@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-20'
---

The patch adds an RVV implementation of `strncat` for both multiarch and non-multiarch RISC-V systems. The reviewer questions why the patch introduces `riscv_libc_ifunc_redirected` instead of reusing the existing `riscv_libc_ifunc` macro used in similar `memset` and `strcat` implementations.
