---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- pdb
- linker
- memory management
- bugfix
- segfault
discussion_id: 20260930193657.733-4-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] ld/pdb: Avoid double-free on malformed symbol data'
headline: 'ld/pdb: Avoid double-free on malformed symbol data'
tldr: Fixes a double-free bug when handling malformed PDB symbol data.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch corrects a memory management error in the PDB writing code
  of binutils' linker (ld). Specifically, it addresses a double-free condition that
  arises when processing debug sections (`handle_debugs_section`) encounters an error.
  The error handling logic in `create_module_info_substream` correctly frees module
  file arrays. However, `populate_module_stream`, which is called during this process,
  also contained a `free(mod_source->files)` call. This second free operation on the
  same memory block caused a double-free. The patch removes the redundant `free` call
  from `populate_module_stream…
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft for storing debugging
    and project-related information for Microsoft Windows applications.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or shared library.
- term: double-free
  definition: A memory corruption error that occurs when memory is freed more than
    once.
- term: symbol data
  definition: Information related to symbols (names of functions, variables, etc.)
    within an object file or executable, used for linking and debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-4-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch prevents a double-free error that can occur when handling malformed symbol data within PDB files. When the `handle_debugs_section` function fails, it triggers cleanup that frees file arrays for all modules. Subsequently, the `populate_module_stream` function was also attempting to free the current module's file array, leading to the double-free. This change removes the redundant free call in `populate_module_stream`, ensuring proper memory management.
