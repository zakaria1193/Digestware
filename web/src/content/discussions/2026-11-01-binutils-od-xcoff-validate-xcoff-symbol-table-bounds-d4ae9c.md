---
project: binutils
subsystem: binutils
patch_id: null
tags:
- XCOFF
- hardening
- objdump
- security
- parsing
discussion_id: 20261101105139.573422-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/6] binutils: od-xcoff: validate XCOFF symbol table bounds'
headline: 'binutils: od-xcoff: validate XCOFF symbol table bounds'
tldr: Hardens XCOFF parsing by validating symbol table bounds, preventing heap buffer
  overflows from malformed auxiliary record counts.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves robustness and security against malformed input.
- Adds complexity to the symbol table parsing code.
- New test cases are introduced to verify the fixes.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Validates XCOFF symbol table bounds to prevent heap buffer overflows caused
    by malformed auxiliary record counts.
  quote: 'xcoff32_read_symbols reads each symbol''s auxiliary records into &s[j +
    1].aux, advancing by e_numaux entries.  If a symbol claims more auxiliary entries
    than remain in the table, the read writes an 18-byte auxiliary record past the
    end of the allocated data->syms array (AddressSanitizer: heap-buffer-overflow)
    before any dump pass.  objdump''s standalone XCOFF dumper parses the format itself
    and th…'
primer_expert: This is the first patch in a series hardening the `od-xcoff` dumper.
  It specifically targets the symbol table parsing logic. By validating the `e_numaux`
  field against the available entries and adding file-size and pointer-wrap checks,
  it prevents heap buffer overflows that could occur with malformed XCOFF files. The
  changes ensure that the dumper's own parsing is as robust as the linker's entry
  points, complemented by new test cases for various boundary conditions.
primer_glossary:
- term: XCOFF
  definition: A file format used on IBM AIX systems, similar to COFF and ELF.
- term: symbol table
  definition: A table within an object file that lists the symbols (functions, variables)
    defined or referenced by the file.
- term: auxiliary records
  definition: Additional data associated with a symbol entry in some object file formats,
    providing more details.
- term: heap buffer overflow
  definition: A vulnerability where a program writes data beyond the allocated buffer
    in the heap, potentially corrupting adjacent memory.
- term: string table
  definition: A section in an object file that stores string literals, often used
    for symbol names or other text data.
series_id: 'binutils:binutils: od-xcoff: validate xcoff symbol table bounds'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261101105139.573422-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch addresses a heap buffer overflow vulnerability in the XCOFF dumper's symbol table parsing. It validates the number of auxiliary records claimed by each symbol against the remaining entries in the table, preventing out-of-bounds writes. The patch also adds file-size bounds checks, 32-bit pointer wrap protection, and string table termination, with new tests to cover these scenarios.
