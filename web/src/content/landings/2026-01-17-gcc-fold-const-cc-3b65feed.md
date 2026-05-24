---
project: gcc
subsystem: gcc/fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- overflow
commit_hash: 3b65feed776df4c79a958406ad1bd25aeb08b38e
source_type: github
author: Daniel Barboza
headline: Remove strict overflow flag from make_range helpers
tldr: The strict_overflow flag was removed from make_range helpers, as part of deprecating
  the -Wstrict_overflow warning.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the `strict_overflow_p` flag from `make_range`
  and `make_range_step` within `fold-const.cc`. These helpers, used both locally and
  in files like `tree-ssa-reassoc.cc`, construct ranges for value-range analysis.  The
  change directly supports the deprecation of `-Wstrict_overflow`. The impact is primarily
  on compile-time constant folding and associated warning behavior.
primer_general: GCC uses value ranges to optimize code. The `make_range` and `make_range_step`
  functions are used to create these ranges during constant folding. The `-Wstrict_overflow`
  flag instructs the compiler to warn about potential integer overflows during constant
  folding. This commit removes the `strict_overflow_p` flag from these functions,
  as part of a larger effort to deprecate the `-Wstrict_overflow` compiler flag.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3b65feed776df4c79a958406ad1bd25aeb08b38e
date: '2026-01-17'
is_stub: false
---

The `strict_overflow_p` flag was removed from the `make_range` and `make_range_step` helper functions in `fold-const.cc`. These functions generate ranges of values, and the change is a step towards deprecating the `-Wstrict_overflow` warning. Callers in other files were updated to accommodate the removal of the flag.
