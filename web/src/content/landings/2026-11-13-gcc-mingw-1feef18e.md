---
project: gcc
subsystem: gcc/mingw
patch_id: null
tags:
- mingw
- pe
- symbols
- directives
- linker
commit_hash: 1feef18e79273e7ed102f4e3240ad8e6a44725e9
source_type: github
author: LIU Hao
headline: Fix user symbol prefix handling for directives in mingw PE targets
tldr: Correctly handle user symbol prefixes for directives like `asm` labels and `-export:`
  in GCC's mingw PE backend.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `i386_pe_assemble_visibility` function in GCC's mingw backend had
  issues correctly applying user label prefixes (e.g., leading underscores) to symbols,
  particularly when using `asm` labels or the `-export:` directive. The `i386_pe_drectve_name`
  function was modified to accept a string and selectively apply prefix logic based
  on whether the name originated from an `asm` label. This corrects cases where user
  prefixes were stripped incorrectly or where `asm` labels themselves needed to be
  prefixed correctly before being passed to the PE object file directives. New test
  cases target `dllexpor…
primer_glossary:
- term: PE
  definition: Portable Executable; the file format used for executables, object code,
    DLLs, and other files used in 32-bit and 64-bit versions of Windows operating
    systems.
- term: user symbol prefix
  definition: A prefix, typically an underscore, that GCC adds to symbols in assembly
    output for certain targets, distinguishing them from user-defined symbols.
- term: asm label
  definition: A label explicitly provided in C/C++ code using the `asm` keyword, used
    to control the symbol name generated in assembly output.
- term: '-export:'
  definition: A GCC driver option for PE targets used to explicitly export symbols
    from a DLL.
- term: visibility
  definition: A symbol attribute that controls the linkage and visibility of symbols,
    affecting how they are exported from or imported into shared libraries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1feef18e79273e7ed102f4e3240ad8e6a44725e9
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in GCC's mingw PE (Portable Executable) backend where user symbol prefix handling was incorrect for certain directives. Previously, the compiler might incorrectly strip leading underscores from function or variable names when they lacked an `asm` label. Conversely, when an `asm` label was used, the compiler needed to correctly incorporate the user label prefix into the directive, which was not happening. The fix modifies `i386_pe_drectve_name` and related functions to properly handle these scenarios, ensuring correct symbol visibility and directive processing, and adds new test cases.
