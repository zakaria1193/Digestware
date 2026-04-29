---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- phiprop
- tree-ssa
commit_hash: 994c0e9a2692e076ee57139ec584c36cdefcee01
source_type: github
author: Andrew Pinski
headline: 'Testsuite: Add phiprop testcase that is already fixed.'
tldr: A new test case for the phiprop optimization pass has been added to the GCC
  testsuite.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a new test case to the GCC testsuite specifically
  for the phiprop pass. The test, located at ``g++.dg/tree-ssa/phiprop-1.C``, was
  derived from ``fold-const.cc``.  The issue it targets was resolved by commit ``r16-4212-gf256a13f8aed83``,
  which eliminated an unnecessary clobber.
primer_general: This commit adds a new test case to the GCC testsuite.  The testsuite
  is a collection of programs used to verify that the compiler is working correctly.  This
  new test focuses on the 'phiprop' optimization, which involves propagating values
  through 'phi nodes' in the compiler's intermediate representation.  The test ensures
  that a previously fixed issue in this optimization remains resolved.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/994c0e9a2692e076ee57139ec584c36cdefcee01
date: '2026-04-09'
---

A new test case, ``g++.dg/tree-ssa/phiprop-1.C``, has been added to the GCC testsuite for the phiprop optimization pass.  The test case was extracted from ``fold-const.cc`` and was already fixed by a previous commit that removed a clobber.  This new test will help ensure that the fix remains effective.
