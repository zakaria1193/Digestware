---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- opcode matching
- macros
discussion_id: 8788ef02-dad2-411b-b4a0-29139d976b0d@suse.com
source_type: public_inbox
title: '[PATCH 04/19] RISC-V: match_*() improvements'
headline: 'RISC-V: Improve match_*() functions'
tldr: Stops blindly invoking match_opcode() in match_* functions used by macro instructions.
  Adds an assertion that match_rs1_nonzero() is only used by macro insns.
stakes: Prevents potential false negatives due to macro enumeration changes within
  the assembler.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds an assertion, which has runtime cost in debug builds.
- Slightly changes the logic of opcode matching to avoid false negatives.
exchanges: []
primer_expert: The patch modifies `opcodes/riscv-opc.c`, specifically the `match_*`
  functions involved in opcode matching during assembly. These functions determine
  if an instruction matches a given opcode based on specific criteria (e.g., even
  register, non-zero register). The change addresses a potential issue where macro
  instructions could be incorrectly filtered due to changes in macro enumeration.
primer_general: In assembly, opcodes are symbolic representations of machine instructions.
  The assembler translates these opcodes into machine code. This patch focuses on
  the opcode matching process for RISC-V, a modern open-source instruction set architecture
  (ISA).  The `match_*` functions in the assembler's source code are responsible for
  determining if a given instruction matches a specific opcode, ensuring correct translation.
  This patch aims to improve the precision and reliability of this matching process,
  particularly for macro instructions, which are essentially shorthand for a sequence
  of simpler instructions.
series_id: 'binutils:risc-v: match_*() improvements'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8788ef02-dad2-411b-b4a0-29139d976b0d@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves the `match_*()` functions in the RISC-V opcode matching logic. It ensures that `match_opcode()` is not unconditionally invoked by macro instructions, preventing potential false negatives if the macro enumeration grows. An assertion is added to `match_rs1_nonzero()` to confirm its exclusive use by macro instructions, accompanied by removal of a redundant attribute from `match_rs1_nonzero_rs2_even()`.
