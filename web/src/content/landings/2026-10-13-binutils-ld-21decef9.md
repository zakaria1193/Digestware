---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- linker
- Xtensa
- garbage collection
- embedded
commit_hash: 21decef93421234ff87dc0f963cca9dc96fc57d6
source_type: public_inbox
author: Max Filippov <jcmvbkbc@sourceware.org>
headline: 'Xtensa linker: Correctly handle property tables for COMDAT sections'
tldr: Xtensa linker now correctly manages property tables, preventing unwanted code
  resurrection and ensuring correct garbage collection.
impact_score: 5
performance_win: true
breaking_change: true
outcome: committed
primer_expert: This patch modifies the Xtensa ELF backend in BFD and the linker to
  correctly garbage collect property sections (.xt.prop/.xt.lit). Previously, unconditional
  `KEEP()` directives in linker scripts for these sections would resurrect entire
  COMDAT groups, including unused code and literals, especially for C++ template instantiations.
  The fix uses `elf_xtensa_gc_mark_extra_sections` to mark property sections only
  after the sections they describe are marked, and it sets `gc_mark` directly to avoid
  dragging in other COMDAT group members.
primer_glossary:
- term: COMDAT
  definition: A COMDAT (common object file data) section is a special type of section
    that allows the linker to select only one instance of several identical sections
    from different object files. This is often used for functions or data that are
    defined in multiple translation units but should only appear once in the final
    executable.
- term: linker script
  definition: A file that provides detailed instructions to the linker on how to arrange
    sections in the output file, how to assign addresses, and how to handle symbols.
    It allows fine-grained control over the final executable's layout.
- term: KEEP()
  definition: A directive within a linker script that explicitly tells the linker
    to preserve a specified symbol or section, preventing it from being garbage collected
    even if it appears unused.
- term: garbage collection
  definition: The process by which the linker identifies and removes unused sections
    or symbols from the final executable to reduce its size. This is crucial for embedded
    systems and for optimizing code size.
- term: property tables
  definition: In the context of Xtensa architecture, these are special sections that
    store metadata or properties related to code or data sections. They are essential
    for certain dynamic features or architectural requirements.
- term: resurrected
  definition: In linker terminology, 'resurrected' refers to a section or symbol that
    was intended to be removed by garbage collection but is kept in the final executable
    due to some directive or indirect reference.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261013111407.14C294BA23CA@sourceware.org
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit refactors how the Xtensa linker handles property tables associated with COMDAT sections. Previously, linker scripts used KEEP() directives to preserve these tables, which inadvertently caused unused code and literals to be retained. The new implementation marks property tables directly via a garbage collection hook, avoiding the resurrection of unrelated code and eliminating the need for linker script KEEP() directives for these sections.
