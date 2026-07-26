---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- MIPS
- disassembler
- opcode
- floating point
discussion_id: amTYLdrTAhjBPlZ3@freefall.freebsd.org
source_type: public_inbox
title: '[Patch] MIPS opcodes: fix transposed FS and FT in vadda and vmsuba'
headline: 'MIPS opcodes: fix transposed FS and FT in vadda and vmsuba'
tldr: Fixes a bug in MIPS opcodes where the order of source operands FS and FT was
  transposed in vadda and vmsuba instructions.
proposer: '"Piotr P. Stefaniak" <pstef@freebsd.org>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Correcting the operand order fixes incorrect calculations but requires updating
  the opcode definitions.
- Ensuring accurate instruction decoding is critical for disassemblers and emulators
  to correctly represent and process MIPS code.
exchanges:
- author: Piotr P. Stefaniak <pstef@freebsd.org>
  role: proposer
  position: Submits a patch to correct the order of FS and FT operands in MIPS VLIW
    instructions vadda and vmsuba, explaining the impact on calculation correctness.
  quote: 'Of the 36 three-operand ACC-destination VU0 macro-mode entries in

    `opcodes/mips-opc.c`, all but two list FS before FT.  The two exceptions

    are vadda and vmsuba.


    For `vmsuba` this reversal silently changes results. The PS2 multiplier

    is not symmetric in its two source fields: the Booth recoder consumes FT

    while FS is shifted, so `vf[fs] * vf[ft]` and `vf[ft] * vf[fs]` differ

    by one ULP.'
primer_expert: This patch corrects a subtle but significant bug in the MIPS opcode
  definitions used by the binutils disassembler and possibly emulator/assembler. The
  `vadda` and `vmsuba` instructions, part of the MIPS VLIW (Very Long Instruction
  Word) extensions for the PS2, incorrectly implemented the order of their two floating-point
  source operands (FS and FT). This resulted in incorrect calculations due to the
  asymmetric nature of the underlying Booth recoder used in the multiplication step.
primer_glossary:
- term: MIPS
  definition: Microprocessor without Interlocked Pipeline Stages. A RISC instruction
    set architecture widely used in embedded systems and formerly popular in workstations
    and servers.
- term: opcodes
  definition: Operation codes. The part of a machine language instruction that specifies
    the operation to be performed.
- term: vadda
  definition: A MIPS VLIW (Very Long Instruction Word) instruction likely related
    to vector addition of floating-point values, utilizing multiple source registers.
- term: vmsuba
  definition: A MIPS VLIW (Very Long Instruction Word) instruction likely related
    to vector subtraction and addition, involving multiple source and destination
    registers.
- term: FS, FT
  definition: Source registers 'FS' and 'FT' in MIPS VLIW instructions, specifying
    operands for arithmetic or vector operations.
- term: ULP
  definition: Unit in the Last Place. The smallest possible difference between two
    floating-point numbers. A difference of one ULP indicates a minimal error in floating-point
    computation.
- term: Booth recoder
  definition: An algorithm used in hardware for fast multiplication, particularly
    of signed two's complement numbers. Its asymmetry means operand order can affect
    results.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/amTYLdrTAhjBPlZ3@freefall.freebsd.org
bugzilla_url: null
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

A patch addresses a bug in the MIPS opcode definitions within `opcodes/mips-opc.c` where the source operands FS and FT were transposed in the `vadda` and `vmsuba` instructions. This transposition causes incorrect results in some cases because the PS2 multiplier is not symmetric and the order matters for the Booth recoder, leading to a one ULP difference.
