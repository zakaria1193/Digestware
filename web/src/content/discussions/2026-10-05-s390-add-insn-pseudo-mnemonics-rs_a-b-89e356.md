---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- tests
- assembler
- instructions
discussion_id: 20261005153947.363053-72-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 24/46] s390: Add .insn pseudo-mnemonics rs_a/b'
headline: 's390: Add .insn pseudo-mnemonics rs_a/b'
tldr: Adds gas test cases and support for RS pseudo-mnemonics (rs_a, rs_b) on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add pseudo-mnemonics for RS instruction formats (rs_a,
    rs_b) to the s390 gas assembler and includes corresponding test cases and documentation
    updates.
  quote: While at it add comments to the ESA/390 .insn pseudo-mnemonic test.
primer_expert: This patch adds pseudo-mnemonics 'rs_a' and 'rs_b' for the RS (Register
  and Storage) instruction format to the s390 GNU Assembler (gas). It defines the
  instruction formats and operand orders in `opcodes/s390-opc.c` and enhances the
  `gas/testsuite/gas/s390/esa-operands.d/s` and `zarch-operands.d/s` test cases to
  cover these new mnemonics.
primer_glossary:
- term: RS instruction format
  definition: A common instruction format in IBM mainframe architectures, typically
    involving register operands and a displacement/base register for memory access.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
series_id: 'binutils:s390: add .insn pseudo-mnemonics rs_a/b'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-72-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces two new pseudo-mnemonics, rs_a and rs_b, for the RS instruction format in the s390 GNU Assembler (gas). It updates opcode definitions to include the specific instruction formats and operand ordering for these variations and adds corresponding tests to the ESA/390 and z/Architecture operand test suites to ensure accurate assembly and disassembly.
