---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- aarch64
- performance
commit_hash: 81a34bdbcb3e27a8fb2438fd90bbb76ec506fb40
source_type: github
author: Kyrylo Tkachov
headline: Do not widen multiply-add across shared conversion
tldr: Fixes a bug where a multiply-add was incorrectly widened, leading to performance
  regressions.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `convert_plusminus_to_widen` pass in `tree-ssa-math-opts.cc` attempts
  to fold a multiplication and an addition into a `WIDEN_MULT_PLUS_EXPR`. It requires
  the multiply's result to be single-use. When a conversion is inserted between the
  multiply and the addition, the pass incorrectly checked the single-use of the multiply's
  result rather than the conversion's result, leading to the multiply being duplicated.
  This commit corrects the check to apply to the conversion's result, fixing the pass's
  invariant.
primer_glossary:
- term: WIDEN_MULT_PLUS_EXPR
  definition: A GCC internal representation node for a multiply-add operation that
    widens the operands or result. It's used to optimize patterns like `(a * b) +
    c`.
- term: Single-use
  definition: In compiler optimization, a value or expression is single-use if it
    is read by only one subsequent operation. This property is often a prerequisite
    for certain transformations.
- term: AArch64
  definition: The 64-bit ARM architecture, commonly used in mobile devices and servers.
    GCC supports code generation for this architecture.
- term: SMADDL
  definition: A specific AArch64 assembly instruction for a fused signed multiply-add
    operation with a 32-bit accumulator and 64-bit result.
- term: SBFIZ
  definition: A specific AArch64 assembly instruction for a signed field insert with
    zeroing.
- term: LDP
  definition: A specific AArch64 assembly instruction for loading two registers from
    memory with a single address, often used for performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/81a34bdbcb3e27a8fb2438fd90bbb76ec506fb40
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

The `convert_plusminus_to_widen` optimization pass incorrectly widened multiply-add operations when a conversion was involved. This pass requires the multiply operation to be single-use, but the conversion meant the multiply's result was shared, causing the pass to apply the widening to the wrong value. This change ensures the single-use requirement applies to the conversion's result, preventing the generation of redundant multiply operations. This optimization was found in a sparse affine kernel and resulted in a 4.7% instruction count reduction on AArch64.
