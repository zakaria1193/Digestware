---
project: gcc
subsystem: gcc/phiopt
patch_id: null
tags:
- optimization
- gcc
commit_hash: dc8aa54843e5813d046a8b2fc3758b9e4064425d
source_type: github
author: Aldy Hernandez
headline: 'phiopt: Run condition replication in early optimization phase'
tldr: Condition replication over PHI nodes now runs earlier in the optimization pipeline
  for improved code generation.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `replicate_conds_over_phis` pass, part of GCC's `tree-ssa-phiopt.cc`,
  normally runs in the later stages of optimization. This commit moves its execution
  to also occur during the `early_p` phase, controlled by `phiopt::execute`. This
  change aims to leverage condition replication across PHI nodes earlier in the SSA
  optimization pipeline, potentially improving optimization results before further
  passes occur.
primer_glossary:
- term: PHI node
  definition: A special construct in Static Single Assignment (SSA) form that represents
    the merging of values from different control flow paths. It selects one of its
    incoming values based on which path was taken to reach the node.
- term: SSA form
  definition: Static Single Assignment form is an intermediate representation in compilers
    where every variable is assigned a value exactly once. This simplifies many optimizations
    by making data flow explicit.
- term: phiopt
  definition: The GCC pass responsible for optimizing PHI nodes in the SSA representation,
    aiming to simplify or eliminate them, often through techniques like constant folding
    or value propagation.
- term: early optimization phase
  definition: An earlier stage in the compiler's optimization pipeline, typically
    focusing on simpler and faster transformations before more complex, time-consuming
    optimizations are applied.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dc8aa54843e5813d046a8b2fc3758b9e4064425d
date: '2026-08-29'
is_stub: false
stub_reason: ''
---

The `replicate_conds_over_phis` pass in the phiopt pass was previously gated by `!early_p`. This change removes that gate, allowing the pass to run during the early optimization phase as well. This adjustment, suggested by Jeff, aims to improve code generation by applying condition replication more broadly.
