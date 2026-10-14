---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- optimization
- x86
commit_hash: e2d1ca54a787da164e748075abfb35d5b789a8b6
source_type: github
author: Vineet Gupta
headline: 'forwprop: Only pass zero value to CLZ/CTZ if target defines it'
tldr: Compiler forward propagation pass correctly handles target-specific behavior
  for CLZ/CTZ instructions with a zero input.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_count_zeroes` function in `tree-ssa-forwprop.cc` optimizes
  bitwise count queries. Previously, it incorrectly assumed `ctx(0)` was always defined
  (e.g., 32 for CTZ) and passed this value to target intrinsics. This commit aligns
  with `fold_builtin_bit_query` by only passing the zero input when the target macro
  explicitly defines it, preventing undefined behavior when folding `COND_EXPR` involving
  such intrinsics.
primer_glossary:
- term: forwprop
  definition: Forward propagation is a compiler optimization pass that replaces uses
    of a variable with its defining expression. This can simplify subsequent analysis
    and optimizations.
- term: CLZ/CTZ
  definition: Count Leading Zeros (CLZ) and Count Trailing Zeros (CTZ) are bitwise
    operations that determine the number of zero bits from the most or least significant
    bit, respectively, up to the first set bit. Compilers often translate these into
    specific hardware instructions for performance.
- term: BMI
  definition: BMI (Bit Manipulation Instructions) is a set of x86 instructions that
    provide efficient bitwise operations, including instructions for counting leading
    and trailing zeros.
- term: undefined result
  definition: An operation whose outcome is not specified by the architecture or language
    standard. Compilers must be careful not to rely on or produce undefined results,
    as this can lead to unpredictable program behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e2d1ca54a787da164e748075abfb35d5b789a8b6
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

The forwprop pass in GCC previously generated incorrect code for count-leading-zeroes (CLZ) and count-trailing-zeroes (CTZ) instructions when the input was zero. This commit corrects the behavior by only passing the zero value to the target-specific instruction if the target explicitly defines its behavior for zero input. This prevents undefined results on targets like x86 without BMI, where CLZ/CTZ(0) is undefined, and avoids miscompilations.
