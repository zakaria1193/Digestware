---
project: gcc
subsystem: gcc/riscv
patch_id: null
tags:
- risc-v
- optimization
- cost model
commit_hash: 0cfd3de946cedafc0948fe4fde5a015c63b8993c
source_type: github
author: Jeff Law
headline: RISC-V cost model adjusted for LO_SUM expressions
tldr: RISC-V backend increases cost of LO_SUM expressions to improve code generation.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The RISC-V backend's cost model in `riscv.cc` was updated to increment
  the cost of `LO_SUM` RTX expressions. This change addresses PR target/108031 by
  influencing CSE's decision-making. Previously, `LO_SUM` and a simple `PLUS` had
  equal cost, leading CSE to retain `LO_SUM` to avoid gratuitous RTL changes. Increasing
  `LO_SUM`'s cost incentivizes its elimination, which often also removes the associated
  `HIGH` expression.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0cfd3de946cedafc0948fe4fde5a015c63b8993c
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

The RISC-V GCC backend has slightly increased the cost associated with LO_SUM expressions. This adjustment aims to prevent the Common Subexpression Elimination (CSE) pass from unnecessarily preserving LO_SUM forms when alternative, equivalent values exist. By making LO_SUM costlier, the compiler is encouraged to eliminate them along with associated HIGH expressions, potentially leading to more optimized code.
