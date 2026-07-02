---
project: gcc
subsystem: gcc/phiopt
patch_id: null
tags:
- optimization
- gimple
- phiopt
commit_hash: c43fed44d9ac34ce88b261cbc0da65e5d3db7132
source_type: github
author: Andrew Pinski
headline: Phiopt now factors out more than single-operand operations
tldr: The phiopt pass in GCC has been enhanced to factor out operations with more
  than two operands, improving code optimization.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `phiopt` pass operates on GIMPLE trees, specifically focusing on
  optimizing code that arises from `if` statements or conditional expressions by transforming
  them into equivalent, more efficient forms. This change in `factor_out_conditional_operation`
  extends its capabilities beyond unary and binary operations, drawing inspiration
  from `ifcvt`'s `factor_out_operators`. The optimization aims to hoist common subexpressions
  out of conditional branches, reducing redundant computations. The exclusions for
  `POINTER_PLUS` with constant operand 1, division/modulo by constant 1 (unless equal),
  and…
primer_general: Compilers try to make your code run as fast as possible, and one way
  they do this is through 'optimization passes'. `phiopt` is one such pass in the
  GCC compiler that focuses on cleaning up code generated from `if` statements or
  other conditional logic. Imagine you have a calculation that happens in both the
  'true' and 'false' branches of an `if` statement. `phiopt` tries to 'factor out'
  this common calculation so it only happens once before the `if` statement, saving
  computation time. Previously, it was limited to very simple operations. This update
  makes `phiopt` much smarter, allowing it to move more complex calculations out of
  conditional blocks. However, the compiler is careful not to factor out operations
  that might actually make the code slower or introduce bugs, like issues with pointer
  math or losing warnings about uninitialized variables.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c43fed44d9ac34ce88b261cbc0da65e5d3db7132
date: '2026-06-04'
is_stub: false
---

The `phiopt` pass in GCC, responsible for optimizing conditional code, now supports factoring out operations that involve more than just a single operand. This expansion builds upon existing `ifcvt` functionality and allows for broader optimization opportunities. Specific cases, such as certain pointer arithmetic and complex expressions, are strategically excluded to avoid profitability issues or correctness problems like lost uninitialization warnings.
