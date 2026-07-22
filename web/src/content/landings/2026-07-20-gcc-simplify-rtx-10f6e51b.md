---
project: gcc
subsystem: gcc/simplify-rtx
patch_id: null
tags:
- gcc
- optimization
- x86
- vector
- simplify
commit_hash: 10f6e51b8250ce4f553c055ad737607332311a5d
source_type: github
author: Richard Biener
headline: Simplify scalar vec_select of vec_concat patterns
tldr: GCC's RTX simplification pass now handles scalar `vec_select` operations applied
  to `vec_concat`, enabling further optimization opportunities.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `simplify_context::simplify_binary_operation_1` function in `simplify-rtx.cc`
  now includes logic to simplify expressions of the form `(vec_select:scalar (vec_concat
  ...))`. This addresses a specific RTX pattern where a scalar extraction from a concatenated
  vector was not being reduced. The simplification aims to expose opportunities for
  instruction combining, as demonstrated by the example pattern which, after simplification,
  could potentially be recognized by x86 instruction selection (though a related PR,
  126328, notes issues with consting that prevent full combination in that specific…
primer_glossary:
- term: RTX
  definition: Representation of Tree-EXpression. This is GCC's internal intermediate
    representation (IR) used for representing code during optimization and before
    final code generation. It's a Lisp-like structure.
- term: Vector extension (SIMD)
  definition: Instructions that perform the same operation on multiple data elements
    simultaneously. Examples include SSE, AVX on x86, and NEON on ARM.
- term: '`vec_select`'
  definition: An RTX operation representing the selection of elements from a vector.
    In this context, `vec_select:scalar` implies selecting a single element or a scalar
    part from a vector.
- term: '`vec_concat`'
  definition: An RTX operation representing the concatenation of two or more vectors
    to form a larger vector. This is often used to combine smaller vector chunks into
    a larger one.
- term: simplify-rtx
  definition: A GCC optimization pass that performs local simplifications on the RTX
    intermediate representation. It aims to reduce complexity and expose opportunities
    for further optimization.
- term: combine pass
  definition: A GCC optimization pass that attempts to combine sequences of instructions
    into more efficient patterns. This is a crucial pass for performance on many architectures.
- term: x86
  definition: A family of instruction set architectures originating from the Intel
    8086 microprocessor, widely used in desktops and servers. This commit relates
    to optimizations for x86 processors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/10f6e51b8250ce4f553c055ad737607332311a5d
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's `simplify-rtx` pass by introducing simplification for scalar `vec_select` operations that wrap `vec_concat`. Previously, such patterns might not have been simplified effectively, hindering subsequent optimizations. The new simplification allows these complex vector concatenations and selections to be resolved into simpler forms that the backend, particularly x86, can better recognize and optimize, potentially leading to improved performance.
