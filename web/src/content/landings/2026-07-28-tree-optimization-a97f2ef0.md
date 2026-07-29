---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorizer
- bugfix
commit_hash: a97f2ef0d90d46144b39a8c9ea670b52dd13233a
source_type: github
author: Richard Biener
headline: tree-optimization/126404 - Fix CTZ pattern to not break reductions
tldr: Prevents the CTZ pattern recognizer from breaking vector reduction chains by
  avoiding recursion on reduction patterns.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes GCC PR tree-optimization/126404. The `vect_recog_popcount_clz_ctz_ffs_pattern`
  function incorrectly recursed into `vect_recog_ctz_ffs_pattern` even when the original
  pattern was intended for vector reduction. This commit modifies `vect_recog_popcount_clz_ctz_ffs_pattern`
  to avoid this recursion when a reduction pattern is detected, preventing the premature
  breaking of reduction chains.
primer_glossary:
- term: CTZ
  definition: Count Trailing Zeros. An instruction or function that counts the number
    of zero bits from the least significant bit up to the first set bit.
- term: vector reduction
  definition: A loop transformation technique where operations within a loop, such
    as summation or finding a minimum/maximum, are parallelized across vector lanes.
    The final result is then produced by combining the results from each lane.
- term: pattern recognition
  definition: In compilers, a technique used by optimizers to identify specific sequences
    or structures in the intermediate representation that correspond to known efficient
    operations or idioms.
- term: tree-optimization
  definition: A phase in GCC's compilation pipeline where the intermediate representation
    (GIMPLE, which resembles an abstract syntax tree) is analyzed and transformed
    to improve code efficiency.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a97f2ef0d90d46144b39a8c9ea670b52dd13233a
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

A bug in the Count Trailing Zeros (CTZ) pattern recognition logic could cause it to incorrectly recurse into a temporary pattern statement. This led to the vectorizer breaking reduction chains because the setup was incomplete, resulting in multiple uses of the intermediate pattern. The fix ensures that the recognizer avoids recursing when the original pattern is part of a reduction, thus preserving the integrity of vector reductions.
