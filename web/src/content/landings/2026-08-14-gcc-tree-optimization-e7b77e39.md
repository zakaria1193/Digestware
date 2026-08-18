---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- constant folding
- builtin
commit_hash: e7b77e39552d82141f71f039f70885754de72093
source_type: github
author: Daniel Barboza
headline: Enable constant folding for `strnlen` calls with constant length.
tldr: Compiler now folds `__builtin_strnlen` into constants when the length argument
  is known, improving optimization.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Enhances `fold_const_call.cc` to handle `CFN_BUILTIN_STRNLEN`. Previously,
  only `CFN_BUILTIN_STRLEN` was folded. This allows optimization of calls like `__builtin_strnlen(s,
  N)` where `N` is a constant. The PR example shows how this enables folding a `strnlen`
  with a PHI node argument into a constant range, avoiding runtime calls. Test cases
  were updated to reflect changes in warnings/behavior.
primer_glossary:
- term: Constant folding
  definition: An optimization technique where expressions with constant operands are
    evaluated at compile time rather than at runtime. This reduces the amount of computation
    needed when the program executes.
- term: strnlen
  definition: A C standard library function that calculates the length of a string,
    but stops after a specified maximum number of characters. It is safer than `strlen`
    as it prevents buffer overflows.
- term: PHI node
  definition: In Static Single Assignment (SSA) form, a PHI node is an instruction
    that merges values from different control flow paths. It represents a variable
    that has different values depending on which path of execution was taken to reach
    that point.
- term: tree-optimization
  definition: A phase in the GCC compiler that operates on the compiler's intermediate
    representation (IR) called GENERIC and GIMPLE, performing various high-level optimizations
    before code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e7b77e39552d82141f71f039f70885754de72093
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit enhances the `fold_const_call.cc` pass to recognize and constant-fold calls to `__builtin_strnlen` when the maximum length argument is a compile-time constant. Previously, only `__builtin_strlen` was optimized this way. This change allows for better constant propagation and dead code elimination in cases involving bounded string length checks, as demonstrated by an example where a `strnlen` call with a PHI node input is successfully reduced.
