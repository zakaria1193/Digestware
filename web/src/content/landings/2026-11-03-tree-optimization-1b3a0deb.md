---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- SIMD
- vectorization
- AVX512
commit_hash: 1b3a0deba8302912cfbc5faf850a6abcdb3e984a
source_type: github
author: Richard Biener
headline: Fix loop mask for multi-part SIMD clone calls.
tldr: Correctly applies loop masks to all parts of multi-argument SIMD clone calls
  to prevent out-of-bounds lane execution.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR tree-optimization/127924 exposes a bug in `vectorizable_simd_clone_call`
  when handling fully-masked loops that require multiple mask arguments per inbranch
  SIMD clone call. The issue stems from using the `J` (copy index) instead of `M`
  (mask part index) to fetch the loop mask, resulting in all mask parts being ANDed
  with the first loop mask. This patch corrects the loop mask index to `M` to ensure
  correct lane masking.
primer_glossary:
- term: SIMD
  definition: Single Instruction, Multiple Data. A type of parallel processing where
    a single instruction operates on multiple data points simultaneously. Often used
    for accelerating graphics, scientific simulations, and multimedia processing.
- term: SIMD clone
  definition: A function or code path that is specifically designed to be vectorized,
    often by being called within a loop that is also being vectorized. 'Clone' here
    refers to a specialized version adapted for SIMD execution.
- term: inbranch
  definition: Refers to a function call that is inlined or otherwise integrated directly
    within the execution path of its caller, often to facilitate optimizations like
    loop unrolling or vectorization.
- term: AVX512
  definition: An extension to the x86 instruction set architecture that provides 512-bit
    wide SIMD registers and instructions, allowing for more data parallelism.
- term: loop mask
  definition: A mask used in vectorized loops to control which elements are processed
    in each iteration. It ensures that only valid data within the current iteration
    bounds is operated upon, especially important for handling loop tails or partial
    vector operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1b3a0deba8302912cfbc5faf850a6abcdb3e984a
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This commit resolves an issue in `vectorizable_simd_clone_call` where multi-part SIMD clone calls with multiple mask arguments were incorrectly using the same loop mask for all parts. This led to lanes beyond the intended iteration count being enabled in later mask parts, causing the clone to be called on inactive lanes. The fix ensures that the correct mask part index is used when fetching the loop mask for explicit mask arguments.
