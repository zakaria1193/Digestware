---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- analyzer
- testing
commit_hash: ebe2e4d6569de8d1d8aca3cc1086be7c29eac757
source_type: github
author: David Malcolm
headline: Add analyzer-torture.exp
tldr: Introduces a new testsuite script, `analyzer-torture.exp`, to run analyzer torture
  tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds `g++.dg/analyzer/torture/analyzer-torture.exp` which
  presumably runs existing and future analyzer torture tests. Toolchain devs should
  care because this improves the automated testing of the static analyzer, potentially
  catching regressions and improving its reliability.
primer_general: This commit enhances GCC's testing infrastructure by adding a new
  script for running "torture tests" on the static analyzer. A static analyzer is
  a tool that examines code for potential errors without actually running the program.
  Torture tests are particularly complex and challenging test cases designed to expose
  hidden bugs and ensure the analyzer's reliability. This addition helps ensure the
  analyzer produces accurate and dependable results.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ebe2e4d6569de8d1d8aca3cc1086be7c29eac757
date: '2026-05-20'
is_stub: false
---

This commit introduces a new testsuite script, `analyzer-torture.exp`. The script is designed to run torture tests specifically for the GCC static analyzer. Torture tests are collections of complex test cases that push the boundaries of the compiler's capabilities, helping uncover obscure bugs and ensure robustness.
