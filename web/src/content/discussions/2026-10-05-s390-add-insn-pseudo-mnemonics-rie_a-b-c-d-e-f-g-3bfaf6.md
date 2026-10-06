---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- tests
- instructions
- assembler
discussion_id: 20261005153947.363053-64-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 16/46] s390: Add .insn pseudo-mnemonics rie_a/b/c/d/e/f/g'
headline: 's390: Add .insn pseudo-mnemonics rie_a/b/c/d/e/f/g'
tldr: Adds gas test cases and support for various RIE instruction formats on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add support for RIE pseudo-mnemonics (rie_a to rie_g)
    to the s390 gas assembler, detailing their history and requirements.
  quote: 'History of instruction format RIE:

    - RIE-e got initially introduced as RIE with IBM z900. [1, 2]

    - RIE-a/b/c and RIE-f got introduced with IBM z10. [3]

    - RIE-d got introduced with IBM z196. [4]

    - RIE-g got introduced with IBM z13. [5]'
primer_expert: This patch adds support for RIE instruction formats (Register and Index
  Extension) to the s390 GNU Assembler (gas) via pseudo-mnemonics 'rie_a' through
  'rie_g'. It defines specific instruction formats and operand orders in `opcodes/s390-opc.c`
  and adds tests to `gas/testsuite/gas/s390/zarch-operands.d/s` to cover the evolution
  of RIE formats across different IBM mainframe architectures (z900, z10, z196, z13).
primer_glossary:
- term: RIE
  definition: Register and Index Extension, a type of instruction format in IBM s/390
    architectures that uses registers for addressing and index components, with variations
    introduced over different hardware generations.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
series_id: 'binutils:s390: add .insn pseudo-mnemonics rie_a/b/c/d/e/f/g'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-64-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for seven variations of the RIE (Register and Index Extension) instruction format in the s390 GNU Assembler (gas), denoted by pseudo-mnemonics rie_a through rie_g. It updates opcode definitions with specific instruction formats and operand ordering, and adds corresponding tests to the gas test suite to ensure correct assembly and disassembly for different hardware generations.
