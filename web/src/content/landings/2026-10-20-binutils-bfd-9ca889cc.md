---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- linker
- ELF
- bugfix
commit_hash: 9ca889ccf1da85afa5e1e662a423bd90eb867430
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix DT_GNU_HASH symoffset for empty tables
tldr: Correctly calculates the symoffset for ELF DT_GNU_HASH tables with no exported
  symbols.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The DT_GNU_HASH table in ELF objects uses `symoffset` to denote the
  number of non-exported dynamic symbols that precede the hashed, exported symbols.
  When no symbols are exported, binutils previously generated an "empty" table with
  a fixed `symoffset` of 1. This commit corrects `elflink.c` to properly calculate
  `symoffset` in this edge case, ensuring all non-hashed symbols are accounted for,
  aligning with PR 34736.
primer_glossary:
- term: DT_GNU_HASH
  definition: A section in an ELF executable or shared library that provides a hashed
    index for dynamic symbols, enabling faster lookups of exported symbols by the
    dynamic linker.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: dynamic symbol table
  definition: A symbol table within an ELF file that lists symbols (functions, variables)
    that are visible to the dynamic linker at runtime. This includes both exported
    (public) and imported (private) symbols.
- term: symoffset
  definition: A field within the DT_GNU_HASH table header that indicates the index
    of the first exported (hashed) symbol in the dynamic symbol table. It effectively
    counts the number of non-exported symbols.
discussion_id_link: public_inbox:binutils#34736
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261020231520.0DE5D4BA2E28@sourceware.org
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This change corrects how binutils generates ELF DT_GNU_HASH tables when there are no exported symbols. Previously, an empty table incorrectly set the symoffset to 1, assuming only a single special symbol. The fix ensures symoffset accurately reflects the count of non-hashed, non-exported dynamic symbols, addressing a bug where these symbols might be omitted.
