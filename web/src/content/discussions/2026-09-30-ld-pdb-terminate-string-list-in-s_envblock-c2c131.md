---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- pdb
- linker
- debugging
- bugfix
discussion_id: 20260930193657.733-14-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] ld/pdb: Terminate the string list in S_ENVBLOCK'
headline: 'ld/pdb: Terminate string list in S_ENVBLOCK'
tldr: Adds a null terminator to the string list in S_ENVBLOCK symbols to fix parsing
  errors.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch corrects an error in the PDB writer within binutils' linker
  (ld). The S_ENVBLOCK symbol type, used for environment variables, stores strings
  in a list. The previous implementation failed to append a null terminator to this
  list, which, combined with specific alignment conditions, could cause buffer overflows
  and parsing failures in tools like llvm-pdbutil. The fix ensures the list is properly
  terminated.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft for storing debugging
    and project-related information for Microsoft Windows applications.
- term: S_ENVBLOCK
  definition: A specific symbol type within the PDB format that encapsulates environment
    variable information.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or shared library.
- term: llvm-pdbutil
  definition: A utility from the LLVM project used for inspecting and manipulating
    PDB files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-14-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where the list of strings in an S_ENVBLOCK symbol was not properly terminated, leading to parsing errors when the strings ended on a four-byte boundary. Specifically, it adds a null terminator to the string list, preventing readers like llvm-pdbutil from running off the end of the record and reporting "Stream Error".
