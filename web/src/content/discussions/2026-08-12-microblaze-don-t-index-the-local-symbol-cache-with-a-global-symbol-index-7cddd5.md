---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- binutils
- microblaze
- linker
- elf
- relocations
discussion_id: anwpt0exztiKYco9@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] microblaze: don''t index the local symbol cache with a global
  symbol index'
headline: 'microblaze: don''t index the local symbol cache with a global symbol index'
tldr: Reviewer suggests a tidy-up to a patch that fixes an out-of-bounds read in microblaze
  ELF relaxation by ensuring global symbols are not indexed.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixes an out-of-bounds read, preventing silent corruption of relocation addends.
- Simplifies the `microblaze_elf_relax_section` function by removing unnecessary global
  symbol lookups.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Approves the patch and suggests a code cleanup to remove unnecessary global
    symbol lookups.
  quote: The patch looks good to me. As you correctly point out, the symtab_hdr->contents
    buffer is supposed to only contain local syms, so indexing at symtab_hdr->sh_info
    or above is wrong. What's more, none of the code in microblaze_elf_relax_section
    needs to re-read global syms so you might like to add the following tidy-up to
    your patch.
- author: Sam Price
  role: proposer
  position: Submitted a patch to fix an out-of-bounds read in microblaze_elf_relax_section
    by adding a missing bounds check.
  quote: microblaze_elf_relax_section() was copied from sh_elf_relax_delete_bytes()
    in 2009 (7ba29e2a41) but the copy dropped a bounds check that was already present
    in the sh original. This adds the missing two-line guard from bfd/elf32-sh.c:1227-1228,
    preventing an out-of-bounds read that silently corrupts relocation addends.
primer_expert: This discussion pertains to the `microblaze_elf_relax_section` function
  within binutils' BFD library. A patch corrects an out-of-bounds read caused by incorrect
  indexing into the local symbol table (`symtab_hdr->contents`). The reviewer suggests
  an additional cleanup to prevent the function from accessing global symbols altogether,
  as they are not required for the relaxation process on microblaze.
primer_glossary:
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
- term: BFD
  definition: Binary File Descriptor. A library used by GNU binary utilities to provide
    a common interface for handling various executable file formats.
- term: Symbol Cache
  definition: An internal data structure used by the linker or assembler to store
    information about symbols (variables, functions, etc.) for quick lookup.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/anwpt0exztiKYco9@squeak.grove.modra.org
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

Alan Modra reviews a patch that fixes an out-of-bounds read in microblaze ELF relaxation by adding a missing bounds check. He agrees with the fix, noting that the `symtab_hdr->contents` buffer should only contain local symbols. Modra suggests a further tidy-up to the patch, removing the need to re-read global symbols entirely, as they are not used within the `microblaze_elf_relax_section` function.
