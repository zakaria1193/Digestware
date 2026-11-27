---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- DWARF
- fuzzing
- crash fix
- parser
commit_hash: fc9fb2983d1953f2b2984f8d3c498966cd592312
source_type: public_inbox
author: Alan Modra <amodra@gmail.com>
headline: 'binutils: Fix DWARF parsing segfaults from fuzzed objects'
tldr: 'binutils: DWARF parsing now robust against malformed input, preventing segfaults.'
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `insert_element_in_list` function and its callers (`get_or_create_enum_constant`,
  `get_or_create_subrange_type`) in `dwarf.c` relied on the assumption that DWARF
  list pointers (e.g., `enum_type_list`, `tab_type_list`) were correctly set up by
  prior tags. Fuzzed inputs violate these ordering invariants, causing NULL pointer
  dereferences. The commit removes these assumptions and associated assertions, making
  the parsing more tolerant of malformed DWARF data.
primer_glossary:
- term: DWARF
  definition: A standard debugging data format used by many compilers and debuggers
    to represent information about program variables, types, and structure in a portable
    way.
- term: tag
  definition: In DWARF, a tag is a DW_TAG_* value that identifies the type of debugging
    information entry, such as DW_TAG_enumeration_type or DW_TAG_array_type.
- term: NULL pointer dereference
  definition: An attempt to access memory at a NULL address, which typically results
    in a program crash (segmentation fault).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261127033206.6732B4436DE2@sourceware.org
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

The binutils DWARF parser has been hardened against malformed input that could lead to segmentation faults. Specifically, functions like `get_or_create_enum_constant` and `get_or_create_subrange_type` previously assumed correct ordering of DWARF tags, which fuzzed inputs violated. Assertions that incorrectly declared these invalid states as impossible have also been removed, improving robustness.
