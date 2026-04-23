---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- zve64x
- eew64
- disassembler
- assembler
discussion_id: 180db539-b81a-44c4-8bb9-d6ff5065a427@suse.com
source_type: public_inbox
title: '[PATCH 05/19] RISC-V: EEW64 checking'
headline: 'Risc-V: Eew64 checking'
tldr: Enforces EEW64 instruction restrictions in the RISC-V disassembler and removes
  a redundant Zve32x check in the assembler.
stakes: Ensures correct code disassembly and prevents the use of EEW64 instructions
  when the Zve64x extension is not enabled.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The new check in the disassembler adds a small performance overhead.
- Existing code that incorrectly uses EEW64 instructions without Zve64x will now produce
  an error.
exchanges: []
primer_expert: The RISC-V vector extension (RVV) allows instructions to operate on
  different element widths (EEW). EEW64 instructions require the Zve64x extension.
  The patch modifies `opcodes/riscv-dis.c` to prevent disassembly of EEW64 instructions
  without Zve64x and removes a redundant check in `gas/config/tc-riscv.c` because
  `INSN_CLASS_V` already implies Zve32x.
primer_general: RISC-V's vector extension allows for powerful SIMD-style operations
  on vectors of data. This patch makes sure that instructions that operate on 64-bit
  elements within these vectors are only used when the appropriate extension (Zve64x)
  is enabled. It also cleans up the assembler code by removing an unnecessary check.
series_id: 'binutils:risc-v: eew64 checking'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/180db539-b81a-44c4-8bb9-d6ff5065a427@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch enforces that EEW64 instructions (instructions operating on 64-bit elements within the vector register) are not disassembled or used in assembly unless the Zve64x extension is enabled. The patch updates the disassembler to check for the `INSN_V_EEW64` flag and the presence of the Zve64x extension. Additionally, it removes a redundant Zve32x check from the assembler.
