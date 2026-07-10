---
project: gcc
subsystem: gcc/risc-v
patch_id: null
tags:
- risc-v
- testsuite
- vector extension
- register allocation
commit_hash: 7af6db6d7b5903c118f9cc57ff2496128c78f518
source_type: github
author: Pan Li
headline: 'RISC-V: New test cases for vsext.vf4 register overlap'
tldr: Added RISC-V test cases for `vsext.vf4` to verify register group overlap behavior.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Several new test cases are introduced for `vsext.vf4` (vector sign-extend,
  float factor 4) in the RISC-V testsuite. These tests specifically scrutinize the
  'group overlap' behavior, ensuring that instructions that might use destination
  registers that partially or fully overlap with registers used by subsequent operations
  are handled correctly according to the RISC-V V extension specification.
primer_glossary:
- term: vsext.vf4
  definition: RISC-V Vector instruction for sign-extending elements to a wider format.
    The '.vf4' indicates an operation involving four vector elements.
- term: register group overlap
  definition: In the context of RISC-V vectors, this refers to situations where an
    operation on a vector of a certain length (e.g., `vf4`) might consume or alias
    registers that would also be used by subsequent operations, even if those subsequent
    operations are not immediately adjacent in the instruction stream.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7af6db6d7b5903c118f9cc57ff2496128c78f518
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit adds a set of new test cases for the RISC-V vector instruction `vsext.vf4`. These tests are designed to check for correct behavior when the destination registers for `vsext.vf4` operations overlap with subsequent registers, particularly across different vector element widths and mask factors.
