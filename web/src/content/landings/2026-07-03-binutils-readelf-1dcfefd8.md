---
project: binutils
subsystem: binutils/readelf
patch_id: null
tags:
- binutils
- readelf
- elf
- validation
- bugfix
commit_hash: 1dcfefd8dd49e32a9880a79c8fbb9276eaade23c
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: Update dynamic tag processing and validate section info.
tldr: readelf now counts DT_RELR relocations using dynamic tags and validates section
  header info to prevent segfaults.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch enhances `readelf`'s handling of relocations and section
  validation. It implements `count_relr_relocations` to use dynamic tags (DT_RELSZ,
  DT_RELASZ) for relocation counts, addressing PR binutils/34326. A new `validate_section_info`
  function is introduced to check and sanitize `sh_offset` and `sh_size` against file
  size, preventing segfaults as reported in PR binutils/34339. The scope extends to
  `get_32bit_section_headers` and `get_64bit_section_headers` in `binutils/readelf.c`
  and includes testsuite updates in `ld/`.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: dynamic tag
  definition: Tags within the ELF dynamic section (e.g., DT_RELR, DT_RELSZ) that provide
    information for dynamic linking and execution.
- term: section header
  definition: A structure in an ELF file that describes a section, containing information
    such as its name, type, and location in the file.
- term: DT_RELR
  definition: An ELF dynamic tag used to indicate the presence and location of relocation
    entries.
- term: sh_offset
  definition: A field in an ELF section header that specifies the offset of the section
    from the beginning of the file.
- term: sh_size
  definition: A field in an ELF section header that specifies the size of the section
    in bytes.
- term: segfault
  definition: A segmentation fault, an error that occurs when a program accesses a
    memory location that it is not allowed to access.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260703135427.958A44BA23C7@sourceware.org
date: '2026-07-03'
is_stub: false
stub_reason: ''
---

This update enhances `readelf`'s ability to process ELF files by accurately counting DT_RELR relocations using dynamic tags when section headers are unavailable. It also adds validation for section header offsets and sizes, preventing segfaults caused by out-of-range values. A side effect is the display of warnings for ignored invalid section data.
