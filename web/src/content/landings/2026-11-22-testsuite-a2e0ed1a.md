---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
commit_hash: a2e0ed1a1b264aa50a17db1053cd924e90320502
source_type: github
author: Torbjörn SVENSSON
headline: 'testsuite: Simplify vector test configuration'
tldr: A vector test case now uses the default test execution mode, reducing configuration
  boilerplate.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The testsuite uses `dg-do` directives to specify how a test case should
  be executed (e.g., `dg-do run`, `dg-do compile`). For tests within `vect.exp`, the
  execution mode is configured globally. The test `gcc.dg/vect/pr128689-2.c` had an
  explicit `dg-do run` that duplicated this default setting. This change removes the
  redundant directive, relying on the default from `check_vect_support_and_set_flags`
  within `vect.exp`.
primer_glossary:
- term: dg-do run
  definition: A directive used in GCC's testsuite to specify that a test case should
    be compiled, linked, and executed.
- term: vect.exp
  definition: A GCC testsuite file that contains configuration and test cases related
    to vectorization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a2e0ed1a1b264aa50a17db1053cd924e90320502
date: '2026-11-22'
is_stub: true
stub_reason: low_score
---

This commit simplifies the configuration for a specific test case within the GCC testsuite. The test `pr128689-2.c` previously had an explicit `dg-do run` directive, which is now removed. The test will now inherit the default execution mode from its containing `vect.exp` file, making the test configuration cleaner.
