---
project: binutils
subsystem: s390/opcodes
patch_id: null
tags:
- s390
- architecture
- opcodes
- linker
discussion_id: 20260930081834.2948939-36-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 14/20] s390: vlr uses instruction format VRR'
headline: 's390: vlr uses instruction format VRR'
tldr: Corrects the S/390 `vlr` instruction to use the VRR_VV format instead of the
  erroneous VRX_VV.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch corrects the opcode definition for the `vlr` instruction
  on S/390. Previously, it was associated with the `INSTR_VRX_VV` format. This change
  updates it to use the `INSTR_VRR_VV` format, which is the correct format according
  to the architecture's principles of operation for the `vlr` instruction. The `INSTR_VRX_VV`
  and `MASK_VRX_VV` definitions are removed as they are no longer valid for this instruction.
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
- term: VRX
  definition: A type of S/390 instruction format, now considered erroneous for the
    'vlr' instruction.
series_id: 'binutils:s390: vlr uses instruction format vrr'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-36-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch corrects the instruction format used for the S/390 `vlr` instruction. It updates the opcode definitions to specify that `vlr V1,V2` uses the VRR_VV format, not the previously incorrectly assigned VRX_VV. The erroneous VRX_VV definition is removed from the opcode implementation.
