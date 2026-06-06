---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- builtins
- enums
- c
- c++
commit_hash: eaebd987e5492b23419b5c52482038a94066c640
source_type: github
author: Jakub Jelinek
headline: 'Testsuite: Improve enum argument testing of built-in functions'
tldr: The GCC testsuite now performs more thorough testing of built-in functions'
  handling of enumerated type arguments, including those with fixed underlying types,…
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC testsuite includes comprehensive tests for built-in functions
  (`__builtin_*`), which are intrinsic functions implemented directly by the compiler.
  This change specifically targets the `c-c++-common` test cases for `__builtin_clz`,
  `__builtin_ctz`, `__builtin_clrsb`, `__builtin_ffs`, `__builtin_parity`, `__builtin_popcount`,
  `__builtin_bswapg`, and `__builtin_bitreverseg`. The improvement ensures adequate
  testing for enumerated types, including those with explicit underlying types, by
  exercising the front-end's argument type checking and the back-end's code generation
  for these built-i…
primer_general: 'Compilers like GCC provide special "built-in" functions that perform
  common operations very efficiently, often by directly mapping to specific CPU instructions.
  Examples include `__builtin_clz` (count leading zeros) or `__builtin_bswapg` (byte
  swap). These functions are typically used with integer types. This change improves
  the tests for these built-in functions to ensure they behave correctly when given
  "enumerated types" as arguments. An enumerated type (or `enum`) lets you define
  a set of named integer constants (like `enum Color { Red, Green, Blue };`). Sometimes,
  enums have a specified underlying integer type (e.g., `enum class Status : int {
  OK, Error };`). The updated tests now thoroughly check that these built-in functions
  work as expected with all kinds of enums in both C and C++ programs, helping to
  guarantee reliable and correct code generation.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eaebd987e5492b23419b5c52482038a94066c640
date: '2026-06-05'
is_stub: false
---

The GCC testsuite now includes expanded tests for how built-in functions such as `__builtin_clz`, `__builtin_ctz`, and `__builtin_bswapg` handle enumerated type arguments. This enhancement specifically addresses cases involving enumerations with fixed underlying types, which were previously only partially covered in C++. The improved coverage ensures the compiler's robustness when these built-ins process enum values in both C and C++ code, preventing potential silent miscompilations.
