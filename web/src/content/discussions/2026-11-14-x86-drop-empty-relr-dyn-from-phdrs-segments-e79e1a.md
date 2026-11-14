---
project: binutils
subsystem: binutils/x86
patch_id: null
tags:
- binutils
- ld
- linker
- x86
- elf
discussion_id: TgP8p7tEVGbqpoYa46zHoemhxRo3jrHeMA1u2ptjwP28hAabYXc1j3ugRegMT3A0ymyL7goAvI3js-O1ukLvw6mOhD14wLppWLkXmrYb0-0=@protonmail.com
source_type: public_inbox
title: '[PATCH] x86: Drop an empty .relr.dyn from segments given by PHDRS'
headline: 'x86: Drop empty .relr.dyn from PHDRS segments'
tldr: Ensures empty .relr.dyn sections are correctly excluded from segments when using
  PHDRS in the linker script.
proposer: mintsuki <mintsuki@protonmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures correct handling of empty sections, preventing potential runtime errors
  or incorrect executable layouts.
exchanges:
- author: mintsuki@protonmail.com
  role: proposer
  position: Submits a patch to correctly exclude empty .relr.dyn sections when PHDRS
    are used.
  quote: "Set SEC_EXCLUDE on it before removing it, as those do.\n\nbfd/\n\t* elfxx-x86.c\
    \ (_bfd_elf_x86_size_relative_relocs): Set SEC_EXCLUDE\n\ton the empty .relr.dyn\
    \ output section before removing it.\n\nld/\n\t* testsuite/ld-i386/dt-relr-3.d:\
    \ New file.\n\t* testsuite/ld-i386/i386.exp: Run dt-relr-3.\n\t* testsuite/ld-x86-64/dt-relr-3-x32.d:\
    \ New file.\n\t* testsuite/ld-x86-64/dt-relr-3.d: Likewise.\n\t* testsuite/ld-x86-…"
primer_expert: In `binutils/ld`, when using `-z pack-relative-relocs` and a linker
  script with `PHDRS`, an empty `.relr.dyn` section can cause issues. The `_bfd_elf_x86_size_relative_relocs`
  function removes this section from the section list but doesn't mark it with `SEC_EXCLUDE`.
  This prevents `elf_modify_segment_map` from dropping it, leading to incorrect segment
  assignment and sizing when `PHDRS` are processed before section exclusion. This
  patch adds `SEC_EXCLUDE`.
primer_glossary:
- term: .relr.dyn
  definition: A dynamic section in ELF executables that contains relocation information,
    specifically for position-independent code (PIC) or position-independent executables
    (PIE), used at runtime by the dynamic linker.
- term: PHDRS
  definition: Program Headers in an ELF file, which describe how the segments of the
    program should be mapped into memory by the operating system. Linker scripts can
    use PHDRS to control segment layout.
- term: SEC_EXCLUDE
  definition: A flag or attribute associated with a section in the linker's internal
    representation, indicating that the section should not be included in the final
    executable's segments or memory map.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: linker script
  definition: A file used by the linker to control the memory layout of the output
    file, specifying where sections should be placed and how segments are formed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/TgP8p7tEVGbqpoYa46zHoemhxRo3jrHeMA1u2ptjwP28hAabYXc1j3ugRegMT3A0ymyL7goAvI3js-O1ukLvw6mOhD14wLppWLkXmrYb0-0=@protonmail.com
bugzilla_url: null
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where an empty `.relr.dyn` section could be incorrectly included in a segment when using linker scripts with `PHDRS`. The linker currently removes this section but doesn't mark it as excluded, leading to it being processed during segment map creation and potentially causing errors or incorrect segment sizing. The fix ensures the section is marked with `SEC_EXCLUDE` before removal, aligning its handling with other excluded sections.
