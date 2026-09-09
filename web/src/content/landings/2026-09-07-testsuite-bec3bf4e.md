---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
commit_hash: bec3bf4e06cf2c69ce3f7f78ddf98a3a2cef26ea
source_type: github
author: Torbjörn SVENSSON
headline: 'testsuite: Allow vect-alias-check-ptr-info-2.c to use default dg-do mode'
tldr: A test case now uses the default `dg-do` mode, simplifying test suite configuration.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Removes explicit `dg-do run` from `gcc.dg/vect/vect-alias-check-ptr-info-2.c`,
  allowing it to inherit the default mode from `vect.exp`'s `check_vect_support_and_set_flags`
  helper. Simplifies test execution and configuration within the testsuite.
primer_glossary:
- term: dg-do
  definition: A GCC testsuite directive that specifies how a test case should be executed.
    Common values include 'run', 'compile', and 'assemble', controlling whether the
    test is compiled, run, or both.
- term: vect.exp
  definition: An exponent file in the GCC testsuite that contains common definitions
    and setup logic for vectorization tests.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bec3bf4e06cf2c69ce3f7f78ddf98a3a2cef26ea
date: '2026-09-07'
is_stub: true
stub_reason: low_score
---

The test case `vect-alias-check-ptr-info-2.c` has been updated to remove its explicit `dg-do run` setting. It will now automatically use the default `dg-do` mode defined in `vect.exp` via `check_vect_support_and_set_flags`. This change simplifies the test suite's configuration by reducing redundancy and relying on established defaults.
