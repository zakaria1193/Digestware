---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- pattern matching
- vectorization
commit_hash: 5e26bbfbdfa875ef464896bb8768669dd5a9ceb9
source_type: github
author: Netanel Komm
headline: Simplify conditional additions involving constants and vectors.
tldr: 'GCC simplifies conditional expressions of the form ''x != CST1 ? x + CST2 :
  CST3'' to ''x + CST2'' when CST1 + CST2 == CST3, including uniform vectors.'
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The ``match.pd`` file in GCC defines pattern-matching rules for simplifying
  expressions during compilation. This patch extends an existing rule to handle conditional
  additions with constants and uniform vectors.  Specifically, it transforms ``x !=
  CST1 ? x + CST2 : CST3`` to ``x + CST2`` when ``CST1 + CST2 == CST3``. This optimization
  occurs during tree-ssa optimization.'
primer_general: During compilation, GCC performs various optimizations to improve
  code efficiency. One technique is pattern matching, where the compiler identifies
  specific code patterns and replaces them with simpler, equivalent forms. This commit
  adds a new pattern-matching rule to simplify conditional addition expressions where
  the result is equivalent to a simple addition. This simplification applies to both
  scalar values and uniform vectors (vectors where all elements have the same value).
discussion_id_link: github:gcc-mirror/gcc#122996
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5e26bbfbdfa875ef464896bb8768669dd5a9ceb9
date: '2026-04-27'
---

This patch extends GCC's pattern matching to simplify conditional addition expressions. When the condition is of the form ``x != CST1 ? x + CST2 : CST3`` and ``CST1 + CST2 == CST3``, the expression is simplified to ``x + CST2``. This handles cases with a third constant and uniform vectors, resolving a missing vector addition fold. New test cases have been added to verify the simplification for both scalar and vector types.
