---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- ivopt
- ssa
- uninitialized
commit_hash: d84a91bbd60bfabc1cd2dac6aae10a427a770627
source_type: github
author: Richard Biener
headline: IVOPT Avoids Using Undefined SSA Variables.
tldr: The IVOPT pass now prevents rewriting comparisons when the involved induction
  variables have undefined SSA variables.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses an issue in the IVOPT pass (``tree-ssa-loop-ivopts.cc``)
  where a compare was rewritten using an IV that involved undefined SSA vars. The
  ``may_eliminate_iv`` function is updated to avoid using candidate IVs that involve
  undefs, preventing the emission of uninitialized uses during loop optimization.
primer_general: The "middle-end" of GCC performs many transformations on a program's
  intermediate representation, with the goal of making the code more efficient.  One
  such transformation is induction variable optimization, which rewrites loop counters
  to make them easier to optimize.  This commit fixes a bug where the optimization
  could introduce uninitialized variables, by ensuring that only valid loop counters
  are used.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d84a91bbd60bfabc1cd2dac6aae10a427a770627
date: '2026-04-21'
---

The IVOPT (Induction Variable OPTimization) pass was rewriting comparisons using induction variables that involved undefined SSA variables, leading to uninitialized use. This commit prevents IVOPT from performing such rewrites, ensuring that only induction variables with defined SSA vars are used in comparisons. This fix avoids potential undefined behavior and improves the reliability of the generated code during loop optimizations.
