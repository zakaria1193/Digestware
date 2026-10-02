---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- gcov
- coverage
commit_hash: a6c53e9b737d57ec2954a2d69690719663be8323
source_type: github
author: Jørgen Kvalsvik
headline: 'testsuite: Add test for gcov function summaries.'
tldr: A new test suite has been added to verify the functionality of gcov's function
  summaries.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: N/A
primer_glossary:
- term: gcov
  definition: GCC's code coverage tool. It generates output files that detail which
    lines of source code were executed during a program's run.
- term: function summaries
  definition: A feature of gcov that provides aggregated coverage information for
    entire functions, summarizing execution counts and line coverage within each function.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a6c53e9b737d57ec2954a2d69690719663be8323
date: '2026-09-19'
is_stub: false
stub_reason: ''
---

This commit introduces a new test suite for gcov function summaries, addressing recent bugs that highlighted the need for better test coverage. The test is designed to be simple, checking for a summary header in test files and comparing it against gcov's standard output. This provides essential validation for an existing but previously untested feature.
