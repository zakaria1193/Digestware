---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- optimization
- ICE
- RISC-V
- RTL
commit_hash: 87eeb9ed5d5932c4777f1a4358f21fec76cc420b
source_type: github
author: Robin Dapp
headline: Prevent ICE in lower-subreg by distinguishing CONCATN types.
tldr: Fix compiler crash related to register decomposition by better identifying temporary
  concatenations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `lower-subreg` pass in GCC's RTL (Register Transfer Language) optimization
  pipeline is responsible for simplifying subregister accesses. It can decompose `CONCATN`
  subregisters, which represent concatenations of smaller register modes. The pass
  has logic specifically for handling `CONCATN`s it generates itself. However, when
  encountering pre-existing `CONCATN`s from other compiler passes (e.g., in `rtl.h`
  or from vector operations), it could trigger ICEs. This patch introduces a `DECOMPOSED_REGISTER_P`
  flag, similar to how `volatil` is used in `var-tracking.cc`, to mark `CONCATN`s
  created…
primer_glossary:
- term: RTL
  definition: Register Transfer Language. An intermediate representation used by GCC
    after the initial tree-based optimizations, closer to machine instructions and
    register allocations.
- term: subregister
  definition: A portion of a larger hardware register that can be accessed independently.
    Optimizations often manipulate subregisters to make efficient use of machine registers.
- term: CONCATN
  definition: A GCC internal representation for a concatenation of two or more smaller
    values or register modes into a larger one. This is distinct from the simpler
    CONCAT in some contexts.
- term: ICE
  definition: Internal Compiler Error. A bug within the compiler itself that causes
    it to crash during compilation.
- term: RVV
  definition: RISC-V Vector extension. A set of instructions for performing operations
    on multiple data elements in parallel, similar to SIMD extensions on other architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/87eeb9ed5d5932c4777f1a4358f21fec76cc420b
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

The `lower-subreg` optimization pass could encounter an ICE when processing pre-existing `CONCATN` (concatenation) subregisters. This was because the pass incorrectly attempted to decompose these, leading to assertions about inner modes being splittable. This commit enhances `lower-subreg` to distinguish between temporary `CONCATN`s it creates and those that already exist in the code.

A new flag is set on temporary `CONCATN`s, preventing them from being decomposed inappropriately and thus avoiding the compiler crash. This also includes updates to RTL structures and test cases for RVV.
