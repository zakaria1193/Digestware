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
headline: 'Risc-V: Make FP rounding mode an optional argument'
tldr: Makes the floating-point rounding mode argument optional for certain RISC-V
  instructions, reducing opcode table size.
stakes: Reduces the size of the opcode table, potentially improving performance and
  reducing memory usage.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Slightly more complex assembler logic for handling optional arguments.
- Smaller opcode table, potentially improving performance and reducing memory usage.
exchanges: []
primer_expert: The RISC-V assembler uses an opcode table to map instruction names
  to their corresponding encodings.  This patch modifies the assembler to allow the
  rounding mode ('m') argument to be optional for some instructions, reducing the
  number of opcode table entries. The patch modifies `riscv_ip` to handle the optional
  rounding mode.
primer_general: When writing RISC-V assembly code, some floating-point instructions
  can take an optional rounding mode argument.  This patch modifies the assembler
  to correctly handle these optional arguments, potentially leading to a smaller and
  more efficient assembler.
series_id: 'binutils:risc-v: make fp rounding mode an optional argument'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/bdfcf3d2-18bf-4e3a-98c6-cd0ebbf4b7d2@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the RISC-V assembler to make the floating-point rounding mode argument optional for certain instructions. This is modeled after the handling of the 'Vm' argument, and reduces the number of entries required in the opcode table. The exception is the FCVTMOD.W.D instruction where the 'M' argument is required.
