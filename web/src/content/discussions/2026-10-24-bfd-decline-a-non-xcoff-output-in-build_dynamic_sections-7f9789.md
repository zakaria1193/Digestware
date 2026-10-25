---
project: binutils
subsystem: bfd
patch_id: null
tags:
- security
- aix
- bfd
- linker
- vulnerability
discussion_id: 20261024095819.1905597-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/3] bfd: decline a non-XCOFF output in build_dynamic_sections'
headline: 'bfd: decline a non-XCOFF output in build_dynamic_sections'
tldr: Prevents heap read overflows in AIX linker emulations by ensuring `bfd_xcoff_build_dynamic_sections`
  only runs for XCOFF outputs.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a heap read overflow vulnerability.
- Ensures correct function dispatch based on output file format.
- Improves robustness of AIX emulation linking.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes to add a guard in `bfd_xcoff_build_dynamic_sections` to ensure
    it only runs for XCOFF outputs, preventing out-of-bounds reads when non-XCOFF
    formats are selected.
  quote: The AIX emulations allow a linker script to select a non-XCOFF output format
    via OUTPUT_FORMAT (such as elf32-little). When that happens, the link hash table
    is a generic bfd_link_hash_table, not the larger xcoff_link_hash_table.
primer_expert: This patch addresses a vulnerability where the `bfd_xcoff_build_dynamic_sections`
  function, which expects an `xcoff_link_hash_table`, can be called even when the
  linker script has selected a generic ELF output format. In such cases, a generic
  `bfd_link_hash_table` is used, and accessing `xcoff_hash_table(info)` results in
  an out-of-bounds read. The fix adds a check at the beginning of the function to
  ensure `bfd_get_flavour(output_bfd)` is `bfd_target_xcoff_flavour` before proceeding,
  mirroring a similar guard in `bfd_xcoff_size_dynamic_sections`.
primer_glossary:
- term: XCOFF
  definition: Extended Common Object File Format, a file format used on IBM AIX systems.
- term: bfd
  definition: The Binary File Descriptor library, used by GNU Binutils for object
    file manipulation.
- term: link hash table
  definition: A data structure used by the linker to store and quickly access symbol
    information.
- term: heap read overflow
  definition: A security vulnerability where a program reads data beyond the allocated
    buffer on the heap, potentially accessing sensitive information or causing crashes.
- term: OUTPUT_FORMAT
  definition: A linker script command used to specify the output file format.
series_id: 'binutils:bfd: decline a non-xcoff output in build_dynamic_sections'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024095819.1905597-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This patch prevents heap read overflows in AIX linker emulations by adding a check to `bfd_xcoff_build_dynamic_sections`. The function previously ran even when a linker script specified a non-XCOFF output format (like `elf32-little`), leading to out-of-bounds reads when accessing the link hash table. The fix ensures this function only operates on XCOFF outputs, aligning with existing guards in related functions.
