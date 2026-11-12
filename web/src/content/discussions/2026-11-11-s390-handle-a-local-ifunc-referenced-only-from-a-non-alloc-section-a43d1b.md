---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- linker
- ifunc
- relocations
- debugging sections
discussion_id: 20261111110350.3761956-8-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 7/7] s390: handle a local IFUNC referenced only from a non-alloc section'
headline: 's390: handle a local IFUNC referenced only from a non-alloc section'
tldr: Fixes s390 linker to correctly handle local IFUNC symbols referenced from non-allocatable
  sections.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensures correct linking of local IFUNCs from non-allocatable sections on s390.
- Adds test cases to cover this specific scenario.
- Maintains consistency with how global symbols are handled.
exchanges: []
primer_expert: This patch series addresses a common problem across multiple architectures
  concerning the linking of `STT_GNU_IFUNC` symbols, specifically when they are local
  to an object file and only referenced from sections that are not intended for runtime
  allocation (e.g., `.debug_info`, `.comment`). The linker's relocation scan typically
  skips non-`SEC_ALLOC` sections. When an `IFUNC` is only present in such a section,
  the linker fails to find its PLT slot (or equivalent mechanism for indirect functions)
  and either aborts or mismanages the relocation. This patch for s390 implements a
  fix by ensuring th…
primer_glossary:
- term: s390
  definition: A 31-bit and 64-bit computer architecture family from IBM, used in their
    mainframe systems.
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format that represents an Indirect Function.
    IFUNCs allow for dynamic selection of function implementations at runtime, typically
    based on processor capabilities.
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to resolve external function calls.
- term: Non-alloc section
  definition: A section in an object file that is not loaded into memory when the
    program runs (e.g., debugging information sections). Marked by `SEC_ALLOC` flag
    being unset.
- term: Relocation
  definition: The process of updating symbolic references in an object file to absolute
    addresses when linking. Relocations contain information about which parts of the
    code need to be modified and how.
- term: SEC_ALLOC
  definition: A flag in BFD that indicates whether a section should be allocated memory
    when the program is loaded.
series_id: 'binutils:s390: handle a local ifunc referenced only from a non-alloc section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-8-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the s390 linker where local STT_GNU_IFUNC symbols referenced only from non-allocatable sections were not handled correctly. The relocation scan skips these sections, leading to incorrect linking behavior: either the link fails without a diagnostic, or an incorrect PLT slot is used. The fix ensures that these local IFUNCs are relocated against themselves, similar to how global symbols without PLT slots are handled, across both 31-bit and 64-bit s390 backends. New test cases are included to verify the fix.
