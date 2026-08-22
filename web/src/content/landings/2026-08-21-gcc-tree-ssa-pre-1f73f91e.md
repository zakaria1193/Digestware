---
project: gcc
subsystem: gcc/tree-ssa-pre
patch_id: null
tags:
- optimization
- compiler bug
commit_hash: 1f73f91ea78c9c6b986630d236cabd8298788aa6
source_type: github
author: Richard Biener
headline: Simplify PRE phi-translation expression simplification.
tldr: Ensures correct handling of SSA names during PRE phi-translation to avoid incorrect
  simplifications.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-pre.cc` file handles PRE optimization. The `phi_translate_1`
  function simplifies expressions involving PHI nodes. This commit enhances `get_or_alloc_expr_for_nary`
  to assert that SSA names or constants are not encoded as NARY. It also modifies
  `phi_translate_1` to save and restore the translated NARY value, preventing incorrect
  simplifications to SSA names that were previously rejected.
primer_glossary:
- term: PRE
  definition: Partial Redundancy Elimination. A compiler optimization pass that identifies
    and eliminates redundant computations within a program.
- term: PHI translation
  definition: A process within SSA (Static Single Assignment) form where PHI nodes,
    which merge values from different control flow paths, are translated into expressions.
    This is often part of optimization passes like PRE.
- term: SSA name
  definition: In Static Single Assignment (SSA) form, a variable is renamed each time
    it is assigned a value. An SSA name refers to a specific version of a variable,
    ensuring each has a single definition.
- term: NARY
  definition: Represents a general tree node in GCC's internal representation (GIMPLE)
    that can have multiple children, often used for complex expressions or operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1f73f91ea78c9c6b986630d236cabd8298788aa6
date: '2026-08-21'
is_stub: false
stub_reason: ''
---

This commit corrects expression simplification in the PRE (Partial Redundancy Elimination) pass's phi-translation. Previously, limitations on what SSA names were allowed were ineffective, leading to the encoding of previously rejected names. The fix restores the original unsimplified NARY representation when simplification to an SSA name would be invalid, addressing a bug reported in PR126965.
