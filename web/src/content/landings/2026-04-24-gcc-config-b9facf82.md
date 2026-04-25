---
project: gcc
subsystem: gcc/config
patch_id: null
tags:
- risc-v
- vectorization
- optimization
- code generation
commit_hash: b9facf8263e7de298606b2629f8b78bb6b0d4906
source_type: github
author: Raphael Zinsly
headline: 'RISC-V: Improve codegen for constant permutes using vslideup+vslidedown.'
tldr: This commit optimizes RISC-V vector code generation for specific constant permutes
  by using `vslideup+vslidedown` instead of `vslideup+vcompress`.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch modifies `riscv-v.cc` to improve RISC-V vector code generation
  for specific constant permutations, addressing PR target/123839.  It replaces a
  `vslideup+vcompress` sequence with `vslideup+vslidedown` for certain permutes, which
  eliminates the need for a mask and its setup.  This optimization targets the RISC-V
  V extension and benefits code that uses these specific permutation patterns.
primer_general: Modern processors use vector instructions process multiple data elements
  with a single instruction, which is much faster.  Rearranging elements within a
  vector is called a permutation.  This commit improves the way GCC generates RISC-V
  vector instructions for specific constant permutations, replacing a less efficient
  instruction sequence with a more efficient one.  The result is faster code execution
  on RISC-V processors when these permutations are used.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b9facf8263e7de298606b2629f8b78bb6b0d4906
date: '2026-04-24'
---

This commit improves RISC-V vector code generation by implementing certain constant permutes with a `vslideup+vslidedown` instruction sequence, instead of the existing `vslideup+vcompress` which requires a mask.  This change avoids the overhead of mask setup and potentially improves performance for these permute operations. A new test case is added to verify the improved code generation.
