---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- embedded
- instruction-set
discussion_id: 20261029115244.1979808-3-yoshinori.sato@nifty.com
source_type: public_inbox
title: '[PATCH 2/2] gas: Add RXv3e instructions support'
headline: 'gas: Add RXv3e instructions support'
tldr: Adds new RXv3e instructions to the GNU assembler, updating relevant definition
  and test files.
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
  position: Submits a patch to add RXv3e instruction support to gas.
  quote: 'Add support for the instructions introduced in RXv3e.


    gas/config/

    * rx-defs.h(rx_cpu_type): Add type RXV3E and split RXDFPU.

    * rx-parse.y(INT): Add RXv3e enhancement operand.

    * (PUSHC): Add RXv3e control register.

    * (POPC): Likewise.

    * (MVFC): Likewise.

    * (MVTC): Likewise.

    * (MVTIPL): Expand interrupt level.

    * (TRCALL): New.

    * (TRMVFC): New.

    * (TRMVTC): New.

    * (TRRTE): New.

    * (token_table): Add…'
primer_expert: This patch series extends the GNU assembler (gas) and libopcodes to
  support the Renesas RXv3e ISA. Changes involve updating RX-specific definition files
  (e.g., `rx-defs.h`, `rx-parse.y`) and decoding/disassembly logic (`opcodes/rx-decode.c`,
  `opcodes/rx-decode.opc`) to recognize and handle new instructions and control registers.
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
series_id: 'binutils:gas: add rxv3e instructions support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029115244.1979808-3-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch adds support for the instructions introduced in the RXv3e architecture to the GNU assembler (gas). It modifies configuration files, definition files, and test cases to recognize and correctly handle the new instructions and associated enhancements like control registers.
