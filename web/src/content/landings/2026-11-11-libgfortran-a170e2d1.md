---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- bugfix
- atomics
- 32-bit
commit_hash: a170e2d13746b5c2449408dc7a6a1ede98f5cab5
source_type: github
author: Jerry DeLisle
headline: Avoid libatomic calls for unit file ID
tldr: Fixes libgfortran to avoid unnecessary libatomic calls for unit file IDs on
  32-bit targets lacking lock-free 64-bit atomics.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR118935's fix incorrectly relied on `HAVE_ATOMIC_FETCH_ADD` to guard
  accesses to `gfc_unit`'s 64-bit `file_dev` and `file_ino` fields. This configure
  check only tests for `int` atomics. On 32-bit targets without lock-free 64-bit atomics,
  this resulted in calls to `libatomic`, which libgfortran does not link. The fix
  reverts r17-6152's attempt to test 64-bit types, which also broke atomicity for
  the unit waiting count. Instead, it reintroduces a check specifically for lock-free
  64-bit atomics for the file ID access, ensuring correctness on affected architectures.
primer_glossary:
- term: libgfortran
  definition: The runtime library for the GNU Fortran compiler (gfortran). It provides
    functions for input/output, intrinsic procedures, and other runtime services.
- term: libatomic
  definition: A library that provides atomic memory access operations, useful for
    multi-threaded programming. Compilers may use it when built-in atomic operations
    are not available or suitable.
- term: gfc_unit
  definition: A data structure within libgfortran that represents an opened Fortran
    file unit, managing its state and associated metadata.
- term: HAVE_ATOMIC_FETCH_ADD
  definition: A configuration macro that indicates whether the target system supports
    the atomic fetch-and-add operation, typically used for thread-safe incrementing.
- term: lock-free atomics
  definition: Atomic operations that can be performed without requiring locks or synchronization
    primitives, typically implemented directly using special CPU instructions for
    better performance in concurrent environments.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a170e2d13746b5c2449408dc7a6a1ede98f5cab5
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This change addresses a bug in libgfortran where accesses to 64-bit `file_dev` and `file_ino` fields of `gfc_unit` incorrectly used `__atomic` builtins, leading to calls into `libatomic` on 32-bit targets without lock-free 64-bit atomics. This caused crashes as libgfortran doesn't link `libatomic`. The fix reverts a previous change that tested for 64-bit types, and instead uses atomic accesses for the file ID only when 64-bit atomics are lock-free, preventing incorrect linking issues and ensuring thread safety.
