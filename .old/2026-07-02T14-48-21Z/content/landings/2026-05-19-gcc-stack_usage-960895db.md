---
project: gcc
subsystem: gcc/stack_usage
patch_id: null
tags:
- stack usage
- debugging
- c++
- tooling
commit_hash: 960895db66868a81fafbebe4392bf0f1054fc101
source_type: github
author: Andrew Pinski
headline: 'stack_usage: Print out the user visibility name, too'
tldr: The GCC stack usage tool now prints human-readable function names alongside
  mangled names.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The stack usage analysis tool (``toplev.cc``) outputs stack usage information
  for functions.  This commit modifies the output to include the user-visible name
  alongside the mangled name, improving readability. The mangled name is retained
  for correlation with assembly.
primer_general: When compiling code, it's important to understand how much memory
  each function uses on the stack.  The stack_usage tool in GCC helps developers analyze
  this.  This commit improves the tool's output by now showing both the internal (mangled)
  name of a function, and the name as it appears in the code. This makes it easier
  for developers to quickly identify which functions are using the most stack space.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/960895db66868a81fafbebe4392bf0f1054fc101
date: '2026-05-19'
is_stub: false
---

The stack usage analysis tool in GCC now prints both the mangled and human-readable names of functions.  This makes the output easier to understand, especially for C++ code where mangled names can be difficult to decipher. The mangled name is still included for correspondence with assembly code.
