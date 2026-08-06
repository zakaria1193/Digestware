---
project: gcc
subsystem: gcc/fold-const
patch_id: null
tags:
- optimization
- compiler
- C++
commit_hash: 141edd02af705696f89ff9a804879dc51834898d
source_type: github
author: Jakub Jelinek
headline: Improve pointer arithmetic optimizations in fold-const and match.pd.
tldr: Enhances optimization of pointer differences involving casts and address expressions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit targets the constant folding of pointer difference expressions,
  specifically addressing regressions in the C++ frontend. The optimization in `fold-const.cc`
  that casts pointer arithmetic `(T1)(X p+ Y)` to `((T1)X p+ Y)` when `X` is a cast
  was found to be problematic. The fix introduces `STRIP_NOPS` in `split_address_to_core_and_offset`
  and adds ADDR_EXPR requirements to simplification patterns in `match.pd`. This ensures
  that `ptr_difference_const` correctly handles complex scenarios involving casts,
  `SSA_NAME`s, `ADDR_EXPR`s, and `POINTER_PLUS_EXPR`s, preventing ICEs and incorrec…
primer_glossary:
- term: fold-const
  definition: A compiler pass or optimization technique that evaluates constant expressions
    at compile time rather than runtime. This includes arithmetic on constant values,
    pointer arithmetic on constant addresses, etc.
- term: match.pd
  definition: A file or component within GCC's optimization framework that likely
    defines patterns for matching and simplifying various expression trees. '.pd'
    might refer to 'pattern definition'.
- term: POINTER_DIFF_EXPR
  definition: An intermediate representation (IR) or tree node in GCC representing
    the difference between two pointers, which results in an integer value (e.g.,
    number of elements).
- term: ADDR_EXPR
  definition: An intermediate representation (IR) or tree node in GCC representing
    an address of a variable or expression.
- term: SSA_NAME
  definition: Static Single Assignment form. In SSA, each variable is assigned exactly
    once. SSA_NAME represents a named temporary or variable in SSA form, often resulting
    from computations.
- term: ICE
  definition: Internal Compiler Error. An unexpected condition encountered by the
    compiler during its execution, indicating a bug in the compiler itself.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/141edd02af705696f89ff9a804879dc51834898d
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

Optimizations for constant pointer differences have been improved by refining the `ptr_difference_const` logic in `match.pd` and `fold-const.cc`. The changes address issues where certain pointer arithmetic expressions, particularly those involving casts and address expressions, were not handled correctly. By adding checks for no-operation conversions and ADDR_EXPR requirements, the compiler can now more reliably fold these expressions, preventing potential regressions and ICEs (Internal Compiler Errors).
