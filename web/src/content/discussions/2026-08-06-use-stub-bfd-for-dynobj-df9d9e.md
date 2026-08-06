---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- ELF
- refactoring
discussion_id: 20260806042109.536514-1-amodra@gmail.com
source_type: public_inbox
title: Use stub bfd for dynobj
headline: Use stub bfd for dynobj
tldr: A series of patches refactors binutils' dynamic object handling, introducing
  a stub BFD for dynobj and improving various ELF linking routines.
proposer: Alan Modra
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: proposer
  position: Introduces a series of patches to improve dynamic object handling in binutils,
    including using a stub BFD and refining ELF linking logic.
  quote: 'This series is a followup to

    https://sourceware.org/pipermail/binutils/2026-May/149276.html

    being the first patch mentioned there, split into nine.'
- author: Alan Modra
  role: proposer
  position: Explains a specific change to move GOT section creation functions outside
    of dynamic object tests for better code clarity.
  quote: 'It isn''t obvious that it is correct to call the various create got

    section functions inside a !dynobj test, ie. somebody reading the code

    is left wondering whether the got might not be be created.'
- author: Alan Modra
  role: proposer
  position: Details a change to avoid duplicate dynobj assignments in elfnn-kvx.c
    and elfnn-loongarch.c.
  quote: 'bfd/elfnn-kvx.c (kvx_elf_create_got_section): Don''t set dynobj.

    bfd/elfnn-loongarch.c (loongarch_elf_check_relocs): Don''t repeat

    dynobj assignment already done.'
- author: Alan Modra
  role: proposer
  position: Describes the extraction of input object compatibility checks into a new
    function in elflink.c.
  quote: 'A number of places in elflink.c need to check that the input object

    relocs are compatible with the output.  Extract those checks into a

    new function.'
- author: Alan Modra
  role: proposer
  position: Explains the splitting of `_bfd_elf_link_create_dynstrtab` into two functions
    to improve modularity.
  quote: '_bfd_elf_link_create_dynstrtab doesn''t just create dynstrtab, it also

    sets dynobj.  This patch splits it into two separate functions,

    _bfd_elf_link_dynobj and _bfd_elf_link_dynstr.'
primer_expert: This patch series refactors binutils' ELF linker, specifically focusing
  on dynamic object (`dynobj`) handling. It introduces a "stub BFD" to represent dynamic
  objects more cleanly and reorganizes several functions within `elflink.c` and architecture-specific
  ELF BFD code. The goal is to improve code clarity, reduce redundancy, and enhance
  robustness by performing better input object compatibility checks and refining how
  dynamic sections like GOT and dynstrtab are managed.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level interface used by GNU
    binutils to manipulate object file formats.
- term: dynobj
  definition: Abbreviation for dynamic object, referring to shared libraries or dynamically
    linked executables.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executable,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: GOT
  definition: Global Offset Table, a table used in position-independent executable
    code to store addresses of global and static variables.
- term: dynstrtab
  definition: Dynamic string table, part of the ELF format, containing strings used
    in the dynamic linking section.
- term: relocation
  definition: Information in an object file that describes how to modify code or data
    addresses when the object is linked with other modules or loaded into memory.
series_id: 20260806042109.536514-1-amodra@gmail.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260806042109.536514-1-amodra@gmail.com
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

This patch series, a follow-up to a previous discussion, aims to refactor binutils' handling of dynamic objects. It introduces a stub BFD intended for use as a dynamic object and makes several improvements to ELF linking, including input object compatibility checks, splitting functions for clarity, and adding sanity checks for dynamic relocation sections. The changes touch upon numerous architecture-specific ELF BFD implementations.
