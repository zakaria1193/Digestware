---
project: binutils
subsystem: readelf
patch_id: null
tags:
- binutils
- readelf
- debugging
- elf
discussion_id: CAMe9rOrai4QD0Jq52-Zsd=hBNe9k2KnaqLZ7022yW=+8n_dX9w@mail.gmail.com
source_type: public_inbox
title: 'readelf: Save and dump the original section header values'
headline: 'readelf: Save and dump original section header values'
tldr: Preserve and display original section header values in readelf to aid debugging
  of malformed object files.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds memory overhead to store original section header data, but this is managed
  by on-demand allocation.
- Improves debuggability of malformed object files at the cost of slightly increased
  complexity in `readelf`.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes to save and dump original section header values in readelf to
    make garbage values visible for debugging malformed object files, modifying the
    approach to save original values on demand.
  quote: validate_section_info clears the garbage values in the section header to
    avoid crash later. Save and dump the original section header values to make the
    garbage values in the section header visible when dumping section headers.
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Suggests an alternative approach where a separate structure holds "sane"
    section headers, allocating entries only when corrections are needed, rather than
    always storing original values.
  quote: I think this would be better done the other way around. ie. have a Elf_Internal_Shdr
    **sane_section_headers that is initialised to point at entries in section_headers,
    with sane_section_headers[i] allocated as necessary when needing to correct a
    bogus header.
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Rejects the alternative approach due to complexity, opting instead to
    modify the `orig_section_headers` to be allocated on demand.
  quote: I have thought about something similar and decided against it since filedata->section_headers
    is used in many places. However, I can change filedata->orig_section_headers to
    on demand.
primer_expert: This series of patches for `readelf` aims to improve debugging of malformed
  object files by preserving and displaying original section header data. The `validate_section_info`
  function currently cleans up bad data, obscuring the original issue. The proposal
  introduces `orig_section_headers` to store the initial values, allowing them to
  be shown when `readelf` dumps section header information. A discussion occurred
  regarding the best way to manage this data, with a preference for on-demand allocation
  over a separate "sane" structure.
primer_glossary:
- term: readelf
  definition: A utility program that displays information about ELF (Executable and
    Linkable Format) files, including sections, symbols, and relocation entries.
- term: section header
  definition: A structure within an ELF file that describes a section, such as its
    name, type, load address, and size.
- term: malformed object files
  definition: Object files (like ELF or PE/COFF) that do not strictly adhere to their
    defined format, often containing incorrect or corrupt data.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps used in most Unix-like systems.
- term: validate_section_info
  definition: A function within binutils' readelf that checks and potentially corrects
    or sanitizes section header information.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOrai4QD0Jq52-Zsd=hBNe9k2KnaqLZ7022yW=+8n_dX9w@mail.gmail.com
bugzilla_url: null
date: '2026-07-04'
is_stub: false
stub_reason: ''
---

This patch for readelf introduces functionality to save and display the original, potentially garbage, section header values before they are cleaned up or validated. This is intended to aid debugging by making inconsistent or incorrect header data visible when dumping section headers, helping to diagnose issues in malformed object files. The changes involve adding a new field to store these original values and a function to save them, with a modification to clear this storage on demand.
