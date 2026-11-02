---
project: binutils
subsystem: binutils
patch_id: null
tags:
- XCOFF
- memory-leak
- debugging
- hardening
- objdump
discussion_id: 20261101105139.573422-5-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 4/6] binutils: od-xcoff: fix traceback leak and .text lookup'
headline: 'binutils: od-xcoff: fix traceback leak and .text lookup'
tldr: Fixes a memory leak and improves .text section lookup in XCOFF traceback handling,
  preventing leaks and incorrect section association.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves memory safety and correctness.
- Adds complexity to section identification logic.
- Introduces specific tests for memory leak detection.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Corrects a memory leak and improves .text section lookup logic in XCOFF
    traceback dumping.
  quote: 'dump_xcoff32_traceback allocated the .text section buffer before looking
    for the STYP_TEXT section header.  If no STYP_TEXT section existed, the function
    returned early without freeing the buffer (AddressSanitizer / LeakSanitizer: leak).  Check
    for the section before allocating.


    The section lookup previously checked s_flags == STYP_TEXT, which missed sections
    that combine STYP_TEXT with another…'
primer_expert: This patch addresses two key issues in the `od-xcoff` dumper related
  to traceback processing. First, it prevents a memory leak by ensuring the `.text`
  section buffer is allocated only after the section is confirmed to exist. Second,
  it refines the logic for identifying the `.text` section to use both name matching
  and flag bit checking, resolving a discrepancy where the section used for symbol
  lookups might differ from the one used for traceback tags, thus improving accuracy
  and preventing data corruption.
primer_glossary:
- term: XCOFF
  definition: A file format used on IBM AIX systems, similar to COFF and ELF.
- term: traceback
  definition: Information used for debugging and stack unwinding, particularly in
    exception handling.
- term: memory leak
  definition: A situation where a program fails to release memory that is no longer
    needed, leading to increased memory consumption over time.
- term: .text section
  definition: The section in an object file that typically contains the executable
    code of a program.
- term: STYP_TEXT
  definition: A section type flag in some object file formats indicating that the
    section contains executable code.
- term: LeakSanitizer
  definition: A tool for detecting memory leaks, often integrated with AddressSanitizer.
series_id: 'binutils:binutils: od-xcoff: fix traceback leak and .text lookup'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261101105139.573422-5-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch addresses two issues in the XCOFF dumper's traceback handling: a memory leak and an incorrect association between the .text section and traceback tags. It now checks for the .text section before allocating memory, thus preventing leaks when the section is not found. The patch also refines the section lookup to correctly match by name and flag bits, ensuring symbols and tags are associated with the correct section.
