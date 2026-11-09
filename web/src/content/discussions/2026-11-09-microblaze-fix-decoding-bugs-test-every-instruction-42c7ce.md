---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- binutils
- microblaze
- disassembler
- decoder
- testing
discussion_id: 20261109040811.26266-1-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 0/7] microblaze: fix decoding bugs, test every instruction'
headline: 'MicroBlaze: fix decoding bugs, test every instruction'
tldr: Fixes four instruction decoding bugs in MicroBlaze binutils and adds a test
  for all instructions.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Manual maintenance of the opcode table is error-prone, necessitating automated tests
  for comprehensive coverage.
- Ensuring ABI compatibility and correct behavior across different tools (objdump,
  simulator, GDB) requires careful handling of instruction decoding.
exchanges:
- author: Samuel Price <thesamprice@gmail.com>
  role: proposer
  position: Submits a series of patches to fix instruction decoding bugs in the MicroBlaze
    binutils. The series also adds a test to cover every instruction, addressing inaccuracies
    in objdump and the simulator.
  quote: The MicroBlaze opcode table in opcodes/microblaze-opc.h is written by hand,
    and the gas testsuite checks the disassembly of only 26 of its 278 instructions.
    This series fixes four decoding bugs in the table and the disassembler, explains
    some mbar forms, removes one instruction that no documentation defines, and adds
    a test that covers every instruction.
primer_expert: This series targets the MicroBlaze's instruction decoding logic within
  binutils, specifically within `opcodes/microblaze-opc.h`. The bugs affect how `objdump`
  and the bundled simulator (`sim/microblaze`) interpret certain instructions due
  to errors in the manually maintained opcode table. The fix ensures correct disassembly
  and simulation, with a new test suite aiming for 100% instruction coverage.
primer_glossary:
- term: MicroBlaze
  definition: A soft processor core from Xilinx, commonly used in FPGAs. Binutils
    provides tools like the assembler (gas), disassembler (objdump), and debugger
    (GDB) for this architecture.
- term: opcode table
  definition: A data structure used by assemblers and disassemblers to map instruction
    mnemonics and their operands to their binary representations (opcodes), and vice
    versa.
- term: disassembler
  definition: A tool (like objdump) that converts machine code (binary instructions)
    back into human-readable assembly language.
- term: simulator
  definition: A program that mimics the behavior of a hardware processor, allowing
    software to be run and tested without the actual hardware. In this context, it
    refers to the MicroBlaze simulator integrated with binutils.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    code into machine code.
- term: objdump
  definition: A GNU Binutils tool that displays information from object files, including
    disassembly of the code sections.
series_id: 'binutils:microblaze: fix decoding bugs, test every instruction'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-1-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This series addresses four bugs in the MicroBlaze instruction decoder and disassembler within binutils. The hand-written opcode table has been corrected, improving the accuracy of objdump and the integrated simulator. A new test suite has been added to cover all 278 instructions, aiming to catch regressions.
