---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- gcc
- control flow
commit_hash: 3e43b55eb8fb520b6ed161697249fcef6699d11b
source_type: github
author: Aldy Hernandez
headline: Backward threader handles abnormal PHIs
tldr: Improves the backward threader to correctly handle SSA names within abnormal
  PHI nodes, enabling better optimization for computed gotos.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The backward threader now follows abnormal PHIs. Previously, it restricted
  itself to normal PHIs. This commit removes that restriction, allowing it to resolve
  SSA names in abnormal PHIs when the control flow path does not involve abnormal
  edges. This is safe because the path solver only considers normal predecessor edges.
  This fixes issues with computed gotos targeting blocks that are also targets of
  abnormal control flow, as seen in PR tree-optimization/126103.
primer_glossary:
- term: Backward threader
  definition: A component within GCC's optimizers that traces control flow paths backward
    to determine how values propagate.
- term: SSA name
  definition: In GCC's Static Single Assignment (SSA) form, an SSA_NAME represents
    a variable that has been assigned a value exactly once. It's a core concept for
    many compiler optimizations.
- term: PHI node
  definition: A construct in SSA form that merges values from different control flow
    paths. A PHI node indicates which value of a variable should be used based on
    which predecessor block was executed.
- term: Abnormal PHI
  definition: A PHI node where one of the incoming edges from a predecessor block
    is considered 'abnormal'. This typically relates to control flow constructs like
    computed gotos or exceptions.
- term: Computed goto
  definition: A control flow statement where the target of a goto is determined dynamically
    at runtime, usually by loading an address into a register and then jumping to
    it.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3e43b55eb8fb520b6ed161697249fcef6699d11b
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

The backward threader in GCC now correctly handles SSA names that appear in abnormal PHI nodes. Previously, it refused to process these, hindering optimizations like threading computed gotos where the destination might be part of an abnormal PHI. This change aligns with gimple_range_ssa_p's ability to process such names, improving the path solver's accuracy and enabling optimizations in complex control flow scenarios. New test cases verify the fix.
