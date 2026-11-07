---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- ld
- security
- elf
- memory-safety
- linker-scripts
commit_hash: f6d98c0bc403261fafba98b233c985068cf78c05
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: ld stops reading ELF fields from generic hash tables after OUTPUT_FORMAT
tldr: ldelf_after_open_output now checks for an ELF hash table first, which fixes
  a heap over-read when a script picks a generic-table ELF format.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: '`ldelf_after_open_output` in ld/ldelf.c runs after the output BFD
  is opened. It compares `elf_object_id` with `elf_hash_table_id` on `link_info.hash`.
  A script''s OUTPUT_FORMAT can retarget the output BFD after the emulation has already
  created `link_info.hash`. The BFD flavour is then no longer a reliable guide to
  which hash table struct is in use. Backends that use `_bfd_generic_link_hash_table_create`
  return a much smaller table than `struct elf_link_hash_table`.'
primer_glossary:
- term: OUTPUT_FORMAT
  definition: A linker-script command that sets the BFD target name of the output
    file, for example elf64-nfp. It can override the format the emulation selected,
    and the linker may do this after it has already set up emulation state.
- term: link hash table
  definition: The linker's symbol table, held in a `struct bfd_link_hash_table` that
    each backend can extend. ELF backends use `struct elf_link_hash_table`. Other
    backends use a smaller generic table.
- term: is_elf_hash_table
  definition: A BFD macro or function that checks whether a link hash table was created
    by an ELF backend. Code should call it before casting the table to ELF-specific
    structures.
- term: AddressSanitizer
  definition: A compiler-instrumented memory error detector. It finds heap overflows
    and use-after-free bugs at runtime. This bug only shows up reliably under it.
- term: BFD flavour
  definition: A coarse classification of an output format, such as ELF or COFF, returned
    by `bfd_get_flavour`. Different targets of the same flavour can still use different
    hash table layouts.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261106131601.E51AA4BA5434@sourceware.org
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

A linker script can switch the output to an ELF flavour that uses the generic link hash table, such as OUTPUT_FORMAT("elf64-nfp"). `ldelf_after_open_output` assumed an ELF output BFD meant an ELF hash table. It then read `hash_table_id` past the end of the smaller generic table, which AddressSanitizer reports as a 4-byte heap-buffer-overflow read. The hook now calls `is_elf_hash_table` and returns early if the check fails. This matches the check `compatible_format` in bfd/elflink.c already makes. The commit also extends the `ld-x86-64/arch-confusion.exp` test to cover this case with elf64-nfp, or elf32-little when nfp isn't built (PR ld/34874).
