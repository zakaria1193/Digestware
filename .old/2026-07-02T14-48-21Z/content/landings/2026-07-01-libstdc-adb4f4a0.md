---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- build
- atomic
- timezone
commit_hash: adb4f4a064c009cd616106fa4c648182c18f96d9
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Fix tzdb.cc build failure with specific atomic configurations'
tldr: libstdc++ tzdb.cc build failures due to mismatched atomic lock-free settings
  are fixed by unconditionally defining required functions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A bootstrap failure was occurring in `libstdc++`'s `tzdb.cc` when the
  target had `ATOMIC_POINTER_LOCK_FREE != 2 && ATOMIC_INT_LOCK_FREE == 2`. This was
  due to `_Node::NumLeapSeconds` not defining `set_locked` in this specific configuration,
  while `_S_replace_head` attempted to call it. The fix involves redefining `set_atomically`
  (renaming it to `set`) and `set_locked` unconditionally within `_Node::NumLeapSeconds`.
  This ensures both functions are always present, regardless of the `#if/#else` conditions
  related to atomic lock-free properties, thus resolving the ABI mismatch and build
  error.
primer_general: This commit fixes a build error in the C++ standard library (libstdc++),
  specifically when compiling code related to timezone data (`tzdb.cc`). The error
  occurred on certain systems where the compiler's settings for atomic operations
  (operations that must complete entirely without interruption) had a specific configuration
  mismatch. This mismatch meant a required function (`set_locked`) was missing in
  some cases. The fix ensures that the necessary functions for handling leap second
  data are always defined, regardless of these atomic settings, allowing the library
  to build correctly across different configurations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/adb4f4a064c009cd616106fa4c648182c18f96d9
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

A recent change in libstdc++ caused a bootstrap failure on targets where `ATOMIC_POINTER_LOCK_FREE != 2` and `ATOMIC_INT_LOCK_FREE == 2`. The error occurred in `tzdb.cc` because the `NumLeapSeconds` struct was missing the `set_locked` member in some configurations. This commit resolves the issue by ensuring that both `set_atomically` (renamed to `set`) and `set_locked` functions are defined unconditionally within `_Node::NumLeapSeconds`. This guarantees their availability regardless of the target's atomic properties, fixing the build problem.
