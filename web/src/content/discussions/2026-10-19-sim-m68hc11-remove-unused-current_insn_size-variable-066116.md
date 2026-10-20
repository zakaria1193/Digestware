---
project: binutils
subsystem: sim/m68hc11
patch_id: null
tags:
- binutils
- gdb
- simulator
- m68hc11
- compiler warnings
discussion_id: 50618a5e-0c68-4380-b2b3-32f3ed487b67@efficios.com
source_type: public_inbox
title: 'Re: [PATCH 11/18] sim/m68hc11: remove unused current_insn_size variable'
headline: 'sim/m68hc11: remove unused current_insn_size variable'
tldr: Removes unused `current_insn_size` variable from the m68hc11 simulator, fixing
  compiler warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes unused code and resolves compiler warnings.
- Simplifies the codebase.
- No impact on the simulator's functionality.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to remove the unused `current_insn_size` variable and
    associated code from the m68hc11 simulator.
  quote: "Building the m68hc11 simulator with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/sim/m68hc11/gencode.c:1143:12:\
    \ error: variable 'current_insn_size' set but not used [-Werror,-Wunused-but-set-global]\n\
    \nThe only read of current_insn_size is an instruction size consistency check,\
    \ which has been disabled with \"#if 0\" since commit 81e09ed8322b (\"Improve\
    \ HC11 simulator to support HC12\"…"
primer_expert: This patch addresses unused code in the `sim/m68hc11/gencode.c` file,
  which is part of the Motorola 68HC11 microcontroller simulator within binutils/gdb.
  The variable `current_insn_size` was used to track the size of the instruction being
  generated. However, the code that utilized this variable for an internal consistency
  check has been commented out (`#if 0`) for many years. Consequently, the variable
  is now flagged as unused by modern compilers like Clang, and this patch removes
  it entirely, along with the dead code, to clean up the source and resolve warnings.
primer_glossary:
- term: simulator
  definition: A program that mimics the behavior of a hardware device or system. In
    this context, it simulates the execution of instructions for a specific microcontroller
    or processor.
- term: m68hc11
  definition: A popular 8-bit microcontroller family manufactured by Motorola (now
    Freescale/NXP). Binutils includes a simulator for it.
- term: gencode.c
  definition: A source file likely containing code generation logic for the simulator,
    possibly responsible for translating instruction definitions into executable simulation
    code.
- term: instruction size consistency check
  definition: A verification mechanism to ensure that the generated code correctly
    reflects the size of the instructions being simulated. This check appears to have
    been disabled.
series_id: 'binutils:sim/m68hc11: remove unused current_insn_size variable'
series_role: reply
series_parts:
- title: 'sim/m68hc11: remove unused current_insn_size variable'
  url: https://inbox.sourceware.org/binutils/20261019193231.1708375-12-simon.marchi@efficios.com
  n: 11
  total: 18
url: https://inbox.sourceware.org/binutils/50618a5e-0c68-4380-b2b3-32f3ed487b67@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch removes the `current_insn_size` variable from the m68hc11 simulator's code generation source file (`gencode.c`). The variable, along with the code that computed it, was only used for an instruction size consistency check that has been disabled (`#if 0`) since 2001. Compiling with recent Clang flags this variable as unused, leading to warnings. The patch removes the variable, its computation, and the disabled check, cleaning up the codebase.
