---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-ssa
commit_hash: 85ae7d8c7c16d1ad96c2e19e17f2e2aa739bd72e
source_type: github
author: Richard Biener
headline: Split basic block SLP regions at asm goto statements
tldr: Vector SLP optimization now splits basic block regions at asm goto statements
  to handle SSA definitions correctly.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP vectorization pass, operating on the compiler's intermediate
  representation (tree-ssa), performs basic block vectorization. It optimizes sequences
  of identical scalar operations into vector instructions. This commit modifies `vect_slp_function`
  to identify control statements that involve SSA definitions, specifically after
  an `asm goto`. Such points act as delimiters, preventing vector code insertion,
  thus requiring the SLP region to be split to avoid incorrect code generation or
  ICEs.
primer_glossary:
- term: SLP vectorization
  definition: Superoptimizer-based vectorization. A compiler optimization that finds
    sequences of identical scalar operations within a basic block and replaces them
    with equivalent vector instructions. It operates on the compiler's intermediate
    representation.
- term: asm goto
  definition: An extension to the C language that allows inline assembly code to include
    computed jumps to C labels. This enables the assembly code to transfer control
    directly to C code blocks, often used for performance-critical sections or when
    interacting with external hardware.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once. This simplifies many compiler
    analyses and optimizations by making data-flow explicit.
- term: basic block
  definition: A sequence of instructions with a single entry point and a single exit
    point. Control flow can only enter at the beginning and leave at the end. Optimizations
    often operate on basic blocks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/85ae7d8c7c16d1ad96c2e19e17f2e2aa739bd72e
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

The vector super-optimization (SLP) pass now correctly splits basic block regions when encountering an asm goto statement. This is necessary because a vector definition cannot be inserted after an asm goto, and the change ensures that regions are split at such points, as previously suggested by existing comments. A new test case is included to verify this behavior.
