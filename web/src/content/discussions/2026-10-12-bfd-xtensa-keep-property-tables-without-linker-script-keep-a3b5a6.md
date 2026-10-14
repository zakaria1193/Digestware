---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- xtensa
- linker
- garbage collection
discussion_id: 20260825075218.16121-1-alexey.lapshin@espressif.com
source_type: public_inbox
title: '[PATCH v3] bfd: xtensa: keep property tables without linker script KEEP'
headline: 'bfd: xtensa: keep property tables without linker script KEEP'
tldr: Patch modifies BFD's Xtensa ELF backend to correctly handle property sections,
  preventing unwanted resurrection of code by the garbage collector.
proposer: Alexey Lapshin <alexey.lapshin@espressif.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Ensures correct garbage collection of property sections, reducing executable size.
- Removes the need for manual KEEP directives in linker scripts for these sections.
- Introduces a new hook for GC marking, adding complexity to the BFD Xtensa backend.
exchanges:
- author: Alexey Lapshin
  role: proposer
  position: Proposes a change to BFD's Xtensa ELF backend to correctly garbage collect
    unreferenced property tables.
  quote: 'Property sections are unreferenced, so linker scripts kept them alive

    with KEEP(). That does not work: gas puts .xt.prop/.xt.lit for a COMDAT

    function into that function''s group, and _bfd_elf_gc_mark marks every

    member of a group when one member is marked. KEEP() on the property

    section therefore resurrected the code, literals, rodata and exception

    tables of unused C++ template instantiations and…'
- author: Max Filippov
  role: reviewer
  position: Reviews the patch, acknowledging the problem description and the proposed
    solution's mechanism.
  quote: null
primer_expert: The patch addresses an issue in binutils' BFD library concerning the
  Xtensa ELF backend's garbage collection (GC) of property sections. Specifically,
  unreferenced .xt.prop and .xt.lit sections were being kept alive by linker script
  KEEP directives, which incorrectly caused related COMDAT group members to be preserved.
  The fix modifies the GC marking process to only mark property sections based on
  their described sections, and introduces a new hook (`elf_xtensa_gc_mark_extra_sections`)
  to avoid dragging entire COMDAT groups when only the property section needs to be
  preserved.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a part of GNU Binutils, provides
    a common interface for handling various executable file formats.
- term: Xtensa
  definition: A configurable processor architecture, often used in embedded systems,
    for which binutils provides specific support.
- term: Property sections
  definition: Sections in an executable file format that contain metadata or properties
    related to other sections or symbols. In Xtensa, these are .xt.prop and .xt.lit.
- term: Linker script
  definition: A script used by the linker to control how input sections from object
    files are combined into output sections in the final executable or library.
- term: KEEP
  definition: A directive in linker scripts that prevents specified sections or symbols
    from being removed during garbage collection.
- term: COMDAT
  definition: Common constructor/destructor or 'COMDAT' sections are a way to handle
    duplicate or equivalent sections in different object files. The linker selects
    one instance based on certain criteria.
- term: Garbage collection (GC)
  definition: A memory management technique where the runtime environment automatically
    reclaims memory that is no longer in use by the program. In linkers, it's used
    to remove unused sections or symbols.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261012162732.3903809-1-alexey.lapshin@espressif.com
bugzilla_url: null
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This patch revises the Xtensa ELF backend in binutils' BFD library to properly manage property sections (.xt.prop/.xt.lit). Previously, linker scripts used KEEP() to prevent these unreferenced sections from being garbage collected, which inadvertently caused other related code sections to be kept alive. The patch introduces a new hook to mark property sections only after the sections they describe are marked, thus avoiding the resurrection of unrelated COMDAT group members and allowing the removal of KEEP directives.
