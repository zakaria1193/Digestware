---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler bug
- integer overflow
- printf
commit_hash: 311e3ba953862ea9279b5af443ce6448834505a4
source_type: github
author: Kyrylo Tkachov
headline: 'gimple-ssa-sprintf: Fix %lc argument range check for ASCII'
tldr: Ensures %lc format specifier correctly handles ASCII character ranges in snprintf
  optimizations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple-ssa-sprintf.cc` pass performs optimizations based on `snprintf`
  behavior. The `format_character` function's logic for handling `%lc` arguments,
  particularly when determining if a range is purely ASCII, was flawed. It checked
  the minimum value but not the maximum, leading to incorrect assumptions about `mayfail`
  when the upper bound exceeded 127. This patch modifies `get_int_range` usage to
  enforce the `[0, 127]` range for ASCII, ensuring that the `printf` return value
  optimization correctly folds comparisons only when truly safe.
primer_glossary:
- term: gimple-ssa-sprintf
  definition: A GCC optimization pass that analyzes and optimizes code involving the
    sprintf family of functions using the SSA (Static Single Assignment) form of GIMPLE
    (GCC's internal representation).
- term: '%lc'
  definition: A format specifier for `printf`-like functions that expects a wide character
    (typically `wint_t`) as an argument.
- term: snprintf
  definition: A C standard library function that formats data into a string, similar
    to sprintf, but with a buffer size limit to prevent buffer overflows. It returns
    the number of characters that *would have been* written, including the null terminator.
- term: SSA
  definition: Static Single Assignment. An intermediate representation property where
    each variable is assigned a value exactly once. This simplifies many optimization
    analyses.
- term: GIMPLE
  definition: GCC's internal three-address code representation used for optimization
    passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/311e3ba953862ea9279b5af443ce6448834505a4
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit corrects an optimization in `gimple-ssa-sprintf` that incorrectly assumed `%lc` format specifiers always succeed for ASCII characters, even when the input range included values beyond the ASCII set. The optimization, which folds comparisons of `snprintf` results, failed for ranges like `[0, 200]` where characters above 127 can cause `snprintf` to return an error. The fix tightens the range check to `[0, 127]`, ensuring the optimization correctly accounts for potential failures and prevents incorrect code transformations.
