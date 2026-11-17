---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- warning
- optimization
- tree-ssa
commit_hash: bcf94a94bc385270d80a97800d20dec378d668ab
source_type: github
author: Sendao Yan
headline: Fix uninitialized warnings from late switch lowering.
tldr: Corrects `is_use_guarded` logic to prevent false positives in uninitialized
  variable warnings after switch lowering.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch targets `gcc/tree-ssa/uninit.cc` and `gcc/tree-ssa/cfg.cc`,
  specifically `uninit_analysis::is_use_guarded` and `predicate::simplify_2`. The
  defect arose because `is_use_guarded` incorrectly returns `false` for empty use
  predicates (where a PHI is defined and used in the same basic block). This commit
  corrects this by ensuring the definition predicate is checked. Additionally, it
  refactors how `predicate::simplify_2` handles tautological disjunctions (simplifying
  to `TRUE`) and normalizes predicates to correctly identify guarded uses, resolving
  false positives from PR107919 and PR44…
primer_glossary:
- term: PHI node
  definition: A special node in Static Single Assignment (SSA) form that represents
    the value of a variable which might have different definitions depending on the
    control flow path taken to reach it.
- term: GIMPLE
  definition: GNU Intermediate Representation Language. A low-level, three-address
    code representation used by GCC after initial parsing and before machine code
    generation.
- term: SSA form
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once, simplifying many compiler optimizations.
- term: predicate
  definition: In this context, a logical expression representing a condition, often
    used to determine if a variable is initialized or if a use is guarded.
- term: uninitialized warning
  definition: A compiler warning (e.g., `-Wuninitialized`) that alerts the programmer
    to potential uses of variables before they have been assigned a defined value.
- term: jump threading
  definition: An optimization technique that identifies sequences of conditional branches
    and replaces them with direct branches to the ultimate target, simplifying control
    flow.
discussion_id_link: null
bugzilla_pr: null
series_id: gcc:tree-optimization/128102 - fix -wuninitialized fps from lowering switches
  late
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bcf94a94bc385270d80a97800d20dec378d668ab
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This commit addresses false positives in the `-Wuninitialized` warning pass by fixing the `uninit_analysis::is_use_guarded` function. The issue stemmed from `pass_lower_switch` being moved after late jump threading, which exposed a defect where an empty use predicate (PHI defined and used in the same block) was incorrectly treated as unguarded. The fix ensures this condition is properly evaluated based on the definition predicate.
