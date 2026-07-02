---
project: gcc
subsystem: c++/modules
patch_id: null
tags:
- c++
- modules
- noexcept
- return type deduction
commit_hash: b4edbe6ff3393733c0bbe9717e0f5abd6775e5d3
source_type: github
author: Patrick Palka
headline: 'C++/modules: Handle noexcept and deduced auto when merging functions.'
tldr: Fixes a return type issue when merging functions with instantiated noexcept
  specifiers and deduced return types in C++ modules.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When streaming in a function from a C++ module (e.g., data() from view_interface<int>),
  the streamed-in version might have its noexcept specifier already instantiated and
  its return type deduced. During merging with the in-TU version, is_matching_decl
  logic updates the in-TU version. The patch modifies trees_in::is_matching_decl in
  module.cc to propagate the instantiated noexcept specifier more narrowly, avoiding
  premature return type updates that interfere with deduced return type checks.
primer_general: C++ modules allow you to import code from other files, similar to
  headers but with better isolation and compilation speed. When the compiler merges
  a function definition from a module with an existing definition in your code, it
  needs to reconcile properties like whether the function can throw exceptions (noexcept)
  and whether the return type was automatically deduced. This commit fixes an issue
  where the compiler was incorrectly handling these properties during the merge, which
  led to errors when using modules.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b4edbe6ff3393733c0bbe9717e0f5abd6775e5d3
date: '2026-05-01'
---

When merging functions from streamed-in C++ modules with in-TU (translation unit) versions, GCC can prematurely update the return type, leading to issues with deduced return type checks. This patch narrowly propagates the instantiated noexcept specifier using build_exception_variant and ensures the function type isn't stale during updates. This fixes PR125115.
