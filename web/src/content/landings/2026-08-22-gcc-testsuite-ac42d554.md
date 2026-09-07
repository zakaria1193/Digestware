---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- algol68
- testing
commit_hash: ac42d5541d9d4c72b9f364a73cb4a6bd7251b13e
source_type: github
author: Iain Sandoe
headline: Algol68 test suite now supports and uses dg-timeout-factor.
tldr: Algol68 test suite gains dg-timeout-factor support to increase test execution
  time limits.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Algol68 test harness in GCC uses `dg-timeout-factor` to adjust
  test execution time limits. Previously, tests failing due to timeouts on certain
  platforms could not be accommodated without altering the global timeout. This change
  adds support for `dg-timeout-factor` to the `algol68.exp` framework, allowing individual
  tests like `whole-1.a68` to specify a multiplier for the base timeout, thus increasing
  their execution budget without affecting other tests.
primer_glossary:
- term: dg-timeout-factor
  definition: A GCC test suite directive that allows increasing the maximum execution
    time allowed for a specific test case. It multiplies a base timeout value, providing
    more time for tests that are computationally intensive or run on slower systems.
- term: algol68.exp
  definition: The GCC test suite support file for the Algol68 language, containing
    logic and setup for executing and verifying Algol68 test cases.
- term: test suite
  definition: A collection of programs and test cases used to verify the correctness
    and functionality of software. For compilers like GCC, test suites ensure that
    code compiles and runs as expected across various platforms and configurations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ac42d5541d9d4c72b9f364a73cb4a6bd7251b13e
date: '2026-08-22'
is_stub: true
stub_reason: low_score
---

The `algol68.exp` test suite now supports the `dg-timeout-factor` directive, allowing specific tests to have their execution time limits increased. This capability is immediately applied to `whole-1.a68`, which previously failed on some platforms due to exceeding the default 20-second limit, thus improving test reliability.
