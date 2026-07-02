---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- diagnostics
- vectorization
- code-safety
- compiler
commit_hash: df1eb95b6e915117dc33cf70dbd46be66c23057f
source_type: github
author: Richard Biener
headline: Tree-optimization expands uninitialized detection for RMW patterns
tldr: GCC's tree-optimization now detects uninitialized read-modify-write patterns
  involving `VIEW_CONVERT_EXPR` for better code safety, especially in vectorized cod…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `maybe_warn_operand` function in `tree-ssa-uninit.cc` is responsible
  for detecting uses of potentially uninitialized values. Specifically, it analyses
  RMW bit clear/set patterns to ensure operands are initialized. This patch extends
  this detection to include `VIEW_CONVERT_EXPR` within this analysis. `VIEW_CONVERT_EXPR`
  is particularly relevant in generic word-mode vectorization, where an expression's
  type might be internally changed for vector operations without an explicit cast.
  Prior to this change, such expressions could mask RMW patterns, leading to missed
  uninitialized warnings. By r…
primer_general: Compilers aim to catch potential errors in your code before it even
  runs. One common and dangerous error is using a variable that hasn't been given
  an initial value, leading to unpredictable program behavior. This is called using
  an "uninitialized variable." This change improves the GCC compiler's ability to
  detect such errors, especially in a specific type of operation called "Read-Modify-Write"
  (RMW), where a value is read from memory, changed, and then written back. This is
  particularly important with "vectorization," a compiler optimization technique that
  processes multiple data elements at once using special CPU instructions (SIMD).
  During vectorization, the compiler sometimes internally changes how it views data
  types using something called `VIEW_CONVERT_EXPR`. This update teaches the compiler
  to look through these internal type conversions when checking for uninitialized
  variables in RMW patterns, ensuring that even complex, optimized code is safer and
  less prone to runtime cra…
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/df1eb95b6e915117dc33cf70dbd46be66c23057f
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's uninitialized variable detection within the tree-optimization pass by expanding its ability to recognize Read-Modify-Write (RMW) bit clear/set patterns. Specifically, it now accounts for `VIEW_CONVERT_EXPR` which often appears in generic word-mode vectorization, where data types are implicitly converted. This improvement helps the compiler identify potential uses of uninitialized memory in more complex, vectorized code, preventing runtime errors and improving code quality, addressing PR tree-optimization/110743.
