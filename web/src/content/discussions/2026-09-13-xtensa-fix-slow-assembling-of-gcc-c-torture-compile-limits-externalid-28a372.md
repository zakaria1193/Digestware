---
project: binutils
subsystem: xtensa
patch_id: null
tags:
- xtensa
- performance
- gas
- optimization
discussion_id: 20260913022512.3431965-1-jcmvbkbc@gmail.com
source_type: public_inbox
title: '[COMMITTED] xtensa: fix slow assembling of gcc.c-torture/compile/limits-externalid'
headline: 'xtensa: fix slow assembling of gcc.c-torture/compile/limits-externalid'
tldr: Optimize Xtensa assembler by returning fragment range from branch target checks.
proposer: Max Filippov <jcmvbkbc@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Improves assembly time significantly for specific cases by optimizing fragment iteration.
exchanges: []
primer_expert: The Xtensa assembler's `xtensa_fix_target_frags` function previously
  called `next_frag_is_branch_target` repeatedly. This function, which iterates through
  fragments to find branch targets or fixed frags, could lead to O(N^2) complexity.
  This patch optimizes it by having `next_frag_is_branch_target` return the `valid_until`
  fragment and by tracking the branch target status within `xtensa_fix_target_frags`
  for a range, thus calling the check function only once per relevant range.
primer_glossary:
- term: fragment (frag)
  definition: A unit of code or data within the assembler's intermediate representation,
    typically corresponding to a machine instruction or data element.
- term: branch target
  definition: A location in code that a branch instruction can jump to.
- term: torture test
  definition: A test case designed to exercise a specific, often complex or edge-case,
    functionality of a compiler or assembler.
- term: RELAX_DESIRE_ALIG
  definition: A specific fragment subtype used in the Xtensa assembler, likely related
    to alignment requirements.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913022512.3431965-1-jcmvbkbc@gmail.com
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This commit optimizes the Xtensa assembler's fragment processing by modifying `next_frag_is_branch_target` to return the end of the checked fragment range. This prevents redundant checks within loops, reducing the assembly time for specific torture tests from minutes to seconds. The change significantly improves performance for certain complex code generation scenarios.
