---
project: gcc
subsystem: libbacktrace
patch_id: null
tags:
- debugging
- libbacktrace
- stripped binaries
commit_hash: 8858cb3a6af52e4425d1635a7666d3f3658005d5
source_type: github
author: Ian Lance Taylor
headline: 'libbacktrace: Handle MOREDATA correctly without debug info'
tldr: Improves libbacktrace's symbol lookup in stripped binaries when debug info is
  absent.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libbacktrace` library provides stack unwinding capabilities. When
  dealing with stripped binaries (lacking debug symbols), it sometimes needs to fetch
  additional data related to symbols. This patch, based on work by Andi Kleen, correctly
  implements the handling of `state->moredata` within the `elf_nodebug` function in
  `elf.c`. A new callback `backtrace_syminfo_to_full_callback_moredata` is introduced,
  and a new test case `strippedtest.c` is added to verify functionality on stripped
  executables.
primer_glossary:
- term: libbacktrace
  definition: A library used for generating stack traces, typically invoked after
    a program crash or error to provide information about the call sequence.
- term: stripped binary
  definition: An executable file or library from which debugging symbols and other
    non-essential information have been removed, making the file smaller but harder
    to debug.
- term: MOREDATA
  definition: A state indicator used within `libbacktrace` to signify that additional
    data needs to be fetched or processed during symbol lookup, particularly when
    debug information is limited or absent.
- term: symbol lookup
  definition: The process of finding the names and addresses of functions and variables
    within an executable or object file, often using symbol tables.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8858cb3a6af52e4425d1635a7666d3f3658005d5
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This commit enhances `libbacktrace`'s ability to correctly handle the `MOREDATA` state when retrieving symbol information from binaries that have been stripped of debug information. It introduces a new function `backtrace_syminfo_to_full_callback_moredata` and ensures that the `elf.c` module correctly processes this state, along with adding tests for stripped binaries.
