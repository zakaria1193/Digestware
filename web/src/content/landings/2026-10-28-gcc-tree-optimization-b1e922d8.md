---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- vectorization
- optimization
- bugfix
commit_hash: b1e922d8fc9cc38945cb9cdb062c232ae0c57f9b
source_type: github
author: Richard Biener
headline: Fix ICE with vectorizer and dead code elimination
tldr: Removes an assertion in the vectorizer that incorrectly assumed certain masked
  calls would prevail after dead code elimination.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The vectorizer in GCC, particularly in `tree-vect-loop.cc`, had an
  assertion that `.MASK_CALL` instructions, even scalar ones, would be preserved if
  they had side effects. This commit removes that assertion because, under specific
  flags (`-fno-tree-dce -fno-tree-dse`), such calls might be eliminated even if they
  don't have side effects. This prevents an ICE by relaxing the verification logic.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A severe error that causes the compiler to
    crash during the compilation process.
- term: vectorizer
  definition: A compiler optimization component that transforms loops to operate on
    multiple data elements simultaneously using vector instructions.
- term: dead code elimination (DCE)
  definition: A compiler optimization pass that removes code that does not affect
    the program's output.
- term: .MASK_CALL
  definition: A pseudo-instruction or intrinsic used in some intermediate representations,
    often related to masked operations in SIMD or vector processing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b1e922d8fc9cc38945cb9cdb062c232ae0c57f9b
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit resolves an internal compiler error (ICE) related to the vectorizer and dead code elimination. An assertion in `vect_transform_loop` incorrectly assumed that only scalar `.MASK_CALL` instructions with side effects would remain after dead code elimination (`-fno-tree-dce`). The change removes this assertion, allowing the compiler to proceed correctly when such calls do not have side effects, and includes a new test case to cover this scenario.
