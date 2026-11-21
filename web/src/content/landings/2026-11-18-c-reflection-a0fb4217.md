---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler bug
commit_hash: a0fb421786d4cdc18a12954f4c87c8df5c1fece8
source_type: github
author: Marek Polacek
headline: Ensure non-constant flag is set in reflection error paths.
tldr: Fixes reflection error handling to correctly flag non-constant expressions.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/cp/reflect.cc`, the `get_meta_exception_object` function's
  error path was missing the crucial step of setting `*non_constant_p` when an error
  occurred. This commit adds that setting, ensuring that the compiler correctly tracks
  expressions that cannot be determined to be constant during compile-time evaluation.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0fb421786d4cdc18a12954f4c87c8df5c1fece8
date: '2026-11-18'
is_stub: true
stub_reason: low_score
---

This commit corrects an oversight in the C++ reflection module where an error path in `get_meta_exception_object` failed to set the `*non_constant_p` flag. This flag is crucial for indicating that an expression cannot be evaluated at compile time. By setting this flag, subsequent compilation stages can correctly identify and handle such non-constant expressions, preventing potential errors.
