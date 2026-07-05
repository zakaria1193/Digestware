---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- gccrs
- Rust
- compiler
discussion_id: CAHtgQQtrT15qEWG7y4bN7ZKrPxhWh=iwv7yh4FCLShjmKnorxQ@mail.gmail.com
source_type: public_inbox
title: '[GSoC] Rust Drop trait support in gccrs - Status Report 3'
headline: Rust Drop trait support in gccrs - Status Report 3
tldr: GSoC student Janet Chien reports progress on implementing Rust's Drop trait
  in GCC's Rust frontend (gccrs), with several patches merged or under review.
proposer: Janet Chien <lishin1008@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Balancing the need for manual Drop call emission versus a more integrated try/finally-like
  cleanup mechanism.
exchanges:
- author: Janet Chien <lishin1008@gmail.com>
  role: proposer
  position: Provides an update on her GSoC project, detailing merged and in-review
    patches for Rust Drop trait implementation in gccrs, and outlining next steps.
  quote: "Since my last report, I have pushed the following patches:\n\n1. Refactor\
    \ the Drop infrastructure (CompileDrop / DropBuilder)\n    Merged:\n    https://github.com/Rust-GCC/gccrs/pull/4586\n\
    \n2. Add support for function-scope drops\n    Under review:\n    https://github.com/Rust-GCC/gccrs/pull/4591"
primer_expert: This is a project status update for the Google Summer of Code (GSoC)
  concerning the Rust frontend for GCC (gccrs). The focus is on implementing support
  for Rust's `Drop` trait, which handles resource deallocation. The report details
  progress on refactoring the drop infrastructure, adding support for various scoping
  mechanisms (function-scope, explicit returns), and testing, indicating advancement
  towards enabling safe Rust code compilation within GCC.
primer_glossary:
- term: GSoC
  definition: Google Summer of Code, an annual program that offers student developers
    stipends to contribute to open-source projects.
- term: gccrs
  definition: The Rust frontend for the GNU Compiler Collection (GCC).
- term: Drop trait
  definition: In Rust, a trait that allows custom cleanup logic to be executed when
    a value goes out of scope, ensuring resources are properly deallocated.
- term: GIMPLE
  definition: GCC's internal representation of code, used after parsing and before
    final code generation.
- term: try/finally
  definition: Control flow structures common in many programming languages for exception
    handling and guaranteed execution of cleanup code.
- term: defer
  definition: A Go language keyword that schedules a function call to be run later,
    typically used for cleanup actions, similar in concept to Rust's Drop trait.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAHtgQQtrT15qEWG7y4bN7ZKrPxhWh=iwv7yh4FCLShjmKnorxQ@mail.gmail.com
bugzilla_url: null
date: '2026-07-04'
is_stub: false
stub_reason: ''
---

Janet Chien, a Google Summer of Code student, provides her third status report on implementing Rust's Drop trait functionality in gccrs. Notable progress includes merging patches for Drop infrastructure refactoring and test cases for nested scopes, while other patches for function-scope drops, explicit returns, and non-unit tail expressions are currently under review. Future work involves refining existing patches and exploring a try/finally-based cleanup mechanism using the GCC Go frontend's defer implementation.
