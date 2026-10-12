---
project: gcc
subsystem: gcc/rtl-optimization
patch_id: null
tags:
- optimization
- rtl
commit_hash: ad8e1fbd322b089d0cf0ebac12b1398861926c1e
source_type: github
author: Richard Biener
headline: Simplify XOR of IOR with B to AND (NOT B) A
tldr: Adds a new RTX simplification rule for bitwise operations, complementing an
  existing transform.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `simplify_context::simplify_binary_operation_1` function in `simplify-rtx.cc`
  has been augmented to handle the simplification of `(xor (ior A B) B)` to `(and
  (not B) A)`. This pattern is the dual of an existing simplification `(xor (and A
  B) B)` to `(and (not A) B)`. The need for this specific rule was observed during
  the investigation of PR127606, indicating it's a meaningful pattern in real-world
  code.
primer_glossary:
- term: RTL
  definition: Register Transfer Language. An intermediate representation used in GCC
    that describes operations on registers and memory. Optimizations often operate
    on RTL.
- term: simplification
  definition: The process of transforming code into an equivalent but simpler form,
    often to make subsequent optimizations easier or to generate more efficient instructions.
- term: bitwise operations
  definition: Operations that manipulate individual bits of data, such as AND, OR,
    XOR, and NOT.
- term: PR127606
  definition: Problem Report 127606. A bug report filed against GCC, indicating an
    issue that this commit helps to address or resolve.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ad8e1fbd322b089d0cf0ebac12b1398861926c1e
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

GCC's RTL (Register Transfer Language) simplification has gained a new transformation rule. It simplifies the expression `(xor (ior A B) B)` into `(and (not B) A)`. This new rule complements an existing transformation and was identified as a potential optimization during the analysis of a specific bug report (PR127606).

This change enhances the compiler's ability to optimize bitwise operations at the RTL level, potentially leading to more efficient machine code.
