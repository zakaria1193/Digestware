---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- gcc
commit_hash: ef24b6ea01070061fcecc24033dcc759a03d99e5
source_type: github
author: Jakub Jelinek
headline: 'testsuite: Fix mem-notrap-load-builtin.C test arguments'
tldr: Corrects argument order in a test case for scan-rtl-dump.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `scan-rtl-dump` tool in GCC''s testsuite expects its arguments
  in a specific order: dump name first, then the regular expression. A previous commit
  accidentally reversed this order. This fix restores the correct order to ensure
  the test accurately checks for the presence or absence of specific RTL dump patterns.'
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ef24b6ea01070061fcecc24033dcc759a03d99e5
date: '2026-10-20'
is_stub: true
stub_reason: low_score
---

This commit corrects the argument order for the scan-rtl-dump command within the mem-notrap-load-builtin.C test file. An earlier change inadvertently swapped the dump name and the regular expression, leading to the test failing to resolve.
