---
project: binutils
subsystem: elflink.c
patch_id: null
tags:
- code-quality
- refactoring
- bfd
- elf
discussion_id: ajM0JFFTrcuYy6JA@squeak.grove.modra.org
source_type: public_inbox
title: 'elflink.c: remove unnecessary casts'
headline: Remove unnecessary casts in elflink.c
tldr: This patch removes legacy C-style casts and tidies size calculations in `elflink.c`
  for improved code clarity and maintainability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes removing unnecessary casts and tidying size calculations in elflink.c
    to improve code hygiene.
  quote: I noticed when going through elflink.c looking for places where memory allocation
    function return values weren't checked, that many places still have the now unnecessary
    casts from K&R days. This patch removes them, and tidies some places that don't
    need to use a variable to pass the size.
primer_expert: This patch targets `bfd/elflink.c`, a core component of the Binary
  File Descriptor (BFD) library responsible for linking ELF objects. It specifically
  addresses coding style and minor optimizations in memory allocation related code
  paths, like `bfd_elf_link_record_local_dynamic_symbol`. The changes involve simplifying
  variable usage and removing redundant casts within memory allocation calls, impacting
  code readability and potentially very slightly the generated assembly due to simplified
  expressions, though not runtime performance in any measurable way for typical usage.
  It is a maintenance p…
primer_general: This change is in `elflink.c`, a part of the Binutils project's BFD
  library that handles linking executable and library files in the ELF format. ELF
  (Executable and Linkable Format) is a common standard for executables, object code,
  and shared libraries on Unix-like systems. Linking is the process of combining various
  code and data segments into a final executable program. This patch removes old-fashioned
  ways of writing code, specifically 'casts' that tell the compiler how to treat a
  variable's type. Modern C compilers don't need these casts in these specific contexts,
  so removing them makes the code cleaner and easier to understand. This is a code
  quality improvement that does not change how programs behave.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajM0JFFTrcuYy6JA@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-17'
is_stub: false
---

This patch removes unnecessary C-style casts from `elflink.c` that are remnants from K&R C days, improving code readability. It also refines size calculations in some areas, eliminating the need for temporary variables and simplifying the code. This is a clean-up patch that addresses code style and minor inefficiencies.
