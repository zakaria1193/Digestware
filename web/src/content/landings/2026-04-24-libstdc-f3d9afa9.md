---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- ranges
- documentation
- C++
commit_hash: f3d9afa91c740fe441ede6f9320664a952375d97
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Add LWG4083 resolution comment for views::as_rvalue.'
tldr: This commit adds a comment to the standard library to indicate the resolution
  of LWG4083 regarding `views::as_rvalue`.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch adds a comment to `include/std/ranges` to indicate that
  LWG4083 is resolved. The defect report specified that `views::as_rvalue` should
  reject non-input ranges. The resolution is that the existing trait `__detail::__can_as_rvalue_view<_Range>`
  already implies `input_range<_Range>`, so no further changes are needed. This commit
  improves code clarity by documenting this resolution.
primer_general: In C++, `views` provide a way to lazily process ranges of data. `as_rvalue_view`
  converts a range to a range of rvalue references.  An `input_range` is a range that
  can be read from.  This commit adds a comment to the standard library's code to
  indicate how a particular issue (LWG4083) regarding `as_rvalue_view` and input ranges
  has been resolved, improving the code's documentation and understandability.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f3d9afa91c740fe441ede6f9320664a952375d97
date: '2026-04-24'
---

This commit adds a comment to the `include/std/ranges` header file to document the resolution of LWG4083, which concerns the requirement that `views::as_rvalue` should only accept input ranges. The resolution is that `input_range<_Range>` is implied by `__detail::__can_as_rvalue_view<_Range>`, clarifying the standard library's behavior.
