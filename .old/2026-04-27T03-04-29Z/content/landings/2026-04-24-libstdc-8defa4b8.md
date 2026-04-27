---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- ranges
- C++20
- bugfix
commit_hash: 8defa4b8b1ce23c68e681a42ba82c471c2a10bff
source_type: github
author: Tomasz Kamiński
headline: Libstdc++ Constrains views::adjacent(_transform)?<0> to forward_ranges
tldr: The libstdc++ now requires `forward_range` for `views::adjacent<0>`, fixing
  LWG 4098.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `std::ranges::views::adjacent` adaptor (and its `_transform` variant)
  produces a view of tuples of adjacent elements. For N=0, the view would need to
  repeatedly re-read elements from a non-forward range (e.g. an input stream). This
  commit enforces the `forward_range` constraint via SFINAE.  See also LWG issue 4098.
  The fix involves modifying `_AdjacentTransform::operator()` and `_Adjacent::operator()`
  in `include/std/ranges`.
primer_general: '`std::ranges` is a C++20 feature that provides a way to compose transformations
  on sequences of data in a lazy and efficient manner.  `views::adjacent` takes a
  range and produces a new range where each element is a tuple of adjacent elements
  from the original range. A forward range is a range that can be traversed multiple
  times without invalidating iterators. This commit enforces that `views::adjacent`
  only works with forward ranges to avoid undefined behavior.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8defa4b8b1ce23c68e681a42ba82c471c2a10bff
date: '2026-04-24'
---

The C++ standard library's `views::adjacent` and `views::adjacent_transform` now require that the input range be a `forward_range` when the adjacency window size is zero. This resolves LWG 4098, which clarifies that these views are not well-defined for non-forward ranges, as their behavior relies on iterating over the same range multiple times. The change adds compile-time checks to enforce this requirement.
