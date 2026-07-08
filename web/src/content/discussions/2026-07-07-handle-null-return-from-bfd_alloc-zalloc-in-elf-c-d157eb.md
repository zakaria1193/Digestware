---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- elf
- memory management
- robustness
- bug fix
discussion_id: aky79AMZtaPhprfE@squeak.grove.modra.org
source_type: public_inbox
title: Check the result of two bfd_alloc calls in elf.c
headline: Handle NULL return from bfd_alloc/zalloc in elf.c
tldr: Adds checks for NULL return values from bfd_alloc and bfd_zalloc in elf.c to
  prevent potential crashes.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adding null checks increases code verbosity slightly but significantly improves
  stability.
- Removing unnecessary casts can improve code clarity and potentially avoid subtle
  type-related issues.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to elf.c that adds checks for NULL return values from
    `bfd_zalloc` and `bfd_alloc` calls, fixes PR 34131, and removes unnecessary casts.
  quote: "\tPR 34131\n\t* elf.c: Remove unnecessary casts on bfd_[zm]*alloc return\
    \ value.\n\tDo without \"amt\" temp var in a few cases.\n\t(assign_section_numbers):\
    \ Check for NULL return from bfd_zalloc.\n\t(elfobj_grok_stapsdt_note_1): Likewise\
    \ for bfd_alloc."
primer_expert: This patch for binutils' `elf.c` addresses Potential Bug Report (PR)
  34131 by adding crucial null-pointer checks for memory allocations made via `bfd_zalloc`
  and `bfd_alloc`. It also cleans up the code by removing redundant type casts on
  the return values of these functions and consolidating temporary variables. These
  changes enhance the robustness of the ELF file parsing in binutils, preventing potential
  crashes if memory allocation fails.
primer_glossary:
- term: elf.c
  definition: A C source file within the binutils project that handles the parsing
    and manipulation of ELF (Executable and Linkable Format) object files.
- term: bfd_alloc
  definition: A function within the BFD (Binary File Descriptor) library used for
    general-purpose memory allocation.
- term: bfd_zalloc
  definition: Similar to bfd_alloc, but `bfd_zalloc` zeroes the allocated memory.
- term: NULL return
  definition: When a memory allocation function fails, it typically returns a NULL
    pointer instead of a valid memory address.
- term: PR 34131
  definition: A bug report identifier within the binutils project's tracking system,
    indicating a specific issue that this patch aims to fix.
- term: type casts
  definition: Explicit conversions in programming code that change a value from one
    data type to another. In this context, removing them suggests the casts were unnecessary
    due to implicit type compatibility.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aky79AMZtaPhprfE@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This patch addresses a potential issue in binutils' elf.c by adding checks for NULL return values from `bfd_zalloc` and `bfd_alloc` calls. It also removes unnecessary casts on the return values of these allocation functions and simplifies variable usage in a few cases, aiming to improve robustness.
