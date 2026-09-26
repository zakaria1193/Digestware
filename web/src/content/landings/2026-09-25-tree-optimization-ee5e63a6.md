---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
commit_hash: ee5e63a6531defa646b995592f577c05ed288d63
source_type: github
author: Richard Biener
headline: Fix bogus INTEGER_INDUC_COND_REDUCTION detection
tldr: Correctly handle integer conditional reductions after adding new induction kinds.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit fixes a bug in the vectorization pass where the introduction
  of additional induction kinds interfered with the correct detection of INTEGER_INDUC_COND_REDUCTION.
  The fix explicitly initializes loop evolution types and causes the pass to bail
  out for alternate induction types, preventing misidentification of valid reductions.
  This ensures loop vectorization remains correct for code involving conditional reductions.
primer_glossary:
- term: INTEGER_INDUC_COND_REDUCTION
  definition: A compiler optimization that identifies and optimizes conditional arithmetic
    reductions within loops, where the reduction operation's operands depend on the
    loop counter.
- term: induction kinds
  definition: Refers to different ways loop induction variables (variables that are
    incremented or decremented in a loop) can be represented or evolved. New types
    of induction can increase optimization opportunities but also introduce complexity.
- term: vectorization
  definition: An optimization technique where the compiler transforms a loop to operate
    on multiple data elements simultaneously using SIMD (Single Instruction, Multiple
    Data) instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ee5e63a6531defa646b995592f577c05ed288d63
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

The compiler incorrectly identified integer conditional reductions after new induction kinds were introduced. This change ensures that these reductions are unaffected by the new induction types. A new test case is added to verify the fix.
