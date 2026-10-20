---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- arm
- vectorization
commit_hash: d80deed256650bf0b0ac14dc599b77500992115e
source_type: github
author: Torbjörn SVENSSON
headline: 'testsuite: Add -fno-associative-math to resolve warning in vect-pr127876-1.c'
tldr: Add -fno-associative-math to a test case to prevent a warning when -fsigned-zeros
  conflicts with ARM NEON's -ffast-math.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC testsuite uses flags like -fsigned-zeros and -ffast-math for
  vectorization tests. On ARM NEON, -ffast-math can lead to warnings if -fsigned-zeros
  is also enabled. Adding -fno-associative-math prevents this specific warning by
  disabling the associativity optimization, ensuring test stability.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d80deed256650bf0b0ac14dc599b77500992115e
date: '2026-10-19'
is_stub: true
stub_reason: low_score
---

This commit addresses a warning in the vect-pr127876-1.c test case. It adds the -fno-associative-math flag to resolve a conflict between -fsigned-zeros and the ARM NEON test suite's use of -ffast-math. This ensures the test suite functions correctly without unnecessary warnings.
