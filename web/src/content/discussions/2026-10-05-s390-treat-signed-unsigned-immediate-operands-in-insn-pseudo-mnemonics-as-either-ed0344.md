---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- .insn
- operands
- fixups
discussion_id: 20261005153947.363053-56-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 08/46] s390: Treat signed/unsigned immediate operands in .insn pseudo-mnemonics
  as either'
headline: 's390: Treat signed/unsigned immediate operands in .insn pseudo-mnemonics
  as either'
tldr: Handle mixed signed/unsigned immediate operands in s390 .insn pseudo-mnemonics.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new PSEUDO_MNEMONIC instruction flag to distinguish this special range
  check, potentially increasing the instruction flag space.
- Modifies the fixup data structure to store pointers, increasing its size but simplifying
  operand handling.
exchanges: []
primer_expert: This change in gas for s390 enables the correct range checking for
  immediate operands within .insn pseudo-mnemonics. It uses the PSEUDO_MNEMONIC flag
  to signal a mixed signed/unsigned range check in s390_insert_operand, passing opcode
  pointers for context. Fixup data now stores both opcode and operand pointers to
  facilitate this, removing reliance on operand index encoding in relocation types.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: fixup
  definition: A placeholder in assembled code that needs to be resolved later, typically
    by the linker, to a correct address or value based on symbolic information.
- term: operand
  definition: A value or symbol that an instruction operates on.
- term: range check
  definition: Verifying that a given value falls within a specified minimum and maximum
    boundary.
series_id: 'binutils:s390: treat signed/unsigned immediate operands in .insn pseudo-mnemonics
  as either'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-56-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch modifies the s390 gas assembler to correctly handle immediate operands in .insn pseudo-mnemonics, which can be either signed or unsigned depending on the instruction. It introduces a new flag and modifies the operand range check to accommodate this, storing opcode and operand pointers for fixup processing. This change also cleans up how operand indices are handled in fixup data.
