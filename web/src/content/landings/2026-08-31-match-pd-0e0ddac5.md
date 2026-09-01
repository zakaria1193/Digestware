---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- complex numbers
commit_hash: 0e0ddac529e215ea605541f8613a0777b6f533a6
source_type: github
author: Dipesh Sharma
headline: Fold nested CPROJ inside CPROJ or CABS.
tldr: Optimized folding of complex number operations improves code generation.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match.pd` pass in GCC's tree-ssa optimization pipeline has been
  updated with new patterns to handle nested `__builtin_cproj` and `__builtin_cabs`
  calls. Previously, the optimizer might not have recognized that the result of an
  outer `cproj` or `cabs` could be folded directly, potentially leaving redundant
  calls in the GIMPLE representation. These new patterns allow the optimizer to simplify
  such constructs, reducing redundant computations.
primer_glossary:
- term: CPROJ
  definition: Represents the `cproj` intrinsic function, which computes the projection
    of a complex number onto the Riemann sphere. This is used to handle infinities
    and NaNs in complex arithmetic.
- term: CABS
  definition: Represents the `cabs` intrinsic function, which computes the absolute
    value (or magnitude) of a complex number.
- term: GIMPLE SSA
  definition: An intermediate representation (IR) used by GCC. It is based on Gimple
    statements and uses Static Single Assignment (SSA) form, which makes optimizations
    easier by ensuring each variable is assigned a value only once.
- term: tree-ssa optimization
  definition: A phase in GCC's compilation pipeline that performs various optimizations
    on the 'tree' intermediate representation after it has been converted to SSA form.
    This includes constant folding, dead code elimination, and more complex transformations.
discussion_id_link: github:gcc-mirror/gcc#126690
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0e0ddac529e215ea605541f8613a0777b6f533a6
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit enhances the `match.pd` optimization pass by introducing patterns to fold complex projection (CPROJ) operations when they are nested within other CPROJ or complex absolute value (CABS) operations. This resolves an issue in GIMPLE SSA where nested calls were not being optimized, leading to less efficient code generation. A new test case verifies the correct folding.
