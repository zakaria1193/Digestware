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
discussion_id: 20261005153947.363053-86-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 38/46] s390: Add .insn pseudo-mnemonics ss_a/b/c/d/e/f'
headline: 's390: Add .insn pseudo-mnemonics ss_a/b/c/d/e/f'
tldr: Adds gas test cases and support for various SS format pseudo-mnemonics on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add pseudo-mnemonics for SS instruction formats to
    the s390 gas assembler and includes corresponding test cases.
  quote: 'While at it improve the ESA/390 .insn pseudo-mnemonic test so that one

    can understand how the SS-a instruction MVC can be pieced together using

    .insn ss, which is format SS-d.'
primer_expert: This patch introduces pseudo-mnemonics for various SS instruction formats
  (ss_a through ss_f) into the s390 GNU Assembler (gas). It adds entries to `s390-opc.c`
  and extends the gas test suites (`esa-operands` and `zarch-operands`) with tests
  for these mnemonics, improving the assembler's support for S/390 and z/Architecture
  instructions.
primer_glossary:
- term: SS instruction format
  definition: A format for System/370 and later IBM mainframe instructions that typically
    involve two operands, each specifying a register and a displacement, used for
    string operations.
- term: MVC
  definition: A common S/390 instruction (Move Character) that copies a block of storage
    from a source to a destination.
- term: .insn
  definition: A GNU Assembler directive that allows embedding raw machine instructions
    or pseudo-mnemonics, useful for testing or specific instruction generation.
- term: pseudo-mnemonic
  definition: An assembly language construct that resembles a machine instruction
    but is processed by the assembler to generate one or more actual machine instructions
    or to represent a complex instruction format.
series_id: 'binutils:s390: add .insn pseudo-mnemonics ss_a/b/c/d/e/f'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-86-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch enhances the s390 GNU Assembler (gas) by adding support for multiple pseudo-mnemonics corresponding to the SS instruction format (ss_a through ss_f). It updates the opcode definitions and introduces comprehensive test cases in both ESA/390 and z/Architecture suites to verify assembly and disassembly for these new mnemonics.
