---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- opcodes
- maintenance
- code-style
discussion_id: 20261005153947.363053-49-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 01/46] s390: Sort .insn pseudo-mnemonics table alphabetically'
headline: 's390: Sort .insn pseudo-mnemonics table alphabetically'
tldr: Alphabetizes the .insn pseudo-mnemonics table in the s390 opcode definitions
  and adds a header comment.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Sorts the s390_opformats table alphabetically and adds a header comment
    to opcodes/s390-opc.c.
  quote: null
primer_expert: This patch tidies up the `s390_opformats` array in `opcodes/s390-opc.c`
  by sorting the entries alphabetically. It also adds a descriptive header comment
  to the array definition. This is a maintenance change to improve code organization
  and readability without altering functional behavior.
primer_glossary:
- term: .insn
  definition: An assembler directive that allows direct insertion of machine instructions
    using their opcode and operands, often used for undefined or specialized instructions.
- term: pseudo-mnemonic
  definition: A symbolic name used in assembly language that corresponds to a machine
    instruction or a sequence of instructions, often used for convenience or to represent
    complex operations.
series_id: 'binutils:s390: sort .insn pseudo-mnemonics table alphabetically'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-49-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch applies a purely mechanical change to the s390 opcode definitions within the GNU Assembler by sorting the `.insn` pseudo-mnemonics table alphabetically. Additionally, it adds a header comment to the table for improved readability and maintainability. This change aims to standardize the internal representation of instruction formats.
