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
discussion_id: 20261005153947.363053-77-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 29/46] s390: Add .insn pseudo-mnemonics rx_a/b'
headline: 's390: Add .insn pseudo-mnemonics rx_a/b'
tldr: Adds gas test cases and support for RX pseudo-mnemonics (rx_a, rx_b) on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add pseudo-mnemonics for RX instruction formats (rx_a,
    rx_b) to the s390 gas assembler and includes corresponding test cases.
  quote: While at it add a z/Architecture test for .insn rx pseudo-mnemonic.
primer_expert: This patch adds pseudo-mnemonics 'rx_a' and 'rx_b' for the RX (Register
  and Index) instruction format to the s390 GNU Assembler (gas). It updates the opcode
  definitions in `opcodes/s390-opc.c` and extends the `gas/testsuite/gas/s390/esa-operands.d/s`
  and `zarch-operands.d/s` test cases to cover these new mnemonics.
primer_glossary:
- term: RX instruction format
  definition: A common instruction format in IBM mainframe architectures, typically
    involving a register and an index register with a displacement for memory access.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
series_id: 'binutils:s390: add .insn pseudo-mnemonics rx_a/b'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-77-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces two new pseudo-mnemonics, rx_a and rx_b, for the RX instruction format in the s390 GNU Assembler (gas). It updates opcode definitions and adds corresponding test cases to the ESA/390 and z/Architecture operand test suites to ensure accurate assembly and disassembly for these instruction variations.
