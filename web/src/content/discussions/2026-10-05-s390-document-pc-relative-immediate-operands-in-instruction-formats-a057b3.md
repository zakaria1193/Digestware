---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- documentation
- instruction-formats
discussion_id: 20261005153947.363053-53-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 05/46] s390: Document PC-relative immediate operands in instruction
  formats'
headline: 's390: Document PC-relative immediate operands in instruction formats'
tldr: Updates s390 instruction format documentation to use 'RIx' for PC-relative immediate
  operands in RIE, RIL, and RSI formats.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Introduces 'RIx' notation for PC-relative immediate operands in the documentation
    for RIE, RIL, and RSI instruction formats.
  quote: null
primer_expert: This patch updates the s390 assembler's documentation (`gas/doc/c-s390.texi`)
  to standardize the representation of PC-relative immediate operands. It introduces
  the `RIx` notation (e.g., `RI2`) to denote signed PC-relative immediates used in
  instruction formats like RIE, RIL, and RSI, improving clarity and consistency with
  the z/Architecture specification.
primer_glossary:
- term: PC-relative immediate
  definition: An immediate value in an instruction that is calculated relative to
    the current value of the Program Counter (PC).
- term: RIE format
  definition: A s390 instruction format that includes register and PC-relative immediate
    operands.
- term: RIL format
  definition: A s390 instruction format that includes a register and a PC-relative
    immediate operand.
- term: RSI format
  definition: A s390 instruction format that includes register and PC-relative immediate
    operands.
series_id: 'binutils:s390: document pc-relative immediate operands in instruction
  formats'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-53-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch enhances the GNU Assembler's documentation for the s390 architecture by introducing the 'RIx' (Relative Immediate) notation for PC-relative immediate operands. This change applies to instruction formats like RIE, RIL, and RSI, ensuring clearer and more accurate documentation that aligns with the z/Architecture Principles of Operation.
