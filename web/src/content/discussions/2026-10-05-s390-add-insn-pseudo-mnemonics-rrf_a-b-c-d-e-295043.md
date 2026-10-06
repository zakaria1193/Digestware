---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- assembler
- instruction-formats
- documentation
discussion_id: 20261005153947.363053-70-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 22/46] s390: Add .insn pseudo-mnemonics rrf_a/b/c/d/e'
headline: 's390: Add .insn pseudo-mnemonics rrf_a/b/c/d/e'
tldr: Adds s390 assembler support for RRF instruction format variants (rrf_a/b/c/d/e)
  and fixes related test cases.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Handling the unique operand order and optional operand specification for the RRF
  format requires careful implementation.
- Ensuring backward compatibility with older RRF formats while supporting extensions.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds pseudo-mnemonics rrf_a/b/c/d/e to opcodes/s390-opc.c and documents
    them in gas/doc/c-s390.texi, while also fixing and adding test cases in gas/testsuite/gas/s390.
  quote: null
primer_expert: This patch adds support for the RRF instruction format and its variants
  (rrf_a through rrf_e) as '.insn' pseudo-mnemonics in the s390 GNU Assembler. It
  correctly implements the specified operand order and optional operands for RRF,
  which is unique in its documentation of this aspect. The patch also fixes existing
  ESA/390 tests and adds new z/Architecture tests for these instructions. The RRF
  format, originating before the z900, was later extended with an optional M4 mask.
primer_glossary:
- term: .insn
  definition: An assembler directive that allows direct insertion of machine instructions
    using their opcode and operands, often used for undefined or specialized instructions.
- term: pseudo-mnemonic
  definition: A symbolic name used in assembly language that corresponds to a machine
    instruction or a sequence of instructions, often used for convenience or to represent
    complex operations.
- term: RRF format
  definition: A s390 instruction format that includes register-to-register operations,
    with specific rules for operand ordering and optional operands.
- term: z/Architecture
  definition: IBM's 64-bit enterprise architecture, an evolution of the System/360
    and System/370 lineage.
series_id: 'binutils:s390: add .insn pseudo-mnemonics rrf_a/b/c/d/e'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-70-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for the RRF instruction format variants (rrf_a, rrf_b, rrf_c, rrf_d, rrf_e) as '.insn' pseudo-mnemonics in the s390 GNU Assembler. It addresses special operand ordering and optional operands defined in the RRF format, as per the z/Architecture specification. The changes include updates to opcode definitions, documentation, and test cases for both ESA/390 and z/Architecture assemblers. Notably, RRF format predates z900 and was extended with an optional M4 mask field.
