---
project: binutils
subsystem: bfd
patch_id: null
tags:
- security
- bfd
- coff
- xcoff
- linker
discussion_id: 20261006073641.1044917-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2] bfd: validate COFF and XCOFF symbol tables before the linker walks
  them'
headline: 'bfd: validate COFF and XCOFF symbol tables before the linker walks them'
tldr: Harshit Kumar submits a patch to validate COFF and XCOFF symbol tables in bfd
  to prevent buffer overflows when the linker processes them.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds runtime checks for symbol table parsing, potentially incurring a small performance
  overhead.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Submits a patch to validate COFF and XCOFF symbol tables in binutils'
    bfd library to prevent buffer overflows during linker processing.
  quote: null
primer_expert: This patch addresses a security vulnerability in the binutils BFD library
  concerning the parsing of COFF and XCOFF symbol tables. Specifically, it fixes potential
  buffer overflows in `cofflink.c` and `xcofflink.c` that occur when a symbol's auxiliary
  entry count exceeds the available data, leading to out-of-bounds writes.
primer_glossary:
- term: COFF
  definition: Common Object File Format, a standard file format for object files,
    executable files, and dynamic libraries.
- term: XCOFF
  definition: Extended Common Object File Format, an extension of COFF used on some
    Unix systems, notably AIX.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface within binutils
    for handling various object file formats.
- term: symbol table
  definition: A data structure within an object file that lists the symbols (e.g.,
    function names, variable names) defined or referenced by the file.
- term: auxiliary entries
  definition: Additional information associated with a symbol in some object file
    formats (like COFF) that provides further details, such as the number of external
    references.
- term: buffer overflow
  definition: A condition where a program attempts to write data beyond the allocated
    buffer's boundary, potentially corrupting adjacent memory or causing a crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261006073641.1044917-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

Harshit Kumar proposes a patch to enhance the robustness of the binutils linker by validating COFF and XCOFF symbol tables. The current implementation can lead to buffer overflows if a symbol claims more auxiliary entries than available, potentially causing heap writes. This patch addresses unvalidated paths in both COFF and XCOFF processing, building upon previous hardening efforts.
