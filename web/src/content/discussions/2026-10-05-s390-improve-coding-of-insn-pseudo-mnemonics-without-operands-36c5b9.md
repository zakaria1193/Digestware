---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- gas
- s390
- assembler
- syntax
discussion_id: 20261005153947.363053-58-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 10/46] s390: Improve coding of .insn pseudo-mnemonics without operands'
headline: 's390: Improve coding of .insn pseudo-mnemonics without operands'
tldr: Allows omitting the trailing comma in .insn pseudo-mnemonics when all operands
  are optional, improving syntax for s390 assembly.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Slightly more flexible syntax.
- Backward compatible, existing code with trailing comma still works.
exchanges: []
primer_expert: This patch modifies `gas/config/tc-s390.c` to relax the syntax requirement
  for s390 `.insn` pseudo-mnemonics. Specifically, it allows omitting the comma that
  traditionally follows the opcode constant when all operands are optional and absent.
  This change, located within the `s390_insn` function, simplifies the syntax for
  certain s390 instructions, such as `rre` and `s`, by removing the need for a trailing
  comma (e.g., `.insn RRE,0x,` becomes `.insn RRE,0x`). This is a prerequisite for
  fully optional operands in these mnemonics, aligning with the architecture specification.
primer_glossary:
- term: .insn
  definition: An assembler pseudo-mnemonic that allows embedding raw machine instructions
    using their format and opcode.
- term: pseudo-mnemonic
  definition: An assembler directive that represents a machine instruction or a sequence
    of instructions using a symbolic name.
- term: s390
  definition: IBM's mainframe and enterprise server architecture.
- term: optional operands
  definition: Operands for an instruction or pseudo-mnemonic that are not required
    and can be omitted, often controlled by the instruction format or specific flags.
series_id: 'binutils:s390: improve coding of .insn pseudo-mnemonics without operands'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-58-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch enhances the s390 assembler's handling of the `.insn` pseudo-mnemonic by allowing the omission of the trailing comma when all operands are optional and none are provided. Previously, a trailing comma was required even when no operands were specified (e.g., `.insn INSN-FMT,OPCODE,`). The change simplifies the syntax to `.insn INSN-FMT,OPCODE`, making it more natural and aligning with future changes to make all operands optional for `rre` and `s` mnemonics. It also generalizes the logic for handling `.insn` mnemonics with no operands.
