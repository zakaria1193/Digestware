---
project: binutils
subsystem: opcodes
patch_id: null
tags:
- binutils
- opcodes
- rx
- isa
- disassembler
discussion_id: 20261029120303.1987315-2-yoshinori.sato@nifty.com
source_type: public_inbox
title: 'opcodes: Add RXv3e instructions'
headline: 'opcodes: Add RXv3e instructions'
tldr: Adds support for new instructions from the RXv3e ISA to the binutils opcodes
  library.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases the size and complexity of the opcodes database and decoder logic.
- Requires regeneration of decoder C files, which can be an involved process.
exchanges: []
primer_expert: This patch adds support for the RXv3e instruction set architecture
  (ISA) to the binutils opcodes component. It involves updating the instruction definition
  files (`rx-decode.opc`) and regenerating the decoder (`rx-decode.c`), as well as
  updating the disassembler's register names (`rx-dis.c`) to accommodate the new instructions
  and control registers introduced in this ISA revision.
primer_glossary:
- term: opcodes
  definition: The part of a machine language instruction that specifies the operation
    to be performed. In the context of binutils, this refers to the component responsible
    for understanding and translating assembly instructions.
- term: RXv3e
  definition: A specific version or extension of the RX instruction set architecture,
    likely introduced by Renesas.
- term: ISA
  definition: Instruction Set Architecture. The set of commands and instructions that
    a particular processor can understand and execute.
- term: Disassembler
  definition: A program that translates machine code (binary instructions) back into
    assembly language, making it human-readable.
series_id: 'binutils:rx: bfd rx-linux fdpic support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029120303.1987315-2-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch updates the opcodes library within binutils to include support for new instructions introduced in the RXv3e ISA. It modifies the instruction decoder and disassembler configurations, specifically `rx-decode.opc` and `rx-decode.c`, to recognize and correctly disassemble these new instructions, as well as updates register names in `rx-dis.c`.
