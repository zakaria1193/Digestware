---
project: binutils
subsystem: binutils
patch_id: null
tags:
- dead-code-removal
- refactoring
- binutils
discussion_id: auJ3rRzI1GbOGGHM@squeak.grove.modra.org
source_type: public_inbox
title: Remove dead code in arm check_relocs
headline: Remove dead code in arm check_relocs
tldr: Removes unnecessary check for zero symbols in the ARM ELF check_relocs function.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the function. Relies on prior validation to ensure
  symbol table existence, making the code cleaner.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Removes dead code from `elf32_arm_check_relocs` that checked for zero
    symbols, as this condition is now handled by earlier validation.
  quote: 'Now that we reject object files with relocs lacking a proper .symtab

    section, checking for zero nsyms is no longer necessary.'
primer_expert: In `bfd/elf32-arm.c`, this patch removes the `nsyms` variable and its
  initialization, along with the conditional block that used it to distinguish between
  local symbols and global hash table entries. This simplification is possible because
  a prior change ensures that relocations are only processed if a valid symbol table
  exists, making the `nsyms > 0` check redundant. The logic now directly uses `r_symndx
  < symtab_hdr->sh_info` to determine if a symbol is local.
primer_glossary:
- term: Relocation
  definition: A modification needed in an object file or shared library to resolve
    references to symbols or addresses that are not yet known at link time. This process
    is typically handled by the linker.
- term: Symbol Table
  definition: A data structure within an object file or executable that maps symbol
    names to their addresses and other attributes, used by linkers and debuggers.
- term: .symtab
  definition: The section in an ELF object file that contains the symbol table, mapping
    symbol names to their addresses and attributes.
- term: Dead Code
  definition: Code that is never executed or whose execution has no effect on the
    outcome of the program. Removing dead code simplifies maintenance and can sometimes
    improve performance.
- term: ARM
  definition: Advanced RISC Machine. A family of reduced instruction set computing
    (RISC) architectures for computer processors, widely used in mobile devices and
    embedded systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ3rRzI1GbOGGHM@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch removes dead code from the `elf32_arm_check_relocs` function in BFD. Specifically, it eliminates a check for zero symbols (`nsyms`), which is no longer necessary because the library now rejects object files with relocations that lack a proper symbol table. This simplifies the function and removes outdated logic.
