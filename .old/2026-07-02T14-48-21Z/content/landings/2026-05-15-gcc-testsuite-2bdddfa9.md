---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- warning
- uninitialized
- bugfix
commit_hash: 2bdddfa9e31918fcb1829070866e9428c3606def
source_type: github
author: Marek Polacek
headline: 'Testsuite: Fix Wuninitialized-pr107919-1.C'
tldr: The test case 'Wuninitialized-pr107919-1.C' in GCC's testsuite has been fixed
  to avoid false positives.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit fixes a false positive in the test case ``g++.dg/warn/Wuninitialized-pr107919-1.C``.
  The test case was incorrectly marked as ``dg-bogus``, indicating an unexpected behavior.
  The fix likely involves adjusting the test case to align with the expected compiler
  behavior, ensuring that the test now correctly assesses the uninitialized variable
  warning.
primer_general: GCC's testsuite includes a collection of programs used to verify the
  correctness of the compiler. These test cases check for various language features,
  optimizations, and warnings. When a test case is marked as ``dg-bogus``, it means
  that the test is known to produce incorrect results. This commit fixes a test case
  related to the ``-Wuninitialized`` warning, which detects the use of potentially
  uninitialized variables. The fix ensures that the test case now behaves as expected,
  improving the overall reliability of the testsuite.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2bdddfa9e31918fcb1829070866e9428c3606def
date: '2026-05-15'
is_stub: false
---

The test case ``g++.dg/warn/Wuninitialized-pr107919-1.C`` was incorrectly flagged as ``dg-bogus`` which means that the test case was expected to fail but it didn't. This commit addresses this by fixing the test case so it behaves as expected.
