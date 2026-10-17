---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- c++20
- ranges
commit_hash: b3a3ecc460237948d924bca6cb8fe15622e5025b
source_type: github
author: Jesse Connell
headline: libstdc++ ranges::mismatch returns correct iterator type.
tldr: The ranges::mismatch function in libstdc++ now returns the correct iterator
  type as specified by the standard.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `<ranges>` library in C++20 introduces various algorithms. For
  algorithms like `mismatch` that return iterators, the standard specifies using `std::ranges::borrowed_iterator_t<I>`
  for the return type to correctly handle iterators that might become invalidated
  after the algorithm returns. This commit updates the `ranges::mismatch` implementation
  in libstdc++ to adhere to this, fixing a deviation from the standard.
primer_glossary:
- term: ranges::mismatch
  definition: A C++20 algorithm that compares two ranges element by element and returns
    a pair of iterators pointing to the first differing elements.
- term: borrowed_iterator_t
  definition: A C++20 type trait that determines the appropriate iterator type to
    return from a ranges algorithm, ensuring it's not a dangling reference.
- term: libstdc++
  definition: The standard C++ library implementation used by GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3a3ecc460237948d924bca6cb8fe15622e5025b
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

The C++ standard library's implementation of `ranges::mismatch` in libstdc++ has been corrected to return the `borrowed_iterator_t` type. This ensures consistency with the standard's specification and prevents potential issues with dangling iterators in certain use cases. A new test case verifies this fix.
