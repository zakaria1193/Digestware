---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- PRE
- SSA
- compiler-bug
commit_hash: dfd857530e0bda541d4112c5c19bda0567b521ef
source_type: github
author: Richard Biener
headline: Limit recursive PRE expression generation to avoid cycles.
tldr: Prevents infinite loops in PRE optimization by limiting recursive expression
  generation.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ssa-pre.cc` file implements the Partial Redundancy Elimination
  pass, which aims to eliminate redundant computations. The `find_or_generate_expression`
  function recursively constructs expressions to be substituted. This commit addresses
  an issue (PR tree-optimization/126965) where cycles in the SSA value graph could
  lead to unbounded recursion. By adding a recursion depth limit to `find_or_generate_expression`,
  the pass now safely handles such cyclic dependencies, preventing infinite loops
  and potential compiler hangs.
primer_glossary:
- term: PRE
  definition: Partial Redundancy Elimination, an optimization technique that identifies
    and removes redundant computations within a program.
- term: SSA
  definition: Static Single Assignment, an intermediate representation where every
    variable is assigned exactly once, simplifying many optimization analyses.
- term: tree-ssa-pre.cc
  definition: The GCC source file containing the implementation of the Partial Redundancy
    Elimination pass operating on SSA-form GIMPLE.
- term: value graph
  definition: A data structure representing dependencies between values, often used
    in optimization passes to track computations and their relationships.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dfd857530e0bda541d4112c5c19bda0567b521ef
date: '2026-08-21'
is_stub: false
stub_reason: ''
---

This commit limits the recursion depth during the generation of complex expressions within the PRE (Partial Redundancy Elimination) optimization pass. It was discovered that the value graph used by PRE can contain cycles, and recursive expression generation could enter infinite loops when encountering these cycles. A new test case exposed this issue, and the fix introduces a depth limit to prevent such recursions, ensuring stability and correctness of the PRE pass.
