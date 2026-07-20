---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gccrs
- rust
- gsoc
- drop-trait
discussion_id: CAHtgQQsDtZD8pJtRSZym-9_p_C56qfceAG3uYJ_s95F9F+Pm+Q@mail.gmail.com
source_type: public_inbox
title: '[GSoC] Rust Drop trait support in gccrs - Status Report 4'
headline: Rust Drop trait support in gccrs - Status Report 4
tldr: GSoC student reports progress on implementing Rust's Drop trait in GCC, focusing
  on exception handling.
proposer: Janet Chien <lishin1008@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Migrating from manual drop call emission to `TRY_FINALLY_EXPR` simplifies code but
  requires careful mapping of Rust's drop semantics to GCC's internal exception handling.
exchanges:
- author: Janet Chien <lishin1008@gmail.com>
  role: proposer
  position: Reports on progress incorporating Rust's `Drop` trait, including migrating
    to `TRY_FINALLY_EXPR` for cleanup and updating existing patches based on review
    feedback.
  quote: null
primer_expert: gccrs aims to implement Rust language features. This report details
  progress on `Drop` trait support, focusing on exception handling semantics within
  the compiler's intermediate representation. The work involves adapting cleanup strategies
  to align with GCC's internal expression handling.
primer_glossary:
- term: Drop trait
  definition: In Rust, a trait that defines the behavior of objects when they go out
    of scope, akin to a destructor in C++.
- term: gccrs
  definition: The Rust frontend for GCC, enabling GCC to compile Rust code.
- term: TRY_FINALLY_EXPR
  definition: A GCC internal expression type used for structured exception handling,
    similar to try-finally blocks in other languages.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAHtgQQsDtZD8pJtRSZym-9_p_C56qfceAG3uYJ_s95F9F+Pm+Q@mail.gmail.com
bugzilla_url: null
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

This is a status report on a Google Summer of Code project to implement Rust's `Drop` trait in gccrs, the Rust frontend for GCC. The primary focus has been on refactoring cleanup mechanisms to use `TRY_FINALLY_EXPR` instead of manual drop calls, with several patches merged or under review. The project also aims to align the gccrs design with rustc's approach.
