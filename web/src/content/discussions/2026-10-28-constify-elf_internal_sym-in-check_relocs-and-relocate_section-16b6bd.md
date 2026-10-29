---
project: binutils
subsystem: binutils
patch_id: null
tags:
- const-correctness
- refactoring
- binutils
discussion_id: auJ4TRFxFSLjHqYU@squeak.grove.modra.org
source_type: public_inbox
title: Constify Elf_Internal_Sym in check_relocs and relocate_section
headline: Constify Elf_Internal_Sym in check_relocs and relocate_section
tldr: Makes Elf_Internal_Sym pointers const in check_relocs and relocate_section functions
  for safety and clarity.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Enhances type safety and code clarity by ensuring symbol data is not inadvertently
  modified. No functional or performance impact.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes making `Elf_Internal_Sym` pointers `const` in `check_relocs`
    and `relocate_section` functions to reflect that the symbol data is not modified.
  quote: 'At one point when looking at pr34835 I started changing check_relocs

    and relocate_section to support relocs against STN_UNDEF without a

    .symtab section present.  I gave up on that idea because there are

    many other functions that would need changing too, but kept this part

    which involves making some variable and function parameter pointers

    const.'
primer_expert: This patch introduces `const` correctness to `Elf_Internal_Sym` pointers
  passed to `_bfd_elf_rela_local_sym`, `_bfd_elf_rel_local_sym`, and `mn10200_elf_relocate_section`.
  The motivation was an attempt to handle relocations against `STN_UNDEF` without
  a `.symtab` present, which was not fully pursued. However, the `const` additions
  clarify that these functions do not intend to modify the symbol entries they receive,
  improving code safety and signaling intent.
primer_glossary:
- term: const
  definition: A type qualifier in C that indicates a variable or pointer cannot be
    modified after initialization. It helps prevent accidental data corruption and
    can allow for compiler optimizations.
- term: Elf_Internal_Sym
  definition: An internal structure used by BFD to represent an ELF symbol table entry.
- term: check_relocs
  definition: A function within BFD's ELF backends responsible for validating relocation
    entries against symbol table information.
- term: relocate_section
  definition: A function that processes relocation entries for a given section, applying
    the necessary address adjustments.
- term: STN_UNDEF
  definition: A special symbol type in ELF representing an undefined symbol, typically
    a reference to a symbol defined in another object file or library.
- term: .symtab
  definition: The section in an ELF object file that contains the symbol table, mapping
    symbol names to their addresses and attributes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ4TRFxFSLjHqYU@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch makes function parameter pointers to `Elf_Internal_Sym` `const` in the `check_relocs` and `relocate_section` functions. The change stems from an abandoned effort to support relocations against `STN_UNDEF` without a `.symtab` section. By marking these pointers as `const`, the code enforces that the symbol data is not modified through these parameters, improving type safety and indicating intent.
