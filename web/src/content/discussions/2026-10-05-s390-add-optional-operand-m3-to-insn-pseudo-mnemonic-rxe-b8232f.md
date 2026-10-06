---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- instruction-format
- optional-operand
discussion_id: 20261005153947.363053-78-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 30/46] s390: Add optional operand M3 to .insn pseudo-mnemonic rxe'
headline: 's390: Add optional operand M3 to .insn pseudo-mnemonic rxe'
tldr: Makes the M3 mask operand optional for the .insn rxe pseudo-mnemonic in the
  s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Increases the flexibility of the `.insn rxe` directive.
- Requires careful validation to ensure correct parsing with and without the M3 operand.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Makes the M3 operand optional for the .insn rxe pseudo-mnemonic and adds
    corresponding tests and documentation.
  quote: 'The RXE instruction format has an optional M3 mask field.  Add this

    mask operand to the pseudo-mnemonic rxe as optional to enable coding

    of all operands in a backward compatible manner.'
primer_expert: This patch enhances the s390 support in GNU Assembler (gas) by making
  the M3 mask operand optional for the `.insn rxe` (RX Extension) pseudo-mnemonic.
  This change ensures that the assembler can correctly handle instructions where the
  M3 field is omitted, providing backward compatibility as specified by the RXE instruction
  format. The updates include changes to opcode definitions, assembler documentation,
  and the addition of test cases.
primer_glossary: []
series_id: 'binutils:s390: add optional operand m3 to .insn pseudo-mnemonic rxe'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-78-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch makes the M3 mask operand optional for the `.insn rxe` pseudo-mnemonic in the s390 assembler, allowing for backward-compatible coding of all operands. This aligns with the RXE instruction format's optional M3 field. The changes include documentation updates and new test cases for both ESA/390 and z/Architecture operand formats.
