---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- tree-optimization
- exception handling
commit_hash: a859e978a52ee6b9828d6dabfc26d5f8511970c3
source_type: github
author: Kyrylo Tkachov
headline: Prevent sinking of trapping statements when dead exceptions are kept
tldr: Stops sinking of potentially trapping statements when dead exceptions are preserved.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This addresses PR tree-optimization/128147, modifying the statement
  sinking logic in `tree-ssa-sink.cc`. The `statement_sink_location` function previously
  only checked `gimple_has_side_effects` before sinking. However, a plain load, which
  may trap, does not have side effects in this check. When `-fnon-call-exceptions`
  and `-fno-delete-dead-exceptions` are used, such loads must execute even if their
  values are unused. Sinking them into a conditional block (e.g., into an `if (c)
  return x;` where `x` is the loaded value) can cause the trap to be missed on the
  `else` path (where `c` is false). Th…
primer_glossary:
- term: GIMPLE
  definition: GCC's internal representation (IR) used after the front-end has parsed
    the source code. It's a three-address-like code that simplifies many optimization
    passes.
- term: SSA
  definition: Static Single Assignment form. A program representation where every
    variable is assigned exactly once. This simplifies many dataflow analyses and
    optimizations. GIMPLE often uses SSA form.
- term: Statement Sinking
  definition: An optimization technique that moves statements from an earlier basic
    block to a later one, typically to enable other optimizations or improve code
    layout, provided the move does not change program semantics.
- term: Trap
  definition: An exceptional condition (like a division by zero or an invalid memory
    access) that interrupts normal program execution and transfers control to an exception
    handler.
- term: Dead Exception
  definition: An exception that is thrown but never caught or handled by the program.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a859e978a52ee6b9828d6dabfc26d5f8511970c3
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit prevents the `tree-ssa-sink` pass from sinking statements that may trap when the compiler is configured to keep dead exceptions (`-fnon-call-exceptions -fno-delete-dead-exceptions`). Previously, loads that could trap were sunk into conditional blocks, even if their values were unused, leading to the potential loss of trap behavior on certain code paths. The change ensures such statements are not sunk unless dead exceptions can be safely removed.
