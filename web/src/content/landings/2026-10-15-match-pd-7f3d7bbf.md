---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- idiom recognition
commit_hash: 7f3d7bbf2c6a826222af622e9700193ca9afd86c
source_type: github
author: Igor Shevlyakov
headline: match.pd recognizes signbit-based copysign idiom
tldr: GCC now recognizes a common C idiom involving signbit comparisons to optimize
  into copysign.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `match.pd` pattern recognizer in GCC now includes a new pattern
  to detect and fold the idiom `(signbit(x) != 0) == (signbit(y) != 0) ? y : -y` and
  its variants into `copysign`. This addresses a gap where C code using `signbit`
  macros was not optimized as effectively as expected. The new pattern, similar to
  an existing one for PR109843, handles the raw comparison of `signbit` outputs. This
  optimization is exact for signed zeros, infinities, and NaNs.'
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7f3d7bbf2c6a826222af622e9700193ca9afd86c
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

The match.pd pattern recognizer has been updated to identify a C idiom that uses signbit comparisons to implement copysign functionality. This optimization applies to code comparing raw signbit values, which previously was not folded into a copysign intrinsic. The new pattern ensures this idiom is correctly recognized, improving code generation for certain math operations without requiring -ffast-math.
