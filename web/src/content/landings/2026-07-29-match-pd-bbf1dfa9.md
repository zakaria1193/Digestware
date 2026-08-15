---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- vectorization
- pattern matching
- SIMD
commit_hash: bbf1dfa9da862caadf97ebf9a21b877b1553dbf4
source_type: github
author: Kyrylo Tkachov
headline: Combine vector comparisons against zero
tldr: Optimizes vector comparisons by combining pairs of comparisons against zero.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match.pd` optimization rule now handles vector integer comparisons
  more effectively. It recognizes that a lane-wise AND of two zero-comparisons is
  equivalent to a single zero-comparison on the bitwise OR of the operands. This rule
  is extended to cover signed and unsigned comparisons, as well as their De Morgan
  duals. A new helper function, `vector_nop_conversion_p`, is introduced to manage
  cases where operands might require view conversions before comparison, improving
  generated code for vector operations.
primer_glossary:
- term: match.pd
  definition: A file containing pattern matching rules used by GCC's optimization
    passes to recognize and transform specific code sequences.
- term: vector integer
  definition: A data type representing multiple integer values that can be operated
    on in parallel by a single instruction.
- term: lane
  definition: An individual element within a vector data type. For example, a 4-element
    vector of integers has 4 lanes.
- term: De Morgan dual
  definition: In logic, De Morgan's laws describe how to distribute negation over
    conjunction (AND) and disjunction (OR). For example, NOT (A AND B) is equivalent
    to (NOT A) OR (NOT B).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bbf1dfa9da862caadf97ebf9a21b877b1553dbf4
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This commit introduces optimizations for vector comparisons in GCC's `match.pd` pattern matching system. It combines pairs of vector comparisons against zero, leveraging the identity `(A == 0) & (B == 0) <=> (A | B) == 0`. This applies to both equality and inequality, and handles cases where operands differ in signedness. The optimization is demonstrated with an aarch64 example and includes a new test case.
