---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembly
- floating-point
- rounding mode
- operand
discussion_id: 4fe30051-625f-448d-82b3-a232e9b0308a@suse.com
source_type: public_inbox
title: '[PATCH v3 06/13] RISC-V: make FP rounding mode an optional operand'
headline: 'RISC-V: make FP rounding mode an optional operand'
tldr: This patch makes the floating-point rounding mode an optional operand in RISC-V
  assembly, reducing opcode table entries while maintaining explicit setting for…
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Changes the assembly syntax for floating-point instructions, which might require
  updates to existing assembly code that explicitly specifies rounding modes where
  they are now optional.
- Reduces entries in the opcode table, offering a small optimization in terms of binary
  size or parsing speed.
- Introduces an exception for `FCVTMOD.W.D`, which adds a minor complexity to the
  ruleset.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to make the floating-point rounding mode an optional operand
    in RISC-V assembly, aiming to reduce opcode table entries and simplify parsing.
  quote: 'Model this after Vm (and somewhat after its VM counterpart): It''s similarly
    always last, and we can hence similarly reduce the number of entries in the opcode
    table. The exception being FCVTMOD.W.D, where M needs using.'
primer_expert: In the RISC-V `gas` backend (`gas/config/tc-riscv.c`) and disassembler
  (`opcodes/riscv-dis.c`), floating-point instructions often include a rounding mode
  operand (`rm`). Currently, this operand is always specified. This patch differentiates
  between mandatory ('M') and optional ('m') rounding mode operands in the instruction
  template strings used by `validate_riscv_insn` and `riscv_ip`. When a 'm' operand
  is encountered and the assembly argument list has already been consumed (`*asarg
  == '\0'`), the rounding mode is implicitly treated as default (or not explicitly
  encoded, represented by `OP_M…
primer_general: 'This discussion is about how instructions for Floating-Point (FP)
  math are handled in RISC-V assembly code, specifically within the GNU Assembler
  (`gas`) and disassembler (`opcodes` component of binutils). FP operations often
  need to specify how results should be rounded (e.g., round to nearest, round down).
  Currently, this "rounding mode" is always written out in the assembly instruction.
  This patch proposes a change to make the rounding mode optional for most FP instructions.
  This means if you don''t specify it, the assembler will assume a default rounding
  behavior. This makes the assembly code slightly shorter and simpler, and it also
  helps reduce the complexity of the internal tables the assembler uses to understand
  instructions. There''s one exception: for a specific instruction called `FCVTMOD.W.D`,
  the rounding mode will still need to be explicitly stated.'
series_id: 'binutils:risc-v: make fp rounding mode an optional operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4fe30051-625f-448d-82b3-a232e9b0308a@suse.com
bugzilla_url: null
date: '2026-06-19'
is_stub: false
---

This proposal modifies the RISC-V assembler to treat the floating-point rounding mode as an optional operand, similar to how vector mask (`Vm`) is handled. This change aims to simplify the instruction parsing process and reduce the size of the opcode table. The rounding mode will default if not explicitly provided, except for the `FCVTMOD.W.D` instruction where it remains mandatory.
