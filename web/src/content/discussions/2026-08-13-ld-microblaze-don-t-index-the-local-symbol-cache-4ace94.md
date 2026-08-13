---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- linker
- microblaze
- elf
- relocations
discussion_id: 20260813021826.84333-1-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v2 1/1] ld: microblaze: don''t index the local symbol cache'
headline: 'ld: microblaze: don''t index the local symbol cache'
tldr: Adds a missing bounds check to microblaze ELF relaxation to prevent an out-of-bounds
  read that corrupts relocation addends.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixes an out-of-bounds read that silently corrupts relocation addends, preventing
  miscompilations.
- Introduces new tests to ensure addend survival during relaxation.
- The fix is detected by ASan in specific test cases, highlighting its importance
  for memory safety.
exchanges:
- author: Samuel Price <thesamprice@gmail.com>
  role: proposer
  position: Submits a patch to add a missing bounds check in microblaze ELF relaxation,
    fixing an out-of-bounds read that corrupts relocation addends and causes miscompilations.
  quote: microblaze_elf_relax_section() was copied from sh_elf_relax_delete_bytes()
    in 2009 (7ba29e2a41) but the copy dropped a bounds check that was already present
    in the sh original. This adds the missing two-line guard from bfd/elf32-sh.c:1227-1228,
    preventing an out-of-bounds read that silently corrupts relocation addends.
- author: Alan Modra
  role: reviewer
  position: Reviewed v1 and pointed out that the code does not need to re-read global
    symbols, suggesting a further cleanup.
  quote: Alan Modra reviewed v1 and pointed out that none of the code in microblaze_elf_relax_section
    needs to re-r
primer_expert: This patch series targets the `ld` linker for the microblaze target,
  specifically within the `microblaze_elf_relax_section` function. The core problem
  is an out-of-bounds read due to a missing bounds check copied from the `sh_elf_relax_delete_bytes`
  function. This read corrupts relocation addends, leading to silent miscompilations,
  particularly in structure member accesses. The proposed solution reinstates the
  missing bounds check and includes new tests for robustness, including detection
  by ASan in specific scenarios.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another object file.
- term: microblaze
  definition: A configurable soft processor core from Xilinx, often used in embedded
    systems and FPGAs.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps, commonly used on Unix-like systems.
- term: Relaxation
  definition: A linking process where the linker adjusts relocation entries based
    on the final placement of code and data. This can involve changing instruction
    encoding or operand values.
- term: Relocation Addend
  definition: A value stored in a relocation entry that is added to the symbol's address
    to form the final address. In this context, it's being corrupted during relaxation.
- term: ASan
  definition: AddressSanitizer. A fast memory error detector for C/C++ that finds
    issues like out-of-bounds accesses and use-after-free.
- term: --gc-sections
  definition: A linker option that discards unused sections from the output file,
    helping to reduce executable size.
- term: .eh_frame
  definition: A section in an ELF object file containing DWARF debugging information,
    primarily used for stack unwinding and exception handling.
series_id: 'binutils:ld: microblaze: don''t index the local symbol cache'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813021826.84333-1-thesamprice@gmail.com
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch series addresses a silent miscompilation in the microblaze target by fixing an out-of-bounds read in `ld`'s `microblaze_elf_relax_section` function. The issue arises from a copied function missing a bounds check, leading to incorrect relocation addend adjustments when scanning global symbols. The fix reapplies the missing guard, preventing corruption that affected structure member accesses. It also introduces new tests to verify addend survival during relaxation, with ASan builds catching the error in a test specifically designed for `.eh_frame` editing.
