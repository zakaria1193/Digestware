---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- darwin
- linker
- asan
- c++
commit_hash: 6c3b1e2e972d2fb331b4ea37080c5bf5e4c1d7ae
source_type: github
author: Iain Sandoe
headline: 'Testsuite: Removes duplicate Asan and pthread libraries for Darwin'
tldr: GCC's testsuite for C++ on Darwin no longer includes redundant Asan and pthread
  libraries, avoiding linker complaints.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in `gcc/testsuite/g++.dg/asan/deep-thread-stack-1.C` modifies
  the linker flags for Darwin targets. Specifically, it removes redundant explicit
  links to `asan` and `pthread` libraries. On modern Darwin toolchains, the `asan`
  library is implicitly added via compiler driver specs (`-fsanitize=address`), and
  `pthread` functionality is subsumed by `libSystem`. Duplicate explicit linking of
  these libraries generates linker warnings or errors, which this patch rectifies
  by ensuring the testsuite avoids these redundant specifications, aligning it with
  current Darwin linker behavior.
primer_general: 'This update affects how GCC''s automated tests for C++ programs run
  on Apple''s Darwin operating system (which powers macOS). The tests, especially
  those checking memory safety features like AddressSanitizer (Asan), were encountering
  problems with the linker—the tool that combines compiled code into a final program.
  The linker on newer Darwin systems would complain because it saw the `asan` and
  `pthread` (for multi-threading) libraries being included twice: once automatically
  by the compiler setup and again explicitly in the test configuration. This fix removes
  the redundant explicit inclusions from the test configuration, making the tests
  run smoothly on modern Darwin environments without unnecessary errors from the linker.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6c3b1e2e972d2fb331b4ea37080c5bf5e4c1d7ae
date: '2026-06-01'
is_stub: false
---

This commit updates the GCC C++ testsuite for Darwin to prevent duplicate linking of libraries. On newer versions of Darwin, the linker reports errors when `asan` (AddressSanitizer) and `pthread` libraries are included redundantly. The `asan` library is already provided by the compiler's specifications, and `pthread` is part of `libSystem`, so the test configuration has been adjusted to omit these explicit links, resolving linker complaints and ensuring cleaner test execution.
