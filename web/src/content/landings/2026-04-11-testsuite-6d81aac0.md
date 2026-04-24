---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- floating-point
- ieee
- testing
commit_hash: 6d81aac02a9cd39a67c129054795f9626c658056
source_type: github
author: feedable
headline: 'Testsuite: Convert IEEE Tests to the New Test Format'
tldr: The IEEE floating-point tests are converted to use dg-* annotations, replacing
  separate test setup files.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modernizes the IEEE tests by converting them to use ``dg-*``
  annotations instead of separate ``.exp`` files, aligning them with the current testsuite
  conventions. The main change involves replacing ``ieee.exp`` with a modified ``execute/execute.exp``
  and porting the individual test cases to the new format.
primer_general: This commit updates the format of GCC's IEEE floating-point tests.  Modern
  compiler tests often embed directives directly in the test file using special comments.  This
  commit replaces the older system of separate test setup files with these inline
  directives, streamlining the tests and making them easier to understand.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6d81aac02a9cd39a67c129054795f9626c658056
date: '2026-04-11'
---

This commit converts the IEEE floating-point tests in ``gcc.c-torture/execute/ieee`` to use the new test format with ``dg-*`` annotations.  This replaces the older system of separate test setup files (``.exp``) with inline directives, making the tests easier to read and maintain.
