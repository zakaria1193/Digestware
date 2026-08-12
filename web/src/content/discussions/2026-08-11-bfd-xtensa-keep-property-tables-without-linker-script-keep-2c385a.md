---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- xtensa
- garbage collection
- linker
discussion_id: 12fadd324212a4171569d0c545bd4e9b3888a163.camel@espressif.com
source_type: public_inbox
title: '[PATCH] bfd: xtensa: keep property tables without linker script KEEP'
headline: 'bfd: xtensa: keep property tables without linker script KEEP'
tldr: Improve garbage collection for Xtensa property tables to avoid bloating images
  with dead code.
proposer: Alexey Lapshin <alexey.lapshin@espressif.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Reduced executable size by eliminating dead code retained due to incorrect garbage
  collection of property tables.
- Simplified linker scripts by removing the need for explicit `KEEP()` directives
  for `.xt.prop` and `.xt.lit` sections.
exchanges:
- author: Alexey Lapshin
  role: proposer
  position: Submits a patch to correctly mark Xtensa property tables during garbage
    collection, removing the need for linker script `KEEP()` and preventing image
    bloat.
  quote: 'Mark property tables from the gc_mark_extra_sections hook, once the

    sections they describe have been marked, using the existing

    xtensa_get_property_section lookup. Set gc_mark directly rather than

    calling _bfd_elf_gc_mark, so a property section that belongs to a COMDAT

    group does not drag in the rest of the group. Linker scripts no longer

    need KEEP() for .xt.prop/.xt.lit'
primer_expert: This patch addresses an issue with garbage collection (GC) in the Xtensa
  BFD backend for Binutils. Unreferenced `.xt.prop` and `.xt.lit` sections, which
  store Xtensa-specific properties, were being retained by linker scripts using `KEEP()`.
  This practice led to the inclusion of dead code and other unused sections when these
  property sections were part of COMDAT groups. The solution involves using the `gc_mark_extra_sections`
  hook to identify and mark these property sections after their associated code has
  been marked, thus allowing them to be garbage collected if not otherwise referenced.
  Thi…
primer_glossary:
- term: bfd
  definition: Binary File Descriptor library. A library provided by GNU binutils that
    provides a generic interface to a wide variety of object file formats.
- term: Xtensa
  definition: A configurable processor architecture used in many embedded systems.
    Binutils provides support for generating code for Xtensa processors.
- term: property tables
  definition: In the context of Xtensa, these are sections (e.g., .xt.prop, .xt.lit)
    that store metadata or configuration information related to the code.
- term: garbage collection
  definition: A memory management technique where the runtime environment automatically
    reclaims memory that is no longer in use by the program. In the context of linkers,
    it refers to discarding unused code and data sections.
- term: COMDAT
  definition: COMDAT (COmmon DATa) sections are groups of sections that are treated
    as a single unit by the linker. If any part of a COMDAT group is referenced, the
    entire group is retained.
- term: KEEP()
  definition: A linker script directive that prevents a section or symbol from being
    discarded by the garbage collector.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/12fadd324212a4171569d0c545bd4e9b3888a163.camel@espressif.com
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Alexey Lapshin proposes changes to how Xtensa property tables are handled during garbage collection in Binutils' BFD library. Previously, linker scripts used `KEEP()` to retain these unreferenced tables, which inadvertently kept dead code and other unreferenced sections. This patch modifies the garbage collection process to mark property tables correctly, eliminating the need for `KEEP()` and preventing image bloat.
