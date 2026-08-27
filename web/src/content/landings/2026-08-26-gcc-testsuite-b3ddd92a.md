---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- integer overflow
commit_hash: b3ddd92a2eee5bdc5c9d322bc5642f2a92614ac2
source_type: github
author: Georg-Johann Lay
headline: Fixes PR126415 test case by requiring int32plus.
tldr: Adjusts a test case to avoid overflow warnings by requiring a 32-bit integer
  type.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a testsuite issue in PR126415 where a conversion
  from `long int` to `int` resulted in an overflow warning. To preserve the test's
  intent, the test case now explicitly requires `int32plus`, ensuring the conversion
  is safe on platforms where `int` is smaller than `long`.
primer_glossary:
- term: int32plus
  definition: A compiler testsuite requirement indicating that the target platform
    must have an integer type at least 32 bits wide. This ensures that certain test
    cases, which rely on the range of 32-bit integers, can be executed without overflow
    or other type-related issues.
- term: PR126415
  definition: A bug report filed against the GCC compiler, specifically concerning
    an issue in the testsuite related to integer overflow warnings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3ddd92a2eee5bdc5c9d322bc5642f2a92614ac2
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

The test case pr126415.c generated overflow warnings due to converting a long int to a regular int. This commit modifies the test to require an int32plus type, resolving the warning without altering the test's integrity. It addresses PR126415 and PR52641.
