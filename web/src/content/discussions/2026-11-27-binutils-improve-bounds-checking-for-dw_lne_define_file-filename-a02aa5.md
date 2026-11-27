---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- readelf
- dwarf
- security
- vulnerability
discussion_id: 203ee8f9-ec34-4c6d-b885-b95723aace63@suse.com
source_type: public_inbox
title: 'Re: [PATCH] binutils: validate DW_LNE_define_file filename bounds'
headline: 'binutils: Improve bounds checking for DW_LNE_define_file filename'
tldr: Reviewer agrees with a patch to fix heap-buffer-overflow in readelf by validating
  filename bounds in DW_LNE_define_file, but suggests improvements and asks abo…
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixes a security vulnerability by improving input validation.
- Introduces minor code style adjustments and maintains robustness.
exchanges:
- author: Alhuda Khan
  role: proposer
  position: Submitted a patch to fix a heap-buffer-overflow in `readelf` by validating
    filename bounds within `DW_LNE_define_file` opcodes.
  quote: 'readelf -wL can read past the end of the .debug_line buffer on a malformed

    DWARF line program. In display_debug_lines_decoded(), the DW_LNE_define_file

    opcode reads the file name with an unbounded strlen() on op_code_data. If the

    name has no terminating NUL before the end of the opcode payload - which can

    happen once the section is decompressed into an exact-size heap allocation -

    strlen() runs o…'
- author: Jan Beulich <jbeulich@suse.com>
  role: maintainer
  position: Agreed with the patch's goal but suggested code improvements and inquired
    about AI involvement in its development.
  quote: 'This wants to be the description of the patch (rather than leaving it empty).


    The patch is attached. It uses memchr() bounded by op_code_end to find the

    terminator, and if there isn''t one it warns and stops processing that opcode

    instead of walking past the end.


    This wants to be the description of the patch (rather than leaving it empty).
    [...] I''ll make these adjustments and get the patch in.'
primer_expert: This discussion concerns a security vulnerability in `binutils`' `readelf`
  utility, specifically when parsing DWARF debugging information's line number program.
  The issue is a heap-buffer-overflow triggered by malformed `DW_LNE_define_file`
  opcodes that lack a null-terminated string for the filename. The proposed fix uses
  a bounded `memchr` to find the string terminator, preventing out-of-bounds reads.
  The reviewer also comments on code style and asks about the use of AI in development.
primer_glossary:
- term: readelf
  definition: A utility in the binutils package that displays information about ELF
    (Executable and Linkable Format) files, including debugging information.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about source code, variables, and execution flow.
- term: line number program
  definition: A part of the DWARF debugging information that maps machine code addresses
    to source code lines.
- term: DW_LNE_define_file
  definition: A DWARF line number statement opcode used to associate a file name with
    subsequent debugging information.
- term: heap-buffer-overflow
  definition: A security vulnerability where a program writes data beyond the allocated
    buffer in the heap, potentially corrupting adjacent memory or control structures.
- term: ASan
  definition: AddressSanitizer, a fast memory error detector for C/C++ that finds
    use-after-free, buffer overflows, and other memory errors.
- term: memchr
  definition: A C standard library function that searches for the first occurrence
    of a character within a given block of memory.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/203ee8f9-ec34-4c6d-b885-b95723aace63@suse.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

A reviewer has evaluated a patch for binutils that aims to fix a heap-buffer-overflow vulnerability in `readelf -wL`. The vulnerability occurred because the `DW_LNE_define_file` opcode in DWARF line programs could read past the end of the buffer if a filename lacked a null terminator. The reviewer agrees with the proposed fix, which uses `memchr` with a boundary check, but suggests several minor improvements to the code and asks about the extent of AI involvement in the patch's creation.
