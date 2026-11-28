---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- alias analysis
commit_hash: 6ae1cf8abb6c1e2379b04be20c2e74174e16c637
source_type: github
author: Richard Biener
headline: Fix wrong alias set for BIT_FIELD_REF wrapped ref
tldr: Corrected alias set determination for BIT_FIELD_REF on loaded registers in GCC.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `reference_alias_ptr_type_1` function in `alias.cc` incorrectly
  computed alias sets for `BIT_FIELD_REF`s that wrap register loads. This was due
  to a failure to prune the access path to only its TBAA-relevant components before
  applying special handling for view-converted `MEM_REFs`. This commit corrects the
  order of operations, ensuring accurate alias analysis for such constructs.
primer_glossary:
- term: BIT_FIELD_REF
  definition: An intermediate representation in GCC that refers to a specific bitfield
    within a larger data structure or register.
- term: alias set
  definition: In compiler optimization, an alias set groups memory references that
    might potentially refer to the same memory location. Accurate alias set management
    is crucial for enabling optimizations like dead code elimination and common subexpression
    elimination.
- term: TBAA
  definition: Type-Based Alias Analysis. A technique used by compilers to determine
    memory access disambiguation based on type information, reducing the need for
    conservative assumptions about aliasing.
- term: MEM_REF
  definition: An intermediate representation in GCC that represents a memory access.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ae1cf8abb6c1e2379b04be20c2e74174e16c637
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This change fixes an issue in GCC's alias analysis where BIT_FIELD_REF on a register loaded from memory was assigned an incorrect alias set. The fix ensures that the alias set is correctly determined by first considering the TBAA-relevant parts of the access path before handling view-converted MEM_REFs.
