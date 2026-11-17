---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- cleanup
- compiler
commit_hash: bb5c3bfcb28b423544676b30df5a3bc97e91c41f
source_type: github
author: Mikael Morin
headline: Simplify Fortran argument handling by removing unused pointer conditional
tldr: Removed an obsolete `formal_ptr` argument and related code in Fortran argument
  conversion routines.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `formal_ptr` argument in `gfc_conv_subref_array_arg`, which conditionally
  enabled one-based array descriptor bounds generation for dummy pointer arguments,
  has been removed. Analysis revealed this argument was always false in the contexts
  where `gfc_conv_subref_array_arg` is invoked for copy-in/copy-out operations on
  array arguments. Consequently, the associated code for handling pointer-specific
  bound generation was dead code and has been stripped out across various Fortran
  translation routines including `gfc_conv_gfc_desc_to_cfi_desc`, `gfc_conv_procedure_call`,
  and array/IO-related fun…
primer_glossary:
- term: Fortran frontend
  definition: The part of the compiler that parses and analyzes Fortran source code,
    converting it into an intermediate representation.
- term: dummy argument
  definition: A parameter in a procedure (function or subroutine) definition that
    receives a value from the caller.
- term: pointer attribute
  definition: In Fortran, a declaration that indicates a variable holds the address
    of another data object.
- term: array descriptor
  definition: A data structure containing information about an array, such as its
    base address, bounds, and stride, used for runtime access.
- term: copy-in/copy-out
  definition: A mechanism for argument passing where the value of an argument is copied
    into the procedure before execution and copied back out to the caller after execution,
    effectively simulating pass-by-value for mutable arguments.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb5c3bfcb28b423544676b30df5a3bc97e91c41f
date: '2026-09-10'
is_stub: true
stub_reason: low_score
---

This commit cleans up the Fortran frontend by removing the `formal_ptr` argument from the `gfc_conv_subref_array_arg` function and its callers. This argument controlled specific bound generation for dummy pointer arguments, but it was consistently false in all current call sites. The removal simplifies the code and eliminates dead logic related to one-based array descriptor bounds for pointer arguments in copy-in/copy-out scenarios.
