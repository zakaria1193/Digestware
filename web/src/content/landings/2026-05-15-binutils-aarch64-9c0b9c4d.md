---
project: binutils
subsystem: binutils/aarch64
patch_id: null
tags:
- aarch64
- assembler
- code cleanup
commit_hash: 9c0b9c4d841a34d8300aac9e86c6bcf5fcda19e3
source_type: public_inbox
author: Alice Carlotti <acarlotti@sourceware.org>
headline: 'AArch64: Remove unused operand SM3_IMM2.'
tldr: Removes the unused `SM3_IMM2` operand from the AArch64 assembler.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `AARCH64_OPND_SM3_IMM2` operand was defined but unused in the AArch64
  assembler. It was intended for the `sm3tt*` instructions, which ended up using `AARCH64_OPND_Em`
  instead. The operand is removed from `gas/config/tc-aarch64.c`, `include/opcode/aarch64.h`,
  `opcodes/aarch64-asm-2.c`, `opcodes/aarch64-dis-2.c`, `opcodes/aarch64-opc-2.c`,
  `opcodes/aarch64-opc.c`, and `opcodes/aarch64-tbl.h`.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.
  This commit removes an unused operand definition from the AArch64-specific part
  of the assembler. This simplifies the codebase by removing parts that aren't used.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260515140827.3025340A1F86@sourceware.org
date: '2026-05-15'
is_stub: false
---

The `SM3_IMM2` operand was intended for `sm3tt*` instructions in the AArch64 assembler, but these instructions were implemented using the `Em` operand instead. This commit removes the unused `SM3_IMM2` operand, simplifying the code and removing a potential source of confusion.
