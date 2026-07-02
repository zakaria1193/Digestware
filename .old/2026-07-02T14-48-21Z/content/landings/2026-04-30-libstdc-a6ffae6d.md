---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- C++
- atomic
- performance
commit_hash: a6ffae6d7f0fb4515103a5f056b691301988268d
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Use hardware_destructive_interference_size in atomic.cc.'
tldr: The libstdc++ now uses `std::hardware_destructive_interference_size` for aligning
  atomic variables to improve performance.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit removes `__waitable_state::_S_align` and uses `std::hardware_destructive_interference_size`
  for aligning `__waitable_state::_M_waiters` and `__waitable_state::_M_ver` in `src/c++20/atomic.cc`.
  This is done to avoid false sharing. Search snippets should focus on `std::hardware_destructive_interference_size`
  and false sharing.
primer_general: False sharing occurs when multiple threads access different data items
  that happen to reside within the same cache line. Even if the threads don't access
  the same variables, modifications by one thread can invalidate the cache line for
  other threads, leading to performance degradation. `std::hardware_destructive_interference_size`
  is a C++17 feature that provides the recommended alignment to avoid false sharing.
  This commit uses it to align atomic variables, which are commonly used for inter-thread
  communication, thereby reducing the likelihood of false sharing and improving performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a6ffae6d7f0fb4515103a5f056b691301988268d
date: '2026-04-30'
---

The libstdc++ now uses `std::hardware_destructive_interference_size` to align atomic variables in `atomic.cc`. This improves performance by reducing false sharing between threads. The code was moved from a header into the library, making it possible to use `std::hardware_destructive_interference_size` directly.
