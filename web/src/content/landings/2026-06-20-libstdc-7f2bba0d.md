---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- testing
commit_hash: 7f2bba0d2d08219e79ab6ba543be42ccdb37a760
source_type: github
author: Arsen Arsenović
headline: 'libstdc++: Set LD_LIBRARY_PATH for installed compiler tests'
tldr: Ensures tests for installed GCC compilers can find libstdc++.so by setting LD_LIBRARY_PATH.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The libstdc++ testsuite now uses `gcc-set-multilib-library-path` to
  determine and set `LD_LIBRARY_PATH` when testing an installed compiler. This addresses
  a failure mode where an installed toolchain without an RPATH configured for its
  libraries would prevent the test runner from finding `libstdc++.so`, failing dynamic
  symbol resolution at runtime for the test executable.
primer_glossary:
- term: LD_LIBRARY_PATH
  definition: An environment variable that specifies a list of directories to search
    for shared libraries (e.g., .so files) before the standard system directories.
    It's commonly used for development and testing to override or supplement the default
    library paths.
- term: RPATH
  definition: A runtime library search path embedded directly into an executable or
    shared library. When the program runs, the dynamic linker searches these paths
    before the standard system library paths. It's an alternative to using LD_LIBRARY_PATH.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7f2bba0d2d08219e79ab6ba543be42ccdb37a760
date: '2026-06-20'
is_stub: false
stub_reason: ''
---

When testing an installed GCC compiler, this change now correctly sets the `LD_LIBRARY_PATH` environment variable. This is crucial for ensuring that newly compiled programs, which depend on `libstdc++.so`, can locate and link against the necessary shared libraries when the compiler does not embed an RPATH. Without this fix, tests could fail due to missing symbols.
