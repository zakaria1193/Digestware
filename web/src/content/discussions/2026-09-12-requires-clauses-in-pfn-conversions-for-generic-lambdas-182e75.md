---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c++
- lambda
- compiler
- standard
- gcc
discussion_id: 20260912030100.325efc83@aabbin
source_type: public_inbox
title: Requires clauses in pfn conversions for generic lambdas
headline: Requires clauses in pfn conversions for generic lambdas
tldr: Proposes adding requires clause evaluation to generic lambda conversions to
  function pointers, matching Clang's behavior.
proposer: Ivan Sokolov <sugrob9000aero@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 6
technical_tradeoffs:
- Enforcing constraints on lambda-to-function-pointer conversions improves type safety
  and consistency but might break existing code that relies on GCC's current lenient
  behavior.
- Aligning GCC's behavior with Clang's for this feature could improve cross-compiler
  compatibility.
- Potential standard defect investigation may lead to further language clarifications
  or modifications.
exchanges:
- author: Ivan Sokolov <sugrob9000aero@gmail.com>
  role: proposer
  position: Suggests that GCC should apply requires clauses to generic lambda conversions
    to function pointers, citing Clang's behavior and potential GCC bugs. Offers to
    provide a patch.
  quote: "Clang says yes, and to me this seems like solid and useful behavior.\n\n\
    GCC seems not to apply them, which in some cases results in weird reports of ambiguity:\n\
    \tstruct foo: decltype([]<std::integral I>()->I {}),\n\t            decltype([]<std::floating_point\
    \ F>()->F {}) {};\n\tfloat(*pfn)() = foo{};\n\t// accepted by clang, gcc thinks\
    \ the conversion is ambiguous\n\n...and in others results in ICE:\n\n\tfloat(…"
- author: Ivan Sokolov <sugrob9000aero@gmail.com>
  role: proposer
  position: Revises earlier statement, noting that both Clang and GCC deviate from
    the standard concerning lambda conversion operators.
  quote: 'On a second look, it seems Clang and GCC both do another useful deviation
    from that the standard.


    The paragraph says that the return value of the conversion operator should be
    as if decltype(/*operator() call'
primer_expert: This proposal addresses the behavior of C++ generic lambdas when converted
  to function pointers. Specifically, it concerns whether the constraints (requires
  clauses) applied to the lambda's `operator()` should also be enforced during the
  implicit conversion to a function pointer type. GCC's current implementation differs
  from Clang's, potentially leading to incorrect behavior or compiler issues, suggesting
  a possible gap in the standard's wording or GCC's interpretation.
primer_glossary:
- term: generic lambda
  definition: A C++ lambda expression that uses `auto` as a parameter type, allowing
    it to be called with different argument types. Its return type can also be deduced
    or specified using trailing return type syntax.
- term: requires clause
  definition: A C++20 feature that specifies constraints on template parameters, often
    used with concepts. It dictates which types are valid arguments for a template
    or, in this case, a generic lambda.
- term: function pointer
  definition: A variable that stores the memory address of a function, allowing functions
    to be called indirectly or passed as arguments.
- term: conversion to pointer to function
  definition: An implicit or explicit conversion from a callable entity (like a lambda)
    to a type that represents a pointer to a function, enabling interoperation between
    different callable forms.
- term: ICE
  definition: Internal Compiler Error. A severe error within the compiler itself that
    prevents it from completing the compilation process, often indicating a bug in
    the compiler.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260912030100.325efc83@aabbin
bugzilla_url: null
date: '2026-09-12'
is_stub: false
stub_reason: ''
---

This discussion proposes adding support for 'requires' clauses in C++ generic lambdas when converting them to function pointers. Currently, GCC does not apply these constraints, leading to ambiguities or internal compiler errors in certain cases, unlike Clang which appears to handle them correctly. The author offers to provide a patch if the change is deemed desirable for GCC and potentially the standard.
