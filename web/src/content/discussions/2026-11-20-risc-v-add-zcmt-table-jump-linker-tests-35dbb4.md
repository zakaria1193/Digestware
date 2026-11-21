---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- relaxation
- optimization
- testing
discussion_id: 20261120142506.264748-4-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v5 3/3] RISC-V: Add Zcmt table-jump linker tests'
headline: 'RISC-V: Add Zcmt table-jump linker tests'
tldr: Adds comprehensive linker tests for the Zcmt table-jump relaxation extension
  in RISC-V.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Extensive test coverage for the new Zcmt relaxation feature.
- Ensures correct behavior across various scenarios and configurations.
- Increases confidence in the stability and correctness of the implementation.
exchanges: []
primer_expert: This is the third patch in a series introducing Zcmt table-jump relaxation
  to GNU ld for RISC-V. This specific patch focuses on the test suite (`ld/testsuite/ld-riscv-elf/`)
  to validate the functionality added in the preceding patches. It defines new test
  cases (`.d` and `.s` files) to cover scenarios such as table generation, profitability,
  relocation and symbol handling, relaxation ordering, and unsupported link modes.
  It also exercises option parsing and global relaxation control, verifying emitted
  relocations and section garbage collection.
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: Zcmt
  definition: A RISC-V standard extension that allows for table-jump relaxation, an
    optimization technique for jumps and calls.
- term: table-jump relaxation
  definition: An optimization technique in linkers where indirect jumps or calls are
    replaced with a more efficient form, potentially using a jump table.
- term: linker
  definition: A program that combines object files and libraries into an executable
    program.
- term: relocation
  definition: The process of updating symbolic references and memory addresses in
    object code or executable files after compilation, typically performed by the
    linker.
- term: option parser
  definition: The component of the linker responsible for interpreting command-line
    options provided by the user.
- term: relaxation
  definition: An optimization process in linkers that adjusts code, such as branch
    offsets, to improve performance or reduce code size.
series_id: 'binutils:risc-v: add zcmt table-jump linker tests'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120142506.264748-4-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch introduces a suite of linker tests for the RISC-V Zcmt extension, which enables table-jump relaxation. The tests cover various aspects including table generation, profitability analysis, relocation handling, symbol management, relaxation ordering, and unsupported link modes. They exercise option parsing, global relaxation control, and verify that emitted relocations do not contain linker-private markers, ensuring the robustness of the Zcmt implementation.
