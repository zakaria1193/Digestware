---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- middle-end
commit_hash: a0cbca7aefb94b0241e706fe737e0326eead413d
source_type: github
author: Kyrylo Tkachov
headline: Preserve load MEM_NOTRAP for strub watermarks
tldr: Preserves non-trapping memory access information for strub watermark loads,
  improving optimization safety.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `expand_builtin_strub_update` and `expand_builtin_strub_leave`
  built-ins in `builtins.cc` use `EXPAND_MEMORY` for watermark updates. `EXPAND_MEMORY`
  has conservative store semantics and strips `MEM_NOTRAP`. This commit introduces
  a separate `MEM` for the load operation derived with load trap semantics, preserving
  `MEM_NOTRAP` while the original `MEM` is used for the store. This is done to maintain
  precise non-trapping information for loads used in watermark updates and leaves.
primer_glossary:
- term: MEM_NOTRAP
  definition: A flag indicating that a memory access is guaranteed not to trap (e.g.,
    cause a segmentation fault or other exception). This allows the compiler to perform
    more aggressive optimizations, such as reordering or eliminating the access.
- term: STRUB
  definition: Likely a reference to a specific GCC internal mechanism or built-in
    related to memory profiling or watermark tracking. The exact purpose isn't detailed
    here but involves memory access patterns.
- term: EXPAND_MEMORY
  definition: A GCC internal construct used in RTL (Register Transfer Language) expansion.
    It represents a memory operand and has conservative store semantics, meaning it
    may conservatively assume a memory write operation even if it's only a read.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0cbca7aefb94b0241e706fe737e0326eead413d
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This commit improves the handling of memory accesses within the strub built-in function. Previously, the EXPAND_MEMORY construct used for watermark updates would lose the MEM_NOTRAP flag, which indicates a non-trapping load. By creating a shallow copy for the load and deriving its MEM_NOTRAP flag separately, the compiler now correctly preserves this information. This ensures that subsequent conditional stores are not mistakenly marked as non-trapping, maintaining optimization correctness.
