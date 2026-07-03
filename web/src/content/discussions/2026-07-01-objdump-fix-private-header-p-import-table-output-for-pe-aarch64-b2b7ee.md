---
project: binutils
subsystem: objdump
patch_id: null
tags:
- binutils
- objdump
- PE
- import table
- aarch64
discussion_id: aad43dfe-4fb2-407c-9380-259b44c0422e@suse.com
source_type: public_inbox
title: 'Re: [PATCH] objdump: Fix private header (''-p'') import table output for pe-aarch64'
headline: 'objdump: Fix private header (''-p'') import table output for pe-aarch64'
tldr: Confirms a fix for truncated import table output in objdump for PE files on
  64-bit architectures.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures correct display of import tables for 64-bit PE files, improving debugging
  accuracy.
- Maintains code style by adhering to line length limits.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Approves the revised patch, confirming it resolves the issue of truncated
    import table output for PE files on 64-bit architectures and meets code formatting
    standards.
  quote: null
primer_expert: This discussion concerns a fix for the `objdump` tool within binutils,
  specifically targeting the display of import tables for PE (Portable Executable)
  files on 64-bit architectures like aarch64. The original issue was that the import
  lookup table entries, which are 64-bit in PE32+ files, were being truncated to 32-bit,
  leading to incomplete output. The patch, proposed by Jon Turney, correctly identifies
  PE32+ files and ensures that objdump reads and prints the 64-bit import table entries,
  resolving the truncation problem. Beulich's comments confirm the fix and suggest
  formatting improvements.
primer_glossary:
- term: objdump
  definition: A utility in the GNU Binutils package that displays information from
    object files, including disassembled code and symbol tables.
- term: PE file
  definition: Portable Executable file format, used for executables, DLLs, and object
    files on Windows systems.
- term: import table
  definition: A table in a PE executable that lists the dynamic library functions
    the program needs to call.
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: PE32+
  definition: The 64-bit version of the PE file format.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aad43dfe-4fb2-407c-9380-259b44c0422e@suse.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

Jan Beulich LGTMs a revised patch that addresses an issue where objdump's private header (`-p`) output for PE files on 64-bit architectures (like aarch64) was truncated, showing only the first import. The fix correctly distinguishes between PE32 (32-bit) and PE32+ (64-bit) formats, ensuring that 64-bit import lookup table entries are properly handled. The revised patch also adheres to 80-column line length limits.
