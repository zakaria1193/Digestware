---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- maintenance
commit_hash: e34c8b2b7a4ecc4867230284ba4c82e7ede65836
source_type: github
author: Eric Botcazou
headline: 'Testsuite: Corrects a PR reference in sso-22.c'
tldr: Fixes an outdated or incorrect reference to a bug report in a test case.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates a `pr` tag in `gcc.dg/sso-22.c` to point to the
  correct Problem Report. This is a maintenance task for the testsuite infrastructure.
primer_glossary:
- term: Testsuite
  definition: A collection of tests used to verify the correctness and performance
    of the compiler. It includes various test cases, configurations, and expected
    output comparisons.
- term: PR
  definition: Problem Report. In the context of open-source projects like GCC, a PR
    refers to a bug report or feature request filed by users or developers, typically
    tracked in an issue tracking system.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e34c8b2b7a4ecc4867230284ba4c82e7ede65836
date: '2026-11-25'
is_stub: true
stub_reason: low_score
---

A minor correction has been made to the GCC testsuite by updating an incorrect or outdated Problem Report (PR) reference within the `sso-22.c` test file.
