---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- linker
- debugging
- pdb
discussion_id: 20260930193657.733-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] ld/pdb: Read inlinee-lines signature at correct offset'
headline: 'ld/pdb: Read inlinee-lines signature at correct offset'
tldr: Fixes ld/pdb.c to read the signature at the correct offset within the payload,
  improving PDB parsing.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This change corrects an offset calculation within the PDB (Program
  Database) parsing logic in GNU ld. Specifically, it addresses how the `parse_inlinee_lines`
  function reads the signature for inlinee source line information. The fix ensures
  that the signature is read from the beginning of the data buffer passed to the function,
  rather than after some initial metadata, which was previously causing incorrect
  version checks and potential misinterpretations of PDB debug information.
primer_glossary:
- term: PDB
  definition: Program Database, a file format used by Microsoft for storing debugging
    and project information.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: inlinee-lines signature
  definition: A specific identifier within the PDB format that marks the beginning
    of inlinee source line information, used for debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in ld/pdb.c where the inlinee-lines signature was read from the wrong memory location. The fix ensures the signature is read from the start of the payload, not from the first entry's file ID. Test cases have been updated to reflect this change and to flag linker failures as test failures, making the bug observable.
