---
project: binutils
subsystem: binutils/readelf
patch_id: null
tags:
- readelf
- elf
- error handling
- bugfix
commit_hash: f94273aeb37908c32aa26530ff56e862f0060daf
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: Prevent GOT section dump on readelf errors.
tldr: readelf now avoids dumping GOT section contents if errors are encountered during
  file processing.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces error tracking (`seen_error`, `seen_elf_error`,
  `clear_elf_error`) in `elfcomm.c` and `elfcomm.h`. The `error` function now sets
  `seen_error` to true. Subsequently, `process_got_section_contents` in `readelf.c`
  returns early if `seen_elf_error` is true, preventing the dumping of GOT section
  data after an error has occurred. This addresses PR binutils/34473.
primer_glossary:
- term: readelf
  definition: A command-line utility that displays information about ELF (Executable
    and Linkable Format) files.
- term: GOT
  definition: Global Offset Table. A special section in position-independent code
    (PIC) executables and shared libraries used to indirectly reference global and
    static variables.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: PR binutils/34473
  definition: A specific bug report filed against the Binutils project, identified
    by its number (34473).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260806064038.159994B9DB6E@sourceware.org
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

The `readelf` utility will no longer dump the GOT (Global Offset Table) section if errors are detected during the parsing of an ELF file. This change prevents potentially misleading or corrupt output when the input file has structural issues.
