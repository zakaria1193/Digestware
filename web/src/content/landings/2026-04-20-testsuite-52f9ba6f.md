---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
commit_hash: 52f9ba6f33514cefa4b4de67b570b03531bbfef7
source_type: github
author: Jakub Jelinek
headline: 'Testsuite: Remove -m32 option from an i386 test.'
tldr: Removes the `-m32` option from a test case, ensuring it's executed in relevant
  configurations.
why_it_matters: Ensures that tests are run in the correct configurations, preventing
  false positives or negatives and improving test coverage.
impact_score: 4
impact_rationale: The change improves the testsuite's correctness.
performance_win: false
breaking_change: false
outcome: committed
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/52f9ba6f33514cefa4b4de67b570b03531bbfef7
date: '2026-04-20'
---

The commit removes the `-m32` option from a test case in the `gcc.target/i386` directory. The test doesn't have i386-specific code and should be run during i686-linux testing or x86_64-linux testing with `--target_board=unix{-m32,-m64}`.
