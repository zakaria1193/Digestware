---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gccrs
- rust
- gsoc
- compiler
- frontend
discussion_id: CAHtgQQsQu9zcSpF_+6xdfSnvj16VwTuX1Qc1noLQ4HkuK8utaQ@mail.gmail.com
source_type: public_inbox
title: '[GSoC] Rust Drop trait support in gccrs - Status Report 5'
headline: Rust Drop trait support in gccrs - Status Report 5
tldr: GSoC student reports progress on implementing Rust's Drop trait in GCC's Rust
  frontend, focusing on scope alignment and BIR analysis.
proposer: Janet Chien <lishin1008@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring accurate semantics for Rust's Drop trait within GCC's internal representations.
- Aligning gccrs's implementation with rustc's behavior for compatibility.
- Developing robust analysis passes on BIR to handle complex control flow for drop
  behavior.
exchanges:
- author: Janet Chien <lishin1008@gmail.com>
  role: proposer
  position: Reports progress on implementing Rust's Drop trait in gccrs, detailing
    recent work on scope separation, BIR analysis, and outstanding issues.
  quote: "Since the last report, I have mainly focused on\naligning gccrs with rustc,\
    \ investigating BIR in gccrs,\nand how MIR implements CFG in rustc.\n\nI pushed\
    \ patches to:\n1. Separate argument and function body drop scopes\n    (ref: https://github.com/Rust-GCC/gccrs/issues/4712)\n\
    \    Under review:\n    https://github.com/Rust-GCC/gccrs/pull/4718\n\n2. Add\
    \ straight-line BIR drop style analysis\n    Under review:…"
primer_expert: This GSoC status report details progress on implementing Rust's `Drop`
  trait within the GCC Rust frontend (gccrs). Key activities include aligning gccrs's
  drop scope semantics with rustc's, and developing analyses on GCC's Backend Intermediate
  Representation (BIR) to correctly model drop behavior, particularly for straight-line
  code and control flow.
primer_glossary:
- term: Drop trait
  definition: In Rust, a trait that defines custom behavior when a value goes out
    of scope, typically for resource cleanup.
- term: gccrs
  definition: The Rust frontend for GCC, aiming to compile Rust code using the GCC
    toolchain infrastructure.
- term: BIR
  definition: Backend Intermediate Representation, an internal data structure used
    by GCC to represent code before generating machine code.
- term: MIR
  definition: Mid-level Intermediate Representation, an intermediate representation
    used in the Rust compiler (rustc) that is closer to the source code than LLVM
    IR.
- term: CFG
  definition: Control Flow Graph, a data structure representing the possible paths
    of execution through a program.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAHtgQQsQu9zcSpF_+6xdfSnvj16VwTuX1Qc1noLQ4HkuK8utaQ@mail.gmail.com
bugzilla_url: null
date: '2026-08-01'
is_stub: false
stub_reason: ''
---

Janet Chien provides the fifth status report for her Google Summer of Code project to implement Rust's `Drop` trait in gccrs. Progress includes separating drop scopes, analyzing BIR for drop styles, and addressing an issue with double drops. Ongoing work involves refining patches and extending BIR analysis to control flow.
