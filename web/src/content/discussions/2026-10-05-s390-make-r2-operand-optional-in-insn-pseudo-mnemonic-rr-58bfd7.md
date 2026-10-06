---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction-format
- optional-operand
discussion_id: 20261005153947.363053-67-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 19/46] s390: Make R2 operand optional in .insn pseudo-mnemonic rr'
headline: 's390: Make R2 operand optional in .insn pseudo-mnemonic rr'
tldr: Makes the R2 operand optional for the .insn rr pseudo-mnemonic in the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Increases assembler flexibility by allowing more compact instruction representations.
- Requires careful testing to ensure correct parsing of both present and absent R2
  operands.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Makes the R2 operand optional for the .insn rr pseudo-mnemonic and adds
    corresponding tests and documentation.
  quote: 'The RR instruction format has an optional R2 field.  Make the R2

    operand in the .insn pseudo-mnemonic rr optional.'
primer_expert: This change modifies the gas (GNU Assembler) support for the s390 architecture,
  specifically concerning the `.insn` directive and the 'rr' (Register-Register) pseudo-mnemonic.
  The RR instruction format in s390 architecture permits an optional second register
  operand (R2). This patch updates the opcode definitions and documentation (`s390-opc.c`,
  `c-s390.texi`) to reflect this optionality for the `.insn rr` pseudo-mnemonic, enhancing
  flexibility for assembly code generation, and adds relevant test cases.
primer_glossary: []
series_id: 'binutils:s390: make r2 operand optional in .insn pseudo-mnemonic rr'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-67-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch modifies the s390 assembler's handling of the `.insn rr` pseudo-mnemonic to make the R2 operand optional. This aligns with the RR instruction format's optional R2 field. The changes include documentation updates and new test cases for both ESA/390 and z/Architecture operand formats.
