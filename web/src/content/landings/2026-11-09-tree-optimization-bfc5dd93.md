---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- volatile
commit_hash: bfc5dd9360f265f89234d6f5a00ab8ff007ce773
source_type: github
author: Richard Biener
headline: tree-optimization/128575 - Avoid removing volatile store
tldr: Prevents the Dead Store Elimination pass from incorrectly removing volatile
  stores.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `dse_optimize_redundant_stores` in `tree-ssa-dse.cc`
  to prevent the elimination of volatile stores. The Dead Store Elimination (DSE)
  pass, when encountering redundant zero initializations, could incorrectly identify
  a volatile store as dead and remove it. This change adds a check to ensure that
  stores marked as volatile are not eliminated, even if they appear redundant based
  on SSA analysis alone, thereby preserving their side effects.
primer_glossary:
- term: tree-optimization
  definition: A phase of compilation where optimizations are performed on GCC's intermediate
    representation, known as the 'tree' or GIMPLE representation.
- term: volatile
  definition: A type qualifier in C/C++ that tells the compiler that a variable's
    value may change at any time without any action being taken by the code the compiler
    knows about. This prevents the compiler from optimizing away reads or writes to
    that variable.
- term: Dead Store Elimination
  definition: An optimization pass that removes stores to variables whose values are
    never subsequently read before being overwritten or going out of scope.
- term: SSA
  definition: Static Single Assignment. An intermediate representation where every
    variable is assigned a value exactly once. SSA form simplifies many optimization
    algorithms.
- term: redundant zero initialization
  definition: A situation where a variable is initialized to zero multiple times,
    or initialized to zero when its value is effectively discarded immediately afterward.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bfc5dd9360f265f89234d6f5a00ab8ff007ce773
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This commit fixes a bug (PR tree-optimization/128575) where the Dead Store Elimination (DSE) optimization pass could incorrectly remove volatile stores. This occurred when DSE encountered redundant zero initializations. The fix ensures that volatile stores are preserved, preventing potential miscompilations. A new test case is included to cover this scenario.
