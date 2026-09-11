---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- constexpr
- constant evaluation
- rust
commit_hash: 5adfaf6a4f94913a0833250a428e5c37e55d46fd
source_type: github
author: Philip Herron
headline: 'gccrs: Add maybe fold reference to constexpr from cp/constcexpr.cc'
tldr: gccrs integrates constexpr evaluation by porting reference folding logic from
  C++ frontend.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gccrs` backend, specifically `rust-constexpr.cc`, now incorporates
  `maybe_fold_reference_address_to_pointer` from GCC's C++ frontend (`cp/constcexpr.cc`).
  This function is key for evaluating constant expressions, particularly when dealing
  with references to addresses. By porting this logic, `gccrs` enhances its ability
  to correctly resolve and fold expressions involving references within `constexpr`
  evaluations, addressing issues like Rust-GCC/gccrs#4631.
primer_glossary:
- term: constexpr
  definition: A keyword in C++ and a concept in Rust indicating that an expression
    can be evaluated at compile time. GCC's Rust frontend aims to support Rust's equivalent
    constant evaluation capabilities.
- term: fold reference
  definition: In the context of constant evaluation, this likely refers to simplifying
    or resolving expressions involving references, possibly by evaluating them to
    their underlying values or addresses.
- term: C++ frontend (cp)
  definition: The part of the GCC compiler responsible for parsing, analyzing, and
    generating intermediate representation for C++ code.
- term: constant expression evaluation
  definition: The process by which the compiler determines the value of an expression
    at compile time, rather than at runtime. This is essential for constructs like
    compile-time constants and generic programming.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5adfaf6a4f94913a0833250a428e5c37e55d46fd
date: '2026-08-15'
is_stub: false
stub_reason: ''
---

This commit brings `maybe_fold_reference_address_to_pointer` and related logic from GCC's C++ frontend (`cp/constcexpr.cc`) into `gccrs`. This integration is crucial for evaluating constant expressions (`constexpr`) in Rust, particularly by enabling the correct handling of references to addresses within these constant evaluations. The change aims to improve `constexpr` support and resolve issues related to constant expression evaluation.
