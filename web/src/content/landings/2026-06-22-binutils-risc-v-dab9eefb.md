---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- vendor extension
- assembly
- disassembly
- matrix operations
commit_hash: dab9eefbe337d7855a16c0468954c9b7367f8d10
source_type: public_inbox
author: Jeff Law <law@sourceware.org>
headline: Binutils adds support for SpacemiT’s XsmtVdot RISC-V extension
tldr: Binutils now supports the SpacemiT Vector Dot Product (XsmtVdot) extension,
  enabling assembly and disassembly of these specialized matrix operations for the
  Sp…
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit adds support for a new vendor-specific RISC-V extension,
  XsmtVdot, to GNU Binutils. Specifically, it involves modifying `gas/config/tc-riscv.c`
  to recognize and assemble the new instructions, `opcodes/riscv-opc.h` and `opcodes/riscv-opc.c`
  for instruction definitions and disassembly, and `bfd/elfxx-riscv.c` for ELF object
  file handling related to the new extension. Toolchain developers will interact with
  `riscv-opc.h` for instruction decoding in other components.
primer_general: This update to Binutils, a collection of tools used for working with
  computer programs, adds support for a new set of instructions designed by SpacemiT
  for their RISC-V processors, called the XsmtVdot extension. RISC-V is a type of
  open-standard computer chip architecture. These new instructions are specialized
  for matrix operations, which are common in artificial intelligence and machine learning
  tasks. When you write a program, a compiler translates your code into instructions
  the processor can understand. Binutils then helps with the next steps, like assembling
  these instructions into an executable file and disassembling them back into a human-readable
  format. This change means that developers can now write and analyze programs using
  these new SpacemiT-specific matrix instructions for compatible RISC-V chips, allowing
  for more efficient execution of certain workloads.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260622164807.61A664BA5439@sourceware.org
date: '2026-06-22'
is_stub: false
---

This update to Binutils integrates the SpacemiT Vector Dot Product (XsmtVdot) extension, a subset of the Intrinsic Matrix Extension (IME) specification. This support enables developers to assemble and disassemble code utilizing these specific matrix operations, targeting the SpacemiT X60 processor. The change includes updates to the assembler, disassembler, and ELF object file handling for RISC-V.
