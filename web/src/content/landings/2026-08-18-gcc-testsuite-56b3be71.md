---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- i386
- vectorization
- x86-64
commit_hash: 56b3be71da679072f184304403b0c6910d725b7f
source_type: github
author: H.J. Lu
headline: 'vect-pragma-target-2.C: Compile with -march=x86-64'
tldr: Ensures vectorization tests with pragmas use a specific march for consistent
  behavior.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test case vect-pragma-target-2.C likely uses pragmas to control
  vectorization features. Compiling it with a fixed -march=x86-64 ensures that the
  test behaves predictably irrespective of the host system's CPU capabilities, especially
  when 'native' configurations might enable features beyond the test's scope.
primer_glossary:
- term: -march=x86-64
  definition: A GCC flag that enables code generation for the x86-64 architecture,
    including specific instruction sets available on that baseline. It's used here
    to ensure tests targeting specific features don't inadvertently enable newer,
    potentially incompatible ones.
- term: --with-arch=native --with-cpu=native
  definition: GCC configuration options that instruct the compiler to detect and use
    the architecture and CPU features of the build machine. This commit aims to counteract
    potential over-detection for test purposes.
- term: vect-pragma-target-2.C
  definition: A GCC test file, likely in C++, that tests the compiler's vectorization
    capabilities, possibly using pragmas to influence code generation for the i386
    architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/56b3be71da679072f184304403b0c6910d725b7f
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

This commit modifies the test suite to compile vect-pragma-target-2.C with the -march=x86-64 flag. This prevents features from newer x86-64 microarchitectures (like x86-64-v4) from being unintentionally enabled when GCC is configured with --with-arch=native --with-cpu=native, ensuring the test's intended behavior.
