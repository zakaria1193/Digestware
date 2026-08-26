---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- endianness
commit_hash: ea6bfeafc48af3e6dab598376dda4586752ed990
source_type: github
author: Alexandre Oliva
headline: 'testsuite: explicitly specify expected endianness'
tldr: Test case explicitly specifies little-endian data structures to match expectations.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The pr126650.c testcase in GCC's testsuite had implicit assumptions
  about data structure layout being little-endian. This commit explicitly sets these
  structures to be little-endian to ensure the test case behaves as expected and reliably
  detects regressions.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ea6bfeafc48af3e6dab598376dda4586752ed990
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

The test case pr126650.c relies on data structures being little-endian. This commit makes those expectations explicit by ensuring nonscalar data structures are little-endian. This addresses PR126650.
