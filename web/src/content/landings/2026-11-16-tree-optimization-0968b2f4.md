---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- tree-optimization
- value-numbering
commit_hash: 0968b2f46e731ddbe9fe61508330004ee0060645
source_type: github
author: Richard Biener
headline: Fix miscompilations with value-numbering and multiple memory states
tldr: Corrects value-numbering to avoid miscompilations related to loads from multiple
  memory states.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This addresses PRs tree-optimization/128637 and 128688, which affect
  the SCCVN (Sparse Conditional Constant Propagation Value Numbering) pass in tree-optimization.
  The issue arises from how loads combining multiple memory states are handled. Specifically,
  when a load is value-numbered and its resulting expression is inserted into the
  expression hashtable, it can be misinterpreted as a single store if not handled
  carefully. The fix involves using a dummy VR (Value Range) and skipping expression
  insertion for such loads, preventing incorrect code generation.
primer_glossary:
- term: Value Numbering (VN)
  definition: A compiler optimization technique that identifies equivalent expressions
    or computations within the code and replaces redundant ones. It assigns a unique
    'value number' to each distinct value computed.
- term: Partial-defs
  definition: A situation where a memory location can be written to by multiple operations,
    but not all operations are guaranteed to be executed or reach a specific point
    in the code. This can complicate precise tracking of memory states.
- term: GIMPLE
  definition: GCC's internal representation (IR) used after the front-end has parsed
    the source code. It's a three-address-like code that simplifies many optimization
    passes.
- term: SSA
  definition: Static Single Assignment form. A program representation where every
    variable is assigned exactly once. This simplifies many dataflow analyses and
    optimizations. GIMPLE often uses SSA form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0968b2f46e731ddbe9fe61508330004ee0060645
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This commit addresses miscompilations occurring in value-numbering when dealing with partial-defs and multiple memory states. It prevents the value-numbering pass from incorrectly recording a load that combines different memory states as a single store in the expression hashtable, thus avoiding the generation of wrong code. New test cases are included to cover these scenarios.
