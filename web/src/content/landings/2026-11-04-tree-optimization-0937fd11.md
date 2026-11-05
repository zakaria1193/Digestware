---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- gcc
- dce
- ssa
commit_hash: 0937fd11d029751f43bdf020ebcd9b4872f2d500
source_type: github
author: Richard Biener
headline: 'tree-optimization: Do not propagate zero to abnormal edges in simple-dce'
tldr: Fixes dead code elimination to correctly handle PHI nodes on abnormal control
  flow edges.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simple_dce_from_worklist` function in `tree-ssa-dce.cc` has been
  updated to prevent propagation of zero constants to PHI node arguments that originate
  from abnormal control flow edges. This addresses a bug where DCE would incorrectly
  simplify code by replacing such defs with constants, potentially altering program
  semantics. The change ensures PHI defs on abnormal edges are correctly handled,
  aligning with SSA invariants.
primer_glossary:
- term: simple-dce
  definition: A component of GCC's dead code elimination (DCE) pass that operates
    on the Static Single Assignment (SSA) form of the code. It identifies and removes
    code that has no effect on the program's output.
- term: PHI node
  definition: In Static Single Assignment (SSA) form, a PHI node is a special instruction
    that merges values from different control flow paths. It takes multiple arguments,
    each corresponding to a different predecessor block, and produces a single result.
    `PHI(arg1, arg2, ...)` selects `argN` if control flow comes from the Nth predecessor
    block.
- term: abnormal edge
  definition: In control flow graphs, an abnormal edge typically refers to a control
    flow transfer that is not part of the standard sequential execution or typical
    conditional branching. Examples include exceptions, long jumps, or non-local exits.
- term: SSA
  definition: Static Single Assignment form is an intermediate representation used
    in compilers where every variable is assigned a value exactly once. This simplifies
    many optimization passes, including dead code elimination, by making data flow
    explicit.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0937fd11d029751f43bdf020ebcd9b4872f2d500
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This commit corrects a flaw in the simple dead code elimination (DCE) pass that incorrectly propagated zero values to uses of PHI node operands entering from abnormal control flow edges. Such propagation can lead to incorrect optimization results. The fix ensures that PHI definitions on abnormal edges are preserved, preventing faulty dead code elimination and maintaining program correctness.
