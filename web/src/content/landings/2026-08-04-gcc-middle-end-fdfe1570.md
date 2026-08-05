---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- gcc/middle-end
- optimization
- FMA
- SVE
- ICE
commit_hash: fdfe1570235b1bddc4572255ff161b5dc25cc460
source_type: github
author: Tamar Christina
headline: Fix floating-point FMA to integer negation pattern to prevent ICEs
tldr: Correct a constraint in a negation pattern to prevent floating-point FMAs from
  being incorrectly folded into integer operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The optimization introduced in GCC commit `gca2920882be` (referenced
  internally) contained a flaw in `match.pd` that mistakenly allowed floating-point
  FMAs to be matched by a pattern intended for integer operations. Specifically, pattern
  `match.pd:10328` was applied to SVE vector types (`svfloat32_t`) when the input
  operands were unsigned integers, leading to an ICE because the SVE vector attributes
  on the result did not align with the expected integer output. This change modifies
  the constraint in `match.pd` to restrict this pattern to integral types only, ensuring
  that floating-point FMAs a…
primer_glossary:
- term: FMA (Fused Multiply-Add)
  definition: A floating-point operation that performs a multiplication and an addition
    in a single step, often with higher precision and performance than separate multiply
    and add operations.
- term: ICE (Internal Compiler Error)
  definition: An error that occurs within the compiler itself, indicating a bug or
    an unexpected state during the compilation process. These typically halt compilation.
- term: SVE (Scalable Vector Extension)
  definition: An advanced vector processing instruction set for ARM processors, allowing
    operations on vectors whose length can vary dynamically.
- term: Integral Types
  definition: Data types that represent whole numbers, such as integers (int, long,
    etc.), as opposed to floating-point types (float, double).
- term: Pattern Matching
  definition: A technique used by compilers to identify specific code structures (patterns)
    in the intermediate representation (IR) that can be transformed or optimized.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fdfe1570235b1bddc4572255ff161b5dc25cc460
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in a GCC optimization pattern that incorrectly allowed floating-point Fused Multiply-Add (FMA) operations to be folded into integer negation patterns. The erroneous constraint allowed the pattern to match even when the operands were floating-point types, leading to incorrect type conversions and an internal compiler error (ICE) due to mismatched SVE attributes. The fix adjusts the pattern's guard to ensure it only applies to integral types, thereby preventing these incorrect transformations and compiler crashes.
