---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- testing
commit_hash: 6d81aac02a9cd39a67c129054795f9626c658056
source_type: github
author: feedable
headline: 'Testsuite: Convert gcc.c-torture/execute/ieee to the new test format'
tldr: The GCC testsuite's `gcc.c-torture/execute/ieee` tests are converted to use
  dg-* annotations, replacing separate test setup files.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit replaces the `ieee.exp` file with a modified `execute/execute.exp`
  and converts the individual test cases to use `dg-*` annotations.  The `dg-*` directives
  specify target requirements, compiler flags, and expected outcomes directly within
  the C source file, which is a more modern and maintainable approach than separate
  Tcl-based `.exp` files.
primer_general: The GCC testsuite uses a specific format to define and run tests.  Historically,
  test configuration was often handled in separate files.  The modern approach involves
  embedding test directives directly within the test source code using `dg-*` annotations.  This
  commit updates a portion of the testsuite to use this newer, more streamlined format,
  making the tests easier to understand and maintain.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6d81aac02a9cd39a67c129054795f9626c658056
date: '2026-04-11'
---

This commit converts the tests in `gcc.c-torture/execute/ieee` to use the new test format based on `dg-*` annotations. This replaces the older system of separate test setup files (``.exp``) with inline directives within the test files themselves. This change simplifies test maintenance and improves readability.
