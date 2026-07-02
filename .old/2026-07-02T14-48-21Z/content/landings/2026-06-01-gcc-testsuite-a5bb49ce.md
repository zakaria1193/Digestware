---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- darwin
- fix
commit_hash: a5bb49ce5649751a96b63c1b96d1fde22ede564b
source_type: github
author: Iain Sandoe
headline: Fix spurious fails in mk*temp* tests on Darwin
tldr: GCC test suite now correctly handles temporary file creation functions by including
  both necessary headers and addressing deprecation warnings on Darwin.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC test suite, specifically in `gcc.dg/analyzer`, checks the behavior
  of system calls related to temporary file creation. The fix involves updating test
  cases `mkdtemp-1.c`, `mkstemps-1.c`, and `mktemp-1.c` to correctly include the `unistd`
  header alongside `stdlib` for proper function declaration resolution on Darwin systems.
  `mktemp-1.c` also gains explicit handling for `mktemp`'s deprecation warnings to
  avoid test failures.
primer_general: When you write C code, you often need to create temporary files or
  directories. Functions like `mkdtemp`, `mkstemps`, and `mktemp` are standard ways
  to do this. These functions are typically declared in header files like `stdlib.h`
  or `unistd.h`. Compilers like GCC compile and run a suite of tests to ensure they
  correctly understand and handle these functions across different operating systems.
  This change updates some of those tests on macOS (Darwin) because the declarations
  for these functions were split across two headers, causing compilation issues in
  the test suite. The update also accounts for a warning macOS issues when using the
  older `mktemp` function, ensuring the tests pass without issues.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a5bb49ce5649751a96b63c1b96d1fde22ede564b
date: '2026-06-01'
is_stub: false
---

The GCC test suite previously exhibited spurious failures on Darwin when testing functions like `mkdtemp` and `mkstemps`. This commit resolves these issues by ensuring that `stdlib.h` and `unistd.h` are both included, as these functions may be declared in either header. Additionally, it adds handling for deprecation warnings that Darwin emits for `mktemp`.
