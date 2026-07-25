---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- atomic
commit_hash: b5e6f5d2d435aba79ed8568f19da25378c716714
source_type: github
author: Kael Andrew Alonzo Franco
headline: Simplify atomic built-in handling.
tldr: Replaces INTEGER_CST + expand_normal with tree_to_uwhi for atomic operations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the implementation of `fold_builtin_atomic_always_lock_free`
  to replace a common pattern of handling integer constants. Instead of creating an
  `INTEGER_CST` and then expanding it with `expand_normal`, the code now uses `tree_fits_uwhi_p`
  to check if a constant fits within an unsigned wide integer and `tree_to_uwhi` to
  convert it. This simplifies the code and leverages more specialized tree-to-tree
  transformations.
primer_glossary:
- term: atomic operation
  definition: An operation that is guaranteed to be performed in its entirety without
    interruption. In concurrent programming, atomics are essential for safely accessing
    shared data.
- term: INTEGER_CST
  definition: A GCC internal representation (tree node type) for an integer constant.
- term: expand_normal
  definition: A GCC internal function used to expand a given tree 'exp' into RTL (lower-level
    representation).
- term: tree_fits_uwhi_p
  definition: A GCC internal function that checks if a tree value fits within an unsigned
    wide integer type.
- term: tree_to_uwhi
  definition: A GCC internal function that converts a tree value to an unsigned wide
    integer type.
- term: middle-end
  definition: The part of the compiler that performs optimizations and transformations
    on an intermediate representation (IR) of the code, after the frontend has parsed
    the source code and before the backend generates machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b5e6f5d2d435aba79ed8568f19da25378c716714
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

GCC simplifies the handling of atomic operations by replacing the 'INTEGER_CST + expand_normal' pattern with a more efficient and readable approach using `tree_fits_uwhi_p` and `tree_to_uwhi`. This change targets the `fold_builtin_atomic_always_lock_free` function, improving code clarity and potentially reducing compiler overhead for atomic built-ins.
