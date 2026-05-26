---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- disassembler
- ARC-V APEX
- custom instructions
discussion_id: 20260525133052.1885254-3-luiss@synopsys.com
source_type: public_inbox
title: '[PATCH 2/2] RISC-V: Add ARC-V APEX disassembler support'
headline: 'RISC-V: Add support for ARC-V APEX disassembler'
tldr: This patch adds disassembler support for ARC-V APEX instructions by reading
  metadata from ELF sections.
proposer: Luis Silva <Luis.Silva1@synopsys.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Dynamically allocating memory for `riscv_opcode` entries adds complexity and potential
  memory management issues.
- Reading and processing metadata at startup may increase startup time.
exchanges:
- author: Luis Silva
  role: proposer
  position: Proposes adding ARC-V APEX disassembler support by reading metadata from
    ELF sections.
  quote: 'Add disassembler support for ARC-V APEX instructions by reading metadata
    from

    .riscvapex.* ELF sections (emitted by GAS) and reconstructing instruction

    definitions at startup.'
primer_expert: This patch adds ARC-V APEX disassembler support. It reads metadata
  from `.riscvapex.*` ELF sections, emitted by the assembler, and reconstructs instruction
  definitions at startup.  The disassembler uses this metadata to decode APEX instructions
  when the standard opcode table fails.
primer_general: A disassembler translates machine code back into human-readable assembly
  code. This patch extends the RISC-V disassembler to support ARC-V APEX, a feature
  that allows custom instructions. The disassembler reads information about these
  custom instructions (metadata) embedded in the compiled program to correctly translate
  them back into assembly code.
series_id: 'binutils:risc-v: add arc-v apex disassembler support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260525133052.1885254-3-luiss@synopsys.com
bugzilla_url: null
date: '2026-05-25'
is_stub: false
---

This patch adds support to the RISC-V disassembler for ARC-V APEX instructions. The disassembler reads metadata from `.riscvapex.*` ELF sections (emitted by the assembler) to reconstruct instruction definitions at startup. The metadata is deserialized into a lookup table, and the disassembler attempts to decode instructions using this table when the standard opcode table produces no match.
