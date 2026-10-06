---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- documentation
- instruction format
discussion_id: 20261005153947.363053-48-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 00/46] s390: Complete .insn pseudo-mnemonics'
headline: 's390: Complete .insn pseudo-mnemonics'
tldr: Adds all s390 instruction formats to .insn pseudo-mnemonics and improves documentation.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures consistency with architecture manual but may require users to adapt existing
  assembly code if operand order was previously assumed differently.
exchanges: []
primer_expert: This patch series adds comprehensive support for s390 instruction formats
  via the .insn pseudo-mnemonic in GNU as. It defines operand orderings for various
  instruction formats (e.g., RSL-b) based on the Principles of Operations manual,
  handling register, immediate, and composite operands. This impacts how users can
  express complex or less common s390 instructions in assembly, ensuring consistency
  with the architecture specification.
primer_glossary:
- term: .insn
  definition: A GNU assembler (gas) pseudo-mnemonic that allows specifying machine
    instructions directly, often with operands defined by fields like R#, D#, B#,
    M#, etc.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction
    but is not a direct opcode; it's a directive to the assembler.
- term: z/Architecture Principles of Operations
  definition: The official manual detailing the instruction set architecture, instruction
    formats, and operational behavior of IBM's z/Architecture mainframe processors.
series_id: 'binutils:s390: complete .insn pseudo-mnemonics'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-48-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This series completes the .insn pseudo-mnemonics for all s390 instruction formats and their variants, documenting their operand order according to the z/Architecture Principles of Operations manual. It also enhances the documentation for the .insn directive itself. The changes aim to provide a more complete and accurate way to specify instructions using pseudo-mnemonics in assembly code.
