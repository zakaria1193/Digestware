---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- gcc
- tree-ssa
- vectorization
commit_hash: 75dfd8b97da1ef0e6e70316bf57355453b0e3001
source_type: github
author: Dominic P
headline: Adjust sext-vector-1.c test for lowered vector XORs
tldr: Modifies a test case to scan for XOR constants instead of counting XOR operations
  after vector lowering.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC test `gcc.dg/tree-ssa/sext-vector-1.c` previously counted XOR
  instructions in its optimized dump. However, with `-m32`, the 8-byte vector `vq`
  is lowered into two 4-byte halves, leading to an increase in XOR operations from
  four to five. To maintain test stability across different targets and internal lowering
  strategies, this commit modifies the test to scan for the specific XOR constants
  involved rather than relying on a direct count of the XOR instructions.
primer_glossary:
- term: sext
  definition: Sign-extend. Extending a smaller integer value by replicating its most
    significant bit to fill the higher-order bits of a larger integer type.
- term: Lowering
  definition: The process in a compiler where higher-level intermediate representations
    are transformed into lower-level ones, closer to machine code.
- term: XOR
  definition: Exclusive OR. A bitwise logical operation.
- term: Tree SSA
  definition: An intermediate representation used in GCC that combines concepts of
    Control Dependence Graph (CDG) and Static Single Assignment (SSA) form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/75dfd8b97da1ef0e6e70316bf57355453b0e3001
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This change updates the `sext-vector-1.c` test case to scan for XOR constants rather than counting the XOR operations. This is necessary because on `-m32` targets, the 8-byte vector is lowered into two halves, resulting in five XORs in the optimized dump instead of the previously expected four. Scanning for constants makes the test robust to these internal representation changes.
