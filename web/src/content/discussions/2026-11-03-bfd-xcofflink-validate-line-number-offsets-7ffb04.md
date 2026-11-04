---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- XCOFF
- linker
- security
- memory safety
discussion_id: 20261103160737.2401392-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2] bfd: xcofflink: validate line-number offsets'
headline: 'bfd: xcofflink: validate line-number offsets'
tldr: Patch adds validation for line-number offsets in XCOFF linking to prevent heap
  buffer overflows and other memory errors.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Improves security and robustness by adding validation checks, which may cause previously
  accepted but malformed inputs to now fail linking.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Submits a patch to validate line-number offsets in XCOFF linking to prevent
    heap buffer overflows and other memory corruption issues.
  quote: In the old signed variable, a value below line_filepos became negative. Pass
    1 accepted a negative linoff. Pass 1 then read the first record before the start
    of the table. The read is a heap-buffer-overflow. A misaligned linoff can make
    the scan read a record that starts inside the table and ends past it. Pass 2 had
    no bounds check.
primer_expert: 'The XCOFF linker implementation in binutils is being hardened against
  malformed line-number offsets within XCOFF object files. Corrupt `x_lnnoptr` values,
  when subtracted from `enclosing->line_filepos`, can result in an unsigned `linoff`
  that wraps around or exceeds the bounds of the line-number table. This was previously
  handled by silently skipping line number information or by causing heap buffer overflows
  and out-of-bounds reads. The proposed changes introduce explicit checks in both
  linking passes: Pass 1 now rejects negative, misaligned, or out-of-bounds offsets,
  and Pass 2 performs def…'
primer_glossary:
- term: XCOFF
  definition: Extended Common Object File Format, a file format used for executables,
    object files, shared libraries, and core dumps, particularly on IBM AIX systems.
- term: bfd
  definition: The Binary File Descriptor library, a GNU library used by binutils components
    to provide a common interface to various object file formats.
- term: linker
  definition: A program that combines various object files and libraries into a single
    executable file or library.
- term: line-number offsets
  definition: Pointers or offsets within an object file's debugging information section
    that indicate the location of line number records.
- term: heap buffer overflow
  definition: A type of software vulnerability that occurs when a program writes data
    beyond the allocated buffer in the heap memory, potentially corrupting adjacent
    data or executing arbitrary code.
- term: uint64_t
  definition: An unsigned integer type that occupies 64 bits of memory.
- term: Pass 1
  definition: The first stage of the linking process, often responsible for symbol
    resolution and initial section processing.
- term: Pass 2
  definition: The second stage of the linking process, typically handling relocation
    processing and final output generation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261103160737.2401392-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This patch enhances binutils' XCOFF linker by adding validation for line-number offsets. Previously, corrupt offsets could lead to heap buffer overflows or out-of-bounds reads by causing `linoff` to wrap around or misalign. The patch modifies the linking passes to reject invalid offsets, reporting errors and setting `bfd_error_bad_value`. New tests are added to verify correct handling of malformed offsets, ensuring that invalid inputs result in link-time errors without crashing.
