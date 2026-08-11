---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: b947bd4aac67ba3bdb6030aa4ac2f3eb0204df05
source_type: github
author: Richard Biener
headline: Avoid inferring non-null for TARGET_MEM_REF operands
tldr: Compiler avoids miscompilation by not assuming memory references are non-null.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `non_null_loadstore` and `check_loadstore` routines in GIMPLE and
  range inference are adjusted to avoid inferring non-nullness for the base operand
  of `TARGET_MEM_REF`. This is to prevent issues like the one in PR tree-optimization/126658,
  where jump threading incorrectly assumed the base was dereferenced and thus non-null,
  leading to miscompilation. The change carves out the common case of scaled indexes,
  which are unlikely to be actual pointers.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b947bd4aac67ba3bdb6030aa4ac2f3eb0204df05
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

The compiler now avoids inferring that the base operand of a TARGET_MEM_REF is non-null. This change corrects a miscompilation in jump-threading optimizations that was triggered by a testcase where a non-null assumption was incorrectly made. The fix adjusts three areas within the compiler's GIMPLE and range inference passes to take a more conservative stance, particularly for scaled index operands.
