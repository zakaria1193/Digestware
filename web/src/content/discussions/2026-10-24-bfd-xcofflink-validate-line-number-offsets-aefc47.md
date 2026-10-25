---
project: binutils
subsystem: bfd
patch_id: null
tags:
- security
- xcoff
- bfd
- linker
- vulnerability
discussion_id: 20261024065720.672471-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH] bfd: xcofflink: validate line-number offsets'
headline: 'bfd: xcofflink: validate line-number offsets'
tldr: Adds validation for line-number offsets in XCOFF files to prevent heap buffer
  overflows and misaligned reads.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves security by preventing heap overflows.
- Adds stricter validation, which might cause previously accepted but malformed inputs
  to fail linking.
- Increases robustness of XCOFF parsing.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes to validate line-number offsets in XCOFF files to prevent heap-buffer-overflows
    and misaligned reads, with new test cases.
  quote: Pass 1 now rejects a negative, misaligned, or out-of-table linoff. The rejection
    reports an error and sets bfd_error_bad_value. Pass 2 checks the first record
    and all *lineno_counts records against amt, the table size in bytes. The Pass
    2 check is defensive. Pass 1 already guarantees these bounds.
primer_expert: This patch addresses vulnerabilities in the XCOFF object file format
  parsing within the BFD library, specifically concerning line number information.
  The linker's `xcoff_link_add_symbols` and `xcoff_link_input_bfd` functions compute
  an `linoff` value. Incorrect values for `x_lnnoptr` (relative to `enclosing->line_filepos`)
  can result in invalid `linoff` values, leading to heap buffer overflows (reading
  before the table) or misaligned reads (reading across record boundaries) if not
  properly validated. The fix adds checks for negative, out-of-bounds, and misaligned
  `linoff` values.
primer_glossary:
- term: XCOFF
  definition: Extended Common Object File Format, a file format used on IBM AIX systems
    for executables, object files, and shared libraries.
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils to parse and manipulate various object file formats.
- term: linoff
  definition: Line number offset, a value used within XCOFF files to locate line number
    information relative to a base position.
- term: heap-buffer-overflow
  definition: A vulnerability that occurs when a program writes data beyond the allocated
    buffer on the heap, potentially corrupting adjacent memory or executing malicious
    code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024065720.672471-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This patch enhances the XCOFF linker in BFD by adding validation for line-number offsets. Previously, corrupt offsets (negative, past table end, or misaligned) could lead to heap buffer overflows or incorrect record reads. The changes ensure that line-number offsets are within valid bounds and properly aligned, preventing security vulnerabilities and ensuring correct linking. New test cases are added to verify these fixes.
