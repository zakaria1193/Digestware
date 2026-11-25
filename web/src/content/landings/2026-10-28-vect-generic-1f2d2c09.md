---
project: gcc
subsystem: vect-generic
patch_id: null
tags:
- vectorization
- optimization
- bugfix
commit_hash: 1f2d2c09eab4dbb18c531ab177fac1b977687d79
source_type: github
author: Igor Shevlyakov
headline: 'vect-generic: Avoid giving up on divisor element of -1'
tldr: Ensures vector division optimization does not incorrectly discard valid cases
  when the divisor is -1.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `expand_vector_divmod` in `tree-vect-generic.cc` incorrectly returned
  `NULL_TREE` for a signed divisor element of -1, disabling the power-of-two path.
  This commit removes that early return. Division by -1 (which is `-2^0`) is now handled
  by the `abs_d <= 1` case, which correctly disables only the multiply-high path and
  allows the power-of-two path to be considered, resolving issues with remainder expansion
  and mask sequences.
primer_glossary:
- term: vect-generic
  definition: A subsystem within GCC that handles generic vectorization transformations.
    It provides a common framework for optimizing loops and expressions across different
    target architectures.
- term: vectorization
  definition: A compiler optimization that transforms code to perform the same operation
    on multiple data elements simultaneously, typically by using special SIMD (Single
    Instruction, Multiple Data) instructions. This can significantly improve performance
    for data-parallel tasks.
- term: divisor
  definition: In arithmetic, the number by which another number (the dividend) is
    divided.
- term: power-of-two
  definition: A number that can be expressed as 2 raised to an integer exponent (e.g.,
    1, 2, 4, 8, 16). Division or multiplication by powers of two can often be optimized
    by the compiler using bitwise shifts.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1f2d2c09eab4dbb18c531ab177fac1b977687d79
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit corrects a flaw in the vector generic division optimization where a signed divisor element of -1 was incorrectly handled, causing the optimization to give up on the 'power-of-two' path. By removing an early return for this specific case, the compiler can now correctly process division by -1, which is a negative power of two, leading to more accurate and potentially more efficient vector code generation.
