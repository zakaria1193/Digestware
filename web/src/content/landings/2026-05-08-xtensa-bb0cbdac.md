---
project: gcc
subsystem: xtensa
patch_id: null
tags:
- xtensa
- register allocation
- optimization
- stack frame
commit_hash: bb0cbdac196986de933f4f93097de021c3686d7c
source_type: github
author: Takayuki 'January June' Suwa
headline: 'Xtensa: Define HONOR_REG_ALLOC_ORDER as 1'
tldr: This commit disables incorrect register save cost estimation in function prologues/epilogues
  for Xtensa, potentially reducing stack frame usage.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The ``HONOR_REG_ALLOC_ORDER`` macro affects how the register allocator
  prioritizes registers for saving and restoring.  By defining it as 1, the compiler
  will no longer incorrectly estimate register save costs, avoiding unnecessary stack
  frame allocation.  The issue was introduced by commit 3b9b8d6cfdf59337f4b7ce10ce92a98044b2657b
  ("ira: Scale save/restore costs of callee save registers with block frequency").
  Search terms: GCC Xtensa HONOR_REG_ALLOC_ORDER register allocation.'
primer_general: 'Register allocation is the process of assigning variables and temporary
  values to registers in the CPU. The goal is to minimize memory access and improve
  performance.  This commit changes how the compiler estimates the cost of saving
  and restoring registers in function prologues and epilogues which can lead to more
  efficient code generation and reduced stack usage. Search terms: GCC Xtensa HONOR_REG_ALLOC_ORDER
  register allocation.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb0cbdac196986de933f4f93097de021c3686d7c
date: '2026-05-08'
is_stub: false
---

The Xtensa ISA was allocating slightly more function stack frames after a previous patch related to IRA (Interprocedural Register Allocation). This commit disables the incorrect register save cost estimation in function prologues/epilogues by defining the ``HONOR_REG_ALLOC_ORDER`` macro as 1. This can reduce stack frame usage, especially when using the CALL0 ABI.
