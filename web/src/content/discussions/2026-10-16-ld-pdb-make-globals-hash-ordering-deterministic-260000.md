---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- linker
- PDB
- determinism
- symbols
- debugging
discussion_id: 6902ab2b-57e5-4f31-a0b5-b9c03c80ead8@suse.com
source_type: public_inbox
title: 'Re: [PATCH] ld/pdb: Make globals hash ordering deterministic'
headline: 'ld/pdb: Make globals hash ordering deterministic'
tldr: Ensures deterministic ordering of global symbols in PDB files by sorting colliding
  hashes by symbol offset.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves PDB file reproducibility, beneficial for debugging and build automation.
- Slightly increases the complexity of the sorting logic in `pdb.c`.
- No negative performance impact is expected; sorting is done during the linking phase.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Modified global_compare_hash to sort colliding hashes by symbol-record
    offset for deterministic PDB output.
  quote: 'global_compare_hash treated entries with colliding hashes as equal, leaving
    their relative order to the host qsort implementation.  Sort

    collisions by symbol-record offset so PDB output is reproducible across

    hosts.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the change and approves it.
  quote: Okay.
primer_expert: This change addresses non-determinism in the PDB writer within the
  GNU linker (`ld`). Specifically, when multiple global symbols hash to the same value,
  their relative order in the PDB file was previously determined by the unstable `qsort`
  implementation of the host system. By adding a secondary sort key based on the symbol's
  offset within the object file, this patch ensures that the PDB output is consistent
  regardless of the host environment, which is crucial for reproducible builds and
  reliable debugging.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft's compilers and debuggers
    to store information about program symbols and types, often used for debugging
    C/C++ code.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: global symbols
  definition: Symbols (like function names or global variables) that are visible across
    different object files and libraries.
- term: hash collision
  definition: When two different inputs produce the same hash output. In this context,
    two different symbols have the same hash value.
- term: qsort
  definition: The standard C library function for sorting arrays. Its behavior for
    equal elements can be implementation-defined.
- term: symbol record offset
  definition: The position of a symbol's definition or reference within the symbol
    table of an object file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/6902ab2b-57e5-4f31-a0b5-b9c03c80ead8@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

Oleg Tolmatcev's patch modifies the `global_compare_hash` function in `ld/pdb.c` to ensure deterministic ordering of global symbols in PDB files. Previously, symbols with colliding hash values were ordered by the host's `qsort` implementation, leading to non-reproducible output. The change now sorts these collisions by their symbol record offset, guaranteeing consistent output across different hosts.
