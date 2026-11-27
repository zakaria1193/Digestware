---
project: binutils
subsystem: gprofng
patch_id: null
tags:
- binutils
- gprofng
- dwarf
- debugging
- compiler
discussion_id: 20261127094228.116909-1-claziss@gmail.com
source_type: public_inbox
title: '[committed 1/4] gprofng: Resolve DWARF 5 indexed string and address forms'
headline: 'gprofng: Correctly handle DWARF 5 indexed string and address forms'
tldr: gprofng now correctly interprets DWARF 5's indexed string and address forms,
  fixing issues with compilation unit names, directories, and PC ranges.
proposer: Claudiu Zissulescu <claziss@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 6
sentiment_score: 10
technical_tradeoffs:
- Accurate parsing of advanced DWARF 5 features improves debugging capabilities.
- Requires reading new sections and handling base offsets, increasing complexity.
exchanges:
- author: Claudiu Zissulescu <claziss@gmail.com>
  role: proposer
  position: Submitted a patch series to fix incorrect handling of DWARF 5 indexed
    string and address forms in gprofng.
  quote: Clang emits DW_FORM_strx* and DW_FORM_addrx* by default for DWARF 5. gprofng
    used the strx index as a byte offset into .debug_str and kept the addrx index
    as the address, so compilation unit names, directories and every PC range were
    wrong.
primer_expert: This series of commits addresses issues in `binutils`' `gprofng` profiler
  related to its DWARF 5 debug information parsing. Specifically, it corrects the
  interpretation of `DW_FORM_strx*` and `DW_FORM_addrx*` forms, which are used by
  compilers like Clang to represent strings and addresses via indices into dedicated
  sections (`.debug_str_offsets`, `.debug_addr`). Previously, `gprofng` misinterpreted
  these indices, leading to incorrect source location and function range information.
  The fix involves properly utilizing the `DW_AT_str_offsets_base` and `DW_AT_addr_base`
  attributes to resolve thes…
primer_glossary:
- term: gprofng
  definition: The next-generation version of the gprof performance analysis tool,
    part of the binutils package.
- term: DWARF 5
  definition: The fifth version of the DWARF debugging data format, which includes
    extensions for indexed string and address forms.
- term: DW_FORM_strx*
  definition: A DWARF debugging information form that represents a string index into
    the .debug_str section, using an offset base.
- term: DW_FORM_addrx*
  definition: A DWARF debugging information form that represents an address index
    into the .debug_addr section, using an offset base.
- term: DIE
  definition: Debug Information Entry, a fundamental unit of DWARF debugging information.
- term: .debug_str
  definition: A section in DWARF that stores string constants used in debugging information.
- term: .debug_str_offsets
  definition: A DWARF section that provides offsets into the .debug_str section for
    indexed string forms.
- term: .debug_addr
  definition: A DWARF section that stores addresses for indexed address forms.
- term: DW_AT_str_offsets_base
  definition: A DWARF attribute that specifies the base offset for indices into the
    .debug_str_offsets section.
- term: DW_AT_addr_base
  definition: A DWARF attribute that specifies the base offset for indices into the
    .debug_addr section.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261127094228.116909-1-claziss@gmail.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This commit corrects how gprofng handles DWARF 5's indexed string (DW_FORM_strx*) and address (DW_FORM_addrx*) forms. Previously, gprofng treated these indices as byte offsets or raw addresses, leading to incorrect compilation unit names, directories, and PC ranges. This resulted in "instructions without line numbers" and errors when trying to locate source files. The fix involves reading new DWARF sections (.debug_str_offsets, .debug_addr) and resolving indices using base attributes, ensuring accurate debugging information.
