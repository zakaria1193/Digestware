---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- C++
- memory management
- dead code elimination
commit_hash: a5fabe7e20f4647bdfff5ed9d11d8526b11dae30
source_type: github
author: Ondřej Machota
headline: 'tree-optimization: Remove unused allocations compared against NULL'
tldr: Optimizes C++ code by removing unnecessary memory allocations that are only
  checked for NULL, improving generated code.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Extends `tree-ssa-dce`'s ability to eliminate `operator new`/`delete`
  pairs where the allocation result is only checked against NULL. A prior change handled
  cases where the comparison controlled a branch. This commit also removes the allocation
  when the comparison result is assigned, e.g., `return ptr != 0;`. It modifies `checks_return_value_of_removable_allocation_p`
  to handle `gassign` to `gcond` and ensures `eliminate_unnecessary_stmts` folds such
  comparisons to constants. A typo in the `fmalloc-dce` option name is also corrected.
primer_glossary:
- term: tree-ssa-dce
  definition: The Dead Code Elimination pass within GCC's SSA (Static Single Assignment)
    based optimization framework, responsible for removing code that does not affect
    the program's output.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation where
    every variable is assigned exactly once. This form simplifies many data-flow analyses
    and optimizations.
- term: gimple
  definition: GCC's intermediate representation for statements, designed to be simpler
    and more amenable to optimization than RTL.
- term: operator new
  definition: A C++ operator used to allocate memory dynamically on the heap. `std::nothrow`
    version returns nullptr on failure instead of throwing an exception.
- term: operator delete
  definition: A C++ operator used to deallocate memory previously allocated with `operator
    new`.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a5fabe7e20f4647bdfff5ed9d11d8526b11dae30
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This change enhances the tree-SSA dead code elimination pass to remove memory allocations whose returned pointers are only used in comparisons with NULL. Previously, such allocations were not removed if the comparison result was assigned to a variable. The update extends the optimization to handle assignments involving 'ptr == NULL' or 'ptr != NULL' checks, correctly folding them to constants and eliminating the dead allocation and deallocation code, similar to how conditional checks were already handled.
