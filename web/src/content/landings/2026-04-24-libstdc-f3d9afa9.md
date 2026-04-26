---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- ranges
- C++20
- bugfix
commit_hash: f3d9afa91c740fe441ede6f9320664a952375d97
source_type: github
author: Tomasz Kamiński
headline: Libstdc++ Adds Comment for LWG4083
tldr: The libstdc++ adds a comment resolving LWG4083 about `views::as_rvalue`.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: '`std::ranges::views::as_rvalue` casts each element in the underlying
  range to an rvalue.  LWG4083 asks whether this view should reject non-input ranges.  The
  standard library already constrains this with `__detail::__can_as_rvalue_view<_Range>`.  This
  commit adds a comment to `include/std/ranges` to explain.'
primer_general: '`std::ranges` is a C++20 feature that provides a way to compose transformations
  on sequences of data. `views::as_rvalue` transforms a range by casting each element
  to an rvalue, which can be useful for move semantics. Input ranges are the most
  basic type of range in C++, supporting only single-pass iteration. This commit adds
  a comment to the code to clarify that `views::as_rvalue` correctly handles the constraints
  on input ranges, specifically addressing issue LWG4083.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f3d9afa91c740fe441ede6f9320664a952375d97
date: '2026-04-24'
---

This commit adds a comment to the libstdc++ standard library to indicate the resolution of LWG4083, which concerns the constraints on `views::as_rvalue`. The resolution clarifies that `views::as_rvalue` should reject non-input ranges, and this is implicitly handled by the existing `__detail::__can_as_rvalue_view<_Range>` trait.
