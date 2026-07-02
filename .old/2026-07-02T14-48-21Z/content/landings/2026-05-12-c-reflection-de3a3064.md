---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- bugfix
commit_hash: de3a3064f65bb52053d771fa44fb982e8ec80727
source_type: github
author: Marek Polacek
headline: 'c++/reflection: overzealous complete_type in consteval_only_p [PR125280]'
tldr: The commit fixes a bogus "has incomplete type" error in C++ reflection by removing
  an unnecessary `complete_type` call.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR125280 by removing an overzealous `complete_type`
  call in `consteval_only_p` within `reflect.cc`. The call was causing a bogus "has
  incomplete type" error. The patch also avoids a crash in `consteval_only_p_walker::walk`
  by returning false for `error_mark_node`.
primer_general: This commit addresses a bug in GCC's experimental C++ reflection feature.
  C++ reflection allows programs to inspect and manipulate their own structure at
  compile time. The bug caused the compiler to incorrectly report an incomplete type
  error during constant evaluation, preventing valid code from compiling. This commit
  fixes the error and improves the reliability of the reflection feature.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/de3a3064f65bb52053d771fa44fb982e8ec80727
date: '2026-05-12'
is_stub: false
---

This commit resolves a false positive "has incomplete type" error in the C++ reflection implementation. The error occurred because `complete_type` was being called prematurely. The fix involves removing this call which aligns the behavior with Clang.
