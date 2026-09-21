---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- gcc
- aarch64
- vectorization
commit_hash: b197afc3746ffd256ec1839bbd8b51d7bfe4e594
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Allow wider ranges for signed saturating truncation'
tldr: GCC now supports wider intermediate types for signed saturating truncation,
  improving optimization opportunities.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `signed_integer_sat_trunc` pattern in `match-sat-alu.pd` has been
  broadened to allow a lossless unsigned range type that is at least as wide as the
  signed input. Previously, it required the range type to have the same precision
  as the input, limiting optimizations. The change also continues to require a narrowing
  result type and constructs offset/limit constants at the range precision using wide-int
  operations. This enhancement is beneficial for vectorization, as demonstrated by
  an AArch64 example showing a significant reduction in vector operations and iterations.
primer_glossary:
- term: signed saturating truncation
  definition: A conversion to a narrower signed integer type where the result is clamped
    to the minimum or maximum representable value of the target type if the original
    value falls outside that range. This prevents overflow by capping the result.
- term: unsigned range type
  definition: In the context of saturating operations, this refers to an intermediate
    unsigned data type used to hold values during calculations before they are potentially
    clamped and converted to the final signed result type. A 'lossless' range type
    means it can represent all possible values of the input without overflow.
- term: vector processing
  definition: A type of computation where the same operation is applied to multiple
    data elements simultaneously, typically using specialized processor instructions
    (SIMD). This significantly speeds up tasks involving large datasets.
- term: pattern matcher
  definition: A component within a compiler that identifies specific sequences of
    intermediate representation (IR) operations that can be replaced by more efficient
    instructions or simpler IR forms. This is crucial for optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b197afc3746ffd256ec1839bbd8b51d7bfe4e594
date: '2026-08-15'
is_stub: false
stub_reason: ''
---

GCC's `match-sat-alu.pd` pattern matcher now allows a wider unsigned range type for signed saturating truncation, provided it preserves all input values. This change enables more optimizations, especially in vector processing. An AArch64 example shows a reduction from a complex vector sequence to a simpler one with fewer iterations.
