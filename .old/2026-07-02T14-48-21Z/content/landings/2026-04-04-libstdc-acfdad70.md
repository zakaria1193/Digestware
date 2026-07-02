---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- allocator
- string
- vector
- memory management
commit_hash: acfdad706d8acca6c4ed6ef3b63c2e02f1c47881
source_type: github
author: Nathan Myers
headline: libstdc++ leverages allocate_at_least for string and vector.
tldr: The `std::string` and `std::vector` classes in libstdc++ now use `allocate_at_least`
  to better utilize allocated memory, potentially improving performance with…
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch implements `allocator<>::allocate_at_least` relying on known
  alignment behavior of standard `operator new`. It then uses `allocator_at_least`
  in `string` and `vector`. This change exposes `string::_S_allocate_at_least` and
  `_M_create_plus` symbols to the ABI. Toolchain developers should note the changes
  to allocation logic within `basic_string` and `stl_vector`.
primer_general: In C++, allocators manage memory allocation for containers like `std::string`
  and `std::vector`.  The `allocate_at_least` function allows an allocator to inform
  a container about the minimum amount of memory it has allocated, which might be
  more than requested.  This commit modifies `std::string` and `std::vector` to use
  this information, allowing them to potentially use more of the allocated memory,
  avoid unnecessary reallocations, and improve efficiency, especially when using custom
  memory allocators. This improvement leverages a feature defined by the C++ standard
  (P0401).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/acfdad706d8acca6c4ed6ef3b63c2e02f1c47881
date: '2026-04-04'
is_stub: false
---

This commit introduces the use of `allocate_at_least` in `std::string` and `std::vector` within libstdc++. This function allows the containers to utilize the maximum amount of storage provided by a custom allocator, potentially improving performance and reducing memory fragmentation. The implementation relies on the known alignment behavior of standard `operator new`. This change primarily benefits users employing custom allocators, as it enables them to expose more information about the actual allocated storage to the containers.
