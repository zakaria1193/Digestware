---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- binutils
- opcode
- alias
discussion_id: de2b284f-5c7c-1d6f-f520-ad38388ead8a@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 4/5] aarch64: Remove disassembly restriction on OP_MOV_Z_Zi'
headline: 'aarch64: Remove disassembly restriction on OP_MOV_Z_Zi'
tldr: Removes a disassembly restriction on the OP_MOV_Z_Zi opcode and updates alias
  priority for AArch64.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the aarch64 disassembler (`opcodes/aarch64-dis-2.c`
  and `include/opcode/aarch64.h`) to remove a restriction on the `OP_MOV_Z_Zi` opcode.
  The opcode is related to SVE (Scalable Vector Extension) and alias selection during
  disassembly.
primer_general: This patch modifies the binutils disassembler for the AArch64 architecture.
  It removes a restriction and updates alias priority during the disassembly of `OP_MOV_Z_Zi`
  opcode. Instructions in a given architecture can often be expressed in multiple
  ways; this change impacts how the disassembler prefers one form over another.
series_id: 'binutils:aarch64: remove disassembly restriction on op_mov_z_zi'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/de2b284f-5c7c-1d6f-f520-ad38388ead8a@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

This patch removes an artificial restriction on disassembling the `OP_MOV_Z_Zi` opcode in the aarch64 disassembler.  The restriction was intended to force a different alias to be used for disassembly when the index value was zero.  The patch now uses alias priority to achieve the same result, and removes the unused `OP_MOV_Z_Zi` enum value.
