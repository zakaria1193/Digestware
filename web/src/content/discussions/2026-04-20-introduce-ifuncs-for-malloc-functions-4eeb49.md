---
project: glibc
subsystem: malloc
patch_id: null
tags:
- malloc
- ifunc
- memory allocation
- glibc
- AArch64
discussion_id: 20260420141459.531612-1-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v2 0/2] malloc: introduce ifuncs for malloc functions'
headline: Introduce ifuncs for malloc functions
tldr: This patch introduces ifuncs for malloc-related functions, allowing for target-specific
  implementations.
stakes: Enables optimized or specialized memory allocation routines for different
  architectures, potentially improving performance or adding features like memory
  tagging.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in the malloc implementation.
- Potential performance overhead due to the ifunc indirection.
- Requires careful management of internal calls to avoid unintended recursion.
primer_expert: The patch introduces ifuncs to the malloc API. This allows architectures
  like AArch64 to provide optimized or specialized malloc implementations via dynamic
  function resolution. Generic resolvers are used as a fallback. A new test `tst-check-internal-calls.sh`
  ensures that malloc code uses only the core (non-ifunc) implementations internally.  This
  approach adds a layer of indirection to malloc calls, managed by the dynamic linker.
primer_general: Memory allocation is the process of reserving portions of a computer's
  memory to store data during program execution.  The C standard library (`glibc`)
  provides functions like `malloc` and `free` for this purpose.  Indirect functions
  (`ifuncs`) are a mechanism that allows the dynamic linker to choose between multiple
  implementations of a function at runtime, based on the system's capabilities or
  configuration. This patch uses ifuncs to enable glibc to select specialized `malloc`
  implementations for different hardware architectures, potentially improving performance
  or enabling new features.
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

This patch series introduces ifuncs (indirect functions) for `malloc` and related functions in glibc. This allows targets to provide alternative implementations, such as those leveraging memory tagging on AArch64.  Generic resolvers are provided for targets without custom implementations. The changes pass regression tests on AArch64 and x86-64.
