---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
commit_hash: fba8ef7b727a9d3769accf7eb226af4577b738cb
source_type: github
author: Richard Biener
headline: Avoid moving abnormal defs when rewriting complex loads
tldr: Fixes a bug where abnormal definitions were moved incorrectly during complex
  load rewrites.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/128236 by refining the `pass_forwprop::execute`
  function in `tree-ssa-forwprop.cc`. It specifically avoids moving abnormal definitions
  during the rewriting of complex loads to component loads, a scenario that could
  arise in the SSA form. The fix ensures that the intermediate representation remains
  valid and that subsequent optimizations or code generation are not affected by incorrect
  def movements.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fba8ef7b727a9d3769accf7eb226af4577b738cb
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This change prevents the `forwprop` pass from moving abnormal definitions when rewriting complex loads into component loads. This corrects an issue where such movements could lead to incorrect program behavior. A new test case is included to verify the fix.
