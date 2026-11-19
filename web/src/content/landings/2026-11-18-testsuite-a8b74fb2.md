---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
- gcc
commit_hash: a8b74fb2f65f57c5a1bacc87379f87a5c9a3bd5c
source_type: github
author: Robin Dapp
headline: 'testsuite: Add early-break options to unsigned-assump tests [PR128822].'
tldr: Test suite updated to include 'vect_early_break' option for unsigned assumption
  tests.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Testsuite update for vectorization regression tests. The `dg-add-options
  vect_early_break` directive was missing from several `vect-unsigned-assump` test
  cases. This patch adds the option to ensure these tests correctly check behavior
  related to loop vectorization with early break conditions, addressing PR128822.
primer_glossary:
- term: testsuite
  definition: A collection of programs and tests used to verify the correctness and
    functionality of a software project, in this case, the GCC compiler.
- term: vect
  definition: Refers to the vectorization subsystem within the GCC compiler.
- term: unsigned-assump
  definition: Refers to tests that rely on assumptions about unsigned integer arithmetic
    within loops being vectorized.
- term: vect_early_break
  definition: A GCC test option that enables specific checks or configurations within
    the vectorization test framework, likely related to how loops terminate or break
    early.
- term: PR128822
  definition: A problem report (bug tracker ID) indicating a specific issue that has
    been fixed.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a8b74fb2f65f57c5a1bacc87379f87a5c9a3bd5c
date: '2026-11-18'
is_stub: true
stub_reason: low_score
---

This commit enhances the GCC test suite by adding the `vect_early_break` option to several vectorization regression tests. These tests specifically target unsigned assumptions within loops. By enabling this option, the tests can now better verify the compiler's behavior and correctness when dealing with scenarios that might involve early termination or specific loop-breaking conditions during vectorization, ensuring more robust testing.
