---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- testing
- refactor
commit_hash: 6d81aac02a9cd39a67c129054795f9626c658056
source_type: github
author: feedable
headline: Converts IEEE Tests to New Test Format
tldr: Modernizes the gcc.c-torture/execute/ieee testsuite to use dg-* annotations,
  replacing separate setup files.
why_it_matters: Simplifies test maintenance by embedding test configuration directly
  within the test source files.
impact_score: 5
impact_rationale: Refactors the testsuite, improving maintainability.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit converts tests in `gcc.c-torture/execute/ieee/` to use
  `dg-*` directives.  The `dg-*` annotations are standard directives interpreted by
  the DejaGnu test framework.  Historically, the `*.exp` files contained Tcl code
  to manage test setup, but modern GCC testsuites prefer embedding this configuration
  directly into the C source via special comments.
primer_general: The GCC testsuite uses DejaGnu, a framework that automates the execution
  and verification of tests.  Historically, test configuration was often handled in
  separate `.exp` files written in Tcl.  Modern GCC testsuites, however, prefer embedding
  test configuration directly within the C source code using special comments that
  begin with `dg-`. This commit transitions a portion of the GCC testsuite to this
  newer, more maintainable format.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6d81aac02a9cd39a67c129054795f9626c658056
date: '2026-04-11'
---

The `gcc.c-torture/execute/ieee` testsuite is updated to utilize `dg-*` annotations for test configuration.  This replaces the previous system of separate test setup files, streamlining the testing process and making the tests easier to understand and maintain. The `ieee.exp` file is replaced with a modified copy of `execute/execute.exp`.
