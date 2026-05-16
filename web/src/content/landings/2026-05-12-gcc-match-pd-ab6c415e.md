---
project: gcc
subsystem: gcc/match.pd
patch_id: null
tags:
- optimization
- bitwise
- pattern matching
- tree-ssa
commit_hash: ab6c415e13ca87e3e4c7a24ccd9bf83e23ef30ee
source_type: github
author: Shivam Gupta
headline: Simplify ((~x) & y) ^ (x | y) to x or ~x
tldr: GCC now simplifies certain bitwise operations involving XOR, AND, OR, and NOT
  into simpler forms, potentially improving code generation.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The commit adds a simplification to ``match.pd`` that transforms specific
  XOR/AND/OR/NOT patterns into simpler forms, which can help reduce code size and
  improve instruction selection. The optimization happens at the GIMPLE IR level during
  the tree-ssa phase, and the change should be transparent to other parts of the compiler.
  This is a fairly isolated change within the match.pd framework.
primer_general: Compilers often perform algebraic simplifications to reduce instructions,
  registers, or memory traffic.  GCC represents code internally using an intermediate
  representation (IR) called GIMPLE.  The tree-ssa optimisation pass uses Single Static
  Assignment (SSA) form to enable various optimisations and simplifications by analysing
  data flow. This commit modifies a pattern-matching system within tree-ssa to detect
  and rewrite specific bitwise expressions.  These transformations can lead to smaller
  and faster code by reducing the number of operations that need to be performed at
  runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab6c415e13ca87e3e4c7a24ccd9bf83e23ef30ee
date: '2026-05-12'
is_stub: false
---

The compiler can now simplify expressions of the form ``((~x) & y) ^ (x | y)`` to ``x``, and ``((~x) | y) ^ (x & y)`` to ``~x``.  This pattern is detected during tree-ssa optimisation, using a pattern-matching framework (match.pd) to rewrite the GIMPLE IR.  The change should reduce code size and improve performance in code that uses these bitwise patterns.
