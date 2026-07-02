---
project: gcc
subsystem: gcc/risc-v
patch_id: null
tags:
- risc-v
- vectorization
- register-allocation
- architecture-specific
commit_hash: 0ca2ba3b88532aefff95036205fa0e6db0abe718
source_type: github
author: Robin Dapp
headline: 'RISC-V: Example dependent filter for RVV widen overlap'
tldr: This commit adds a RISC-V Vector (RVV) specific dependent filter to prevent
  illegal overlaps in widening instructions.
impact_score: 8
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit deploys a concrete example of a dependent filter from
  the previous IRA commit, specifically for RISC-V Vector Extension (RVV) widening
  instructions. The `riscv_widen_operand_ok` function, declared in `riscv-protos.h`
  and implemented in `riscv.cc`, is introduced. This function enforces a hardware-level
  constraint: for RVV widening operations, source operands are forbidden from overlapping
  the destination register, with a narrow exception for the highest-numbered part
  when the effective element multiplier (`EMUL`) is greater than 1. This filter is
  attached to the "Wtt" constraint in…'
primer_general: Modern CPUs often have special instructions for working with large
  amounts of data at once, like vector operations on RISC-V processors (RVV). These
  vector instructions can "widen" data, meaning they take smaller numbers and convert
  them into larger ones, for example, from 16-bit to 32-bit. However, some rules about
  which temporary storage locations (registers) can be used are quite strict. This
  update adds a new rule, or "filter," to the GCC compiler specifically for these
  RISC-V vector widening instructions. This rule prevents the compiler from using
  the same register for both the input and output of a widening operation in a way
  that the hardware doesn't allow. Essentially, it helps the compiler generate correct
  and efficient code for RISC-V vector extensions, preventing errors that could otherwise
  occur due to these complex hardware constraints.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0ca2ba3b88532aefff95036205fa0e6db0abe718
date: '2026-04-29'
is_stub: false
---

Building upon the newly introduced dependent filter infrastructure, this commit implements a specific filter for RISC-V Vector (RVV) architectures. This filter addresses a hardware constraint where source operands of widening instructions cannot overlap with the destination, except in specific highest-numbered parts when `EMUL > 1`. By integrating `riscv_widen_operand_ok` into the register allocation constraints, GCC can now avoid generating incorrect RVV widening instructions, improving code correctness for vector extensions.
