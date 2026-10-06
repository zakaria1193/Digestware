---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- documentation
- instruction-format
discussion_id: 20261005153947.363053-54-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 06/46] s390: Document operand ordering rules for .insn directive'
headline: 's390: Document operand ordering rules for .insn directive'
tldr: Documents operand ordering rules for the .insn directive in the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves user understanding of the `.insn` directive.
- Standardizes operand entry, potentially simplifying parser logic.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Documents the general rules for ordering operands in the .insn directive
    for s390.
  quote: 'Document that operands for the .insn directive are to be specified in

    asceding order of their field indices as listed in the Principles of

    Operation manuals.  Composite operands, such as Dx(Bx), Dx(Lx,Bx), and

    Dx(Xx,Bx), are treated as a single operand and share the same index.

    Exceptions to the ascending index order are noted in the respective

    format descriptions.'
primer_expert: This commit adds detailed documentation to the s390 assembler's manual
  (`gas/doc/c-s390.texi`) regarding the operand ordering for the `.insn` directive.
  It clarifies that operands should generally be listed in ascending order of their
  field indices as defined in the architecture's Principles of Operation manuals.
  It also specifies how composite operands (like `Dx(Bx)`) are treated and notes that
  exceptions to the ordering rules exist for certain formats.
primer_glossary:
- term: .insn
  definition: An assembler directive used to specify machine instructions directly,
    often with pseudo-mnemonics.
- term: field indices
  definition: Numerical identifiers assigned to different parts of an instruction
    format in the architecture manuals, used here to determine operand order.
- term: composite operands
  definition: Operands that consist of multiple parts, such as a displacement and
    a base register (e.g., D2(B2)).
series_id: 'binutils:s390: document operand ordering rules for .insn directive'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-54-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch documents the operand ordering rules for the `.insn` directive in the s390 assembler. Operands should generally follow the ascending order of their field indices as specified in the Principles of Operation manuals, with exceptions noted. Composite operands are treated as single units for indexing. This documentation improves clarity and usability of the `.insn` directive.
