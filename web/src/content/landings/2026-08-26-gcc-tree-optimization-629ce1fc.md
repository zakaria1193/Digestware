---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- refactor
commit_hash: 629ce1fc63967f5b8944e32854f359833b76646f
source_type: github
author: Richard Biener
headline: Simplify vector reduction transformation function
tldr: Redundant variable removed and vector input count clarified in vectorization
  pass.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-vect-loop.cc`, `vect_transform_reduction` prepares for vectorizing
  reduction loops. This change removes `effec_reduc_ncopies` as it's a duplicate of
  `effec_ncopies`. The calculation and naming of `vec_num` are clarified to `vec_in_num`,
  directly reflecting the number of input vectors used in the transformation. This
  cleanup is part of the ongoing effort to resolve PR126998, which likely involves
  more complex reduction patterns.
primer_glossary:
- term: vectorization
  definition: An optimization technique where the compiler transforms code to operate
    on multiple data elements simultaneously using SIMD (Single Instruction, Multiple
    Data) instructions. This can significantly speed up array processing and other
    data-parallel tasks.
- term: reduction operation
  definition: An operation that combines elements of a sequence into a single value,
    such as sum, product, minimum, or maximum. In vectorization, these operations
    are often optimized using specialized vector instructions.
- term: PR
  definition: Problem Report. GCC uses a public bug tracking system where users report
    issues and developers track fixes. 'PR tree-optimization/126998' refers to a specific
    bug report in the tree-optimization component.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/629ce1fc63967f5b8944e32854f359833b76646f
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

This commit simplifies the `vect_transform_reduction` function within GCC's vectorization pass as a preparation for addressing PR126998. It removes the redundant `effec_reduc_ncopies` variable, which was always equal to `effec_ncopies`, and renames `vec_num` to `vec_in_num` after computing it based on actual vector inputs for better clarity.
