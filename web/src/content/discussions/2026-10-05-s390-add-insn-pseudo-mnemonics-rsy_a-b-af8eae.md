---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- pseudo-mnemonic
- instruction-format
discussion_id: 20261005153947.363053-76-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 28/46] s390: Add .insn pseudo-mnemonics rsy_a/b'
headline: 's390: Add .insn pseudo-mnemonics rsy_a/b'
tldr: Adds support for RSY-a and RSY-b pseudo-mnemonics for s390 architecture.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Expands the assembler's instruction set coverage for s390.
- Requires careful implementation to match the precise encoding of RSY-a and RSY-b.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds support for RSY-a and RSY-b pseudo-mnemonics, including instruction
    format definitions, documentation, and test cases.
  quote: 'Instruction format RSY got added with IBM z990. [1]


    Require the respective minimum architecture/CPU level.


    While at it add a z/Architecture test for .insn rsy pseudo-mnemonic.'
primer_expert: This patch adds assembler support for two new s390 instruction formats,
  RSY-a and RSY-b, using the `.insn` directive. The RSY format was introduced with
  the IBM z990 processor. The changes include defining the encoding for these formats
  in `opcodes/s390-opc.c`, documenting their operand order in `gas/doc/c-s390.texi`,
  and providing verification tests in the `gas/testsuite/gas/s390/` directory.
primer_glossary: []
series_id: 'binutils:s390: add .insn pseudo-mnemonics rsy_a/b'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-76-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for the RSY-a and RSY-b instruction formats on the s390 architecture using the `.insn` pseudo-mnemonic. The RSY instruction format was added with IBM z990. The changes involve defining the instruction format in `opcodes/s390-opc.c`, documenting it in `gas/doc/c-s390.texi`, and adding test cases in `gas/testsuite/gas/s390/`.
