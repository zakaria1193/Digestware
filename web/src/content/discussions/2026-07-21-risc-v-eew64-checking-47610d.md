---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- extensions
- binutils
- assembler
- disassembler
discussion_id: CAHT-pJywaC76VOWGdEFbKVDkTLxcij0fLmJyAN86V+4rPuay=A@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3 02/13] RISC-V: EEW64 checking'
headline: 'RISC-V: EEW64 checking'
tldr: Discussion on correct handling of RISC-V Zve64x extension checks in assembler
  and disassembler.
proposer: Nelson Chu <nelson.chu1990@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Simplifies checks by introducing a new instruction class, potentially improving
  maintainability.
exchanges:
- author: Nelson Chu
  role: proposer
  position: Agrees with simplifying checks and suggests using `INSN_CLASS_ZVE64X`
    as a better approach.
  quote: 'make sense.


    I forgot, probably just because people argued they want to

    dis-assembler old objects for segment load/store with EEW64 but

    without zve64x since this check may be added later that, but it

    doesn''t matter now.  I think using a new INSN_CLASS_ZVE64X should be

    the right way to go.'
- author: Jan Beulich
  role: reviewer
  position: Suggests that the disassembler should also use the INSN_V_EEW64 flag and
    that Zve32x checks are redundant. Questions the use of a flag when a new instruction
    class could be used.
  quote: 'Like the assembler, the disassembler should also use the INSN_V_EEW64

    flag. Respectively marked insns shouldn''t be disassembled normally when

    Zve64x isn''t enabled.


    While there also drop the redundant Zve32x check from gas: All affected

    insns are INSN_CLASS_V, which means Zve32x was already checked to be

    enabled (both V and Zve64x imply Zve32x).


    Question is why a flag was used in the first place…'
primer_expert: This thread discusses refining the handling of RISC-V vector extension
  (V) checks in binutils. Jan Beulich proposes that the disassembler should align
  with the assembler by using the INSN_V_EEW64 flag and eliminate redundant checks
  for Zve32x. Nelson Chu agrees, suggesting a new `INSN_CLASS_ZVE64X` would be a cleaner
  approach for distinguishing instructions requiring the Zve64x extension, especially
  for segment load/store operations.
primer_glossary:
- term: RISC-V
  definition: An open-source Instruction Set Architecture (ISA) that is modular and
    extensible.
- term: Zve64x
  definition: A RISC-V extension that provides 64-bit vector processing capabilities.
- term: Zve32x
  definition: A RISC-V extension that provides 32-bit vector processing capabilities.
- term: EEW64
  definition: Element Extended Width 64. Refers to scalar data types with 64-bit width
    within RISC-V vector operations.
- term: Assembler
  definition: A program that translates assembly language into machine code.
- term: Disassembler
  definition: A program that translates machine code back into assembly language.
- term: INSN_V_EEW64
  definition: A flag or indicator used in binutils to denote instructions related
    to 64-bit element width in vector operations.
- term: INSN_CLASS_V
  definition: A classification used in binutils for instructions belonging to the
    RISC-V vector extension.
series_id: 'binutils:risc-v: eew64 checking'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHT-pJywaC76VOWGdEFbKVDkTLxcij0fLmJyAN86V+4rPuay=A@mail.gmail.com
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

This discussion addresses the correct implementation of checks for the RISC-V Zve64x extension in binutils' assembler and disassembler. Jan Beulich points out that the disassembler should also use the INSN_V_EEW64 flag and questions the redundancy of Zve32x checks. Nelson Chu agrees with this, suggesting that a new `INSN_CLASS_ZVE64X` would be a more appropriate way to handle these checks, aligning with the assembler's logic and simplifying the code.
