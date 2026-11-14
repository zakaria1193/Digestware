---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- optimization
- rtl
commit_hash: 9ef00f3c4784e2e4fb10eaa720dbde3afbb5baf4
source_type: github
author: Jiawei
headline: Reverse rotations with masked negative counts in generic RTL simplifier
tldr: Generic RTL simplifier reverses rotations with masked negative counts, preserving
  the count mask.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify-rtx.cc` file contains logic for simplifying RTL (Register
  Transfer Language) expressions. This commit modifies `simplify_binary_operation_1`
  to correctly handle reversed rotations when the rotation count is masked and negative.
  The key is preserving the count mask during reversal to maintain the integrity of
  the rotation amount. New selftests are added to verify this behavior, particularly
  for architectures like RISC-V and AArch64 that utilize such operations.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ef00f3c4784e2e4fb10eaa720dbde3afbb5baf4
date: '2026-11-14'
is_stub: false
stub_reason: ''
---

The generic RTL simplifier now correctly reverses rotations with masked negative counts. This change ensures that the reversed count remains within its valid range by keeping the count mask. New selftests for masked negative rotate operations are added for RISC-V and AArch64.
