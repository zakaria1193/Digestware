---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- diagnostics
- c++20
commit_hash: eca81a88ed151269a7a1aa7c37c4036995ded6e4
source_type: github
author: Marek Polacek
headline: 'C++/reflection: Detect more invalid splice-expressions'
tldr: Compiler now correctly rejects invalid template usage in C++20 reflection splice
  expressions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refines the C++20 reflection implementation by improving
  the validation of `splice-expr` syntax, particularly concerning templates. It rectifies
  `check_splice_expr` in `reflect.cc` to correctly reject non-function/variable templates
  in `splice-specifier` contexts, aligning with [expr.prim.splice]/2. Additionally,
  it enforces the restriction that only function and variable templates are allowed
  in `template-splice-specialization-specifier`, per [expr.prim.splice]/4. The changes
  also fix `missing_template_diag` for dependent splices, enhancing diagnostic messages.
primer_glossary:
- term: C++ reflection
  definition: A proposed C++ feature (standardized in C++26, with earlier experimental
    support) that allows code to inspect and manipulate its own structure at compile
    time. This includes examining types, members, and templates.
- term: splice-expression
  definition: A construct within C++20's reflection facilities that allows for the
    inclusion or exclusion of members or bases from a reflected entity, often used
    to conditionally add or remove members during template instantiation.
- term: template
  definition: A blueprint for creating classes or functions in C++. Templates allow
    code to be written generically, working with different types without explicit
    duplication.
- term: dependent splice
  definition: A splice-expression whose evaluation or validity depends on a template
    parameter that is not yet known. Diagnosing errors in these constructs can be
    complex.
- term: ABI
  definition: Application Binary Interface. Defines how low-level code is structured,
    including function calling conventions, data layout, and name mangling. Incorrect
    ABI compliance can lead to runtime errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eca81a88ed151269a7a1aa7c37c4036995ded6e4
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

GCC's C++ reflection support now correctly detects more invalid uses of splice-expressions, specifically addressing issues with template usage. The compiler previously crashed or miscompiled code where templates were incorrectly used in splice-specifiers or template splice-specializations. This fix aligns the compiler with C++20 standard sections [expr.prim.splice]/2 and /4, improving diagnostics and preventing crashes, while also extending error checking for dependent splices.
