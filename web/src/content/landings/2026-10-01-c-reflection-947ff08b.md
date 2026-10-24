---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- constexpr
- compiler bugs
commit_hash: 947ff08bff31425cdcb02b445f135a1ece869873
source_type: github
author: Marek Polacek
headline: 'C++/reflection: Fix extract-ref to correctly handle variable lifetime and
  constant expressions'
tldr: C++ reflection's `extract-ref` is fixed to correctly evaluate variable lifetime
  and constant expression constraints, resolving crashes and improving accuracy.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch for GCC's C++ front-end (`cp/constexpr.cc`, `cp-tree.h`,
  `cp/reflect.cc`) rectifies issues in `reflect::extract_ref` concerning PR127232.
  It refines the checks against [meta.reflection.extract]/5.3 by introducing `constexpr_global_ctx::in_eval_lifetime_p`
  and `cxx_constexpr_in_eval_lifetime_p` to accurately determine if a variable's lifetime
  began within the current constant evaluation. This replaces the imprecise `is_constant_expression`
  check, preventing crashes when `build_address` receives types instead of variables.
  The patch also corrects handling of `DECL_INITIAL` for `PARM_…
primer_glossary:
- term: C++ Reflection
  definition: A C++ language feature (currently a proposal) that allows programs to
    inspect and manipulate their own structure at runtime or compile time, such as
    examining types, variables, and functions.
- term: extract-ref
  definition: A specific operation or function within the C++ reflection mechanism
    designed to extract a reference to a variable or entity.
- term: Constant expression
  definition: An expression in C++ that can be evaluated at compile time. Variables
    usable in constant expressions must meet certain criteria, such as being `const`
    and having their initializer evaluated at compile time.
- term: Lifetime
  definition: The duration during which an object or variable is valid and can be
    accessed in C++. For constant expressions, this includes whether the object's
    lifetime began within the current evaluation context.
- term: PARM_DECL
  definition: A GCC internal representation (tree node) for a function parameter declaration.
- term: NOP_EXPR
  definition: An intermediate representation (IR) node in GCC that represents a no-operation.
    It is often used to wrap expressions or values without changing their meaning,
    sometimes to satisfy type or conversion requirements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/947ff08bff31425cdcb02b445f135a1ece869873
date: '2026-10-01'
is_stub: false
stub_reason: ''
---

This commit corrects the `extract-ref` functionality within C++'s reflection capabilities to align with the standard's requirements regarding variable lifetime and constant expressions. Previously, incorrect checks led to crashes when evaluating variables. The fix ensures that `extract-ref` properly distinguishes between variables usable in constant expressions and those whose lifetimes began within the current evaluation context. It also addresses how parameter declarations are handled and ensures that results are correctly wrapped to maintain type fidelity, resolving PR127232.
