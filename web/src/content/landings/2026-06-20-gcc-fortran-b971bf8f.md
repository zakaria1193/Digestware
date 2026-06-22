---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- bugfix
- parser
- runtime
commit_hash: b971bf8f24ab81615b920fd97fcbbe7e8cc1c5d8
source_type: github
author: Jerry DeLisle
headline: Namelist read with repeat count now handles array members correctly
tldr: Fortran namelist reads with repeat counts now properly distribute values to
  array components within derived types, fixing a long-standing parsing error.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `nml_read_obj` function within `libgfortran/io/list_read.c` is
  central to parsing Fortran namelist input. This fix addresses a subtlety in handling
  array components of derived types when a repeat count (e.g., `VAR = 3*10`) is used.
  Previously, the parser would mishandle the distribution of these repeated values
  across the array elements if they were nested within a derived type structure. The
  `is_component` parameter now guides the logic to correctly traverse and assign to
  each sub-component.
primer_general: In Fortran, `namelist` is a convenient way to read input data into
  a group of variables by name. You can use a 'repeat count' to assign the same value
  multiple times, for example, `MY_ARRAY = 3*10` would set the first three elements
  of `MY_ARRAY` to 10. A 'derived type' is like a custom data structure that can group
  different types of data together, including arrays. This update fixes a problem
  where, if you had an array inside one of these custom data structures, and you tried
  to read values into it using a `namelist` with a repeat count, the compiler wouldn't
  correctly assign the values to each element of that array. The change ensures the
  compiler now understands how to properly fill these array components within complex
  data structures from your namelist input.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b971bf8f24ab81615b920fd97fcbbe7e8cc1c5d8
date: '2026-06-20'
is_stub: false
---

This commit resolves a bug in the Fortran compiler where reading a namelist with a repeat count would fail when the target was an array member of a derived type. The `nml_read_obj` function in `libgfortran/io/list_read.c` now includes an `is_component` parameter, enabling it to correctly iterate through and update each element of such array components. This ensures that data is properly parsed and assigned in complex data structures.
