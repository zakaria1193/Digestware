---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- inplace_vector
- ranges
- static_assert
- lwg
commit_hash: e38acbc88bfede15884009330ab75debb114905d
source_type: github
author: Tomasz Kamiński
headline: 'Libstdc++: Static_assert that static sized range size is less than inplace_vector
  capacity'
tldr: Adds static assertions to `inplace_vector` to ensure the size of a statically-sized
  input range doesn't exceed its capacity.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This change addresses LWG 4396 and improves the `inplace_vector` constructor
  when used with ranges.  The core idea is to leverage static size information (as
  indicated by  `ranges::__static_sized_range`) to `static_assert` the range''s size
  against the `inplace_vector`''s capacity. The interaction with `ref_view` is subtle:
  a `ref_view` to a `std::array` loses static size because it stores a pointer, while
  a `ref_view` to a `std::span` preserves it.'
primer_general: '`inplace_vector` is a container that stores its elements directly
  within its own memory, avoiding dynamic memory allocation if the number of elements
  is known at compile time and fits within its internal buffer. A ''range'' is a sequence
  of elements that can be iterated over. This commit adds compile-time checks to ensure
  that when an `inplace_vector` is constructed from a range whose size is known at
  compile time, the range''s size does not exceed the `inplace_vector`''s capacity,
  preventing potential buffer overflows or unexpected behavior.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e38acbc88bfede15884009330ab75debb114905d
date: '2026-04-24'
is_stub: false
---

This commit resolves LWG 4396 by improving the `inplace_vector(from_range_t, R&& rg)` constructor. It introduces `static_assert` checks to verify that the size of the input range `R` does not exceed the capacity of the `inplace_vector` at compile time, preventing potential buffer overflows. The commit also adds test cases to demonstrate how views applied to `span<T, N>` remain statically sized, while those applied to `array<T, N>` do not, due to the pointer semantics of `ref_view`.
