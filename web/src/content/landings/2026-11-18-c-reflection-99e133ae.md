---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler error
commit_hash: 99e133ae0b93ca33cae497cf3aeeb19567dc910b
source_type: github
author: Marek Polacek
headline: Fix evaluation of reflection functions and improve error reporting.
tldr: Correctly handle non-constant expressions in reflection functions and refine
  error messages.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `eval_reflect_constant`, `eval_reflect_object`, and `eval_reflect_function`
  functions in `gcc/cp/reflect.cc` were not consistently setting the `*non_constant_p`
  flag when encountering errors. This led to `error_mark_node` being present in initializers,
  causing subsequent `display_string_of` calls to crash. The fix guards the error
  reporting with `cxx_constexpr_quiet_p` to prevent duplicate messages and corrects
  type printing in error diagnostics.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/99e133ae0b93ca33cae497cf3aeeb19567dc910b
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This commit addresses issues in C++ reflection's evaluation functions, specifically `eval_reflect_*`. Previously, these functions could return error markers without properly setting a flag indicating a non-constant expression, leading to crashes later in the compilation process. The fix ensures this flag is set and guards against redundant error emissions. Additionally, it improves the clarity of error messages by printing the correct type information.
