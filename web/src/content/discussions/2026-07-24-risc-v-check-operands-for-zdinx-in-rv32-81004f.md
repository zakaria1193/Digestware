---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- extension
- validation
discussion_id: 8873df38-aa72-4643-91b3-4037643b2717@suse.com
source_type: public_inbox
title: '[PATCH v4 06/12] RISC-V: check operands for Zdinx in RV32'
headline: 'RISC-V: check operands for Zdinx in RV32'
tldr: Add operand checks for the RISC-V Zdinx extension specifically for RV32.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures correct instruction encoding for Zdinx by validating register operands.
- Introduces a new macro (`RV32_EVEN_CHECK`), potentially duplicated or refactored
  later based on reuse with Zilsd.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Introduces operand checks for Zdinx in RV32, requiring register pairs
    to have the LSB clear.
  quote: 'Like for Zilsd, register pair operands are required to be encoded with the

    low bit clear. Since match functions don''t have XLEN available, introduce

    respective flags, to be used explicitly in assembler and disassembler.'
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Noted that similar checks could be applied to Zilsd, potentially reducing
    the need for some match functions. Also mentioned that scalar vector instructions
    lack similar encoding clarity, and V/Zdinx cannot be enabled together presently.
  quote: null
primer_expert: This patch adds specific operand validation for the RISC-V Zdinx ('doubleword
  integer load/store') extension in the RV32 configuration. It enforces that register
  pairs used in Zdinx instructions must have the least significant bit (LSB) clear,
  a constraint derived from the instruction encoding. This validation is implemented
  via a new macro, `RV32_EVEN_CHECK`, ensuring that incorrect register pairings are
  caught during assembly.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: Zdinx
  definition: A RISC-V extension for doubleword integer load and store instructions.
- term: RV32
  definition: The 32-bit variant of the RISC-V architecture.
- term: LSB
  definition: Least Significant Bit. The bit with the lowest value or position in
    a binary number.
- term: XLEN
  definition: The native integer width of a RISC-V processor, either 32 or 64 bits.
series_id: 'binutils:risc-v: check operands for zdinx in rv32'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8873df38-aa72-4643-91b3-4037643b2717@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch enhances the RISC-V assembler by adding operand checks for the Zdinx extension in RV32. Similar to the Zilsd extension, it enforces that register pair operands must have their least significant bit clear. This validation is implemented using a new `RV32_EVEN_CHECK` macro, ensuring correct instruction encoding for this extension.
