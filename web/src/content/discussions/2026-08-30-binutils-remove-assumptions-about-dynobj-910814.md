---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- elf
- backend
- patch
discussion_id: apS6I5hd4Fnz7pQU@squeak.grove.modra.org
source_type: public_inbox
title: remove some assumptions about dynobj
headline: 'binutils: remove assumptions about dynobj'
tldr: A patch series cleans up assumptions in various backends that dynamic sections
  must exist if dynobj is non-NULL.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The changes might require re-evaluation of assumptions in other related linker scripts
  or backend code.
- Ensuring comprehensive testing across all affected architectures is crucial.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch series to fix incorrect assumptions about dynamic objects
    in BFD backends.
  quote: 'A number of backends assume that if dynobj is non-NULL then some

    dynamic sections must have been created.  That isn''t the case if

    dynobj is set without a create_dynamic_sections call, for instance, if

    dynobj were set to the stub bfd as ppc64 does early in linking.

    This patch fixes those assumptions, and tidies some code a little.'
primer_expert: Several BFD backends contain logic that assumes `bfd_link_info.dynobj`
  being non-NULL implies `dynamic_sections_created` is true. This commit corrects
  this by ensuring that specific dynamic section checks (like `sgot`, `sdyn`) and
  assertions only occur after verifying `dynamic_sections_created`. This is particularly
  relevant for cases like `ppc64` where `dynobj` might be set to a stub BFD before
  dynamic sections are properly initialized.
primer_glossary:
- term: dynobj
  definition: Likely refers to a pointer to a BFD (Binary File Descriptor) structure
    that represents a dynamic object or section within the linker's internal representation.
- term: dynamic sections
  definition: Special sections in an ELF file (e.g., .dynamic, .dynsym, .dynstr) that
    contain information necessary for dynamic linking at runtime.
- term: create_dynamic_sections
  definition: A function call within the linker that initializes and allocates structures
    for dynamic sections.
- term: stub bfd
  definition: A placeholder or incomplete Binary File Descriptor structure used early
    in the linking process before the full details of an object file are known.
- term: BFD
  definition: Binary File Descriptor. A library used by GNU toolchain components (like
    `ld` and `gas`) to provide a common interface for reading and writing various
    executable file formats.
- term: backend
  definition: In the context of BFD or linker scripts, a specific implementation or
    set of rules tailored for a particular architecture or file format.
- term: sgot
  definition: Likely refers to the 'Static GOT' or 'Small GOT' section, relevant for
    position-independent code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/apS6I5hd4Fnz7pQU@squeak.grove.modra.org
bugzilla_url: null
date: '2026-08-30'
is_stub: false
stub_reason: ''
---

This patch series addresses an issue where several BFD backends incorrectly assume that the existence of `dynobj` implies that dynamic sections have been created. This assumption can fail if `dynobj` is set without `create_dynamic_sections` being called, such as when `dynobj` is assigned a stub BFD early in the linking process. The changes adjust assertions and checks in multiple backends to correctly test for `dynamic_sections_created` or the existence of specific dynamic section symbols.
