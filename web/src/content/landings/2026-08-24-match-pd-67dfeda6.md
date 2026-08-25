---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- tree-optimization
- vector
- bugfix
commit_hash: 67dfeda6483525262abbd26a0789672dfa9a0a33
source_type: github
author: Kyrylo Tkachov
headline: Prevent reduction simplification cycle in match.pd
tldr: Fixes a compiler infinite loop caused by reduction simplification rules.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/127039 by modifying the
  `match.pd` reduction rules. The `REDUC (@0 op VECTOR_CST)` rule, which transforms
  `REDUC (V op C)` into `REDUC (V) op REDUC (C)`, was prone to cycling with its inverse
  `REDUC_PAIR` rule, especially when `REDUC (C)` did not fold for scalable vectors.
  The fix restricts the constant reduction rule to only succeed when `REDUC (C)` simplifies
  to a scalar operand, preventing the inverse rule from matching and breaking the
  infinite loop during forward propagation.
primer_glossary:
- term: match.pd
  definition: A file within GCC that defines pattern-matching rules for various optimization
    passes, particularly for hardware-specific transformations and general tree optimizations.
- term: reduction
  definition: An optimization pattern where an operation is applied cumulatively across
    a sequence of elements, such as summing all elements in a vector. `REDUC(op)`
    is a GCC internal representation for such operations.
- term: simplification cycle
  definition: A situation where compiler optimization rules repeatedly transform code
    into a different form, and then other rules transform it back, leading to an infinite
    loop or excessive resource consumption.
- term: scalable vector
  definition: A type of vector processing where the vector length is determined at
    runtime or is programmable, rather than being fixed at compile time. This is common
    in architectures like ARM's SVE or RISC-V's V extension.
- term: forward propagation
  definition: A compiler optimization phase that involves propagating values, properties,
    or conditions through the control flow graph of a program to discover new optimization
    opportunities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/67dfeda6483525262abbd26a0789672dfa9a0a33
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

A cycle in the reduction simplification rules within `match.pd` could cause the compiler to enter an infinite loop, exhausting memory. This issue occurred when transformation rules for reductions, particularly those involving constants and scalable vectors, repeatedly applied and undid each other. The fix separates reduction rules with inverse pairs from those without, ensuring that constant reductions only apply when they simplify to a scalar, thus breaking the cycle.
