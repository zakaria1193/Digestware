---
project: binutils
subsystem: binutils
patch_id: null
tags:
- XCOFF
- hardening
- objdump
- parsing
- security
discussion_id: 20261101105139.573422-4-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 3/6] binutils: od-xcoff: bound XCOFF loader section parsing'
headline: 'binutils: od-xcoff: bound XCOFF loader section parsing'
tldr: Hardens XCOFF parsing by bounding loader section parsing, preventing out-of-bounds
  reads in symbol, relocation, and string tables.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases parsing robustness at the cost of slightly more complex code.
- Adds overhead for validation checks.
- Requires new test cases for comprehensive coverage.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Implements bounds checking for XCOFF `.loader` section parsing to prevent
    out-of-bounds reads.
  quote: 'dump_xcoff32_loader parsed the .loader section without checking entry counts
    or string offsets against the section size.  A malformed loader section could
    cause out-of-bounds reads in the symbol table, relocation table, import file list,
    or string table.


    Validate that the section is at least as large as the header.  Report a too-short
    section with non_fatal so the diagnostic goes to stderr inste…'
primer_expert: This patch strengthens the `od-xcoff` dumper's resilience against malformed
  XCOFF files by validating the `.loader` section. It ensures that offsets, counts,
  and string lookups within this section are within bounds, preventing heap overflows
  and crashes. The changes include better error reporting using `non_fatal` and guarantee
  that allocated memory is freed on error paths, with new test cases covering various
  malformed input scenarios.
primer_glossary:
- term: XCOFF
  definition: A file format used on IBM AIX systems, similar to COFF and ELF.
- term: .loader section
  definition: A section in an XCOFF object file that contains information related
    to dynamic linking and loading.
- term: out-of-bounds read
  definition: An attempt to access memory outside the allocated buffer, which can
    lead to data corruption or crashes.
- term: string table
  definition: A section in an object file that stores string literals, often used
    for symbol names or other text data.
series_id: 'binutils:binutils: od-xcoff: bound xcoff loader section parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261101105139.573422-4-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch enhances the robustness of the XCOFF dumper by adding bounds checking to the parsing of the `.loader` section. Previously, malformed loader sections could lead to out-of-bounds reads in various tables (symbol, relocation, import, string) due to unchecked entry counts and offsets. The changes validate section size, fit, and string table access, with improved error reporting and resource cleanup.
