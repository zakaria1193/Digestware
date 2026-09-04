---
project: gcc
subsystem: libbacktrace
patch_id: null
tags:
- libbacktrace
- refactor
- elf
commit_hash: 6401cc2efae456806f3376810098d99e518577fe
source_type: github
author: Ian Lance Taylor
headline: 'libbacktrace: Make `backtrace_syminfo_to_full_callback_moredata` static.'
tldr: A helper function in libbacktrace was moved and made static to improve encapsulation.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `backtrace_syminfo_to_full_callback_moredata` symbol, previously
  defined in `fileline.c`, has been relocated to `elf.c` and its linkage changed to
  `static`. This change localizes the function's scope to `elf.c`, as it's only relevant
  to the ELF symbol lookup logic and is not part of the public libbacktrace API. The
  declaration was removed from `internal.h` accordingly.
primer_glossary:
- term: libbacktrace
  definition: A library that provides functionality for generating stack traces (backtraces)
    from a running program, typically used for debugging and error reporting.
- term: static linkage
  definition: A storage class specifier in C/C++ that limits the scope of a function
    or variable to the current translation unit (source file). This prevents name
    collisions and improves encapsulation.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems. Libbacktrace
    uses it to extract symbol information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6401cc2efae456806f3376810098d99e518577fe
date: '2026-09-03'
is_stub: true
stub_reason: low_score
---

The `backtrace_syminfo_to_full_callback_moredata` function has been moved from `fileline.c` to `elf.c` and is now declared `static`. This change enhances code organization and encapsulation within the libbacktrace library, preventing external access to a function that is only intended for internal use within the ELF symbol resolution logic.
