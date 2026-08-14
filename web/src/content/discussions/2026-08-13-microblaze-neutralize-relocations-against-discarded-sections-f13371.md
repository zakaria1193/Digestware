---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- ld
- microblaze
- bugfix
- relocation
- debug
discussion_id: 20260813044529.81534-1-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH] microblaze: neutralise relocations against discarded sections'
headline: 'microblaze: Neutralize relocations against discarded sections'
tldr: Patch corrects GNU ld for MicroBlaze by neutralizing relocations against symbols
  in discarded sections, fixing garbage in debug sections.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: ready
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Neutralizing relocations prevents incorrect data but might mask underlying issues
  if the discarded sections were intended to be present.
- Adopting standard BFD practices ensures consistency across targets.
exchanges:
- author: Sam Price <thesamprice@gmail.com>
  role: proposer
  position: Submits a patch to fix MicroBlaze ELF linker behavior, ensuring relocations
    against discarded sections are neutralized to prevent incorrect data in debug
    sections.
  quote: 'microblaze_elf_relocate_section does not handle relocations against symbols
    defined in sections discarded by linkonce or comdat handling. bfd/elf32-microblaze.c
    contains no RELOC_AGAINST_DISCARDED_SECTION at all, where 60 other bfd/elf*.c
    files use it. The relocation survives and resolves against a dead symbol, so debug
    sections end up holding garbage where zero is expected:'
- author: Neal Frager <neal.frager@amd.com>
  role: other
  position: Acknowledges the issue and the proposed fix, providing context that this
    is related to AMD's systems.
  quote: 'Hello Sam,


    > microblaze_elf_relocate_section does not handle relocations against

    > symbols defined in sections discarded by linkonce or comdat handling.

    > bfd/elf32-microblaze.c contains no RELOC_AGAINST_DISCARDED_SECTION at

    > all, where 60 other bfd/elf*.c files use it.  The relocation survives and

    > resolves against a dead symbol, so debug sections end up holding garbage

    > where zero is expect…'
primer_expert: A bugfix patch for the MicroBlaze ELF linker addresses incorrect handling
  of relocations. Specifically, `microblaze_elf_relocate_section` fails to neutralize
  relocations targeting symbols within sections that have been discarded by linkonce
  or comdat mechanisms. This results in debug sections containing erroneous data (garbage)
  where zeros are expected. The proposed solution introduces the `RELOC_AGAINST_DISCARDED_SECTION`
  handling, mirroring common practice in other BFD ELF backends, and resolves several
  failing tests.
primer_glossary:
- term: MicroBlaze
  definition: A soft processor core from Xilinx, commonly used in FPGAs.
- term: ELF
  definition: Executable and Linkable Format, the standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: relocation
  definition: A process performed by the linker to adjust symbolic references in object
    files to their final memory addresses in the executable or shared library.
- term: discarded sections
  definition: Sections within an object file that are intentionally removed or ignored
    during the linking process, often due to linkonce or comdat grouping.
- term: linkonce
  definition: A linker flag or mechanism that ensures a section or symbol is included
    only once in the final output, even if defined in multiple input files.
- term: comdat
  definition: COMDAT (COMDAT sections) is a mechanism in object files that allows
    multiple identical sections from different input files to be merged into a single
    section in the output file, or discarded entirely if not needed.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface for manipulating various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813044529.81534-1-thesamprice@gmail.com
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the MicroBlaze ELF linker where relocations against symbols in discarded sections were not properly handled. This led to garbage data appearing in debug sections instead of expected zeros. The fix neutralizes these problematic relocations, aligning with behavior in other BFD backends and correcting existing test failures.
