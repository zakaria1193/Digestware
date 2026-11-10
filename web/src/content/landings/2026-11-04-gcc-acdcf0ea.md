---
project: gcc
subsystem: gcc
patch_id: null
tags:
- compiler
- validation
- internal-fn
- robustness
commit_hash: acdcf0ea95e5edaaf14391fbb532a8eeb31245b4
source_type: github
author: Kyrylo Tkachov
headline: Validate arguments for internal function calls
tldr: Adds argument validation for internal function calls to catch errors earlier.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `verify_gimple_call` function and the GIMPLE frontend's call construction
  logic previously lacked validation for internal function (IFN) arguments. This commit
  introduces `check_internal_fn_args` to enforce argument constraints, such as the
  number of arguments for direct IFNs and the type requirements for functions like
  `IFN_CLZ` and `IFN_CTZ`. This prevents later passes from encountering ICEs due to
  malformed IFNs, ensuring that argument errors are caught and reported during frontend
  or verification stages.
primer_glossary:
- term: GIMPLE
  definition: GCC's internal three-assignment representation, an intermediate language
    used for optimization.
- term: Internal Compiler Error (ICE)
  definition: An unrecoverable error within the compiler itself, often caused by unexpected
    program states or invalid input that wasn't caught earlier.
- term: Internal Function (IFN)
  definition: Functions recognized by GCC that have special handling or optimizations,
    often corresponding to intrinsic operations.
- term: .CLZ
  definition: An internal function representation for 'count leading zeros'.
- term: .POPCOUNT
  definition: An internal function representation for 'population count' (counting
    set bits).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/acdcf0ea95e5edaaf14391fbb532a8eeb31245b4
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch introduces argument validation for internal function calls in GCC. Previously, invalid arguments to internal functions, such as signed types for `.CLZ` or incorrect argument counts, would lead to Internal Compiler Errors (ICEs) in later passes. The new `check_internal_fn_args` function verifies argument types and counts, reporting errors at the call site. This improves compiler robustness by detecting and reporting errors sooner.
