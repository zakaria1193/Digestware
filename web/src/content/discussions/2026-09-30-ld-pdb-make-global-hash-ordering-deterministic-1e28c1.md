---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- pdb
- linker
- reproducibility
- bugfix
discussion_id: 20260930193657.733-6-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] ld/pdb: Make globals hash ordering deterministic'
headline: 'ld/pdb: Make global hash ordering deterministic'
tldr: Ensures deterministic ordering of global symbols in PDB files by sorting on
  offset for hash collisions.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Slightly increases the complexity of the comparison function, but ensures consistent
  output.
exchanges: []
primer_expert: This patch addresses a reproducibility issue in the PDB generation
  for binutils' linker (ld). The `global_compare_hash` function is used to sort global
  symbols before writing them to the PDB file. When hash collisions occurred (multiple
  symbols yielding the same hash value), the original implementation treated them
  as equal, relying on the underlying `qsort` to determine their order. This behavior
  is non-deterministic across different architectures or compiler versions. The updated
  function now compares the `offset` of the symbols if their hashes are equal, providing
  a stable, reproducible or…
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft for storing debugging
    and project-related information for Microsoft Windows applications.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or shared library.
- term: hash
  definition: A function that converts an input into a fixed-size value, often used
    for indexing and searching.
- term: qsort
  definition: A standard library function for sorting arrays.
- term: symbol
  definition: An identifier for a memory location, such as a variable or function
    name.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-6-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch makes the ordering of global symbols within PDB files deterministic by introducing a secondary sort key. Previously, when multiple global symbols had the same hash value, their relative order was left to the host system's `qsort` implementation, leading to inconsistencies. The change modifies the `global_compare_hash` function to use the symbol's record offset as a tie-breaker, ensuring reproducible PDB output across different platforms.
