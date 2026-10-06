---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- tests
- assembler
discussion_id: 20261005153947.363053-87-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 39/46] s390: Add test for .insn pseudo-mnemonic sse'
headline: 's390: Add test for .insn pseudo-mnemonic sse'
tldr: Adds gas test cases and documentation for the .insn sse pseudo-mnemonic on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add test cases for the .insn sse pseudo-mnemonic in
    the s390 gas assembler.
  quote: While at it add comments to ESA/390 .insn pseudo-mnemonic test.
primer_expert: This patch adds test cases for the '.insn sse' pseudo-mnemonic in the
  s390 GNU Assembler (gas). It extends the esa-operands and zarch-operands test suites
  by adding definitions and expected outputs for this specific instruction format,
  ensuring correct assembly and disassembly.
primer_glossary:
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
- term: SSE
  definition: A specific instruction format in IBM s/390 architectures, often used
    for string operations.
series_id: 'binutils:s390: add test for .insn pseudo-mnemonic sse'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-87-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds test cases and documentation for the .insn sse pseudo-mnemonic to the s390 GNU Assembler (gas) test suite. The changes update the ESA/390 and z/Architecture operand test files to include specific examples for this mnemonic, ensuring proper assembly and disassembly behavior.
