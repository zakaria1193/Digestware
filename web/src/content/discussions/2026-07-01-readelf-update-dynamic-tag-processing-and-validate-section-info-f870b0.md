---
project: binutils
subsystem: readelf
patch_id: null
tags:
- elf
- readelf
- security
- bugfix
- core-dump
discussion_id: CAMe9rOrB-Y5nRfgKAqjEjNZ3rG7Jxq-fnu7QgFUnzY-TpxxgEA@mail.gmail.com
source_type: public_inbox
title: 'Subject: [PATCH] readelf: Update dynamic tag processing and validate section
  info'
headline: 'readelf: Update dynamic tag processing and validate section info'
tldr: Improves readelf's handling of dynamic tags and section information, preventing
  crashes and providing better warnings for invalid data.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 10
technical_tradeoffs:
- Improves robustness against malformed files by ignoring invalid data, potentially
  hiding underlying issues that might be relevant for debugging.
- Adds warnings for previously unhandled out-of-range values, providing clearer diagnostics.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Introduces changes to `readelf` to handle dynamic tags more robustly and
    validate section information, preventing crashes and adding warnings for invalid
    data.
  quote: 'Count DT_RELR relocations using dynamic tags when section header isn''t

    used.  Ignore section sh_offset and sh_size if they are larger than file

    size.


    One side effect is that we now display


    readelf: Warning: Ignore the out of range sh_offset value of

    2199023261148 for section 17

    readelf: Warning: Ignore the out of range sh_size value of 13 for

    section 17 with sh_offset value of 2199023261148

    ...…'
- author: H.J. Lu
  role: proposer
  position: Provides updated information about the changes, emphasizing the handling
    of out-of-range section offset and size values.
  quote: 'Count DT_RELR relocations using dynamic tags when section header isn''t

    used.  Ignore section sh_offset and sh_size if they are larger than file

    size.


    One side effect is that we now display

    ...

    and segfault.'
primer_expert: This change to `readelf` improves its resilience to malformed ELF files
  by better handling dynamic tag processing, particularly for DT_RELR relocations,
  and by validating section header fields (`sh_offset`, `sh_size`) against the overall
  file size. Previously, excessively large values in these fields could lead to segfaults
  or incorrect output; this patch introduces checks to ignore such out-of-range values
  and provides informative warnings, improving the tool's diagnostic capabilities.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including headers,
    section details, symbol tables, and relocation entries.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: dynamic tag
  definition: Entries in the ELF dynamic section (e.g., DT_RELR) that provide information
    necessary for dynamic linking and runtime loading of executables and libraries.
- term: DT_RELR
  definition: An ELF dynamic tag that indicates the presence and location of the relocation
    array, often used in position-independent code (PIC) or for specific relocation
    types.
- term: section header
  definition: Metadata describing each section within an ELF file, including its name,
    size, offset in the file, and attributes.
- term: sh_offset
  definition: The file offset of the section's content.
- term: sh_size
  definition: The size of the section's content in bytes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOrB-Y5nRfgKAqjEjNZ3rG7Jxq-fnu7QgFUnzY-TpxxgEA@mail.gmail.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch enhances `readelf`'s robustness by updating its dynamic tag processing and introducing validation for section information. It now correctly counts DT_RELR relocations using dynamic tags when section headers are not present, and crucially, it ignores section `sh_offset` and `sh_size` values if they exceed the file size. This prevents segfaults and introduces warnings for out-of-range section data, improving diagnostic capabilities.
