---
project: binutils
subsystem: coff
patch_id: null
tags:
- binutils
- coff
- security
- vulnerability
- linker
discussion_id: loopr.48.mwpeazscidun@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] COFF: Validate auxiliary x_endndx bounds'
headline: 'COFF: Validate auxiliary x_endndx bounds'
tldr: Patch to validate the bounds of COFF auxiliary entries' x_endndx field to prevent
  out-of-bounds reads in the linker.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alhuda Khan <alhuda@research.digiscrypt.com>
  role: proposer
  position: Submits a patch to validate the `x_endndx` bounds in COFF auxiliary entries
    to prevent an out-of-bounds read in the linker.
  quote: Reject COFF tag auxiliary entries whose x_endndx exceeds the input object's
    raw symbol-table entry count. Without this validation, a malformed COFF object
    can cause an out-of-bounds read while processing tag symbols in _bfd_coff_link_input_bfd.
    Check the index before calculating the end pointer used by the symbol-processing
    loop.
primer_expert: This patch for binutils/coff addresses a heap-buffer-overflow read
  vulnerability in `_bfd_coff_link_input_bfd` (specifically `_bfd_pex64i_swap_sym_in`).
  A malformed COFF file with an out-of-bounds `x_endndx` in an auxiliary entry can
  cause the linker to read past the allocated symbol table buffer. The fix validates
  this index before it's used in loop calculations.
primer_glossary:
- term: COFF
  definition: Common Object File Format; a widely used executable and object file
    format, particularly on older versions of Unix and Windows systems.
- term: auxiliary entries
  definition: In the context of COFF files, these entries provide additional information
    related to symbols, such as type information or relocation data.
- term: x_endndx
  definition: A field within a COFF auxiliary entry that likely indicates the end
    index or count related to a symbol or group of symbols.
- term: symbol-table
  definition: A data structure within an object file that stores information about
    the symbols (e.g., function names, variable names) defined or referenced in the
    code.
- term: out-of-bounds read
  definition: An error condition where a program attempts to access memory outside
    the allocated buffer, which can lead to crashes or security vulnerabilities.
- term: AddressSanitizer
  definition: A fast memory error detector for C/C++. It finds uses of memory after
    free, the use of uninitialized memory, and buffer overflows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.48.mwpeazscidun@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch addresses an out-of-bounds read vulnerability in the COFF linker related to auxiliary entries. The issue arises when a malformed COFF object has an `x_endndx` value that exceeds the symbol table's bounds. The proposed fix adds validation to reject such entries, preventing the crash during symbol processing. The reproducer involves linking a specific 'tag-bad.o' file, which triggers an AddressSanitizer error without the patch.
