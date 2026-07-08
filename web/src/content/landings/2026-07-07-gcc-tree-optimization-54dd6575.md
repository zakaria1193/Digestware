---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
- memset
commit_hash: 54dd6575fa5ba7554396039820bee88d4dddab6d
source_type: github
author: Naveen
headline: Improve CDCE memset optimization for {0, N} ranges
tldr: GCC's CDCE optimization now better handles memset calls with {0, N} length ranges.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Extends the `tree-call-cdce.cc` pass to handle `memset` calls with
  an exact two-value length range `{0, N}`, beyond the existing `[0, 1]` range support.
  This involves refining `get_len_nonzero_value` and `can_shrink_wrap_len_p` to correctly
  identify and utilize the non-zero length, pinning the argument in `shrink_wrap_len_call`
  and handling it in `shrink_wrap_conditional_dead_built_in_calls`. The goal is to
  aggressively optimize `memset` calls with known, limited length variations.
primer_glossary:
- term: CDCE
  definition: Conditional Dead Code Elimination is a compiler optimization pass that
    removes code that can never be executed or whose results are never used, under
    certain conditions.
- term: memset
  definition: A C standard library function that fills a block of memory with a particular
    byte value. The compiler can sometimes optimize calls to `memset` if it can determine
    the size and value at compile time.
- term: tree-optimization
  definition: Refers to optimizations performed on GCC's intermediate representation,
    known as the 'tree' or GENERIC/GIMPLE representation. This is typically after
    the parsing and initial front-end processing but before the final code generation.
- term: PR102202
  definition: A 'Problem Report' identifier, indicating a bug or feature request previously
    submitted to the GCC project. This commit addresses an issue raised under this
    ID.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/54dd6575fa5ba7554396039820bee88d4dddab6d
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This patch enhances the CDCE (Conditional Dead Code Elimination) optimization to better support `memset` calls where the length is known to be exactly 0 or another constant N. Previously, this optimization only handled lengths in ranges [0, 1]. The update allows the pass to specialize the `memset` call to a constant length N, improving code generation for these specific cases. New test cases are added to verify the fix.
