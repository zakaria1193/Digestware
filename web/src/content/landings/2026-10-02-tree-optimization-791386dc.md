---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
commit_hash: 791386dc22c978e374863d459c378c64cb6d8f26
source_type: github
author: Yongqiang Tian
headline: Skip GIMPLE_DEBUG stmts before assigning UIDs
tldr: GCC now skips GIMPLE_DEBUG statements before assigning UIDs, preventing them
  from disrupting VEC_PERM simplification and ensuring consistent optimization regar…
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-forwprop.cc`, the `pass_forwprop::execute` method previously
  assigned UIDs to `GIMPLE_DEBUG` statements, which are then filtered out as non-assignments.
  This premature UID consumption and filtering disrupted `VEC_PERM` simplify sequences.
  The change modifies the pass to skip `GIMPLE_DEBUG` statements entirely before UID
  assignment and before processing regular statements, thus preventing them from affecting
  the simplification pipeline and ensuring deterministic optimization behavior.
primer_glossary:
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation (IR) used for
    optimization passes.
- term: UID
  definition: Unique Identifier, a mechanism within GCC's intermediate representation
    to uniquely label statements or expressions.
- term: VEC_PERM
  definition: A GCC internal representation node type, typically related to vector
    permutation operations, which is subject to simplification.
- term: optimization pass
  definition: A distinct phase or transformation within the compiler's optimization
    pipeline that analyzes and modifies the intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/791386dc22c978e374863d459c378c64cb6d8f26
date: '2026-10-02'
is_stub: false
stub_reason: ''
---

This commit fixes a bug where GIMPLE_DEBUG statements interfered with optimization passes by consuming Unique Identifiers (UIDs) prematurely. This consumption caused pending VEC_PERM simplify sequences to be flushed, making optimization results dependent on the presence of debug information. The fix ensures that debug statements are skipped before UID assignment and processing of ordinary statements, leading to more consistent optimization.
