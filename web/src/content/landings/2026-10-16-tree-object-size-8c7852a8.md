---
project: gcc
subsystem: tree-object-size
patch_id: null
tags:
- tree-object-size
- bugfix
commit_hash: 8c7852a8d443b343aacd9e58a5776680e26bcd0a
source_type: github
author: Siddhesh Poyarekar
headline: 'tree-object-size: Fix typo in addr_object_size'
tldr: Corrects a simple typo in the `addr_object_size` function related to size checking.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A trivial typo correction in `addr_object_size`. The function incorrectly
  called `size_unknown_p(BYTES)` twice. It should have called `size_unknown_p(BYTES)`
  and `size_unknown_p(WHOLEBYTES)` to check if either the byte count or the whole
  size is unknown, respectively.
primer_glossary:
- term: tree-object-size
  definition: A GCC optimization pass that determines the size of objects at compile
    time, especially useful for dynamic memory allocation scenarios.
- term: addr_object_size
  definition: A function within the tree-object-size pass that calculates the size
    of an object based on its address and associated size information.
- term: size_unknown_p
  definition: A predicate function used in GCC's tree-object-size pass to check if
    the size of an object or expression is indeterminable at compile time.
- term: BYTES
  definition: Likely refers to the byte size of an object or expression within the
    tree-object-size pass.
- term: WHOLEBYTES
  definition: Likely refers to the total byte size of an object, potentially including
    padding or overhead, as tracked by the tree-object-size pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8c7852a8d443b343aacd9e58a5776680e26bcd0a
date: '2026-10-16'
is_stub: true
stub_reason: low_score
---

This commit fixes a minor typo in the `addr_object_size` function within GCC's `tree-object-size` optimization pass. The original code mistakenly called `size_unknown_p()` twice on the `BYTES` variable instead of once on `BYTES` and once on `WHOLEBYTES`, which could have led to incorrect size analysis.
