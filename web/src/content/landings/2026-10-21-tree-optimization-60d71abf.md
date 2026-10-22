---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- tree-optimization
commit_hash: 60d71abfe4b45507027b6ad63a9ef247b4fc004b
source_type: github
author: Richard Biener
headline: Fix sign-extension bug when widening inner mask in decode_field_reference
tldr: Corrects sign extension for masked bitfields to prevent miscompilation.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `decode_field_reference` GIMPLE-fold function mishandled sign extension
  when a `BIT_AND_EXPR` mask of narrower precision was combined with a wider-precision
  mask from an outer condition. It unconditionally used `UNSIGNED` for zero-extension,
  even when the inner mask was signed and its sign bit was set. This incorrectly zeroed
  out sign-extension bits, causing the outer condition's sign-bit test to fail. The
  fix uses `TYPE_SIGN` of the mask operand to correctly extend `and_mask` to the target
  precision `prec_in`, preserving the sign bit when necessary.
primer_glossary:
- term: BIT_AND_EXPR
  definition: GCC's internal representation for a bitwise AND operation within the
    GIMPLE intermediate language.
- term: GIMPLE
  definition: GCC's main intermediate representation (IR), a three-address code form
    that simplifies many optimizations and transformations.
- term: sign-extension
  definition: The process of converting a signed number to a larger data type by duplicating
    the sign bit. This preserves the number's value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/60d71abfe4b45507027b6ad63a9ef247b4fc004b
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

A bug in `decode_field_reference` incorrectly zero-extended inner bitwise AND masks, leading to incorrect sign extension behavior when masks were widened. This patch ensures that the sign of the inner mask is correctly considered, preventing miscompilation of conditions involving sign extension. A new test case verifies the fix.
