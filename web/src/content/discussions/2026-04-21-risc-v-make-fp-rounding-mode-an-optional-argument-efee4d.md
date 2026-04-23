---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- floating point
- rounding mode
discussion_id: bdfcf3d2-18bf-4e3a-98c6-cd0ebbf4b7d2@suse.com
source_type: public_inbox
title: '[PATCH 09/19] RISC-V: make FP rounding mode an optional argument'
headline: 'Risc-V: Make fp rounding mode an optional argument'
tldr: Makes the floating-point rounding mode (RM) an optional argument for certain
  RISC-V instructions to reduce opcode table size.
stakes: Reduces code duplication and simplifies the instruction encoding for floating-point
  operations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced opcode table size and code duplication.
- Increased code complexity in argument parsing due to optional argument handling.
exchanges: []
primer_expert: This patch modifies `gas/config/tc-riscv.c` and `opcodes/riscv-*.c`
  to make the rounding mode (RM) an optional argument. This change reduces the number
  of required opcode table entries. The code now handles the 'm' operand specifier
  to allow for an optional RM argument, similar to how the 'Vm' argument is handled.
primer_general: The binutils suite includes an assembler that translates assembly
  code into machine code. This patch simplifies the way the assembler handles floating
  point rounding modes. This change makes the assembler more flexible and reduces
  the size of internal tables used to store instruction information, by making the
  RM field optional.
series_id: 'binutils:risc-v: make fp rounding mode an optional argument'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/bdfcf3d2-18bf-4e3a-98c6-cd0ebbf4b7d2@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the RISC-V assembler to treat the floating-point rounding mode (RM) as an optional argument for certain instructions, similar to the handling of the 'Vm' argument. This change allows the assembler to reduce the number of entries in the opcode table, simplifying instruction encoding and potentially reducing code size.
