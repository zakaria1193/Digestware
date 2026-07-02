---
project: gcc
subsystem: fold-const.cc
patch_id: null
tags:
- optimization
- warnings
- constant folding
- overflow
commit_hash: 34c81df45aea8e13d64a02721beb46a3b97ae3d6
source_type: github
author: Daniel Barboza
headline: 'fold-const.cc: Remove fold_overflow_warning()'
tldr: The compiler no longer uses `fold_overflow_warning()` and `pointer_may_wrap_p`
  in constant folding.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Constant folding occurs in `fold-const.cc` during compilation, where
  expressions involving constants are evaluated at compile time. The `fold_overflow_warning`
  function was used to emit warnings related to potential integer overflows during
  this process. The removal of this function simplifies the constant folding logic.
  `pointer_may_wrap_p` was related to pointer arithmetic during constant folding.
primer_general: Compilers perform constant folding to evaluate constant expressions
  at compile time rather than runtime, improving program efficiency. When constant
  folding involves operations that might overflow (exceed the maximum value for a
  data type), the compiler can issue warnings. This commit removes the mechanism for
  issuing such warnings in a specific part of the constant folding process, potentially
  changing the circumstances under which overflow warnings are generated.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/34c81df45aea8e13d64a02721beb46a3b97ae3d6
date: '2026-01-17'
is_stub: false
---

The compiler removes `fold_overflow_warning()` calls within `fold-const.cc`, which avoids generating warnings for strict overflow in constant folding. The associated helper function `pointer_may_wrap_p` no longer has any call sites and is removed as well.  This change also removes some now-unnecessary test cases.
