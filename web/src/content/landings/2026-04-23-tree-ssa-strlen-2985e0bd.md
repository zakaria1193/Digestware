---
project: gcc
subsystem: tree-ssa-strlen
patch_id: null
tags:
- optimization
- refactor
- gimple
- strlen
commit_hash: 2985e0bd9b2aee03a932e5ab406523a95c04de5f
source_type: github
author: Avinal Kumar
headline: 'tree-ssa-strlen: Use gimple_build/gimple_convert_to_ptrofftype'
tldr: The strlen pass in GCC now uses gimple_build and gimple_convert_to_ptrofftype
  for building GIMPLE statements, simplifying the code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies ``tree-ssa-strlen.cc`` to use ``gimple_convert_to_ptrofftype``
  and ``gimple_build`` instead of ``convert_to_ptrofftype``, ``force_gimple_operand_gsi``
  and ``gimple_build_assign``. These are functions used to manipulate GIMPLE representation
  during optimization.  The strlen pass attempts to determine the length of strings
  at compile time. This is mostly a refactoring change to use more modern GIMPLE APIs.
primer_general: GCC transforms source code into a series of intermediate representations
  (IR) during compilation.  GIMPLE is one such low-level IR.  The ``tree-ssa-strlen``
  pass attempts to determine the length of strings at compile time, which enables
  optimizations like eliminating calls to ``strlen``.  This commit refactors the code
  responsible for building GIMPLE statements within that pass to use more modern and
  consistent APIs, improving code quality.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2985e0bd9b2aee03a932e5ab406523a95c04de5f
date: '2026-04-23'
---

The ``tree-ssa-strlen`` pass in GCC now uses ``gimple_build`` and ``gimple_convert_to_ptrofftype`` for constructing GIMPLE statements, replacing older functions like ``convert_to_ptrofftype`` and ``force_gimple_operand_gsi``. This simplifies the code and improves maintainability by using the preferred GIMPLE building APIs. This change is part of ongoing efforts to modernize and streamline GCC's internal APIs.
