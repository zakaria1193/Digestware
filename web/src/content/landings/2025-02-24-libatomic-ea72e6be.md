---
project: gcc
subsystem: libatomic
patch_id: null
tags:
- libatomic
- aarch64
- optimization
- runtime
commit_hash: ea72e6be34c41ccf54aab44d17386a4fba74edcd
source_type: github
author: Wilco Dijkstra
headline: 'libatomic: Use HWCAPs in AArch64 ifunc tests'
tldr: Simplifies AArch64 atomic operation selection by using HWCAPs instead of low-level
  checks.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In libatomic for AArch64, the `ifunc` selection for atomic operations
  now relies solely on HWCAPs, removing the need for explicit checks like `has_lse128()`
  and `has_rcpc3()`. This approach, favored by the kernel team, simplifies the `host-config.h`
  logic and optimizes the runtime dispatch mechanism by avoiding direct system register
  polling.
primer_glossary:
- term: libatomic
  definition: A library that provides atomic built-in functions for C, C++, and Fortran,
    ensuring thread-safe operations on shared data.
- term: AArch64
  definition: The 64-bit ARM architecture. GCC supports compiling for this popular
    mobile and server platform.
- term: ifunc
  definition: Indirect function binding. A mechanism that allows the runtime to select
    the most appropriate function implementation based on the CPU's capabilities at
    load time.
- term: HWCAPs
  definition: Hardware capabilities. Flags exposed by the kernel that indicate features
    supported by the CPU, used to dynamically select optimized code paths.
- term: LSE
  definition: Large System Extension. An extension to the ARM architecture that provides
    enhanced atomic instruction support.
- term: RCPC3
  definition: Likely refers to a specific ARM instruction set or feature related to
    atomic operations or memory ordering, possibly Release Consistent Post-cache Coherency.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ea72e6be34c41ccf54aab44d17386a4fba74edcd
date: '2025-02-24'
is_stub: false
stub_reason: ''
---

The libatomic library on AArch64 now uses hardware capability (HWCAP) flags to select the most efficient atomic operations (ifuncs). This replaces older, more complex checks like `has_lse128()` and `has_rcpc3()`, simplifying the code and speeding up runtime selection by avoiding expensive system register accesses.
