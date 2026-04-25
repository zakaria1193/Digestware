---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- ssa
commit_hash: d84a91bbd60bfabc1cd2dac6aae10a427a770627
source_type: github
author: Richard Biener
headline: IVOPT avoids uninitialized memory in loop comparisons
tldr: GCC's IVOPT (loop optimization) pass will no longer use induction variables
  that involve undefined SSA variables.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `tree-ssa-loop-ivopts.cc` to check for uses of
  undefined SSA variables in induction variables before rewriting comparisons, by
  adding a check to the `may_eliminate_iv` function. IVOPT operates on the SSA (Static
  Single Assignment) form of the program's intermediate representation, and interacts
  with other loop optimization passes.
primer_general: Loop optimization is a crucial part of a compiler's job. One common
  technique is induction variable optimization (IVOPT), which identifies variables
  that change predictably with each loop iteration.  However, problems can arise if
  these variables depend on uninitialized memory. This patch ensures that GCC's IVOPT
  pass avoids using induction variables that rely on undefined SSA variables, preventing
  the compiler from generating code that uses uninitialized memory, which could lead
  to unpredictable program behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d84a91bbd60bfabc1cd2dac6aae10a427a770627
date: '2026-04-21'
---

The IVOPT (Induction Variable OPTimization) pass in GCC could previously rewrite comparisons using induction variables that involved undefined SSA variables, leading to the use of uninitialized memory. This commit prevents IVOPT from using candidate induction variables that involve undefs, avoiding potential crashes or unexpected behavior.
