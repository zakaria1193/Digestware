---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- bugfix
- compiler
commit_hash: c9f26edda05b045d98c87d8c5dc0163f2cd0b652
source_type: github
author: Paul Thomas
headline: 'Fortran: Fix ICE in allocatable finalization expression'
tldr: Fixes an internal compiler error (ICE) in Fortran when finalizing allocatable
  variables before assignment.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `trans.cc`, when handling the finalization of allocatable and pointer
  left-hand sides (LHS) before assignment, `gfc_conv_expr` must be used with the `se.descriptor_only`
  flag. This prevents the implicit invocation of `set_factored_descriptor_value` by
  `gfc_conv_expr_descriptor`, which was causing the ICE. This issue is specific to
  the Fortran front end and doesn't directly interact with other parts of the compiler.
primer_general: In Fortran, allocatable variables can be automatically deallocated
  and finalized when they are no longer needed—for example, before being assigned
  a new value. This commit addresses a bug in the compiler's finalization process,
  where it would crash (an ICE, or internal compiler error) when dealing with allocatable
  variables on the left side of an assignment. The fix ensures the compiler correctly
  handles the descriptor of the allocatable variable during finalization, preventing
  the crash. This makes the compiler more robust when dealing with allocatable variables
  in Fortran code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c9f26edda05b045d98c87d8c5dc0163f2cd0b652
date: '2026-05-23'
is_stub: false
---

This commit fixes an ICE in the Fortran front end that occurred during the finalization of allocatable variables before assignment. The fix ensures that `gfc_conv_expr` is called with the `se.descriptor_only` flag, preventing an implicit call to `set_factored_descriptor_value`. A new test case is added to verify the fix.
