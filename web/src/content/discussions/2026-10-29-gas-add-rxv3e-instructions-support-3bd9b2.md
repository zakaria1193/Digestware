---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- embedded
- instruction-set
discussion_id: 20261029115244.1979808-1-yoshinori.sato@nifty.com
source_type: public_inbox
title: '[PATCH 0/2] Renesas RX Add RXv3e instruction support'
headline: 'gas: Add RXv3e instructions support'
tldr: Add support for new instructions in the Renesas RXv3e architecture to the GNU
  assembler.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in assembler and opcode library code.
- Maintenance overhead for new instruction set support.
exchanges:
- author: Yoshinori Sato <yoshinori.sato@nifty.com>
  role: proposer
  position: Proposes adding support for RXv3e instructions to gas and libopcodes.
  quote: 'Renesas has released RXv3e as an extended instruction set for

    the RX architecture.


    Details are provided in the manual below.

    https://www.renesas.com/ja/document/mas/rx-family-rxv3e-instruction-set-architecture-software-manual?language=en&r=25627634


    These are the changes to support the instructions added in RXv3e within `gas`
    and `libopcodes`.'
primer_expert: This patch series extends the GNU assembler (gas) and libopcodes to
  support the Renesas RXv3e ISA. Changes involve updating RX-specific definition files
  (e.g., `rx-defs.h`, `rx-parse.y`) and decoding/disassembly logic (`opcodes/rx-decode.c`,
  `opcodes/rx-dis.c`) to recognize and handle new instructions and control registers.
  This ensures that binaries targeting RXv3e can be correctly assembled and disassembled.
primer_glossary:
- term: RXv3e
  definition: An extended instruction set architecture for Renesas' RX microcontrollers.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils, which translates assembly
    language code into machine code.
- term: libopcodes
  definition: A library within GNU Binutils that provides functionality for decoding
    and disassembling machine code.
- term: Control Register
  definition: Special-purpose registers used to control the behavior of the processor
    or specific features of the architecture.
series_id: binutils:renesas rx add rxv3e instruction support
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029115244.1979808-1-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch series introduces support for the RXv3e instruction set extensions to the GNU assembler (gas) and the libopcodes library. The changes include updates to instruction parsing, definition files, and test cases to accommodate the new instructions and control registers introduced in RXv3e.
