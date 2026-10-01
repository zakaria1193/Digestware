---
project: binutils
subsystem: s390/opcodes
patch_id: null
tags:
- s390
- architecture
- opcodes
- linker
discussion_id: 20260930081834.2948939-37-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 15/20] s390: Rename insn format RRF_F0FF to RRD_F0FF'
headline: 's390: Rename insn format RRF_F0FF to RRD_F0FF'
tldr: Renames S/390 instruction format RRF_F0FF to RRD_F0FF to match newer architecture
  specifications.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch updates the opcode definitions for the S/390 architecture.
  Specifically, it renames the instruction format `INSTR_RRF_F0FF` and `MASK_RRF_F0FF`
  to `INSTR_RRD_F0FF` and `MASK_RRD_F0FF`. This reflects a clarification in the architecture's
  principles of operation since the z196, which distinguishes between RRF and RRD
  formats based on operand placement. The changes are applied to `s390-opc.c` and
  `s390-opc.txt`, affecting instructions like `madbr` and `madr`.
primer_glossary:
- term: s390
  definition: IBM's 31-bit and 64-bit mainframe architecture.
- term: opcode
  definition: A machine language instruction.
- term: instruction format
  definition: A specific layout of bits within a machine instruction that defines
    the operation code and operand fields.
- term: RRF
  definition: A type of S/390 instruction format that includes register and fixed-point
    fields.
- term: RRD
  definition: A type of S/390 instruction format, distinguished from RRF, used for
    certain instructions.
series_id: 'binutils:s390: rename insn format rrf_f0ff to rrd_f0ff'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-37-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch renames the S/390 instruction format RRF_F0FF to RRD_F0FF. This change reflects a separation of instruction formats in the architecture since IBM z196, where the RRF format (with the first operand in bits 16-19) has been distinguished into the RRD format. The opcode definitions and related text files are updated accordingly.
