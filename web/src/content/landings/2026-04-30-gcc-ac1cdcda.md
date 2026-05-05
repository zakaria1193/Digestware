---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c++
- contracts
- constexpr
- compiler
- bugfix
commit_hash: ac1cdcdad9d364f239d075deb7082071c49ddb6d
source_type: github
author: yxj-github-437
headline: 'C++ Contracts: Fix testsuite failure due to incorrect caching.'
tldr: Prevents caching of constexpr function results when contract violations occur,
  fixing a testsuite failure.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The issue was in `cxx_eval_constant_expression` in `constexpr.cc`.
  The function was caching results even when contract violations were present, leading
  to incorrect behavior in `constexpr` contexts. The commit modifies `cxx_eval_constant_expression`
  to avoid caching results with contract violations.  The test `g++.dg/contracts/cpp26/basic.contract.eval.p8-3.C`
  is added to verify the fix.
primer_general: C++26 introduces contracts, which are a way to specify preconditions,
  postconditions, and invariants for functions. `constexpr` functions are functions
  that can be evaluated at compile time. This commit addresses an issue where the
  results of `constexpr` functions with contract violations were being incorrectly
  cached. By preventing the caching of such results, the compiler will now correctly
  detect and report contract violations even in `constexpr` contexts.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ac1cdcdad9d364f239d075deb7082071c49ddb6d
date: '2026-04-30'
---

The compiler was incorrectly caching the results of `constexpr` functions even when contract violations occurred. This commit prevents caching of results with contract violations in `constexpr_call`, which fixes a testsuite failure in `basic.contract.eval.p8`. This ensures that contract violations are not masked by cached results.
