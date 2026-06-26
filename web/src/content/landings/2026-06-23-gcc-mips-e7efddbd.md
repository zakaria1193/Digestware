---
project: gcc
subsystem: gcc/mips
patch_id: null
tags:
- mips
- atomic-operations
- bugfix
- compiler-internals
commit_hash: e7efddbd351e00fc5cda58dd063947784bf7e8b3
source_type: github
author: Xi Ruoyao
headline: MIPS backend fixes uninitialized operand use in sync_<optab>_12 patterns
tldr: GCC for MIPS now correctly initializes operands in `sync_old` and `sync_new`
  patterns, fixing a bug where uninitialized values led to incorrect atomic operatio…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC's MIPS backend, the `sync_old_<optab><mode>` and `sync_new_<optab><mode>`
  RTL patterns in `sync.md` implement atomic read-modify-write operations. The issue
  (PR 125628) stemmed from an incorrect understanding of how `define_insn` with multiple
  elements generates a `parallel` expression. When a `parallel` is encountered, all
  operand values are computed before any side-effects occur. Therefore, `match_dup
  0` (referring to the output register) was being used before it was assigned, leading
  to an uninitialized value. This could be folded to `0` during optimization, causing
  incorrect result…
primer_general: When you write code that performs "atomic" operations—meaning operations
  that must complete entirely without interruption, especially in multi-threaded programs—the
  compiler needs to translate these carefully to machine instructions. In the GCC
  compiler for MIPS processors, there was a bug in how certain atomic operations (`sync_old`
  and `sync_new` patterns) were described internally using something called Register
  Transfer Language (RTL). The problem was that the compiler was trying to use a value
  from a register *before* that register had been updated, leading to incorrect results,
  particularly when optimizations were turned on. For example, an operation like "add
  1 to something" might mistakenly add 1 to 0 instead of the current value. This commit
  fixes that by ensuring the compiler correctly refers to the already-set value in
  the register, making atomic operations on MIPS processors work as intended and preventing
  subtle bugs in your parallel programs.
discussion_id_link: github:gcc-mirror/gcc#125628
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e7efddbd351e00fc5cda58dd063947784bf7e8b3
date: '2026-06-23'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in the GCC MIPS backend where certain `sync_old` and `sync_new` RTL patterns were using uninitialized operands, causing incorrect behavior in atomic operations. Specifically, the output register, specified by `match_dup 0`, was being referenced before its value was set when RTL templates were treated as parallel expressions. The fix corrects the operand referencing to `match_dup 1` and clarifies the source of memory writes, preventing erroneous folded results at optimization levels.
