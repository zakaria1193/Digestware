---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- performance
discussion_id: a74cc7bb-09e6-9906-d6d1-66e129edf38f@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 03/28] aarch64: Cleanup add/sub immediate decode'
headline: 'aarch64: Cleanup add/sub immediate decode'
tldr: Improves AArch64 ADD/SUB immediate decoding by using a specific bit, avoiding
  linear scans.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves decoding speed by reducing lookup complexity.
- Increases decoder accuracy by using a more specific bit check.
exchanges: []
primer_expert: This patch modifies `opcodes/aarch64-dis-2.c` to refine the decoding
  logic for AArch64 ADD and SUB instructions that use immediate operands. It introduces
  a check against bit 23 of the instruction word as part of the mask, enabling the
  decoder to differentiate these opcodes more effectively. This avoids a fallback
  linear scan through opcode table entries, speeding up disassembly.
primer_glossary:
- term: Immediate Operand
  definition: An operand whose value is specified directly within the instruction
    itself, rather than being fetched from a register or memory location.
- term: Opcode Mask
  definition: A bitmask used during instruction decoding to isolate specific bits
    of the instruction word that determine the instruction's operation or format.
- term: AArch64
  definition: The 64-bit ARM architecture instruction set.
- term: Disassembler
  definition: A program that translates machine code (binary instructions) back into
    human-readable assembly language.
series_id: 'binutils:aarch64: cleanup add/sub immediate decode'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a74cc7bb-09e6-9906-d6d1-66e129edf38f@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch enhances the AArch64 instruction decoder by incorporating bit 23 into the mask for ADD/SUB immediate instructions. This change allows the decoder to more accurately distinguish between similar opcodes, preventing a linear scan through multiple table entries and improving decoding performance.
