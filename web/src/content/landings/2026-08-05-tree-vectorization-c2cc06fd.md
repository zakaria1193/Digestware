---
project: gcc
subsystem: tree-vectorization
patch_id: null
tags:
- vectorization
- optimization
- ICE
commit_hash: c2cc06fdce766d93e45d79ba871b12158c7691d0
source_type: github
author: Richard Biener
headline: Fix vectorization of calls with SLP permute nodes.
tldr: Resolves an ICE when vectorizing calls with SLP permute nodes by improving scalar
  argument type retrieval.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_call` function in `tree-vect-stmts.cc` has been modified
  to correctly obtain the scalar argument type when handling calls involving SLP permute
  nodes. Previously, `vect_is_simple_use` would assign `error_mark_node` to the scalar
  operand if no representative was found, causing an ICE in subsequent type checks.
  The corrected code now retrieves the scalar type from the representative call statement
  itself, bypassing the problematic legacy `op` result.
primer_glossary:
- term: vectorization
  definition: A compiler optimization technique that transforms scalar code into vector
    code, allowing a single instruction to operate on multiple data elements simultaneously.
- term: SLP (Sliding Window Vectorization)
  definition: A compiler technique for vectorizing code that operates on contiguous
    data elements, even if they are not explicitly in an array. It groups independent
    instructions that operate on similar data into a vector instruction.
- term: permute node
  definition: A node in the compiler's intermediate representation that represents
    an operation rearranging elements within a vector.
- term: ICE (Internal Compiler Error)
  definition: An unexpected error encountered during the compilation process that
    halts compilation and typically indicates a bug in the compiler itself.
- term: representative call stmt
  definition: In the context of SLP vectorization, the original scalar statement from
    which a vectorized call is derived.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c2cc06fdce766d93e45d79ba871b12158c7691d0
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

A latent issue in the call vectorization pass has been fixed, preventing an internal compiler error (ICE). The problem occurred when the first argument of a call was an SLP permute node, leading `vect_is_simple_use` to assign `error_mark_node` to the scalar operand. This resulted in subsequent argument processing failing. The fix ensures the scalar argument type is correctly retrieved from the representative call statement, rather than relying on the legacy scalar operand result.
