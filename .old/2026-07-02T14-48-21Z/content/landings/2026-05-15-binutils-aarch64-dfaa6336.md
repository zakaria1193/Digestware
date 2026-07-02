---
project: binutils
subsystem: binutils/aarch64
patch_id: null
tags:
- aarch64
- assembler
- code cleanup
commit_hash: dfaa6336059d14499aefbd433de5b2b473ad33e9
source_type: public_inbox
author: Alice Carlotti <acarlotti@sourceware.org>
headline: 'AArch64: Remove unused operand ADDR_SIMM9_2.'
tldr: Removes the unused ADDR_SIMM9_2 operand from the AArch64 assembler, cleaning
  up the code.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ADDR_SIMM9_2` operand, defined in `include/opcode/aarch64.h` and
  used in the AArch64 assembler, has been unused since commit `c8f89a3423101b25`.
  This commit removes it from `gas/config/tc-aarch64.c`, `include/opcode/aarch64.h`,
  `opcodes/aarch64-asm-2.c`, `opcodes/aarch64-dis-2.c`, `opcodes/aarch64-opc-2.c`,
  `opcodes/aarch64-opc.c`, and `opcodes/aarch64-tbl.h`.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.
  This commit removes an unused operand definition from the AArch64-specific part
  of the assembler, namely `ADDR_SIMM9_2`. This simplifies the codebase by removing
  parts that aren't used, and prevents confusion.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260515140822.107C6490037F@sourceware.org
date: '2026-05-15'
is_stub: true
stub_reason: low-score
---

The `ADDR_SIMM9_2` operand in the AArch64 assembler has been unused since changes in load/store register handling. This commit removes the operand definition, simplifying the code and reducing potential confusion.
