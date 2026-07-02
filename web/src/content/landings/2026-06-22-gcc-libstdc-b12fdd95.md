---
project: gcc
subsystem: gcc/libstdc++
patch_id: null
tags:
- libstdc++
- portability
- atomic
commit_hash: b12fdd952511786bf8d285e7080e94deeb32aa1d
source_type: github
author: Jonathan Wakely
headline: Remove std::atomic dependency in tzdb.cc for non-atomic targets
tldr: Libstdc++ tzdb.cc avoids atomic<unsigned> for targets lacking atomic word operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A previous optimization for leap second handling in `tzdb.cc` (`r17-471-ge79f0f818c0e42`)
  introduced a dependency on `std::atomic<unsigned>`. This commit removes that dependency
  to support targets lacking word-sized atomics (e.g., Cortex-M0). It introduces `_Node::NumLeapSeconds`,
  a struct that conditionally uses `std::atomic_ref<unsigned>` or locks a pre-existing
  mutex (`list_mutex()`) for access. This relies on the assumption that `num_leap_seconds`
  is accessed by only one caller and that the mutex is held when atomics are unavailable.
primer_glossary:
- term: std::atomic
  definition: A C++ class template that provides atomic operations on its value. Atomic
    operations are guaranteed to be indivisible and not interfere with other threads,
    even on multi-core processors.
- term: libstdc++
  definition: The standard C++ library implementation used by GCC.
- term: tzdb
  definition: Time Zone Database. A database containing information about time zones
    worldwide, including historical data and daylight saving rules.
- term: Cortex-M0
  definition: A low-power, 32-bit ARM processor core often used in embedded systems.
    It has limited capabilities, including potentially lacking hardware support for
    atomic word operations.
- term: std::atomic_ref
  definition: A C++ class template that provides atomic operations on an existing
    object, without taking ownership of it. Useful for managing atomic access to shared
    data when direct atomic ownership is not feasible.
- term: mutex
  definition: Mutual Exclusion. A synchronization primitive used to prevent multiple
    threads from accessing a shared resource concurrently, ensuring that only one
    thread can execute a critical section of code at a time.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b12fdd952511786bf8d285e7080e94deeb32aa1d
date: '2026-06-22'
is_stub: false
stub_reason: ''
---

To support targets without atomic word operations, such as Cortex-M0, libstdc++'s timezone database implementation (`tzdb.cc`) now avoids a hard dependency on `std::atomic<unsigned>`. This change replaces the atomic variable with a struct that uses a mutex-protected access or `std::atomic_ref`, depending on the context, ensuring compatibility across a wider range of hardware.
