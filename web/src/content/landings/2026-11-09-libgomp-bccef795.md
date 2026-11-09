---
project: gcc
subsystem: libgomp
patch_id: null
tags:
- libgomp
- openmp
- testing
commit_hash: bccef7957b593def5fbe481588764d31f3922e52
source_type: github
author: Thomas Schwinge
headline: 'libgomp: Fix test for OpenMP device query functions.'
tldr: Adjusts a libgomp test case to correctly handle device settings for OpenMP.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adjusts the testsuite for libgomp's omp_get_device_num_teams
  and omp_get_device_teams_thread_limit functions. The previous test setup incorrectly
  set an internal control variable (ICV) on the device, leading to regressions. The
  fix modifies the test case to set this ICV on the host, aligning with expected behavior
  and resolving test failures observed with code offloading enabled.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bccef7957b593def5fbe481588764d31f3922e52
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This commit fixes a regression in libgomp's test suite that occurred after introducing functions for querying OpenMP device properties. The test case 'teams-nteams-icv-1.c' was incorrectly configured, leading to failures when code offloading was enabled. The fix adjusts the test to set the relevant Internal Control Variable (ICV) on the host rather than the device, resolving the test failures.
