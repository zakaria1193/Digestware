---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- .insn
- instruction-set
- mainframe
discussion_id: 20261005153947.363053-89-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 41/46] s390: Add .insn pseudo-mnemonics vri_a/b/c/d/e/f/g/h/i/j/k/l'
headline: 's390: Add .insn pseudo-mnemonics vri_a/b/c/d/e/f/g/h/i/j/k/l'
tldr: Add support for various s390 VRI instruction formats using .insn.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch introduces support for twelve variations of the VRI instruction
  format (vri_a through vri_l) in the s390 GNU Assembler (gas) using the '.insn' pseudo-mnemonic.
  It defines these formats, including specific operand orderings for VRI-c, in opcodes/s390-opc.c,
  and adds corresponding tests to gas/testsuite/gas/s390/zarch-operands.d/.s, referencing
  historical introduction dates on IBM z/Architecture processors.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: VRI
  definition: A specific instruction format in the s390 architecture, with various
    sub-types introduced across different processor generations.
- term: z13, z14, z17
  definition: IBM mainframe processor generations that introduced different versions
    of the VRI instruction format.
series_id: 'binutils:s390: add .insn pseudo-mnemonics vri_a/b/c/d/e/f/g/h/i/j/k/l'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-89-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This series of patches adds support for numerous variations of the VRI instruction format (vri_a through vri_l) to the s390 gas assembler using the '.insn' directive. Each variant corresponds to different processor generations (z13, z14, z17), and the patches include updates to opcode definitions, documentation, and test suites.
