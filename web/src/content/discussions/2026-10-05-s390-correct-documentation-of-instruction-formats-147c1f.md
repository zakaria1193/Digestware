---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- documentation
- instruction-formats
discussion_id: 20261005153947.363053-51-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 03/46] s390: Correct documentation of instruction formats'
headline: 's390: Correct documentation of instruction formats'
tldr: Corrects the documentation for s390 RIS and RSI instruction formats, adjusting
  bit positions and instruction lengths.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Corrects the bit field definition for the RIS instruction format and the
    byte length for the RSI instruction format in the documentation.
  quote: null
primer_expert: This patch rectifies documentation errors in `gas/doc/c-s390.texi`
  concerning s390 instruction formats. It corrects the bit positioning for the secondary
  opcode in the RIS format (bits 40-47 instead of 36-47) and sets the correct byte
  length for the RSI format to 4 bytes, based on the 'IBM z/Architecture Principles
  of Operation' documentation.
primer_glossary:
- term: RIS format
  definition: A s390 instruction format that uses a specific bit layout for its opcode
    and operands.
- term: RSI format
  definition: A s390 instruction format that includes register and immediate operands,
    with a specified byte length.
- term: bit position
  definition: The specific location (bit index) of a field within a machine instruction's
    binary representation.
series_id: 'binutils:s390: correct documentation of instruction formats'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-51-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch corrects inaccuracies in the GNU Assembler's documentation for the s390 architecture's RIS and RSI instruction formats. Specifically, it adjusts the bit position of the second opcode field in the RIS format to bits 40-47 and corrects the instruction length of the RSI format to 4 bytes, ensuring documentation aligns with the IBM z/Architecture Principles of Operation.
