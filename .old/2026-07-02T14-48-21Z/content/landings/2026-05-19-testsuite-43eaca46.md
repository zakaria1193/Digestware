---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- crc
- regex
- optimization
commit_hash: 43eaca46f9687032afab852a13cc51db1e9d2cb9
source_type: github
author: Kito Cheng
headline: 'Testsuite: Update CRC dump scan regex for reversed crc table'
tldr: Updates testsuite regexes to match the new "emitting reversed crc table" message
  in CRC table dumps.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Commit r17-567 changed the output of CRC table dumps when a reversed
  CRC table is built directly (i.e., without using a crc_rev optab).  The testsuite
  expected "emitting crc table", but the new message is "emitting reversed crc table".  This
  commit updates the regexes in `gcc.dg/crc-builtin-rev-target*.c` to match the new
  output, specifically for targets like x86 without TARGET_CRC32.
primer_general: Cyclic Redundancy Check (CRC) is an error-detecting code commonly
  used in digital networks and storage devices. The compiler generates CRC tables
  to speed up CRC calculations. The testsuite verifies the correctness of these tables
  by examining the compiler's output (dumps). This commit updates the tests to account
  for a recent change in how the compiler describes reversed CRC tables in its output,
  thus preventing false test failures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/43eaca46f9687032afab852a13cc51db1e9d2cb9
date: '2026-05-19'
is_stub: false
---

The middle-end optimization that builds reversed CRC tables directly changed the dump message. This commit updates the testsuite regexes to match the new message, preventing test failures on targets without a crc_rev optab (e.g., x86 without SSE4.2). This ensures that the testsuite continues to function correctly after the CRC table optimization.
