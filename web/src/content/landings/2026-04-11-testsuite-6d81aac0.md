---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- ieee
- test format
commit_hash: 6d81aac02a9cd39a67c129054795f9626c658056
source_type: github
author: feedable
headline: 'Testsuite: Convert gcc.c-torture/execute/ieee to the new test format'
tldr: Converts the ieee test directory to use dg-* annotations instead of separate
  test setup files.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The GCC testsuite uses a domain-specific language to describe test
  expectations.  Older tests relied on ``.exp`` files to set up the test environment;
  newer tests use ``dg-*`` annotations embedded directly in the C source file.  This
  commit modernizes the ``gcc.c-torture/execute/ieee`` directory. search_context returned:
  []'
primer_general: 'The GCC testsuite verifies the compiler''s correctness.  Tests can
  be configured using external files or annotations embedded in the test source code
  itself.  This commit updates the test suite to use embedded annotations for tests
  in the ``ieee`` directory, which should improve maintainability. search_context
  returned: []'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6d81aac02a9cd39a67c129054795f9626c658056
date: '2026-04-11'
---

The ieee test directory is updated to use dg-* annotations within the test files themselves, instead of relying on separate test setup files. This brings the ieee tests in line with the modern test format used by GCC, simplifying test maintenance.
