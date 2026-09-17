---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- documentation
- testsuite
commit_hash: 1d8b0cfa3474c0a9854b8d8340792eaff62b70e7
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Fix typo in comment in testsuite file'
tldr: Corrects a typographical error in a comment within a libstdc++ test file.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a simple typo within a comment in a libstdc++
  test file. No functional change is expected, only an improvement in code readability.
primer_glossary:
- term: libstdc++
  definition: The C++ standard library implementation used by GCC. It provides core
    C++ language features like containers, algorithms, I/O streams, and threading
    support.
- term: testsuite
  definition: A collection of programs and scripts used to verify the correctness
    of the compiler or its standard library implementation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1d8b0cfa3474c0a9854b8d8340792eaff62b70e7
date: '2026-09-16'
is_stub: true
stub_reason: low_score
---

A minor typo in a comment within the libstdc++ test suite file `27_io/basic_filebuf/close/char/4879.cc` has been fixed. This change improves the clarity and correctness of the test suite's source code.
