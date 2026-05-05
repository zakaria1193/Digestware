---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- testcase
- regression
commit_hash: 40f567d9cabc5170ed396025d516b93838f4f141
source_type: github
author: Richard Biener
headline: Added testcase for tree-optimization/125153.
tldr: Added a new testcase (gcc.dg/torture/pr125153.c) for PR tree-optimization/125153
  to verify the fix from a reverted commit.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a testcase for a previously fixed issue in the tree-optimization
  pass. The fix involved reverting a specific revision (r16-303). The new testcase,
  `gcc.dg/torture/pr125153.c`, acts as a regression test to prevent the reintroduction
  of the bug. The tree-optimization pass is a crucial part of GCC that aims to improve
  the generated code by applying various transformations on the intermediate representation.
primer_general: Compiler development involves continuous testing to ensure that bug
  fixes remain effective and that new changes don't reintroduce old problems. This
  commit adds a new test case to specifically check for a previously resolved issue
  in GCC's tree optimization component. This new test will help to prevent regressions,
  where a previously fixed bug reappears in later versions of the compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/40f567d9cabc5170ed396025d516b93838f4f141
date: '2026-05-04'
---

A new testcase, `gcc.dg/torture/pr125153.c`, has been added to verify the fix for PR tree-optimization/125153. The PR was addressed by reverting r16-303, and this testcase ensures the issue remains resolved.
