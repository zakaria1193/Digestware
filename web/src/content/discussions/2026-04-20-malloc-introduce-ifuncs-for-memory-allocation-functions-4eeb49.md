---
project: glibc
subsystem: malloc
patch_id: null
tags:
- glibc
- malloc
- ifunc
- optimization
- memory allocation
discussion_id: 20260420141459.531612-1-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v2 0/2] malloc: introduce ifuncs for malloc functions'
headline: 'Malloc: Introduce ifuncs for memory allocation functions.'
tldr: This patch series introduces ifuncs for malloc-related functions, allowing for
  target-specific memory allocation implementations.
stakes: Enables target-specific optimizations and alternative memory allocation strategies,
  potentially improving performance and security.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to the malloc implementation.
- Introduces a slight overhead for ifunc resolution.
- Enables target-specific optimizations and alternative memory allocation strategies.
primer_expert: This series introduces ifuncs to malloc API functions in `malloc/malloc.c`,
  enabling dynamic selection of implementations at runtime. Generic resolvers in `sysdeps/generic/malloc-ifuncs.c`
  provide core functionality, while targets like aarch64 can provide custom resolvers
  (e.g. `sysdeps/aarch64/malloc-ifuncs.c`) for memory tagging.  A new test (`malloc/tst-check-internal-calls.sh`)
  ensures internal malloc code doesn't directly call non-core variants.
primer_general: The malloc subsystem in glibc manages dynamic memory allocation. When
  a program requests memory (e.g., via `malloc`), the malloc implementation finds
  a suitable block of free memory.  Ifuncs (Indirect Functions) allow the selection
  of different function implementations at runtime, based on factors like CPU features.
  This patch enables the use of ifuncs for the core memory allocation functions, potentially
  allowing for optimized or specialized memory allocators on different platforms.
series_id: 'glibc:malloc: introduce ifuncs for malloc functions'
series_role: cover
series_parts:
- title: 'malloc: introduce ifuncs for malloc functions'
  url: https://inbox.sourceware.org/libc-alpha/20260420141459.531612-3-yury.khrustalev@arm.com
  n: 2
  total: 2
- title: 'malloc: introduce ifuncs for malloc functions'
  url: https://inbox.sourceware.org/libc-alpha/aeXpUaZLnmRN1wbk@arm.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/libc-alpha/20260420141459.531612-1-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch series adds ifuncs to the malloc API functions in glibc, enabling the use of alternative, potentially target-specific, implementations. Generic resolvers provide core implementations for most targets, while others (e.g., aarch64) can supply custom resolvers for features like memory tagging. The changes have passed regression tests on aarch64 and x86-64.
