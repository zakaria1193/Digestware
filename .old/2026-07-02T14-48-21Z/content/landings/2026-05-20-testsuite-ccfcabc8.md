---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- analyzer
- libstdc++
- c++
commit_hash: ccfcabc847eaeb6c1e0b0bec5a12c8af649c8de0
source_type: github
author: David Malcolm
headline: Add libstdc++ -fanalyzer Test Coverage
tldr: Added minimal test coverage for `-fanalyzer`'s handling of basic libstdc++ usage,
  providing end-to-end testing of the interaction between the static analyzer a…
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces basic test coverage for `-fanalyzer` when used
  with `libstdc++` within the GCC testsuite (`g++.dg/analyzer/torture`). The tests
  cover basic functionalities like `std::string` constructors and `std::unique_ptr`.
  This provides regression testing for the interaction between the static analyzer
  and the C++ standard library, and will be extended as more complex issues are resolved
  (PR 125236).
primer_general: The `-fanalyzer` flag in GCC enables static analysis, a process where
  the compiler tries to find potential bugs in the code without running it. This commit
  adds tests that check how well `-fanalyzer` works with the C++ standard library
  (`libstdc++`). These tests cover common usages of `libstdc++` to ensure that the
  analyzer can effectively identify issues in code that uses these standard components.
discussion_id_link: github:gcc-mirror/gcc#125236
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ccfcabc847eaeb6c1e0b0bec5a12c8af649c8de0
date: '2026-05-20'
is_stub: false
---

This commit adds new tests to verify that the `-fanalyzer` flag works correctly with basic `libstdc++` usage. These tests cover scenarios like `std::string` construction and `std::unique_ptr` to improve end-to-end testing of the analyzer's interaction with the C++ standard library. More tests will be added to cover other usages as issues are debugged.
