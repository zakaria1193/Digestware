---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- diagnostics
commit_hash: 8b3e2e68208730dc95a7803a21a545e93c735d5b
source_type: github
author: Marek Polacek
headline: Refines diagnostic for `size_of` with function reflection.
tldr: GCC's C++ reflection now provides a more precise diagnostic message when `size_of`
  is used with a reflection of a function.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's C++ reflection system, specifically `reflect.cc`, handles compile-time
  queries about types. The `eval_size_of` function attempts to determine the size
  of a type based on its reflection. A `FUNCTION_TYPE` (a function's type signature,
  e.g., `int(void)`) does not have a well-defined "size" in the same way an object
  type does. The original diagnostic for this scenario, "reflection with incomplete
  type," was misleading. The fix introduces a specific `throw_exception` path for
  function types, providing a more accurate diagnostic that clarifies that `size_of`
  is not applicable to them.
primer_general: C++ reflection is a new feature that lets programs inspect their own
  code structure at compile time. One of the things you can do with reflection is
  ask for the "size_of" a type, which tells you how much memory an object of that
  type would take up. This commit improves a specific error message within the reflection
  system. If you tried to ask for the "size_of" a function itself (not the size of
  its return value, but the function's type signature), the old error message was
  vague. The new message is much clearer, telling you directly that you can't ask
  for the size of a function's type in this way.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8b3e2e68208730dc95a7803a21a545e93c735d5b
date: '2026-06-11'
is_stub: true
stub_reason: low-score
---

This commit improves the diagnostic message issued by GCC when the `size_of` reflection operation is applied to the reflection of a function type. Previously, the error message ambiguously stated "reflection with incomplete type." The updated diagnostic now specifically clarifies that the issue is with using `size_of` on a function type, providing more helpful feedback to developers.
