---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- optimization
- performance
commit_hash: 0edfdff3040104bb95feebf4c83d4eed71564d5f
source_type: github
author: Jin Ma
headline: 'RISC-V: Tune jump-table threshold for C9501 and SpacemiT X100'
tldr: RISC-V optimization tunes jump-table threshold for specific CPUs, improving
  CPython performance.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The RISC-V target in GCC now tunes the `case-values-threshold` parameter.
  For the C9501 and SpacemiT X100 (K3) CPUs, this threshold is set to 11 when optimizing
  for speed. This allows the compiler to favor conditional branches over jump tables
  for switch statements with a small number of cases, as demonstrated by the CPython
  3.11.15 benchmark results, which show significant improvements in geomean and specific
  string-related operations.
primer_glossary:
- term: jump table
  definition: A data structure used by compilers to implement switch statements efficiently.
    It consists of an array of addresses, where each address corresponds to a case
    label. The program jumps to the appropriate address based on the switch expression's
    value.
- term: conditional branch
  definition: A CPU instruction that changes the flow of program execution based on
    a condition. If the condition is met, the program jumps to a different instruction;
    otherwise, it continues sequentially.
- term: CPython
  definition: The reference implementation of the Python programming language, written
    in C.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0edfdff3040104bb95feebf4c83d4eed71564d5f
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This commit optimizes RISC-V performance on C9501 and SpacemiT X100 (K3) processors by adjusting the jump-table threshold to 11 for speed optimizations. This change enables the eight-way character set dispatch in CPython to use conditional branches instead of a table load and indirect jump, resulting in performance gains up to 14% on certain benchmarks. The generic threshold is retained for other cores and size optimizations.
