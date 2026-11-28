---
project: binutils
subsystem: riscv
patch_id: null
tags:
- binutils
- riscv
- ld
- testing
- relaxation
discussion_id: 20261127135531.306576-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH] riscv: use .s/.d tests for the relax delete-range check'
headline: 'riscv: Switch relax delete-range tests to assembler source'
tldr: RISC-V linker tests for relaxation delete-range now use assembler source and
  dump files instead of hex encoding.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Submits a patch to change RISC-V relax-underflow tests to use assembler
    source and dump files.
  quote: 'The new tests assemble one source with the R_RISCV_ALIGN relocation at

    offset 8 (relaxes and links; .text shrinks to 0x12) or at offset 22

    (the deletion would pass the end of .text, so ld rejects it).'
primer_expert: This patch modifies the test infrastructure for the RISC-V linker (ld)
  within binutils, specifically for testing the relaxation of delete-range operations.
  It replaces existing tests that used hex-encoded object data with a more robust
  approach using assembler source files and objdump outputs. This aligns with previous
  review feedback and aims to provide clearer, more maintainable tests for scenarios
  where linker relaxation might incorrectly delete code past the intended boundaries.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles,
    increasingly adopted for various computing applications.
- term: linker
  definition: A program that combines various pieces of code and data into a single
    file that can be loaded into memory and executed.
- term: relaxation
  definition: A linker optimization technique where the linker adjusts branch offsets
    and other relative addressing information to produce smaller or more efficient
    code, often by overwriting placeholder instructions.
- term: R_RISCV_ALIGN
  definition: A RISC-V relocation type used to adjust alignment, relevant in the context
    of linker relaxation.
- term: objdump
  definition: A command-line utility that displays information from object files,
    including disassembled code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261127135531.306576-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This patch updates the RISC-V linker test suite to use assembler source files (`.s`) and object dump files (`.d`) for testing the relaxation delete-range functionality. This change replaces previous tests that encoded objects as hexadecimal values. The new tests, which assemble source code with specific relocation types, have been verified on master and link identically with and without the patch.
