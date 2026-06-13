---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- openmp
- fortran
- compiler-internals
commit_hash: 5d4b953d53ee9ff6376f67e572d6308bbd977f75
source_type: github
author: Tobias Burnus
headline: OpenMP/Fortran fixes module-use renaming with declare mapper/reduction
tldr: The Fortran OpenMP implementation now correctly handles derived-type renaming
  when using `declare mapper` or `declare reduction` through module use.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Fortran front end's OpenMP implementation (`openmp.cc`) manages
  user-defined mappers (`gfc_omp_udm_find`) and reductions (`gfc_omp_udr_find`). This
  change addresses an issue with derived-type renaming, which occurs when types defined
  in one module are used and potentially renamed in another. The fix ensures that
  the comparison logic for these types, particularly in the context of OpenMP `declare
  mapper` and `declare reduction` directives, correctly accounts for such renamings,
  aligning it with `gfc_compare_derived_types` to prevent misidentification during
  compilation. This is important b…
primer_general: OpenMP is a set of compiler directives that allow programmers to write
  parallel programs. In Fortran, you can define your own specialized operations for
  parallelism called 'mappers' and 'reductions' using `declare mapper` and `declare
  reduction` statements. These operations often work on custom data structures called
  'derived types'. When you define these types and operations in one part of your
  code (a 'module') and then use them in another, you might sometimes rename them.
  This update fixes an issue where the compiler wasn't correctly figuring out that
  a renamed derived type in a different module was the same as the original one when
  used with these OpenMP directives. This correction ensures that parallel programs
  using these advanced OpenMP features compile and run as intended, avoiding incorrect
  behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5d4b953d53ee9ff6376f67e572d6308bbd977f75
date: '2026-06-12'
is_stub: false
---

The GCC Fortran front end for OpenMP has been updated to correctly account for renaming of derived types when they are used with `declare mapper` or `declare reduction` clauses through module imports. Previously, an inconsistency in type comparison logic could lead to errors. The fix aligns the comparison of types with the existing `gfc_compare_derived_types` function, addressing a nuance where only derived types are permitted in `declare` statements, but class variables can be used with mappers and reductions.
