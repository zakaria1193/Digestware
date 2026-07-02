---
project: gcc
subsystem: gcc/match.pd
patch_id: null
tags:
- optimization
- branch removal
- bit manipulation
commit_hash: f6f33ca83cb6b84cc5d157103ac70c143011b176
source_type: github
author: Daniel Barboza
headline: 'Match.pd: Make `if (c) a |= CST1 else a &= ~CST1` unconditional.'
tldr: The compiler transforms conditional bit setting/clearing into an unconditional
  form, potentially improving performance.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit adds a new pattern to `match.pd` that transforms conditional
  bit manipulation operations into unconditional ones. The transformation replaces
  a conditional bitwise OR and AND with an equivalent expression that uses bitwise
  AND, OR, and multiplication. This can improve performance by removing a conditional
  branch. The condition `type <= word_size` limits this to avoid unexpected wide integer
  arithmetic.
primer_general: Compilers optimize code by transforming it into equivalent but more
  efficient forms.  Branching (using `if` statements) can be slow. This commit transforms
  a conditional bit setting/clearing operation into an unconditional form that avoids
  the branch.  Instead of conditionally setting or clearing a bit, the new code always
  clears the bit and then sets it again based on the condition.  This can execute
  faster on some processors because it avoids the overhead of conditional execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f6f33ca83cb6b84cc5d157103ac70c143011b176
date: '2026-05-01'
---

The compiler now transforms code of the form `if (c) a |= CST1 else a &= ~CST1` into an unconditional equivalent: `(a & ~CST1) | (cond * CST1)`. This eliminates the conditional branch, which can improve performance. The transformation is only applied when the type size is less than or equal to the machine's word size to avoid wide integer multiplications.
