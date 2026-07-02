---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- build
- atomic
commit_hash: adb4f4a064c009cd616106fa4c648182c18f96d9
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Fix bootstrap failure in tzdb.cc with specific atomic conditions'
tldr: Fixes a bootstrap build failure in tzdb.cc by ensuring atomic functions are
  always defined, regardless of target atomic pointer and integer lock-free condition…
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a bootstrap failure in `std::chrono::tzdb_list::_Node::_S_replace_head`
  on targets where `ATOMIC_POINTER_LOCK_FREE != 2` and `ATOMIC_INT_LOCK_FREE == 2`.
  The issue stemmed from conditional definitions of `NumLeapSeconds::set_locked` and
  `set_atomically` within `tzdb.cc`. The fix makes these functions unconditional to
  ensure their availability in all relevant code paths, preventing the build error.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/adb4f4a064c009cd616106fa4c648182c18f96d9
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

A recent change in libstdc++ caused a bootstrap failure in tzdb.cc when certain atomic pointer and integer lock-free conditions were met on the target. The error occurred because the `NumLeapSeconds::set_locked` member function was not defined under these specific conditions. This fix ensures that the `set_atomically` and `set_locked` functions are defined unconditionally, resolving the mismatch and allowing the build to complete successfully.
