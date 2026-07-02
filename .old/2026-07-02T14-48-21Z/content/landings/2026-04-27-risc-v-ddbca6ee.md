---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- rvv
- vectorization
- testing
commit_hash: ddbca6eeda6b19ad4e983167921711b214b87556
source_type: github
author: Pan Li
headline: 'RISC-V: Add tests for vector duplicate and vmsgtu.vv combine'
tldr: Adds test cases for combining vec_duplicate and vmsgtu.vv to vmsgtu.vx with
  different GR2VR costs.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit introduces tests exercising the combination of ``vec_duplicate``
  and ``vmsgtu.vv`` into ``vmsgtu.vx``, conditioned on the GR2VR cost. The tests (in
  ``gcc.target/riscv/rvv/autovec/vx_vf/``) use a helper macro and data to generate
  code sequences and verify that the expected ``vmsgtu.vx`` instruction is generated.
primer_general: The RISC-V vector extension (RVV) adds support for vector processing,
  allowing operations to be performed on multiple data elements simultaneously. Vectorization
  can significantly improve performance for data-parallel workloads. The compiler's
  autovectorization pass automatically transforms scalar code into vector code where
  possible.  This commit adds test cases to verify that the compiler correctly combines
  certain vector instructions to generate more efficient code sequences.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ddbca6eeda6b19ad4e983167921711b214b87556
date: '2026-04-27'
---

This commit adds new test cases for the RISC-V vector extension (RVV) to verify the combination of ``vec_duplicate`` and ``vmsgtu.vv`` instructions into ``vmsgtu.vx``. The tests cover scenarios where the cost of transferring data from general-purpose registers to vector registers (GR2VR) is 0, 1, and 15. Assembly code checks are included to ensure that the expected vector instructions are generated.
