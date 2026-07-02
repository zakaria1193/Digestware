---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- optimization
- rtl
- vectorization
- x86
commit_hash: 1bf9bb5f1c5bdaf8f96c64fbf2a081aaaa2b9b2f
source_type: github
author: Roger Sayle
headline: 'simplify-rtx: Optimize nested vec_merge operations on x86'
tldr: Simplifies sequences of vec_merge operations involving repeated operands into
  a single instruction.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `simplify-rtx` pass now canonicalizes the pattern `(vec_merge (vec_merge
  a b m) (vec_duplicate a) n)` to `(vec_merge a b (m|n))`. This addresses a case within
  the combine pass where multiple `vec_merge` operations, each inserting elements
  from a duplicated source `a` into different vector masks, were not being recognized
  as mergeable into a single instruction. The simplification relies on the property
  that the order of operands in `vec_merge` can be swapped by inverting the mask,
  and that elements from `a` can be merged in one go if the masks are combined. This
  benefits vector code genera…
primer_glossary:
- term: simplify-rtx
  definition: A GCC internal pass that simplifies Register Transfer Language (RTL)
    expressions to make further optimizations easier and to canonicalize code patterns.
- term: vec_merge
  definition: An RTL operation that constructs a new vector by selecting elements
    from two source vectors based on a mask. The mask specifies which elements come
    from the first operand and which come from the second.
- term: vec_duplicate
  definition: An RTL operation that creates a vector where all elements are copies
    of a single scalar value.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used within
    GCC to describe operations before they are converted into machine code.
- term: AVX2
  definition: Advanced Vector Extensions 2, a set of SIMD instructions for x86 processors
    that extend AVX capabilities, enabling wider vector operations (256-bit).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1bf9bb5f1c5bdaf8f96c64fbf2a081aaaa2b9b2f
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This commit introduces a new optimization in `simplify-rtx.cc` that simplifies specific sequences of `vec_merge` operations. The optimization targets cases where a `vec_merge` is applied to the result of another `vec_merge` that uses a duplicated operand. For example, `(vec_merge (vec_merge a b m) a n)` can now be simplified to `(vec_merge a b (m|~n))`. This allows GCC to generate more efficient code, particularly for vector types on x86, by collapsing multiple vector manipulation instructions into a single, more powerful one.
