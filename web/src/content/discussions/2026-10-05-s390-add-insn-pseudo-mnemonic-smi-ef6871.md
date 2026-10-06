---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- gas
- s390
- assembler
- instruction format
discussion_id: 20261005153947.363053-85-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 37/46] s390: Add .insn pseudo-mnemonic smi'
headline: 's390: Add .insn pseudo-mnemonic smi'
tldr: Adds support for the SMI instruction format via the .insn pseudo-mnemonic in
  the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds support for a new instruction format.
- Requires users to target specific processor levels.
exchanges: []
primer_expert: This patch adds a new pseudo-mnemonic, `smi`, to the s390 assembler's
  `.insn` directive support, located in `opcodes/s390-opc.c`. The SMI format is a
  machine instruction format introduced in the IBM zEC12. The change ensures that
  the assembler can correctly encode and generate machine code for instructions using
  this format, requiring that the target architecture meets the zEC12 level or higher.
  Documentation in `gas/doc/c-s390.texi` and new test cases are included.
primer_glossary:
- term: .insn
  definition: An assembler pseudo-mnemonic that allows embedding raw machine instructions
    using their format and opcode.
- term: pseudo-mnemonic
  definition: An assembler directive that represents a machine instruction or a sequence
    of instructions using a symbolic name.
- term: s390
  definition: IBM's mainframe and enterprise server architecture.
- term: zEC12
  definition: IBM zEnterprise EC12, a specific model of IBM's mainframe processors.
- term: SMI format
  definition: A specific instruction encoding format for the s390 architecture, introduced
    with the zEC12.
series_id: 'binutils:s390: add .insn pseudo-mnemonic smi'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-85-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for the SMI instruction format, which was introduced with the IBM zEC12 processor, into the s390 assembler using the `.insn` pseudo-mnemonic. It requires the respective minimum architecture or CPU level. The changes involve adding the format to `s390-opc.c`, documenting it in `gas/doc/c-s390.texi`, and adding corresponding tests in the gas testsuite.
