---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- bugfix
commit_hash: 3bae47f716b56fbfbf63653a73f34a768a064d51
source_type: github
author: Jakub Jelinek
headline: Fix up torture test for bit-integers
tldr: Moves a test case for bit-integers to prevent conflicts and ensures correct
  diagnostics.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test suite for GCC's bit-integer support had a naming collision
  between two independently committed test files. This patch resolves the conflict
  by renaming one of the test files and adjusting its content. This change is internal
  to the test suite and does not affect compiler behavior.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3bae47f716b56fbfbf63653a73f34a768a064d51
date: '2026-10-21'
is_stub: true
stub_reason: low_score
---

This commit addresses a naming conflict in the torture test suite by moving the gcc.dg/torture/bitint-112.c test to a new file, gcc.dg/torture/bitint-114.c. The move resolves an issue where a test with the same name was committed in a previous pull request. The change ensures that test cases are correctly organized and that diagnostics are accurate.
