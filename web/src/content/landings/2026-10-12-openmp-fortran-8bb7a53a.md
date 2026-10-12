---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- openmp
- fortran
- simd
- optimization
commit_hash: 8bb7a53a0df5c5c6eb41ae689cba5e1a7b814875
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Support ''simdlen'' scaled modifier and enforce const checks'
tldr: Adds support for the 'scaled' modifier in Fortran's OpenMP 'simdlen' clause
  and enforces constant expressions for relevant length modifiers.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This patch introduces support for the `simdlen( [ scaled(type-name
  [, divisor_expr]) : ] length_expr)` syntax in Fortran OpenMP. It modifies `gfortran.h`
  to include new fields for `simdlen_type` and `simdlen_divisor`. In `module.cc`,
  `mio_omp_declare_simd_clauses` is updated to correctly read the `simdlen` token
  from module files, fixing an issue where it was previously written but not consumed.
  The `resolve_positive_int_expr` and `resolve_nonnegative_int_expr` functions in
  `openmp.cc` are enhanced with a `WARN` argument to enforce constantness, ensuring
  that `simdlen` values are compile-time…'
primer_glossary:
- term: OpenMP
  definition: A standardized API for shared-memory parallel programming, allowing
    developers to easily express parallelism in C, C++, and Fortran.
- term: simdlen clause
  definition: An OpenMP clause that specifies the desired length of SIMD (Single Instruction,
    Multiple Data) vectors for a construct like 'simd' or 'declare simd'.
- term: scaled modifier
  definition: A new modifier for the `simdlen` clause that allows a numeric type and
    an optional divisor to be specified, influencing the effective SIMD length.
- term: Fortran
  definition: A high-level programming language commonly used in scientific and engineering
    computations, known for its performance and array-handling capabilities.
- term: declare simd
  definition: An OpenMP directive that allows a function to be considered for automatic
    vectorization, even if it's not explicitly marked with 'simd'.
- term: constant expression
  definition: An expression whose value can be determined at compile time, rather
    than at runtime.
- term: module file
  definition: In Fortran, a file that stores compiled information about modules, allowing
    them to be used across different compilation units without recompilation of the
    module itself.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8bb7a53a0df5c5c6eb41ae689cba5e1a7b814875
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This commit extends OpenMP support in Fortran to include the 'scaled' modifier for the `simdlen` clause in `simd` and `declare simd` directives. The 'scaled' modifier allows specifying a numeric type and an optional divisor expression. The change also enforces that `divisor_expr` and `length_expr` must be constant and greater than or equal to 1. Additionally, it fixes a bug in module file handling where `simdlen` was not consistently read, and refines expression resolution functions to better enforce constantness requirements.
