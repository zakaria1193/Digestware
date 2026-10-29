---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- elf
- linking
- bfd
- mips
- score
commit_hash: 53705cce3fb2caf917b42fe8945e74786e2a1530
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Correct upper bound check for relocation symbol indices in MIPS and Score
tldr: Relocation symbol index bounds are corrected for MIPS and Score ELF backends
  in BFD.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `check_relocs` functions for MIPS (`_bfd_mips_elf_check_relocs`
  in `elfxx-mips.c`) and Score (`s3_bfd_score_elf_check_relocs` in `elf32-score.c`
  and `s7_bfd_score_elf_check_relocs` in `elf32-score7.c`) had an incorrect upper
  bound check for `r_symndx`. The code previously used `extsymoff + NUM_SHDR_ENTRIES(symtab_hdr)`
  as the limit. This commit corrects it to simply `NUM_SHDR_ENTRIES(symtab_hdr)`,
  which accurately reflects the maximum valid symbol index in the symbol table. This
  ensures that relocations referencing symbols beyond the table are correctly identified
  as errors.
primer_glossary:
- term: r_symndx
  definition: The symbol table index field within an ELF relocation entry. It indicates
    which symbol the relocation refers to.
- term: relocation
  definition: Information in an object file that describes how to modify certain addresses
    or symbols when linking. For example, a relocation entry might indicate that a
    specific address needs to be updated with the actual address of a function.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a generic interface for reading and writing various binary file formats, including
    ELF.
- term: MIPS
  definition: Microprocessor without Interlocked Pipeline Stages. A family of Reduced
    Instruction Set Computing (RISC) architectures.
- term: Score
  definition: A 32-bit RISC instruction set architecture developed by Star Semiconductor.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223619.609284BA23D9@sourceware.org
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This change corrects the upper bound check for relocation symbol indices (`r_symndx`) in the MIPS and Score ELF backends within BFD. The previous logic used an incorrect offset, leading to potential validation errors. The updated code ensures that `r_symndx` is correctly compared against the total number of symbols, improving the accuracy of relocation processing for these architectures.
