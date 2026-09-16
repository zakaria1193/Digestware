---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- switch statement
- bugfix
commit_hash: 6e33c9be872cc7d2474b4224d1a16515e1b0d2b8
source_type: github
author: Richard Biener
headline: tree-optimization/126760 - Fix vectorization of switches
tldr: Corrects CFG shape check for switch statement vectorization after if-conversion.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch corrects the `if_convertible_switch_p` check in `tree-if-conv.cc`
  which was too eager. By delaying the switch validation to within `if_convertible_loop_p_1`,
  specifically after the loop over PHIs, it ensures that the check correctly assesses
  the CFG shape required for if-conversion of switch statements, resolving issues
  where the check was elided for dominating blocks and causing incorrect vectorization
  (PRs tree-optimization/126760, tree-optimization/127391).
primer_glossary:
- term: vectorization
  definition: An optimization technique that allows a single instruction to operate
    on multiple data elements simultaneously, significantly improving performance
    for data-parallel operations.
- term: switch statement
  definition: A control flow statement in C/C++ that selects one of many code blocks
    to execute based on the value of an expression.
- term: if-conversion
  definition: A compiler optimization that replaces conditional control flow (like
    if statements or branches) with conditional execution of instructions, often enabling
    better instruction-level parallelism.
- term: CFG
  definition: Control Flow Graph, a representation of all execution paths through
    a program, used by compilers for analysis and optimization.
- term: PHI node
  definition: In SSA (Static Single Assignment) form, a PHI node is used to merge
    values from different control flow paths. It represents a value that may have
    come from one of several preceding basic blocks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6e33c9be872cc7d2474b4224d1a16515e1b0d2b8
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in GCC's vectorization of switch statements that are converted using if-conversion. The check `if_convertible_switch_p` was incorrectly elided for blocks dominating loop latches, leading to faulty conversion. The fix delays the switch validation until the loop iterating over PHIs, ensuring correct CFG shape analysis and enabling reliable vectorization for such constructs, addressing PRs tree-optimization/126760 and tree-optimization/127391.
