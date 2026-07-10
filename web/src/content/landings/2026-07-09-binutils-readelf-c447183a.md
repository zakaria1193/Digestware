---
project: binutils
subsystem: binutils/readelf
patch_id: null
tags:
- binutils
- readelf
- ELF
- debugging
commit_hash: c447183ab0f32d0c2378e72cfd64f5e048b62cb4
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: Save and dump original section header values in readelf
tldr: readelf now saves and dumps original section header values for better debugging
  of corrupt ELF files.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit enhances `readelf` to preserve the original section header
  values before `validate_section_info` clears them. This is achieved by adding `orig_section_headers`
  to the `filedata` structure and introducing `save_original_section_header_values`.
  The original values can now be displayed, aiding in the analysis of malformed ELF
  files. A larger refactoring to use `sane_section_headers` instead of `section_headers`
  in more places was deferred.
primer_glossary:
- term: readelf
  definition: A utility in GNU Binutils that displays information about ELF (Executable
    and Linkable Format) files. It can show section headers, symbol tables, and other
    details about the object file.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like operating systems.
- term: section header
  definition: A structure within an ELF file that describes a section, such as code,
    data, or symbol tables. Section headers contain information like the section's
    name, type, size, and memory address.
- term: validate_section_info
  definition: A function within `readelf` that checks the integrity of section header
    information. It may clear or modify certain fields to prevent errors during further
    processing.
- term: filedata
  definition: A data structure used within `readelf` to hold information about the
    ELF file being processed, including section headers, symbol tables, and other
    metadata.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260709103152.733A64BA2E10@sourceware.org
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

The `readelf` utility now saves and dumps the original section header values before they are cleared during validation. This change helps in diagnosing issues with corrupt ELF files by making the 'garbage' values visible. New test files and an updated test script are included to verify this functionality.
