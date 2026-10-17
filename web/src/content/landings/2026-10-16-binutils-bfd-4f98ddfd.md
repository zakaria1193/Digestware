---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- cleanup
- backend
commit_hash: 4f98ddfd8b7cb2798d0b27892fed4c3fc37d7f77
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Remove unused coff-x86_64 backend
tldr: Removes the coff-x86_64 backend from BFD as it is not used and does not provide
  a valid backend.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `coff-x86_64.c` file, along with its build system configuration
  in `bfd/Makefile.am` and `bfd/targets.c`, has been removed. This backend was never
  selected by any target configuration, meaning it did not register a valid backend
  for the COFF format on x86-64. Its removal simplifies the build and removes dead
  code, aligning with the removal of other unused COFF backends.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to abstract the differences between various object file formats (like ELF, COFF,
    a.out).
- term: COFF
  definition: Common Object File Format. An older object file format used on Windows
    and some Unix systems.
- term: backend
  definition: In the context of BFD, a specific implementation that handles the details
    of a particular object file format or target architecture.
- term: Makefile.am
  definition: A file used by Automake to generate Makefiles, defining build rules
    and dependencies.
- term: targets.c
  definition: A C source file in BFD that likely registers and manages the available
    backends for different object file formats and architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261016080209.1E6254BA2E1F@sourceware.org
date: '2026-10-16'
is_stub: true
stub_reason: low_score
---

The `coff-x86_64.c` file and its associated build system entries have been removed from the BFD library. This backend was not selected by any target and thus did not provide a functional backend, similar to other unused COFF backends for different architectures.
