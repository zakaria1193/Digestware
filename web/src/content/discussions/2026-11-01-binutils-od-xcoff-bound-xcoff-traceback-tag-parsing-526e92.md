---
project: binutils
subsystem: binutils
patch_id: null
tags:
- hardening
- XCOFF
- objdump
- parsing
- security
discussion_id: 20261101105139.573422-6-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 5/6] binutils: od-xcoff: bound XCOFF traceback tag parsing'
headline: 'binutils: od-xcoff: bound XCOFF traceback tag parsing'
tldr: Hardens XCOFF parsing by bounding traceback tag parsing, preventing heap buffer
  overflows from malformed input.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases parsing code complexity for better safety.
- May incur a minor performance cost due to extra checks.
- Adds new test cases to ensure robustness.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Implements bounds checking for XCOFF traceback tag parsing to prevent
    heap buffer overflows.
  quote: 'dump_xcoff32_tbtags parses the traceback table that follows an XCOFF function
    body.  The parsing loop and several optional fields advanced an offset through
    the section buffer without checking against the section size.  A malformed traceback
    tag could read past the allocated buffer (AddressSanitizer: heap-buffer-overflow).


    Stop the scan when fewer than 4 bytes remain for the next zero word, and…'
primer_expert: This patch in the `od-xcoff` hardening series adds bounds checking
  to the parsing of XCOFF traceback tags. It prevents heap overflows by validating
  offsets and lengths against the available section size. The changes ensure that
  malformed tag data, including issues with symbol values relative to the `.text`
  section and various optional fields, is handled gracefully without corrupting memory.
  New test cases are included to cover these scenarios.
primer_glossary:
- term: XCOFF
  definition: A file format used on IBM AIX systems, similar to COFF and ELF.
- term: traceback table
  definition: A section in an object file that contains information used for debugging
    and stack unwinding, especially for exceptions.
- term: heap buffer overflow
  definition: A vulnerability where a program writes data beyond the allocated buffer
    in the heap, potentially corrupting adjacent memory.
- term: .text section
  definition: The section in an object file that typically contains the executable
    code of a program.
series_id: 'binutils:binutils: od-xcoff: bound xcoff traceback tag parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261101105139.573422-6-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch enhances the robustness of the XCOFF dumper by adding bounds checking to the traceback tag parsing. Previously, malformed traceback tags could lead to heap buffer overflows by reading past the allocated buffer. The changes ensure that parsing stops if fewer than 4 bytes remain for critical data and validate all optional fields against the remaining section size.
