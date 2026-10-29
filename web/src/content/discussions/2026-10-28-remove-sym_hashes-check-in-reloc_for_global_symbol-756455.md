---
project: binutils
subsystem: binutils
patch_id: null
tags:
- cleanup
- macro
- binutils
discussion_id: auJ36NJh_hPCQ4o9@squeak.grove.modra.org
source_type: public_inbox
title: Remove sym_hashes check in RELOC_FOR_GLOBAL_SYMBOL
headline: Remove sym_hashes check in RELOC_FOR_GLOBAL_SYMBOL
tldr: Removes a redundant NULL check for `sym_hashes` in the `RELOC_FOR_GLOBAL_SYMBOL`
  macro.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes a redundant check, simplifying the code. Assumes that other parts of the
  system now guarantee `sym_hashes` is valid, which could mask other underlying bugs
  if that assumption is incorrect.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Removes a redundant NULL check for `sym_hashes` in the `RELOC_FOR_GLOBAL_SYMBOL`
    macro, stating it's now guaranteed to be non-NULL by other functions.
  quote: 'This should not be necessary with the sym_hashes check in

    elf_link_read_relocs_from_section.  BTW, the comment removed traces

    all the way back to the initial cris commit (06c15ad74f39).  NULL

    sys_hashes were likely caused by some other bug, such as not checking

    for the correct tdata.'
primer_expert: This patch cleans up the `RELOC_FOR_GLOBAL_SYMBOL` macro in `bfd/elf-bfd.h`
  by removing a `sym_hashes == NULL` check. This check was likely a safeguard against
  erroneous input or bugs in earlier ELF handling (specifically mentioning the CRIS
  commit). The removal implies that `elf_link_read_relocs_from_section` now reliably
  populates and validates `sym_hashes`, making the macro-level check unnecessary.
  The original comment suggests `NULL` `sym_hashes` might have indicated other deeper
  issues.
primer_glossary:
- term: sym_hashes
  definition: Likely an array or hash table containing symbol information, used for
    efficient symbol lookup during linking.
- term: RELOC_FOR_GLOBAL_SYMBOL
  definition: A macro in BFD used to process relocations that refer to global symbols.
- term: 'NULL'
  definition: A special pointer value that represents an invalid or uninitialized
    memory address. In C, it's typically defined as `(void*)0`.
- term: elf_link_read_relocs_from_section
  definition: A BFD function responsible for reading and processing relocation entries
    from a specific section in an ELF object file.
- term: CRIS
  definition: A 32-bit RISC instruction set architecture developed by Axis Communications.
    The reference to a CRIS commit suggests this check originated from early ELF support
    for that architecture.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ36NJh_hPCQ4o9@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch removes a check for `sym_hashes == NULL` from the `RELOC_FOR_GLOBAL_SYMBOL` macro within `bfd/elf-bfd.h`. The proposer argues that this check is now redundant because `elf_link_read_relocs_from_section` already ensures that `sym_hashes` is valid. The removed comment indicates this check dates back to the initial CRIS ELF commit and might have addressed other bugs related to `NULL` `sym_hashes`.
