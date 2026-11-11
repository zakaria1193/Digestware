---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
- bugfix
- sign extension
commit_hash: 6c4ee1b2ba2330ab71c0f9fbfe146d5119afb290
source_type: github
author: Richard Biener
headline: Fix sign test logic for masked narrowing conversions
tldr: Corrected how sign tests are handled after masked narrowing conversions to prevent
  incorrect optimization decisions.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `fold_truth_andor_for_ifcombine` pass incorrectly propagated sign
  bits when combining a truth mask with a subsequent narrowing conversion. Specifically,
  if a mask `M` was applied to a value `X` before it was narrowed (e.g., `(short)(X
  & M)`), the pass incorrectly used the sign bit of `X` based on `M`'s original width,
  even if `M`'s upper bits were discarded by the narrowing. This commit modifies `decode_field_reference`
  to truncate the mask to the target type's precision when such narrowing occurs,
  ensuring the sign bit is correctly computed based only on the relevant bits of the
  narrowed…
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where optimizations are performed on the compiler's intermediate
    representation, known as 'tree'.
- term: Sign Test
  definition: An operation that checks if a number is positive or negative, typically
    by examining its most significant bit.
- term: Narrowing Conversion
  definition: A type conversion that reduces the size or precision of a value, potentially
    losing information (e.g., converting a 32-bit integer to an 8-bit integer).
- term: Mask
  definition: A value used in bitwise operations to select or clear specific bits
    of another value.
- term: ifcombine
  definition: A GCC optimization pass that attempts to combine conditional branches
    and logical operations for more efficient code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6c4ee1b2ba2330ab71c0f9fbfe146d5119afb290
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

An optimization bug caused incorrect sign tests for values that were masked and then narrowed. The compiler mistakenly considered bits beyond the narrowed type's width when determining the sign bit, leading to faulty simplifications. The fix now correctly truncates the mask to the precision of the narrow type, ensuring sign tests accurately reflect the narrowed value and allowing more correct optimizations.
