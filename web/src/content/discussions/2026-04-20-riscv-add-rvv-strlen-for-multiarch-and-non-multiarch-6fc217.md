---
project: glibc
subsystem: riscv
patch_id: null
tags:
- glibc
- riscv
- rvv
- strlen
- optimization
discussion_id: a42db442-948a-4be6-be91-e68c67394b99@oss.tenstorrent.com
source_type: public_inbox
title: 'Re: [PATCH v5 13/18] riscv: Add RVV strlen for multiarch and non-multiarch'
headline: 'riscv: Add RVV strlen for multiarch and non-multiarch'
tldr: Reviewer asks why a macro definition present in other files is missing from
  strlen-generic.c.
stakes: Ensuring consistency in macro definitions across different files in the library.
proposer: Peter Bergner <bergner@tenstorrent.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding optimized RVV implementations improves performance on RISC-V.
- Ensuring macro consistency improves code maintainability.
exchanges:
- author: Peter Bergner <bergner@tenstorrent.com>
  role: reviewer
  position: Asks why the `libc_hidden_builtin_def` macro definition that is present
    in other generic implementations is missing from this one.
  quote: 'Is it on purpose you don''t have:  +# undef libc_hidden_builtin_def  +#
    define libc_hidden_builtin_def(x) ...above, whereas memset-generic.c and strcat-generic.c
    have it, as does your strlen-vector.S?'
primer_expert: This patch adds a `strlen` implementation optimized for RISC-V Vector
  extensions (RVV). The `IS_IN(libc)` macro guards the definition. The reviewer notes
  a missing macro definition that is present in other similar generic implementations
  (`memset`, `strcat`).
primer_general: '`strlen` is a standard C library function that calculates the length
  of a string. This patch adds optimized versions of `strlen` for the RISC-V architecture
  that take advantage of vector instructions (RVV). The discussion centers on ensuring
  consistency in the use of internal macro definitions within the C library.'
series_id: 'glibc:riscv: add rvv strlen for multiarch and non-multiarch'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/a42db442-948a-4be6-be91-e68c67394b99@oss.tenstorrent.com
bugzilla_url: null
date: '2026-04-20'
---

Peter Bergner is reviewing a patch from Yao Zihong that adds RVV `strlen` implementations for both multiarch and non-multiarch RISC-V systems. Peter asks why the `libc_hidden_builtin_def` macro definition is missing from `strlen-generic.c`, while it's present in other similar files.
