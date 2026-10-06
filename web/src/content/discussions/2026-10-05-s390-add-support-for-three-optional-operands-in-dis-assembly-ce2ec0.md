---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- assembler
- disassembler
- instruction-formats
discussion_id: 20261005153947.363053-57-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 09/46] s390: Add support for three optional operands in dis-/assembly'
headline: 's390: Add support for three optional operands in dis-/assembly'
tldr: Enhances s390 assembler and disassembler to support .insn pseudo-mnemonics with
  up to three optional operands.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in operand parsing logic for optional operands.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds support for .insn pseudo-mnemonics with three optional trailing operands
    by defining new flags and updating gas and opcodes components.
  quote: null
primer_expert: This patch modifies the s390 backend of GNU Binutils (gas and opcodes)
  to correctly parse and format instructions that can have up to three optional operands,
  as specified by formats like VRR-a and VRR-c. It introduces new flags and updates
  logic in `tc-s390.c` and `s390-dis.c` to accommodate this.
primer_glossary:
- term: .insn
  definition: An assembler directive that allows direct insertion of machine instructions
    using their opcode and operands, often used for undefined or specialized instructions.
- term: pseudo-mnemonic
  definition: A symbolic name used in assembly language that corresponds to a machine
    instruction or a sequence of instructions, often used for convenience or to represent
    complex operations.
- term: VRR variants
  definition: Specific instruction formats within the s390 architecture (e.g., VRR-a,
    VRR-c) that handle register-to-register operations and can have varying numbers
    of optional operands.
series_id: 'binutils:s390: add support for three optional operands in dis-/assembly'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-57-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for instruction formats with up to three optional operands for s390 pseudo-mnemonics in the GNU Assembler. It defines new flags `S390_INSTR_FLAG_OPTPARM3` and `S390_INSTR_FLAG_OPTPARM_MASK` and updates `gas`, `opcodes`, and `include` files to handle these extended operand capabilities, specifically for VRR variants.
