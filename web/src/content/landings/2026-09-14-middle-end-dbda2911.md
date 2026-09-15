---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- middle-end
commit_hash: dbda2911da5be5e11b7c776893fbc96938acf3ce
source_type: github
author: Kyrylo Tkachov
headline: Restore MEM_NOTRAP for memory-only loads
tldr: Restores non-trapping information for memory-only loads used in inline assembly
  and partial loads.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `expand_asm_stmt` and `expand_partial_load_optab_fn` in `cfgexpand.cc`
  and `internal-fn.cc` respectively, were using `EXPAND_MEMORY` or `EXPAND_WRITE`
  which strip `MEM_NOTRAP`. This commit restores the `MEM_NOTRAP` attribute for memory-only
  inline assembly inputs and for the source `MEM` in partial loads by calling `tree_could_trap_p`
  after the expansion.
primer_glossary:
- term: MEM_NOTRAP
  definition: A flag indicating that a memory access is guaranteed not to trap (e.g.,
    cause a segmentation fault or other exception). This allows the compiler to perform
    more aggressive optimizations, such as reordering or eliminating the access.
- term: EXPAND_MEMORY
  definition: A GCC internal construct used in RTL (Register Transfer Language) expansion.
    It represents a memory operand and has conservative store semantics, meaning it
    may conservatively assume a memory write operation even if it's only a read.
- term: Partial Load
  definition: A memory load operation that reads a subset of a larger memory unit,
    such as reading only the first few bytes of a 64-bit integer. This can involve
    specific instructions or masking.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dbda2911da5be5e11b7c776893fbc96938acf3ce
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This commit addresses situations where memory-only loads lose their MEM_NOTRAP attribute. This occurs when `EXPAND_MEMORY` is used, which, due to conservative store semantics, discards the non-trapping information. The fix involves restoring the MEM_NOTRAP flag for inline assembly inputs and partial loads by explicitly setting it based on `tree_could_trap_p` after using `EXPAND_MEMORY` or `EXPAND_WRITE`.
