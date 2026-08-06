---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- error-handling
- ELF
discussion_id: CAMe9rOpDwQ-N9Up3yNqzyOnb1hi+pyiSnzA5VZEtSGR=R4B69A@mail.gmail.com
source_type: public_inbox
title: '[PATCH] readelf: Don''t dump GOT section after seeing error'
headline: 'readelf: Don''t dump GOT section after seeing error'
tldr: Fixes readelf to stop dumping the GOT section if it encounters errors while
  parsing the input file.
proposer: H.J. Lu
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: H.J. Lu
  role: proposer
  position: Submits a patch to prevent readelf from dumping the GOT section after
    encountering errors, improving error handling.
  quote: 'Don''t dump GOT section contents after seeing errors in input:


    readelf: Error: Section 10 has invalid sh_entsize of 0

    readelf: Error: (Using the expected size of 18 for the rest of this dump)

    readelf: Error: Too many program headers - 0x3030 - the file is not that big'
primer_expert: The `readelf` utility, part of binutils, is being modified to improve
  its error handling. Specifically, when `readelf` encounters critical errors during
  the parsing of an ELF file (e.g., incorrect section headers, malformed program headers),
  it should now gracefully stop attempting to dump certain sections, like the GOT,
  rather than proceeding and potentially producing misleading or further erroneous
  output. This change introduces a simple error-tracking mechanism within the ELF
  parsing functions.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files.
- term: GOT
  definition: Global Offset Table. A table used by position-independent code to store
    addresses of global variables and functions.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, shared libraries, and core dumps on Unix-like systems.
- term: sh_entsize
  definition: Section header entry size. A field in the ELF section header that specifies
    the size of each entry in a section, applicable to sections like symbol tables
    or string tables.
- term: program headers
  definition: Structures in an ELF file that describe how the operating system should
    load the program into memory.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpDwQ-N9Up3yNqzyOnb1hi+pyiSnzA5VZEtSGR=R4B69A@mail.gmail.com
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

This patch for `readelf` prevents it from attempting to dump the GOT (Global Offset Table) section if it has already encountered errors during file parsing. This addresses an issue where `readelf` would continue processing and potentially produce corrupted output or further errors after detecting problems like invalid section sizes or an excessive number of program headers. A new flag `seen_error` is introduced to track errors.
