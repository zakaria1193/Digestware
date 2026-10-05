---
project: gcc
subsystem: testsuite/powerpc
patch_id: null
tags:
- testsuite
- powerpc
- endianness
commit_hash: 3c64b04a9b2d0b362e1734f38af6d8d6d0dc0630
source_type: github
author: Avinash Jayakar
headline: Correct expected results for vec-replace-word tests on powerpc64 BE
tldr: Fixes incorrect expected outputs in powerpc64 big-endian tests for vec-replace-word
  intrinsics.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vec-replace-word` intrinsic's behavior can vary with endianness.
  This patch updates test expectations for powerpc64 big-endian targets to match the
  correct output, acknowledging that endianness handling is user-level responsibility
  per intrinsic documentation.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3c64b04a9b2d0b362e1734f38af6d8d6d0dc0630
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

This commit corrects the expected results for the `vec-replace-word-runnable_1.c` and `vec-replace-word-runnable_2.c` tests when run on powerpc64 big-endian targets. The documentation for the intrinsic states that the programmer is responsible for handling endianness, so the fix is applied to the test cases rather than the code generation.
