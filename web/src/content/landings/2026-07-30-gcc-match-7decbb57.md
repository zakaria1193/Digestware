---
project: gcc
subsystem: gcc/match
patch_id: null
tags:
- optimization
- pattern matching
- intrinsics
commit_hash: 7decbb57670c3c0f6136be00456fe9c8a41f7aed
source_type: github
author: Reshma Roy
headline: Fixes incorrect POPCOUNT pattern identification.
tldr: Corrects a pattern matcher to accurately identify the POPCOUNT intrinsic, preventing
  incorrect optimizations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file's third 32-bit POPCOUNT matcher, introduced in
  `r17-489-g8ca1e887847e2f`, had a predicate (`compare_tree_int (@5, 0x0F0F0F0F)`)
  that was checked twice, while the outer AND constant (`@7`) was never validated.
  This commit adds `compare_tree_int (@7, 0x0000003F)` to correctly constrain the
  match to the intended popcount idiom, preventing misidentification and potential
  incorrect folding to `IFN_POPCOUNT`.
primer_glossary:
- term: POPCOUNT
  definition: A CPU instruction or intrinsic function that counts the number of set
    bits (1s) in a binary integer.
- term: intrinsic
  definition: A function that is recognized and handled directly by the compiler,
    often mapping to a specific CPU instruction for performance.
- term: pattern matching
  definition: A compiler technique where the compiler looks for specific sequences
    of operations or code structures (patterns) to identify opportunities for optimization
    or transformation.
- term: IFN_POPCOUNT
  definition: Likely an internal GCC representation or flag indicating that a sequence
    of operations has been recognized as a POPCOUNT intrinsic.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7decbb57670c3c0f6136be00456fe9c8a41f7aed
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This commit corrects a bug in GCC's pattern matching for the POPCOUNT intrinsic. A previously introduced 32-bit matcher incorrectly identified patterns, accepting any mask due to a flawed predicate. The fix ensures that only the intended Hacker's Delight popcount idiom is folded into the IFN_POPCOUNT intrinsic by adding a necessary constant check.
