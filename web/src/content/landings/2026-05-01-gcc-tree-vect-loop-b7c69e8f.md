---
project: gcc
subsystem: gcc/tree-vect-loop
patch_id: null
tags:
- loop vectorization
- code cleanup
- optimization
commit_hash: b7c69e8f540ccd41b0368cd5fe650b4aef3758eb
source_type: github
author: Jakub Jelinek
headline: Remove redundant condition in tree-vect-loop.cc
tldr: This removes a pointless `&& 1` condition in the `vectorizable_reduction` function,
  cleaning up the code.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_reduction` function in `tree-vect-loop.cc` is part
  of the loop vectorization pass.  The commit removes a `&& 1` which was introduced
  by r16-476. The condition did not change the behavior of the code, so removing it
  only improves readability.
primer_general: Loop vectorization is a compiler optimization that transforms loops
  to process multiple data elements simultaneously, using vector instructions.  This
  can significantly improve performance.  This change removes an unnecessary condition
  in the loop vectorization code, making it cleaner but without changing its behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b7c69e8f540ccd41b0368cd5fe650b4aef3758eb
date: '2026-05-01'
---

A previous change replaced a condition with `&& 1` in the `vectorizable_reduction` function, which served no purpose.  This commit removes the redundant `&& 1`, simplifying the code and improving readability.  This has no functional impact.
