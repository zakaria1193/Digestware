---
project: binutils
subsystem: s390
patch_id: null
tags:
- documentation
- s390
- gas
discussion_id: 20261005153947.363053-50-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 02/46] s390: Enhance documentation of instruction operands'
headline: 's390: Enhance documentation of instruction operands'
tldr: Update s390 assembler documentation for instruction operands.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- No technical tradeoffs, purely documentation.
exchanges: []
primer_expert: This commit updates gas/doc/c-s390.texi to refine the description of
  instruction operands for the s390 architecture. It adds mentions of vector registers
  and clarifies the R field and RXB field for register identification. The documentation
  for storage operands also sees minor adjustments. This is a documentation-only change
  for the assembler.
primer_glossary: []
series_id: 'binutils:s390: enhance documentation of instruction operands'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-50-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch enhances the documentation for s390 instruction operands in the GAS assembler. It clarifies the types of registers that can be used and provides more detail on how operands are specified, particularly for register and storage operands. This aims to improve clarity and accuracy for developers working with s390 assembly.
