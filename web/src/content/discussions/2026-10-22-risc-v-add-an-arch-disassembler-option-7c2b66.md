---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- disassembler
- option
- elf
discussion_id: 20261022154350.235360-1-khaidari.fg@gmail.com
source_type: public_inbox
title: '[PATCH] RISC-V: add an "arch=" disassembler option'
headline: 'RISC-V: Add an "arch=" disassembler option.'
tldr: Adds an 'arch=' option to the RISC-V disassembler to specify the ISA when the
  object file lacks this information.
proposer: Farid Khaidari <khaidari.fg@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enables disassembly for objects lacking architecture attributes, but relies on user
  input for correct ISA specification.
exchanges:
- author: Farid Khaidari
  role: proposer
  position: Proposes adding an 'arch=' option to the RISC-V disassembler to handle
    objects lacking architecture attributes.
  quote: 'The disassembler uses the ISA from the object''s architecture attribute,

    or rv64gc if there is none.  Some objects cannot carry the attribute.

    A core file is one, and only the program that loads it knows the ISA.


    Add an "arch=" option that overrides the ISA recorded in the object.'
primer_expert: This patch adds a disassembler option for RISC-V to specify the Instruction
  Set Architecture (ISA) when the object file itself (e.g., a core dump or raw binary)
  doesn't contain the necessary ELF architecture attribute. This complements GDB's
  ability to analyze such files by providing the disassembler with the correct ISA
  context.
primer_glossary:
- term: disassembler
  definition: A program that translates machine code (binary instructions) into a
    human-readable assembly language representation.
- term: ISA
  definition: Instruction Set Architecture. Defines the set of instructions that a
    particular processor can execute.
- term: RISC-V
  definition: An open-source instruction set architecture based on RISC principles,
    gaining popularity for its modularity and extensibility.
- term: core file
  definition: A file generated when a program crashes, containing a snapshot of the
    program's memory and state at the time of the crash.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261022154350.235360-1-khaidari.fg@gmail.com
bugzilla_url: null
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

This patch introduces an 'arch=' option for the RISC-V disassembler. This option is crucial for disassembling object files that do not contain architecture information, such as core files or raw binaries, allowing the user to specify the ISA explicitly. The new option overrides the default ISA and is designed to work in conjunction with GDB for analyzing core files without the associated executable.
