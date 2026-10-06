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
discussion_id: 20261005153947.363053-75-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 27/46] s390: Add .insn pseudo-mnemonics rsl_a/b'
headline: 's390: Add .insn pseudo-mnemonics rsl_a/b'
tldr: Adds gas test cases and support for RSL pseudo-mnemonics (rsl_a, rsl_b) on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add pseudo-mnemonics for RSL instruction formats (rsl_a,
    rsl_b) to the s390 gas assembler, detailing their history and requirements.
  quote: 'History of instruction format RSL:

    - RSL-a got initially introduced as RSL. [1, 2, 3]

    - RSL-b got introduced with IBM zEC12. [4]'
primer_expert: This patch introduces pseudo-mnemonics 'rsl_a' and 'rsl_b' for the
  RSL (Register and Storage List) instruction format into the s390 GNU Assembler (gas).
  It adds these to `opcodes/s390-opc.c` and includes tests in `gas/testsuite/gas/s390/zarch-operands.d/s`
  to cover the introduction of RSL-b with the zEC12 architecture.
primer_glossary:
- term: RSL instruction format
  definition: A type of instruction format in IBM mainframe architectures used for
    operations involving registers and storage, with variations like RSL-a and RSL-b
    introduced over different hardware generations.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
series_id: 'binutils:s390: add .insn pseudo-mnemonics rsl_a/b'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-75-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces two new pseudo-mnemonics, rsl_a and rsl_b, for the RSL instruction format in the s390 GNU Assembler (gas). It updates opcode definitions with specific instruction formats and requires the respective minimum architecture/CPU levels. Test cases are added to the z/Architecture operand test suite to ensure accurate assembly and disassembly.
