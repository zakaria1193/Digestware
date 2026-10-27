---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- binutils
- refactoring
- ISA
- cleanup
discussion_id: 20261027034041.1667435-5-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 4/5] RISC-V: Remove the privileged spec classes'
headline: 'RISC-V: Remove the privileged spec classes'
tldr: Removes outdated privileged spec classes and related code from binutils for
  RISC-V.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removes code related to version checking for privileged specs, simplifying the codebase.
- Assumes a stable 1.13 privileged spec version, removing flexibility for potential
  future variations but reducing complexity for current common usage.
exchanges:
- author: Kito Cheng
  role: proposer
  position: Submits patch 4/5 to remove obsolete privileged specification classes
    and associated code from binutils for RISC-V, as the version is now stable at
    1.13.
  quote: The privileged spec is always 1.13 now, and no remaining CSR depends on the
    privileged spec version.  So remove PRIV_SPEC_CLASS_*, the riscv_priv_specs table
    and riscv_get_priv_spec_class_from_numbers.
primer_expert: This patch simplifies the RISC-V support in binutils by removing obsolete
  privileged specification class definitions (`PRIV_SPEC_CLASS_*`). The rationale
  is that the privileged ISA specification version is now stable at 1.13, and no CSRs
  are sensitive to older versions. This eliminates the need for version checking in
  the assembler and disassembler, and updates related code in GDB and binutils/dwarf.c
  where `DECLARE_CSR` usage has changed.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that allows for modularity
    and extensibility.
- term: privileged spec
  definition: Refers to the specification defining the privileged architecture modes
    and features of the RISC-V ISA, including memory management and access control.
- term: CSR
  definition: Control and Status Register. Special registers in a processor used for
    system control, status monitoring, and configuration.
- term: assembler
  definition: A program that translates assembly language into machine code.
- term: disassembler
  definition: A program that translates machine code back into assembly language.
- term: dwarf.c
  definition: A source file likely related to DWARF (Debugging With Attributed Record
    Formats) debugging information, used by compilers and debuggers.
- term: DECLARE_CSR
  definition: A macro or function used in code to declare or define a Control and
    Status Register.
series_id: 'binutils:risc-v: remove the privileged spec classes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261027034041.1667435-5-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This patch, part of a series, removes the `PRIV_SPEC_CLASS_*` definitions and related functions from binutils for the RISC-V architecture. The move is justified because the privileged specification version is now consistently 1.13, and no remaining Control and Status Registers (CSRs) depend on older versions. This simplifies the code by eliminating obsolete checks and tables, affecting assembler, disassembler, and GDB.
