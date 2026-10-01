---
project: binutils
subsystem: s390/opcodes
patch_id: null
tags:
- s390
- architecture
- opcodes
- linker
discussion_id: 20260930081834.2948939-41-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 19/20] s390: Rename insn format VRR_0VVU to VRI_0VVU'
headline: 's390: Rename insn format VRR_0VVU to VRI_0VVU'
tldr: Renames S/390 instruction format VRR_0VVU to VRI_0VVU to correct an earlier
  misclassification.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch rectifies a misnaming of an instruction format for the S/390
  architecture. The macro `INSTR_VRR_0VVU` (and its corresponding mask) is renamed
  to `INSTR_VRI_0VVU`. This correction aligns the format with the VRI-l specification,
  as it was erroneously tagged as VRR in a previous commit related to arch15 instructions.
  The change impacts the `s390-opc.c` and `s390-opc.txt` files, specifically for the
  `vtz` instruction.
primer_glossary:
- term: s390
  definition: IBM's 31-bit and 64-bit mainframe architecture.
- term: opcode
  definition: A machine language instruction.
- term: instruction format
  definition: A specific layout of bits within a machine instruction that defines
    the operation code and operand fields.
- term: VRR
  definition: A type of S/390 instruction format typically involving vector registers.
- term: VRI
  definition: A type of S/390 instruction format typically involving vector registers
    and immediate values.
series_id: 'binutils:s390: rename insn format vrr_0vvu to vri_0vvu'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-41-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch corrects the naming of an S/390 instruction format, renaming VRR_0VVU to VRI_0VVU. The change aligns the format name with the official specification, as it was previously misclassified as VRR instead of VRI in an earlier commit. The opcode definitions and text files are updated accordingly for the `vtz` instruction.
