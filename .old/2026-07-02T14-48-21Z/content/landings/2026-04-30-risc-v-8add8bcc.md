---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vectorization
- type conversion
- zvl
commit_hash: 8add8bccdcdd40103c320648d00a07c54d97160d
source_type: github
author: wangzicong
headline: 'RISC-V: Prevent tuple vector modes from tying to non-tuple modes.'
tldr: Fixes type conversions when using RISC-V vector intrinsics with the zvl extension
  by preventing tuple vector modes from being tieable to non-tuple modes.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When RISC-V's vector length agnostic extension (zvl) is enabled, the
  compiler may perform unnecessary type conversions between vector modes with different
  tuple arities. This patch modifies ``riscv_modes_tieable_p`` in ``riscv.cc`` to
  prevent tuple modes from being tieable to non-tuple modes, avoiding unexpected type
  conversions. The fix targets PR target/124448 and includes a new test case, ``pr124448.c``.
primer_general: The RISC-V vector extension (RVV) adds support for Single Instruction,
  Multiple Data (SIMD) operations, allowing a single instruction to operate on multiple
  data elements simultaneously. The 'zvl' extension enhances RVV by enabling vector
  length agnostic programming, where code can be written without explicit knowledge
  of the vector length.  This commit addresses an issue where the compiler might introduce
  incorrect type conversions between different vector types, leading to unexpected
  behavior. By preventing conversions between tuple and non-tuple vector modes, the
  compiler ensures that vector operations are performed on the correct data types,
  improving the reliability of RVV code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8add8bccdcdd40103c320648d00a07c54d97160d
date: '2026-04-30'
---

This change prevents the RISC-V backend from incorrectly converting between tuple and non-tuple vector modes when the zvl extension is enabled.  Without this fix, extracting an inner vector mode from a tuple could result in an unexpected conversion to a non-tuple mode (e.g., RVVMF2HI converted to DI, rather than RVVM1QI). This ensures that vector types are handled correctly during compilation, avoiding unexpected behavior and potential errors when using RISC-V vector instructions.
