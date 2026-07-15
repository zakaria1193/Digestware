---
project: gcc
subsystem: c-family
patch_id: null
tags:
- c
- c++
- atomic
- bitint
- bugfix
commit_hash: deb5f74feeaf3a43f6d4008a1e01fc4d23c1efdf
source_type: github
author: Jakub Jelinek
headline: 'c-family: Use CAS loop for small _BitInt atomics with padding.'
tldr: Uses CAS loop instead of RMW atomics for small _BitInt types with padding on
  certain architectures.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `sync_resolve_size` function in `gcc/c-family/c-common.cc` now
  returns -1 for fetch operations on `_BitInt` types that have padding bits and where
  the target architecture mandates extension into those bits. This signals the need
  to use a CAS loop, implemented in `atomic_bitint_fetch_using_cas_loop`, which is
  also updated to handle `__sync_*` fetch builtins. This avoids incorrect behavior
  from RMW atomics that do not perform the necessary sign/zero extension.
primer_glossary:
- term: _BitInt
  definition: A non-standard integer type in C and C++ that allows specifying arbitrary
    bit widths, potentially larger than standard integer types.
- term: CAS loop
  definition: Compare-And-Swap loop. An atomic operation that reads a memory location,
    compares its value with an expected value, and if they match, writes a new value.
    A loop is often used to retry the operation if another thread modifies the memory
    location between the read and the write.
- term: RMW atomic
  definition: Read-Modify-Write atomic operations. These are single, indivisible instructions
    that perform a read, modification, and write operation on memory atomically, such
    as `fetch_add` or `fetch_sub`.
- term: Padding bits
  definition: Extra bits in a data type that are not part of the intended value but
    are present due to alignment or internal representation. These bits can sometimes
    be accidentally included or excluded by operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/deb5f74feeaf3a43f6d4008a1e01fc4d23c1efdf
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

For small `_BitInt` types with padding, some atomic/sync builtins that operate on `TYPE *` arguments do not correctly sign or zero-extend the values. This commit changes the implementation to use a Compare-And-Swap (CAS) loop instead of Read-Modify-Write (RMW) atomics for these specific cases. This ensures correct behavior when the target architecture requires extension into the padding bits, addressing PR124948.
