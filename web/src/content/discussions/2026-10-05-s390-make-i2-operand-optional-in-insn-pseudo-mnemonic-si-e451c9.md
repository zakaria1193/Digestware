---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction-format
- optional-operand
discussion_id: 20261005153947.363053-82-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 34/46] s390: Make I2 operand optional in .insn pseudo-mnemonic si'
headline: 's390: Make I2 operand optional in .insn pseudo-mnemonic si'
tldr: Makes the I2 immediate operand optional for the .insn si pseudo-mnemonic in
  the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Provides greater flexibility in generating s390 SI instructions.
- Adds complexity to the parser by handling optional fields.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Makes the I2 operand optional for the .insn si pseudo-mnemonic and adds
    corresponding tests and documentation.
  quote: 'The SI instruction format has an optional I2 field.  Make the I2

    operand in the .insn pseudo-mnemonic si optional.'
primer_expert: This patch enhances the s390 support in GNU Assembler (gas) by making
  the I2 immediate operand optional for the `.insn si` (Store Immediate) pseudo-mnemonic.
  This change aligns the assembler's behavior with the SI instruction format's specification,
  which allows for an optional I2 field. It involves updating opcode definitions,
  assembler documentation, and adding test cases to ensure correct handling of both
  optional and required I2 operands.
primer_glossary: []
series_id: 'binutils:s390: make i2 operand optional in .insn pseudo-mnemonic si'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-82-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch makes the I2 immediate operand optional for the `.insn si` pseudo-mnemonic in the s390 assembler, aligning with the SI instruction format's optional I2 field. This change improves flexibility in assembly coding. It includes documentation updates and new test cases for both ESA/390 and z/Architecture operand formats.
