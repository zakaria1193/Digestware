---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- containers
- flat_map
- flat_set
- C++23
commit_hash: f46eccc9409136831225e30017a1d8ba6654a9b9
source_type: github
author: Patrick Palka
headline: 'libstdc++: Implement P3567R2 flat_meow fixes'
tldr: Implements fixes from P3567R2 for the `flat_map` and `flat_set` containers in
  libstdc++.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses issues in `_Flat_map_impl` and `_Flat_set_impl`
  as outlined in P3567R2. It removes `is_nothrow_swappable_v` assertions, defaults
  the copy constructor, and defines move constructors/assignment operators with corrected
  exception handling. Additionally, it introduces a new `insert_range` overload and
  makes `swap` conditionally noexcept, improving the exception safety and performance
  characteristics of `flat_map` and `flat_set`.
primer_general: '`flat_map` and `flat_set` are associative containers in the C++ standard
  library, similar to `std::map` and `std::set`, but with an underlying flat array
  storage. P3567R2 is a proposal to improve the specification and implementation of
  these containers. This commit incorporates fixes from this proposal into the libstdc++
  implementation, affecting exception safety, move semantics, and insertion behavior.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f46eccc9409136831225e30017a1d8ba6654a9b9
date: '2026-05-28'
is_stub: false
---

This commit implements several fixes from the P3567R2 proposal for the `flat_map` and `flat_set` containers in libstdc++.  The changes include removing unnecessary assertions, explicitly defaulting the copy constructor, correcting exception handling in the move constructor and assignment operator, defining a new `insert_range` overload, and making the `swap` function conditionally noexcept. These changes improve the correctness and efficiency of these containers.
