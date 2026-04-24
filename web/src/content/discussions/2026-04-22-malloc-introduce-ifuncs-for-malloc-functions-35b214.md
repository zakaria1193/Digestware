---
project: glibc
subsystem: malloc
patch_id: null
tags:
- glibc
- malloc
- ifunc
- Hurd
- compilation
discussion_id: aejNe9XR3GwycAYO@arm.com
source_type: public_inbox
title: 'Re: [PATCH v2 2/2] malloc: introduce ifuncs for malloc functions'
headline: 'malloc: introduce ifuncs for malloc functions'
tldr: The patch adding ifuncs for malloc functions fails to compile for Hurd due to
  a missing header.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adding ifuncs can improve performance by selecting optimized code paths at runtime.
- Introduces potential build issues on less common platforms like Hurd.
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: Reports a compilation failure on Hurd systems due to a missing `string.h`
    include in `calloc-clear-memory.h`.
  quote: I've noticed that this file fails to compile for Hurd targets because malloc-internal.h
    includes calloc-clear-memory.h that has function clear_memory() that uses memset(),
    and on Hurd it needs string.h.
primer_expert: This patch adds ifuncs (indirect functions) to the glibc malloc implementation.  Ifuncs
  allow the dynamic linker to choose the optimal implementation of a function at runtime
  based on the target architecture's capabilities. The reported issue arises because
  the Hurd build environment doesn't implicitly include `string.h` when `memset` is
  used via `clear_memory` in `calloc-clear-memory.h`, which is included by `malloc-internal.h`.
primer_general: Glibc's malloc is the memory allocator used by programs to dynamically
  request and release memory.  Ifuncs are a mechanism for resolving function calls
  at runtime, allowing glibc to select the most efficient implementation based on
  the CPU's features. This can improve performance. The patch has a missing header
  which causes it to fail to compile on the Hurd operating system.
series_id: 'glibc:malloc: introduce ifuncs for malloc functions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aejNe9XR3GwycAYO@arm.com
bugzilla_url: null
date: '2026-04-22'
---

Yury Khrustalev reports that the patch introducing ifuncs for malloc functions fails to compile on Hurd systems due to a missing `string.h` include. The `clear_memory()` function, used in `calloc-clear-memory.h` and included by `malloc-internal.h`, requires `memset()` which is declared in `string.h`.  The author plans to address this in the next version of the patch by including `string.h` in `calloc-clear-memory.h`.
