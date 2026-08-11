---
project: gcc
subsystem: gcc/cfgexpand
patch_id: null
tags:
- cfgexpand
- ICE
- bugfix
- gcc
commit_hash: 1ae9479cc0ebde73867123358920752d98465131
source_type: github
author: Kyrylo Tkachov
headline: 'cfgexpand: Check partition MEM_EXPRs once the RTL of parameters is final'
tldr: Moved an internal check in cfgexpand to prevent an ICE during parameter RTL
  restoration.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `verify_partition_mem_exprs` checker in `cfgexpand.cc` was being
  invoked prematurely, before the RTL of `PARM_DECL` and `RESULT_DECL` default definitions
  was fully restored by `adjust_one_expanded_partition_var`. This temporary state,
  where a partition might hold a `MEM_EXPR` from a temporary variable rather than
  the parameter/result, caused the checker to abort with an ICE. The fix delays this
  check until after the restoration loop completes.
primer_glossary:
- term: cfgexpand
  definition: A GCC compiler pass responsible for expanding the Control Flow Graph
    (CFG) and resolving various intermediate representations, including memory expressions.
- term: MEM_EXPR
  definition: A GCC intermediate representation that denotes a memory reference, typically
    comprising a base address and an offset.
- term: RTL
  definition: Register Transfer Language. GCC's internal representation of code, used
    after the initial parsing and optimization stages, before final machine code generation.
- term: PARM_DECL
  definition: A declaration representing a function parameter in GCC's internal data
    structures.
- term: RESULT_DECL
  definition: A declaration representing the return value of a function in GCC's internal
    data structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1ae9479cc0ebde73867123358920752d98465131
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

An internal verification check, `verify_partition_mem_exprs`, within the `cfgexpand` pass has been rescheduled to run only after the RTL for parameter and result default definitions is finalized. This adjustment prevents a false positive ICE that occurred due to temporary mismatches in `MEM_EXPR` assignments between parameter/result declarations and temporary variables during the out-of-SSA restoration process.
