---
project: binutils
subsystem: s390/opcodes
patch_id: null
tags:
- s390
- architecture
- opcodes
- linker
discussion_id: 20260930081834.2948939-40-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 18/20] s390: Rename insn format RRR_FE0FEFE to RRF_FE0FEFE'
headline: 's390: Rename insn format RRR_FE0FEFE to RRF_FE0FEFE'
tldr: Renames the S/390 instruction format RRR_FE0FEFE to RRF_FE0FEFE to reflect architectural
  changes.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch renames an instruction format definition within the S/390
  opcode table. The `INSTR_RRR_FE0FEFE` and `MASK_RRR_FE0FEFE` macros in `s390-opc.c`
  are being renamed to `INSTR_RRF_FE0FEFE` and `MASK_RRF_FE0FEFE`, respectively. This
  reflects a change in the S/390 architecture, where the RRR format has been subsumed
  by RRF-a on newer processors like the z196. The corresponding entries in `s390-opc.txt`
  are also updated to use the new format name for specific instructions.
primer_glossary:
- term: s390
  definition: IBM's 31-bit and 64-bit mainframe architecture.
- term: opcode
  definition: A machine language instruction.
- term: instruction format
  definition: A specific layout of bits within a machine instruction that defines
    the operation code and operand fields.
- term: RRR
  definition: A type of S/390 instruction format where all operands are registers.
- term: RRF
  definition: A type of S/390 instruction format that includes register and fixed-point
    fields.
series_id: 'binutils:s390: rename insn format rrr_fe0fefe to rrf_fe0fefe'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-40-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch renames the S/390 instruction format RRR_FE0FEFE to RRF_FE0FEFE. The change is motivated by architectural updates where the RRR format has been effectively merged into the RRF-a format since the IBM z196 processor. This renaming ensures that the opcode definitions accurately represent the current instruction set architecture.
