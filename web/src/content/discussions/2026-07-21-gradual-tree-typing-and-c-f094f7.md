---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler internals
- c++
- type system
discussion_id: al9pz_27btqZW8Df@tucnak
source_type: public_inbox
title: 'Re: Gradual ''tree'' typing and C++'
headline: Gradual 'tree' typing and C++
tldr: Debate continues on gradual typing for GCC's tree representation; Jakub Jelinek
  argues against it, citing increased complexity and lack of benefit for typical…
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Developer ergonomics vs. potential compile-time safety.
- Code readability and maintainability.
- Flexibility of existing macro system vs. C++ RTTI.
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Argues the proposed gradual typing introduces 'extra pain' and complexity
    without clear advantages for the typical ways GCC's internal code is written.
  quote: It is not an improvement, it is extra pain.
primer_expert: This exchange continues the debate on integrating gradual typing into
  GCC's internal representations (GENERIC, GIMPLE, RTL). The core of the disagreement
  lies in the practical impact of proposed C++ casting mechanisms (like `dyn_cast`)
  versus existing macros (`TREE_CODE`, `gimple_code`, `GET_CODE`). Jelinek contends
  that the common pattern in GCC is to inspect a node's type using macros and then
  act accordingly, rather than performing a strict type-specific cast. He argues the
  proposed casts are cumbersome for this pattern, especially when many distinct node
  types are handled, leading to code…
primer_glossary:
- term: tree
  definition: GCC's internal representation of the Abstract Syntax Tree (AST) and
    other intermediate forms.
- term: GENERIC
  definition: GCC's highest-level intermediate representation, a typed AST.
- term: GIMPLE
  definition: GCC's middle-end intermediate representation, a simplified form of the
    tree AST.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used in GCC's
    backend.
- term: TREE_CODE
  definition: A macro used to determine the type or kind of a GCC tree node.
- term: dyn_cast
  definition: A C++ RTTI (Run-Time Type Information) mechanism used for safe downcasting,
    often employed in frameworks like LLVM and proposed here for GCC's tree manipulation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/al9pz_27btqZW8Df@tucnak
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

Jakub Jelinek reiterates his rejection of the gradual 'tree' typing proposal, characterizing it as 'extra pain.' He elaborates that while static typing might offer theoretical advantages in some scenarios, the typical GCC codebase involves traversing and inspecting diverse tree/GIMPLE/RTL nodes, not expecting specific types. The proposed `dyn_cast` approach, he argues, adds unnecessary verbosity and complexity without significant benefit for these common use cases.
