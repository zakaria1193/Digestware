---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- c++
- consteval
- performance
commit_hash: 54ddb5ff8b91bf518e69ed9221ed4530e7ad55af
source_type: github
author: Jakub Jelinek
headline: Adds a testcase for consteval-only types.
tldr: A new test case was added to ensure that consteval-only type computations in
  GCC are not quadratic in complexity.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit adds a testcase for the `consteval` feature in C++, specifically
  addressing a potential performance issue where computations involving `consteval`-only
  types could exhibit quadratic complexity. The test case `g++.dg/reflect/pr125179.C`
  is designed to expose this issue and ensure that the compiler handles such computations
  efficiently.
primer_general: '`Consteval` functions in C++ are functions that must be evaluated
  at compile time. The result of a `consteval` function can be used in contexts where
  a constant expression is required, such as array sizes or template arguments. This
  test case makes sure that the compiler handles certain consteval computations efficiently,
  preventing excessive compile times.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/54ddb5ff8b91bf518e69ed9221ed4530e7ad55af
date: '2026-05-15'
is_stub: false
---

A new test case, `g++.dg/reflect/pr125179.C`, was added to the GCC testsuite to verify that computations involving `consteval`-only types do not exhibit quadratic complexity. This test creates a loop with 50000 types which could cause a timeout with an earlier quadratic implementation.
