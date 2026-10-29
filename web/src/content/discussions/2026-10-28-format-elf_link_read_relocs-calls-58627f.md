---
project: binutils
subsystem: binutils
patch_id: null
tags:
- cleanup
- formatting
- binutils
discussion_id: auJ4lWhjjOAYIX7u@squeak.grove.modra.org
source_type: public_inbox
title: Format elf_link_read_relocs calls
headline: Format elf_link_read_relocs calls
tldr: Cleans up formatting, removes unnecessary NULL casts, and deletes old comments
  in elf_link_read_relocs calls.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- No functional changes are introduced; the tradeoffs are purely in code readability
  and maintainability.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes formatting changes and cleanup for `_bfd_elf_link_read_relocs`
    calls, removing redundant NULL casts and comments.
  quote: 'At one point I was going to add another parameter to these calls but

    backed that change out.  All that is left here is formatting,

    removing some unnecessary casts of NULL, and removing some comments.'
primer_expert: This patch targets multiple BFD backend files (e.g., `elf-m10200.c`,
  `elf-m10300.c`) to clean up the invocation of `_bfd_elf_link_read_relocs`. The changes
  involve code formatting, removal of redundant casts to `NULL` (likely due to API
  changes or simplification), and deletion of comments that are no longer relevant,
  possibly because the underlying issue they addressed was resolved or refactored.
primer_glossary:
- term: BFd
  definition: Binary Descriptor library. A low-level library used by GNU Binutils
    and GCC for reading and writing various object file formats.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, shared libraries, and core dumps on many Unix-like systems.
- term: Relocation
  definition: A modification needed in an object file or shared library to resolve
    references to symbols or addresses that are not yet known at link time. This process
    is typically handled by the linker.
- term: 'NULL'
  definition: A special pointer value that represents an invalid or uninitialized
    memory address. In C, it's typically defined as `(void*)0`.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ4lWhjjOAYIX7u@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch series cleans up calls to `_bfd_elf_link_read_relocs` by reformatting the lines, removing casts of `NULL` that are no longer necessary, and deleting outdated comments. These changes are purely cosmetic and do not alter the functionality of the code.
