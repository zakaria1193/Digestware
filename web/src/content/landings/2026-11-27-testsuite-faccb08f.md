---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- regression
commit_hash: faccb08f208f4955da65a55fa4424d2dc0d655d9
source_type: github
author: Jakub Jelinek
headline: Add testcase for already fixed PR [PR128930]
tldr: New testcase added to GCC's testsuite for a previously fixed bug.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a regression test to the GCC testsuite for a bug that
  was fixed in the middle-end. The new testcase ensures that the fix for PR128930
  remains effective and increases overall test suite coverage.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/faccb08f208f4955da65a55fa4424d2dc0d655d9
date: '2026-11-27'
is_stub: true
stub_reason: low_score
---

A new test case has been added to the GCC testsuite to cover a bug that has already been fixed. This aims to increase test coverage and prevent regressions for the issue, which was resolved in a previous commit.
