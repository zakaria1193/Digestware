---
project: gcc
subsystem: compare-elim
patch_id: null
tags:
- optimization
- arm
commit_hash: f909c6cebba8005a6042bec3e96781e13c19ab85
source_type: github
author: Dominic P
headline: Compare elimination pass no longer limits flag uses
tldr: The compare-elim pass in GCC now tracks all flag uses, improving code generation
  for conditional operations on ARM.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The compare-elim pass in GCC optimizes conditional code by eliminating
  redundant comparisons. It tracks the uses of flags set by comparison instructions
  to decide if a comparison can be removed. The `MAX_CMP_USE` limit was an arbitrary
  cutoff that caused incorrect handling of common instruction sequences, such as an
  `and; cmp #0` followed by multiple conditional selects. This commit removes the
  limit and uses `auto_vec` to efficiently store uses, improving code generation for
  patterns previously mishandled.'
primer_glossary:
- term: compare-elim
  definition: A GCC compiler optimization pass that removes redundant conditional
    comparison instructions by analyzing how comparison flags are used.
- term: flag uses
  definition: In compiler optimization, refers to how the status flags (like zero,
    carry, overflow) set by an instruction (e.g., a comparison) are subsequently used
    by other instructions (e.g., conditional branches or moves).
- term: conditional select
  definition: An instruction that chooses between two source operands based on the
    state of condition flags, effectively performing a conditional assignment without
    a branch.
- term: auto_vec
  definition: A GCC internal data structure that provides a dynamically sized vector,
    similar to C++'s std::vector, used here to store instruction uses without requiring
    heap allocation for common cases.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f909c6cebba8005a6042bec3e96781e13c19ab85
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

The compare-elim pass in GCC has been enhanced to remove the artificial limit on tracking flag uses. Previously, after three uses, the pass would incorrectly assume uses were unknown, leading to suboptimal code generation for conditional moves and select instructions on architectures like ARM and AArch64. By tracking all uses, this change enables better elimination of compares, resulting in smaller code size.
