---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- zdinx
- rv32
discussion_id: caa092f8-7262-44b3-b139-7478ba5fb2db@suse.com
source_type: public_inbox
title: '[PATCH 10/19] RISC-V: check operands for Zdinx in RV32'
headline: 'Risc-V: Check operands for zdinx in rv32'
tldr: Adds operand checks for the Zdinx extension in RV32 to ensure register pairs
  are properly encoded.
stakes: Ensures correct code generation and prevents undefined behavior when using
  the Zdinx extension on RV32.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased code safety and adherence to the RISC-V specification.
- Slight performance overhead due to additional checks during assembly.
exchanges: []
primer_expert: The RISC-V Zdinx extension requires register pair operands to have
  the low bit clear. This patch modifies `gas/config/tc-riscv.c` to enforce this rule
  during assembly for RV32. The patch introduces `INSN_RV32_EVEN_*` flags to indicate
  when the XLEN is 32 and adds checks in `riscv_ip` to validate the register operands.
primer_general: The binutils suite includes an assembler that translates assembly
  code into machine code. Certain RISC-V extensions, like Zdinx, have specific requirements
  on how registers are used. This patch adds checks to the assembler to ensure these
  requirements are met, catching errors early in the development process and preventing
  programs from misbehaving.
series_id: 'binutils:risc-v: check operands for zdinx in rv32'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/caa092f8-7262-44b3-b139-7478ba5fb2db@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces operand checks for the Zdinx extension in RV32 within the binutils RISC-V assembler. It enforces that register pair operands are encoded with the low bit clear, as required by the Zdinx specification. The patch adds flags to indicate whether the XLEN is available, and uses new assembler and disassembler checks.
