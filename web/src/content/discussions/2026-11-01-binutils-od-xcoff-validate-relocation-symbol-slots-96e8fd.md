---
project: binutils
subsystem: binutils
patch_id: null
tags:
- hardening
- XCOFF
- objdump
- security
- parsing
discussion_id: 20261101105139.573422-7-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 6/6] binutils: od-xcoff: validate relocation symbol slots'
headline: 'binutils: od-xcoff: validate relocation symbol slots'
tldr: Hardens XCOFF parsing by validating relocation symbol slots, preventing crashes
  from malformed auxiliary symbol data.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds complexity to parsing logic for robustness.
- Introduces a slight performance overhead for symbol validation.
- Requires careful testing to ensure all valid cases remain functional.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Introduces validation for XCOFF relocation symbol slots to prevent crashes
    caused by malformed auxiliary symbol data.
  quote: 'xcoff32_print_symbol checks symndx against nsyms, then dereferences syms[symndx].sym.name.  A
    relocation may name an auxiliary symbol slot; the union overlays sym.name with
    aux data, so a malformed aux record can turn that pointer into an arbitrary value.  objdump
    -P relocs then dereferences it and crashes (AddressSanitizer: SEGV).


    Track which symbol slots are primary records while reading the t…'
primer_expert: The final patch in this series focuses on hardening the `od-xcoff`
  dumper against malformed XCOFF files. It specifically targets how relocations refer
  to symbol slots. By differentiating between primary and auxiliary symbol entries,
  it prevents heap buffer overflows and segmentation faults that could occur when
  a relocation points to corrupted auxiliary data, ensuring that only valid symbol
  names are dereferenced.
primer_glossary:
- term: XCOFF
  definition: A file format used on IBM AIX systems, similar to COFF and ELF.
- term: relocation
  definition: Information in an object file that describes how to modify code or data
    addresses after linking.
- term: symbol slot
  definition: An entry in the symbol table of an object file, representing a variable,
    function, or other named entity.
- term: auxiliary symbol data
  definition: Additional information associated with a primary symbol entry in some
    object file formats, like XCOFF.
- term: objdump -P
  definition: A command-line option for `objdump` used to display relocation information.
series_id: 'binutils:binutils: od-xcoff: validate relocation symbol slots'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261101105139.573422-7-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch addresses a vulnerability in the XCOFF dumper where malformed auxiliary symbol data in relocations could lead to crashes. It tracks primary symbol slots and only prints symbol names for them, falling back to numeric indices for auxiliary slots. This prevents dereferencing invalid pointers and introduces tests to cover these scenarios.
