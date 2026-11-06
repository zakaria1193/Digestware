---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bitwise
commit_hash: 06c476d192702a07dc6a8431b7f1a54d7526d3a5
source_type: github
author: Naveen
headline: Simplify popcount of bitwise NOT by rewriting it.
tldr: Rewrites popcount(~x) to operand's precision minus popcount(x), enabling further
  optimizations.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `popcount` intrinsic in GCC's tree-SSA optimization pass is now
  enhanced to recognize and simplify patterns involving bitwise NOT (`~`). The transformation
  `popcount(~x)` is rewritten as `precision(x) - popcount(x)`. This is valuable because
  it eliminates the bitwise NOT operation, allowing subsequent passes to perform further
  constant folding or other optimizations that may not directly apply to `~x` but
  would apply to the rewritten form.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/06c476d192702a07dc6a8431b7f1a54d7526d3a5
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This change simplifies the popcount of a bitwise NOT operation by rewriting it to the operand's precision minus the popcount of the operand. This algebraic transformation removes the bitwise complement and allows for further simplifications, such as folding popcount(~x) + popcount(x) into a constant. New test cases are included to verify this optimization.
