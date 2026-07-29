---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- middle-end
- optimization
- aarch64
- simd
commit_hash: 9acbae69609a41df0f20db6222842414a85067ea
source_type: github
author: Kyrylo Tkachov
headline: 'middle-end: Look through VEC_DUPLICATE_EXPR in ssa_uniform_vector_p'
tldr: Improves `ssa_uniform_vector_p` to correctly handle `VEC_DUPLICATE_EXPR` in
  GIMPLE form.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Enhances `tree.cc`''s `ssa_uniform_vector_p` to correctly resolve
  `VEC_DUPLICATE_EXPR` when it appears as the RHS of a GIMPLE assignment. The prior
  implementation only handled bare tree nodes, and since `VEC_DUPLICATE_EXPR` is a
  unary operation, `gimple_assign_single_p` returned false, causing the SSA name path
  to fall through to `NULL_TREE`. This change is necessary because recent intrinsics
  porting (`aarch64: Port NEON vector creation intrinsics to pragma-based framework`)
  causes `vdup_n_u8` and similar to generate GIMPLE `VEC_DUPLICATE_EXPR` instead of
  `CONSTRUCTOR`, breaking subsequent opt…'
primer_glossary:
- term: ssa_uniform_vector_p
  definition: A GCC internal function that checks if a tree represents a uniform vector
    (i.e., all elements are the same) and returns the duplicated element.
- term: VEC_DUPLICATE_EXPR
  definition: A GCC internal representation for creating a vector where all elements
    are initialized to the same value.
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation used after
    initial parsing and before RTL generation.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation where
    every variable is assigned a value exactly once.
- term: NEON
  definition: An Advanced SIMD (Single Instruction, Multiple Data) instruction set
    extension for ARM processors, used for accelerating media and signal processing.
- term: tree
  definition: GCC's intermediate representation that uses nodes with a generic structure
    to represent code constructs.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used within
    GCC to describe programs before they are lowered to machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9acbae69609a41df0f20db6222842414a85067ea
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

The `ssa_uniform_vector_p` function, which identifies the element a uniform vector is a splat from, has been updated to correctly handle `VEC_DUPLICATE_EXPR` in its GIMPLE form. Previously, it only handled the bare tree form. This oversight caused callers, such as the lowpart-to-highpart NEON builtin fold on aarch64, to miss optimizations. The change ensures that splatted vectors created using `VEC_DUPLICATE_EXPR` in GIMPLE assignments are recognized, restoring expected code generation and optimization for vector operations.
