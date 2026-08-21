---
project: gcc
subsystem: gcc/auto-profile
patch_id: null
tags:
- optimization
- AutoFDO
- LTO
- profile-guided
- compiler-error
commit_hash: ab0712667b0461e34679cade62369a2c92fbc9be
source_type: github
author: Kugan Vivekanandarajah
headline: 'AutoFDO: Prevent entry block count from becoming zero after profile adjustment'
tldr: Fixes AutoFDO profile adjustment to prevent the entry block count from being
  zeroed, avoiding LTO ICEs.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `afdo_adjust_guessed_profile` function in GCC's AutoFDO tooling
  is responsible for reconciling profile data from different sources. When `scale_bbs`
  is invoked, it can scale the entry basic block's count to zero, which conflicts
  with AFDO counts in inner basic blocks. This led to an ICE in `profile-count.h:1192`
  during `ipa_merge_profiles` at LTO time. The fix ensures the entry block count is
  set to a fraction of the scaled sample, maintaining a non-zero value that aligns
  better with subsequent profile merging and verification steps.
primer_glossary:
- term: AutoFDO
  definition: Automatic Feedback-Directed Optimization, a technique that uses runtime
    profile data to guide compiler optimizations.
- term: LTO
  definition: Link-Time Optimization, a compilation strategy where optimization is
    performed at link time, allowing analysis across multiple translation units.
- term: IPA
  definition: Inter-procedural Analysis, a compiler optimization technique that analyzes
    code across function boundaries.
- term: basic block
  definition: A contiguous sequence of code within a function in which control enters
    only at the beginning and leaves only at the end.
- term: entry block
  definition: The first basic block in a function, representing the point where execution
    begins.
- term: profile annotation
  definition: The process of adding or adjusting profile count information to basic
    blocks and code paths.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab0712667b0461e34679cade62369a2c92fbc9be
date: '2026-08-21'
is_stub: false
stub_reason: ''
---

When adjusting profiles for AutoFDO, the entry block's count could incorrectly be scaled to zero while other basic blocks retained non-zero counts. This discrepancy, particularly during LTO's IPA passes, led to an internal compiler error (`in apply_scale`). This commit modifies `afdo_adjust_guessed_profile` to set the entry block count to half of the scaled sample count instead of zero, resolving the issue.
