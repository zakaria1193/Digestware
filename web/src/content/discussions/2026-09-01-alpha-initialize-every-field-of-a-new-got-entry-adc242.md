---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- got
- initialization
- tls
discussion_id: 20260901023318.3503991-2-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 01/11] alpha: initialize every field of a new got entry'
headline: 'alpha: initialize every field of a new got entry'
tldr: Initialize all fields of GOT entries, especially flags and plt_offset, to prevent
  errors.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves memory safety and correctness by ensuring proper initialization.
- Uses `bfd_zalloc` for safer default initialization.
exchanges: []
primer_expert: This patch corrects the allocation of `alpha_elf_got_entry` structures
  in `bfd/elf64-alpha.c`. Previously, `bfd_alloc` was used, leaving fields like `flags`
  uninitialized. This could lead to incorrect merging of GOT entries in `elf64_alpha_merge_gots`
  or issues in `elf64_alpha_relax_tls_get_addr` when `plt_offset` was unexpectedly
  non-zero. The change replaces `bfd_alloc` with `bfd_zalloc` and adjusts assignments
  to ensure all necessary fields, especially `flags`, are correctly initialized to
  zero by default, with only explicitly needed values being set afterwards.
primer_glossary:
- term: GOT
  definition: Global Offset Table. A data structure used in position-independent code
    to hold addresses of global variables and functions, allowing indirect access.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps, commonly used on Unix-like systems.
- term: relocation
  definition: A process performed by the linker to adjust symbolic references (like
    function calls or variable accesses) in object code to their final memory addresses
    in the executable or shared library.
- term: TLS
  definition: Thread-Local Storage. A mechanism that allows variables to have distinct
    values for each thread.
- term: Valgrind
  definition: A debugging and profiling tool suite for Linux and macOS, used here
    to detect memory management errors.
series_id: 'binutils:alpha: initialize every field of a new got entry'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-2-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch addresses an initialization issue in the alpha ELF linker where newly allocated GOT (Global Offset Table) entries were not fully initialized, specifically their `flags` and `plt_offset` fields. This oversight, found via Valgrind, could lead to incorrect behavior when merging GOT entries or when handling TLS relocations. By using `bfd_zalloc` to zero-initialize the entries and explicitly assigning only non-zero initial values, the patch ensures all fields are properly set, preventing potential bugs.
