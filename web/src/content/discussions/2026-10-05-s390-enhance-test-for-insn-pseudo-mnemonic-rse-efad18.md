---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- documentation
- testing
discussion_id: 20261005153947.363053-73-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 25/46] s390: Enhance test for .insn pseudo-mnemonic rse'
headline: 's390: Enhance test for .insn pseudo-mnemonic rse'
tldr: Enhances the test for the .insn rse pseudo-mnemonic by documenting its operand
  order.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves clarity for users of the `.insn rse` directive.
- Enhances test robustness by explicitly covering operand order exceptions.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Documents the specific operand order for the RSE pseudo-mnemonic and enhances
    associated tests.
  quote: 'For historic reasons the .insn rse pseudo-mnemonic operand order differs

    from the field index order.  Document that.'
primer_expert: 'This commit addresses a specific aspect of the s390 assembler''s `.insn`
  directive: the RSE (Register-to-Register, Storage, and Environment) instruction
  format. It documents that the operand order for the `.insn rse` pseudo-mnemonic
  deviates from the general rule of ascending field indices due to historical reasons.
  The changes involve updating the s390 assembler manual (`gas/doc/c-s390.texi`) and
  refining the test cases in `gas/testsuite/gas/s390/` to reflect this exception.'
primer_glossary:
- term: RSE
  definition: A s390 instruction format (Register-to-Register, Storage, and Environment).
- term: .insn
  definition: An assembler directive used to specify machine instructions directly,
    often with pseudo-mnemonics.
- term: field index order
  definition: The standard order of operands based on their numerical field indices
    in the instruction format, as defined in architecture manuals.
series_id: 'binutils:s390: enhance test for .insn pseudo-mnemonic rse'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-73-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch enhances the test coverage for the `.insn rse` pseudo-mnemonic by documenting its operand order, which differs from the standard field index order due to historical reasons. The changes update the s390 assembler's documentation (`gas/doc/c-s390.texi`) and improve test cases in `gas/testsuite/gas/s390/`.
