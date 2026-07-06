---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- ice
- bugfix
commit_hash: 5f2c4cacfcdf9f6ed77ded6467df31cc90181e07
source_type: github
author: Sandra Loosemore
headline: 'Fortran: Fix ICE-on-invalid in trans_code.'
tldr: Prevents an internal compiler error in the Fortran front-end when handling invalid
  expressions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes an ICE in `fortran/trans.cc`'s `trans_code` function by preventing
  `set_location` from being called on non-expression tree nodes, specifically `error_mark_node`.
  This avoids attempting to assign a location to an invalid marker, which would otherwise
  cause an ICE during the tree traversal for code generation.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A severe error detected by the compiler during
    its own processing, indicating a bug in the compiler itself.
- term: Fortran
  definition: A high-level programming language commonly used for scientific and numerical
    computation. GCC includes a front-end for compiling Fortran code.
- term: Tree Expression
  definition: GCC represents code internally using a tree-like data structure. Tree
    expressions are nodes within this structure that represent computations or values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5f2c4cacfcdf9f6ed77ded6467df31cc90181e07
date: '2026-07-04'
is_stub: false
stub_reason: ''
---

This commit addresses an internal compiler error (ICE) that occurred in the Fortran front-end's `trans_code` function. The error happened when the compiler attempted to set the source code location for invalid tree expressions, such as `error_mark_node`.
By adding a check to ensure that location information is only set for valid expression nodes, this commit prevents the ICE and improves the compiler's robustness when encountering errors during code translation.
