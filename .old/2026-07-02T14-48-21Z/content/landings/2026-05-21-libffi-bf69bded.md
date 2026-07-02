---
project: gcc
subsystem: libffi
patch_id: null
tags:
- libffi
- windows
- build
commit_hash: bf69bded7b47b591bdad0cd0ef6ac4c06b6d2b89
source_type: github
author: Pietro Monteiro
headline: 'Libffi: Always define `WIN32_LEAN_AND_MEAN` before <windows.h>'
tldr: '`WIN32_LEAN_AND_MEAN` is now always defined before including `<windows.h>`
  in libffi to reduce header pollution.'
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit ensures that `WIN32_LEAN_AND_MEAN` is defined before including
  `<windows.h>` in `src/aarch64/ffi.c` within the libffi subdirectory. This macro
  reduces the size of the Windows headers included, preventing namespace pollution
  and speeding up compilation. The upstream pull request is at https://github.com/libffi/libffi/pull/937.
  A Windows or cross-platform developer might encounter issues if this macro is not
  defined.
primer_general: When compiling code that uses the Windows operating system's libraries,
  it's often useful to define a macro called `WIN32_LEAN_AND_MEAN`. This macro tells
  the compiler to include only the most essential parts of the Windows libraries,
  which can speed up compilation and prevent conflicts with other libraries. This
  commit ensures that `WIN32_LEAN_AND_MEAN` is always defined when compiling libffi
  on Windows.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bf69bded7b47b591bdad0cd0ef6ac4c06b6d2b89
date: '2026-05-21'
is_stub: false
---

The `WIN32_LEAN_AND_MEAN` macro is defined before including `<windows.h>` in libffi's source code.  Defining this macro reduces the amount of code included from the Windows headers, which speeds up compilation and avoids potential conflicts.  The change has been forwarded upstream to the libffi project.
