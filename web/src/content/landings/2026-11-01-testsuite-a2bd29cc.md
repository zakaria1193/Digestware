---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- regression
- compiler
commit_hash: a2bd29ccfcb372472cccb4552843a10c35e4cf20
source_type: github
author: Torbjörn SVENSSON
headline: Testsuite requires checking for nested crash tests
tldr: Nested compiler crash tests in the testsuite now require the 'checking' target
  to be enabled, preventing failures when GCC is built without checking.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates GCC's testsuite to handle nested compiler crash
  tests more robustly. Previously, tests like `crash-test-nested-ice.c` and `crash-test-nested-write-through-null.c`
  would fail if the compiler was built without the `-fcheck-pointer-bounds` or equivalent
  checking options enabled. This commit introduces a new effective target, `checking`,
  in `lib/et-static.def`, and requires it for these tests. This ensures that these
  tests are only run when the compiler is built with bounds checking enabled, preventing
  test failures on standard configurations.
primer_glossary:
- term: Testsuite
  definition: A collection of tests used to verify the correctness of a software system,
    in this case, the GCC compiler.
- term: Crash test
  definition: A test case designed to trigger a compiler internal error (ICE) or other
    severe failure to verify error reporting and robustness.
- term: Nested crash test
  definition: A crash test where the error-inducing scenario occurs within another
    complex construct, such as within a nested function or a complex control flow
    structure.
- term: Effective target
  definition: A set of compiler options and features that define the target environment
    for a specific test case within the GCC testsuite.
- term: ICE
  definition: Internal Compiler Error, a crash within the compiler itself rather than
    an error in the generated code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a2bd29ccfcb372472cccb4552843a10c35e4cf20
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This commit addresses PR124872 by modifying the testsuite to require the 'checking' effective target for specific nested crash tests. These tests were failing when GCC was compiled without checking enabled. By adding this requirement, the testsuite now correctly skips these tests on configurations where checking is disabled, ensuring the test suite's integrity and preventing spurious failures. Documentation for build configurations has also been updated.
