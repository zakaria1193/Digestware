---
project: gcc
subsystem: gcc/internals
patch_id: null
tags:
- optimization
- register allocation
- compiler internals
commit_hash: f6103f3a1e42fe4db15f3c1d96847cd4a4829e4e
source_type: github
author: Kevin Stefanov
headline: GCC optimizes hard register set iteration by replacing `TEST_HARD_REG_BIT`.
tldr: GCC improves the efficiency of iterating over hard register sets by replacing
  `TEST_HARD_REG_BIT` with `hard_reg_set_iterator` and `hard_reg_set_popcount`.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change focuses on optimizing hard register set manipulation within
  GCC's backend. Previously, iterating through a `hard_reg_set` to check for individual
  bits often involved a `for` loop with `TEST_HARD_REG_BIT`. This has been replaced
  with `EXECUTE_IF_SET_IN_HARD_REG_SET`, which leverages `hard_reg_set_iterator` for
  more efficient iteration over the set bits. Similarly, instances of `hard_reg_set_size`,
  which internally used such a loop to count set bits, are replaced with `hard_reg_set_popcount`,
  which is a more direct and efficient way to achieve the population count. These
  changes pri…
primer_general: Compilers work with 'registers,' which are tiny storage locations
  inside the computer's processor. To make your programs fast, the compiler carefully
  manages which data goes into which registers. Sometimes, the compiler needs to check
  many registers at once to see which ones are available or in use. This commit improves
  how GCC, the compiler, does these checks. Instead of checking each register individually
  in a slow loop, it now uses more specialized and faster techniques that can quickly
  find all the registers that meet a certain condition. This makes the compiler faster
  at its job, which can indirectly lead to faster compilation times for your programs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f6103f3a1e42fe4db15f3c1d96847cd4a4829e4e
date: '2026-06-04'
is_stub: false
---

This GCC commit refactors internal loops that check individual bits in hard register sets, replacing inefficient `TEST_HARD_REG_BIT` calls within loops with the more efficient `EXECUTE_IF_SET_IN_HARD_REG_SET` macro. Additionally, direct calls to `hard_reg_set_size` are replaced with `hard_reg_set_popcount`, as the latter more accurately reflects the intended operation of counting set bits. These changes improve compiler performance by streamlining register set manipulations, primarily in architecture-specific code generation and optimization passes.
