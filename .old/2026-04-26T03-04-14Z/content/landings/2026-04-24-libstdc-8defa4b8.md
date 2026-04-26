---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- ranges
- bugfix
- C++
commit_hash: 8defa4b8b1ce23c68e681a42ba82c471c2a10bff
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Constrain views::adjacent(_transform)?<0> to forward_ranges
  (LWG4098).'
tldr: The standard library now enforces that `views::adjacent<0>` and `views::adjacent_transform<0>`
  only accept forward ranges, as required by LWG4098.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch resolves LWG4098 by adding `forward_range` constraints to
  `_Adjacent::operator()` and `_AdjacentTransform::operator()` when `N == 0`. This
  prevents the use of `views::adjacent<0>` and `views::adjacent_transform<0>` with
  input ranges, which is disallowed by the standard.  The changes are in `include/std/ranges`,
  and tests are added in `testsuite/std/ranges/adaptors/adjacent/1.cc` and `testsuite/std/ranges/adaptors/adjacent_transform/1.cc`.
primer_general: In C++, `views` are a way to lazily process ranges of data. `adjacent_view`
  and `adjacent_transform_view` provide a view of groups of adjacent elements in a
  range.  A `forward_range` is a range that can be traversed multiple times.  This
  commit enforces a requirement in the C++ standard that `views::adjacent` and `views::adjacent_transform`
  with a size of 0 can only be used with forward ranges. This ensures that the code
  behaves as expected and avoids potential errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8defa4b8b1ce23c68e681a42ba82c471c2a10bff
date: '2026-04-24'
---

The C++ standard requires that `views::adjacent<0>` and `views::adjacent_transform<0>` only operate on forward ranges, and the library is now enforcing this constraint.  The `_Adjacent::operator()` and `_AdjacentTransform::operator()` are now constrained to require `forward_range` when `N` is 0. This prevents undefined behavior when using these views with non-forward ranges and resolves LWG4098.
