---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- bitwise
- tree-ssa
commit_hash: b3ade4e315e5bab56eced1e22eceabbf1a8f15c4
source_type: github
author: Kael Andrew Alonzo Franco
headline: Optimize bitwise operations for signed integers to -1
tldr: GCC now simplifies `(~a) >> a` to `-1` for signed integer `a`, reducing unnecessary
  computations during compilation.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file defines tree-level optimizations in GCC. This specific
  optimization rewrites `(~a) >> a` to `-1` for signed `a`. This relies on the property
  that `~a` (all bits flipped) then right-shifted by `a` (which effectively sign-extends)
  will result in an all-ones bit pattern, which is `-1` in two's complement. This
  fold simplifies the intermediate representation, allowing for more streamlined code
  generation by reducing complex bitwise operations to a constant.
primer_general: Compilers often look for mathematical shortcuts to make your programs
  run faster. This change in GCC (within the `match.pd` file) introduces one such
  shortcut for signed integers. If your code calculates `(~a) >> a` – which means
  'bitwise NOT 'a', then right-shift by 'a'' – the compiler now recognizes that for
  signed numbers, this sequence always results in the value `-1`. By knowing this,
  the compiler can directly insert `-1` instead of performing the actual bitwise operations,
  leading to slightly faster and more compact code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3ade4e315e5bab56eced1e22eceabbf1a8f15c4
date: '2026-06-12'
is_stub: false
---

This commit introduces an optimization in `match.pd` where the expression `(~a) >> a` simplifies to `-1` when `a` is a signed integer. This transformation is based on the mathematical equivalence `~(a>>a)` for right shifts of complement operations. By recognizing this pattern and directly substituting `-1`, the compiler eliminates redundant bitwise operations, resulting in more efficient code generation.
