---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- documentation
- optimization
- pointer arithmetic
commit_hash: 9bb79eb94eded396a50af9460ea66c2faffe1fad
source_type: github
author: Richard Biener
headline: Discourage use of -fwrapv-pointer in documentation
tldr: Documentation for -fwrapv-pointer now advises against its use due to potential
  issues.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The documentation in `invoke.texi` for `-fwrapv-pointer` now includes
  a disclaimer that it is not recommended for general use. Similarly, `-fno-strict-overflow`
  documentation now suggests `-fwrapv` as a safer alternative. This is a documentation-only
  change to steer users toward more robust overflow handling practices.
primer_glossary:
- term: -fwrapv-pointer
  definition: A GCC compiler option that enables wrap-around behavior for pointer
    arithmetic, similar to how it handles integer arithmetic. This can lead to unexpected
    behavior and is generally discouraged.
- term: -fno-strict-overflow
  definition: A GCC compiler option that disables optimizations that assume signed
    integer overflow does not occur. It generally permits wrap-around behavior for
    signed integers.
- term: -fwrapv
  definition: A GCC compiler option that enables wrap-around behavior for signed integer
    arithmetic. This means that operations like addition or subtraction that exceed
    the representable range will wrap around to the other end of the range, rather
    than causing undefined behavior.
- term: invoke.texi
  definition: The primary documentation file for GCC command-line options and usage.
    It is processed to generate the GCC manual.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9bb79eb94eded396a50af9460ea66c2faffe1fad
date: '2026-09-22'
is_stub: true
stub_reason: low_score
---

Documentation for the `-fwrapv-pointer` compiler option now includes a disclaimer discouraging its use. The documentation for `-fno-strict-overflow` has also been updated to suggest `-fwrapv` as a preferred alternative. This change aims to guide users away from potentially problematic or less-understood options.
