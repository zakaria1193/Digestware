---
project: binutils
subsystem: binutils/gas/risc-v
patch_id: null
tags:
- risc-v
- assembler
- refactoring
- code-quality
commit_hash: d573596275005ee7c003353e02a1198524889a4a
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: RISC-V `riscv_ip()` code for `.insn` operands simplifies.
tldr: Binutils RISC-V assembler now uses a single, shared code path for parsing 'F'
  and 'O' operands of the `.insn` directive, improving modularity and maintainabili…
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `riscv_ip()` function in `gas/config/tc-riscv.c` handles the parsing
  for the `.insn` directive, which allows developers to manually encode RISC-V instructions.
  Specifically, the 'F' and 'O' operands are used to specify funct fields and opcode
  fields, respectively. This commit refactors the parsing logic for these operands
  by consolidating redundant code. Instead of separate, largely identical code blocks
  for various 'F' and 'O' sub-forms, a unified parsing mechanism now exists. This
  improves code maintainability and simplifies the extension of the `.insn` directive
  to support new sub-form…
primer_general: When you write assembly code, you sometimes need to directly specify
  the exact bit pattern of an instruction, which is done using a special directive
  like `.insn`. For RISC-V processors, the `.insn` directive allows you to specify
  different parts of an instruction using operands like 'F' (for 'function' fields)
  and 'O' (for 'opcode' fields). This change within the Binutils assembler makes the
  internal code that processes these 'F' and 'O' operands more efficient and organized.
  Previously, there was a lot of duplicated code for handling slightly different versions
  of these operands. Now, the code has been streamlined so that common parsing steps
  are handled once, and only the specific details for each operand type are managed
  separately. This makes the assembler's code easier to understand, maintain, and
  extend when new instruction variations are introduced.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260605091331.EE98B4BCA402@sourceware.org
date: '2026-06-05'
is_stub: false
---

The RISC-V assembler's `riscv_ip()` function, responsible for parsing operands of the `.insn` directive, has been refactored to remove redundant code. Previously, the parsing logic for 'F' and 'O' operands was duplicated. Now, common code handles the initial parsing, with a smaller, inner switch statement managing the value insertion specific to each operand type, making it easier to add new operand sub-forms in the future.
