---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- gas
- s390
- assembler
- instruction format
discussion_id: 20261005153947.363053-69-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 21/46] s390: Make R1 and R2 operands optional in .insn pseudo-mnemonic
  rre'
headline: 's390: Make R1 and R2 operands optional in .insn pseudo-mnemonic rre'
tldr: Makes the R1 and R2 operands optional for the s390 .insn pseudo-mnemonic 'rre',
  aligning it with the instruction format.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Better alignment between assembler syntax and hardware instruction format.
- Increased syntax flexibility for the RRE instruction.
exchanges: []
primer_expert: This patch updates `opcodes/s390-opc.c` and related test files to make
  the R1 and R2 operands optional for the `.insn` pseudo-mnemonic `rre` on s390. The
  RRE instruction format itself has optional R1 and R2 fields. This change ensures
  the assembler correctly handles cases where these operands are omitted, improving
  syntax flexibility and adherence to the specification. Documentation in `gas/doc/c-s390.texi`
  and new test cases for ESA/390 and z/Arch are included.
primer_glossary:
- term: .insn
  definition: An assembler pseudo-mnemonic that allows embedding raw machine instructions
    using their format and opcode.
- term: pseudo-mnemonic
  definition: An assembler directive that represents a machine instruction or a sequence
    of instructions using a symbolic name.
- term: s390
  definition: IBM's mainframe and enterprise server architecture.
- term: optional operands
  definition: Operands for an instruction or pseudo-mnemonic that are not required
    and can be omitted, often controlled by the instruction format or specific flags.
- term: RRE format
  definition: A specific instruction encoding format for the s390 architecture, likely
    related to register-to-register operations.
series_id: 'binutils:s390: make r1 and r2 operands optional in .insn pseudo-mnemonic
  rre'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-69-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch modifies the s390 assembler to make the R1 and R2 operands optional in the `.insn` pseudo-mnemonic for the RRE instruction. This change aligns the assembler's syntax with the RRE instruction format, which specifies R1 and R2 as optional fields. The patch also updates documentation and adds corresponding test cases for both ESA/390 and z/Architecture variants.
