---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- opcode table
- qualifier
- cleanup
discussion_id: 15683b9f-7c37-5151-9e32-d19de10bca5c@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 15/23] aarch64: Remove excess operand qualifiers'
headline: 'Aarch64: Remove excess operand qualifiers'
tldr: Remove unused qualifiers from instruction qualifier sequences in the opcode
  table.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Reduces the size of the opcode table slightly.
- Improves code readability by removing unnecessary information.
exchanges: []
primer_expert: The AArch64 opcode table (`opcodes/aarch64-tbl.h`) defines the structure
  of AArch64 instructions, including their operands and associated qualifiers. This
  patch removes redundant qualifiers from instructions where the qualifier sequence
  was longer than the number of operands, cleaning up the table.
primer_general: Assemblers use tables to define the valid structure of machine instructions.
  This patch cleans up the instruction definitions by removing extra, unused information
  about the expected format of operands.  This doesn't change how the assembler works,
  but makes the internal tables simpler and easier to understand.
series_id: 'binutils:aarch64: remove excess operand qualifiers'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/15683b9f-7c37-5151-9e32-d19de10bca5c@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch removes excess operand qualifiers from the opcode table for certain AArch64 instructions. Some instructions had qualifier sequences longer than the number of operands they actually use. Removing these unused qualifiers simplifies the instruction definitions and reduces potential confusion, with minimal functional impact.
