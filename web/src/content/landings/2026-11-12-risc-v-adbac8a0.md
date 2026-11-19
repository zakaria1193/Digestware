---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vector
- testsuite
commit_hash: adbac8a0978e1a985dea4ce3c67ab1d381b8688e
source_type: github
author: Pan Li
headline: 'RISC-V: Adjust vwsub[u].wv m4 test cases for reg overlap'
tldr: RISC-V test cases for `vwsub[u].wv` are adjusted to reflect changes in register
  allocation under high pressure.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: RISC-V vector testsuite adjustments. This patch modifies assembly checks
  in `vwsub[u].wv` test cases (specifically m4 configurations) after a change to the
  Wn4 constraint on operand 3 (vs2). The change reflects that `vs1` may overlap `vd`
  but not `vs2` under certain register pressure conditions, mirroring behavior seen
  with `vfwsub.wv`.
primer_glossary:
- term: vwsub.wv
  definition: A RISC-V vector instruction for wide subtract with a scalar value in
    the second source register. It performs element-wise subtraction, widening the
    elements of the first source vector by the second source register's elements.
- term: vwsubu.wv
  definition: A RISC-V unsigned vector instruction for wide subtract with a scalar
    value in the second source register. It performs element-wise unsigned subtraction,
    widening the elements of the first source vector by the second source register's
    elements.
- term: vs1
  definition: The first source vector register in a RISC-V vector instruction. It
    holds one of the operands for the vector operation.
- term: vs2
  definition: The second source vector register in a RISC-V vector instruction. It
    holds the other operand for the vector operation, often with a different element
    width (EEW) than the destination (vd) or vs1.
- term: Wn4 constraint
  definition: A constraint in RISC-V vector instruction assembly that relates to the
    register group size. 'Wn4' likely refers to a constraint involving a group of
    4 vector registers.
- term: register pressure
  definition: A condition during code generation where the number of simultaneously
    live register values exceeds the available physical registers, forcing the compiler
    to spill values to memory or use more complex register allocation strategies.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/adbac8a0978e1a985dea4ce3c67ab1d381b8688e
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit refines existing test cases for the RISC-V `vwsub[u].wv` instructions to accommodate adjustments in register allocation. Following the application of the Wn4 constraint to the `vs2` operand, register allocation behavior under high pressure has changed. The tests are updated to reflect that `vs1` still overlaps the upper part of `vd` but does not overlap `vs2`, consistent with `vfwsub.wv`, ensuring the tests accurately validate this behavior.
