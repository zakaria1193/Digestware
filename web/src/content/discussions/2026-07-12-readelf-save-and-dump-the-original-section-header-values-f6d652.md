---
project: binutils
subsystem: readelf
patch_id: null
tags:
- binutils
- readelf
- elf
- bugfix
- error-handling
discussion_id: alNf0yuNAobHT3dV@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: readelf: Save and dump the original section header values'
headline: 'readelf: Save and dump the original section header values'
tldr: Improves error handling and fixes a buffer overflow in binutils' readelf tool.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Simplifies error messages, potentially losing some specific detail about malloc
  failures for small allocations.
- Introduces 'xmalloc' for safer memory allocation, which might have slightly different
  behavior than raw 'malloc' in error cases.
exchanges: []
primer_expert: 'Refactors `readelf.c` to address two main issues: 1) improving error
  reporting for `malloc` failures in `save_original_section_header_values` to use
  `xmalloc` and simplify messages, and 2) fixing a potential buffer overflow in `orig_section_headers`.
  The overflow could occur if memory allocation fails during probing, leading to incorrect
  access when `free_filedata` is called. The changes also remove unused function parameters
  and simplify calls to `validate_section_info`.'
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files, part of the GNU Binutils package.
- term: section header
  definition: A data structure within an ELF file that describes a section of the
    file, such as code, data, or symbol tables.
- term: POT file
  definition: Portable Object Template file. A template file used in software internationalization
    containing strings to be translated.
- term: malloc
  definition: A standard C library function that allocates a block of memory on the
    heap.
- term: xmalloc
  definition: A variant of `malloc` that typically includes error checking and exits
    the program if memory allocation fails.
- term: buffer overflow
  definition: A condition where a program writes data beyond the allocated buffer,
    potentially corrupting adjacent memory and leading to crashes or security vulnerabilities.
- term: relr dynamic tags
  definition: Refers to dynamic linking information related to relocation entries,
    specifically the 'relr' (relative relocations) format which is more compact than
    standard relocation entries.
- term: ELF header
  definition: The main header of an ELF file, containing general information about
    the file format and its contents.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alNf0yuNAobHT3dV@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-12'
is_stub: false
stub_reason: ''
---

This patch refactors parts of binutils' `readelf.c` to improve error reporting for `malloc` failures and fix a potential buffer overflow in `orig_section_headers`. It simplifies warning messages, removes unused parameters, and adjusts memory allocation and validation logic, particularly when probing ELF headers or handling relr dynamic tags.
