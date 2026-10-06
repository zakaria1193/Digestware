---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- pseudo-mnemonic
- instruction-format
discussion_id: 20261005153947.363053-68-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 20/46] s390: Add .insn pseudo-mnemonic rrd'
headline: 's390: Add .insn pseudo-mnemonic rrd'
tldr: Adds support for the RRD pseudo-mnemonic for s390 architecture.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Expands the assembler's capability to generate s390 instructions.
- Requires precise implementation of the RRD format encoding.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds support for the RRD pseudo-mnemonic, including instruction format
    definitions, documentation, and test cases.
  quote: 'Instruction format RRD has been introduced with IBM z196. [1]  It

    got separated out from RRF.  Therefore do not require any minimum

    architecture/CPU level.'
primer_expert: This patch adds support for the RRD instruction format to the s390
  assembler using the `.insn` directive. The RRD format, introduced with the IBM z196
  processor, is distinct from the RRF format. The changes involve updating the opcode
  definitions in `opcodes/s390-opc.c`, documenting the new format in `gas/doc/c-s390.texi`,
  and adding test cases in `gas/testsuite/gas/s390/` to verify its functionality.
primer_glossary:
- term: RRD
  definition: A specific instruction format in the s390 architecture, introduced with
    the z196 processor, for certain operations.
- term: RRF
  definition: Another s390 instruction format, from which RRD was separated.
- term: .insn
  definition: An assembler directive used to specify machine instructions directly,
    often with pseudo-mnemonics.
series_id: 'binutils:s390: add .insn pseudo-mnemonic rrd'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-68-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for the RRD instruction format on the s390 architecture using the `.insn` pseudo-mnemonic. The RRD format was introduced with IBM z196 and is a separate format from RRF. The changes include updating opcode definitions, documenting the format, and adding corresponding test cases.
