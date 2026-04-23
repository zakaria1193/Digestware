---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vector extension
- disassembler
- assembler
- EEW64
discussion_id: 180db539-b81a-44c4-8bb9-d6ff5065a427@suse.com
source_type: public_inbox
title: '[PATCH 05/19] RISC-V: EEW64 checking'
headline: 'RISC-V: EEW64 checking'
tldr: The disassembler should respect the INSN_V_EEW64 flag, and the assembler's redundant
  Zve32x check is removed.
stakes: Ensures correct disassembly and assembly of RISC-V vector instructions with
  EEW64 (Element Encoding Width of 64 bits) when the Zve64x extension is enabled.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Ensures correct disassembly of EEW64 instructions.
- Removes redundant check in the assembler, simplifying the code.
exchanges: []
primer_expert: This patch modifies both the assembler (`gas/config/tc-riscv.c`) and
  disassembler (`opcodes/riscv-dis.c`) to handle EEW64 vector instructions correctly.
  It ensures that the disassembler doesn't disassemble EEW64 instructions when the
  `Zve64x` extension isn't enabled, and it removes a redundant check in the assembler
  because `Zve64x` implies `Zve32x`.
primer_general: This patch focuses on the RISC-V vector extension, specifically the
  handling of EEW64 (Element Encoding Width of 64 bits) instructions. It modifies
  the assembler and disassembler to ensure that these instructions are correctly processed
  based on the enabled extensions. The changes ensure that the disassembler only disassembles
  EEW64 instructions when the `Zve64x` extension is enabled, and removes a redundant
  check to simplify the code.
series_id: 'binutils:risc-v: eew64 checking'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/180db539-b81a-44c4-8bb9-d6ff5065a427@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch ensures that the RISC-V disassembler uses the `INSN_V_EEW64` flag to determine if an instruction should be disassembled when the Zve64x extension is not enabled. The patch also removes a redundant `Zve32x` check from the assembler.
