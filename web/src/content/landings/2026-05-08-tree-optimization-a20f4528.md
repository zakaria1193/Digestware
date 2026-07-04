---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
- intrinsics
commit_hash: a20f4528f3ab84afc2568ea1e208f33fe59bec66
source_type: github
author: Philipp Tomsich
headline: tree-optimization/122569 - recognize CLZ via isolated MSB DeBruijn lookup
tldr: Compiler now recognizes a CLZ idiom using an isolated MSB and DeBruijn lookup
  for potential performance gains.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `simplify_count_zeroes` pass now recognizes a CLZ idiom. This idiom
  uses an OR-cascade to set bits up to the MSB, followed by a transformation `(value
  - (value >> 1))` to isolate the MSB as a power of two. A DeBruijn lookup then maps
  this power of two to the bit index. The new `clz_msb_iso_table_index` pattern is
  added to `match.pd`, and the existing `simplify_count_zeroes` function is updated
  to use it. The element type check for tables is relaxed to `integral and precision
  <= 64` to support 64-bit types.
primer_glossary:
- term: CLZ
  definition: Count Leading Zeros. An intrinsic operation that returns the number
    of zero bits preceding the most significant set bit in an integer.
- term: MSB
  definition: Most Significant Bit. The bit with the highest value in a binary number.
- term: DeBruijn lookup
  definition: A technique using a magic number and bit shifts to efficiently find
    the position of the most significant bit (for CLZ) or least significant bit (for
    CTZ) in an integer. It's often used in bit manipulation optimizations.
- term: tree-optimization
  definition: A phase in the GCC compiler pipeline that performs optimizations on
    the compiler's intermediate representation (GIMPLE).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a20f4528f3ab84afc2568ea1e208f33fe59bec66
date: '2026-05-08'
is_stub: false
stub_reason: ''
---

GCC can now recognize a count-leading-zeros (CLZ) optimization pattern. This pattern appears after an OR-cascade and uses a value transformation to isolate the most significant bit (MSB) as a power of two, which is then mapped to the bit position using a DeBruijn lookup. The frontend is updated to support this optimization, potentially improving performance for operations involving CLZ where this specific idiom is present.
