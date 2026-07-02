---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- elf
- memory-allocation
- bugfix
discussion_id: aiz9Oe59t8FzY7Jx@squeak.grove.modra.org
source_type: public_inbox
title: check bfd_alloc/bfd_malloc return in elflink.c
headline: Adds null checks for memory allocation in elflink.c and replaces sprintf
  with memcpy for string concatenation
tldr: A patch improves error handling in Binutils' BFD by adding null checks for `bfd_malloc`
  and `bfd_alloc` calls and optimizes string concatenation using `memcpy`…
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes to add `NULL` checks for `bfd_alloc` and `bfd_malloc` return
    values in `elflink.c` and replace `sprintf` with `memcpy` for string concatenation.
  quote: Add checks in a couple of places for a non-NULL return. While we're at it,
    don't use sprintf to concatenate two strings.
primer_expert: This patch targets `bfd/elflink.c`, a critical part of the Binutils
  BFD library responsible for handling ELF (Executable and Linkable Format) linking.
  Key functions like `bfd_elf_link_record_dynamic_symbol` and `get_dynamic_reloc_section_name`
  are central to how BFD processes and represents ELF symbols and relocations. The
  changes involve adding robustness by checking return values of `bfd_malloc` and
  `bfd_alloc`—internal BFD memory allocation routines. Furthermore, the optimization
  of replacing `sprintf` with `memcpy` for constructing section names like `.rel`
  or `.rela` prefixed to existing…
primer_general: This discussion is about improvements to Binutils, a set of tools
  crucial for working with computer programs, particularly for tasks like linking
  (combining different parts of a program together). Inside Binutils, there's a library
  called BFD (Binary File Descriptor) that helps it understand and manipulate various
  program file formats, like ELF (the standard format for executables on Linux). The
  proposed changes focus on a file called `elflink.c`, which handles how BFD links
  ELF files. Specifically, it's about making sure that when the program asks for memory
  (using functions like `bfd_malloc`), it always checks if the request was successful.
  If memory isn't available, the program should handle it gracefully instead of crashing.
  Additionally, the patch makes a small but important change to how the program puts
  together text strings; instead of using a function (`sprintf`) that can sometimes
  be less safe or slower, it uses a more direct and efficient method (`memcpy`), making
  the progr…
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aiz9Oe59t8FzY7Jx@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-13'
is_stub: false
---

Alan Modra proposes a patch to enhance error handling and efficiency within `elflink.c`, a core component of Binutils' BFD library. The primary changes involve adding explicit null checks for memory allocation functions `bfd_malloc` and `bfd_alloc`, preventing potential crashes if memory allocation fails. Additionally, the patch replaces `sprintf` calls with `memcpy` for concatenating strings, which can offer performance improvements and avoid potential buffer overflows.
