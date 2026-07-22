---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler internals
- c++
- type system
discussion_id: amAAuEOmSKNh-_kZ@tucnak
source_type: public_inbox
title: 'Re: Gradual ''tree'' typing and C++'
headline: Gradual 'tree' typing and C++
tldr: Concerns raised about the syntax and verbosity of gradual typing proposals for
  GCC's internal tree representation.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Static typing and safety vs. dynamic typing flexibility and verbosity.
- Readability and maintainability of compiler code.
- Ergonomics for developers working with internal data structures.
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Criticizes the proposed gradual typing syntax, deeming it ugly, verbose,
    and restrictive compared to current methods like TREE_CODE.
  quote: 'All of it?

    Ugly syntax, having to type more than before (and thus having to deal with

    line wrapping more as well), having to introduce new vars for the dyn_cast

    way and being tied to if statements.'
primer_expert: This discussion concerns the C++ representation of GCC's internal Abstract
  Syntax Tree (AST) data structures, known as 'tree'. The proposal introduces gradual
  typing, allowing some parts of the tree to have statically known types while others
  remain dynamically typed. The debate centers on the C++ syntax and ergonomics for
  developers manipulating these trees, contrasting explicit type checks (like `dyn_cast`)
  with existing macros (like `TREE_CODE`).
primer_glossary:
- term: tree
  definition: GCC's internal representation of the Abstract Syntax Tree (AST) and
    other intermediate forms.
- term: TREE_CODE
  definition: A macro used to determine the type or kind of a GCC tree node.
- term: dyn_cast
  definition: A C++ RTTI (Run-Time Type Information) mechanism used for safe downcasting,
    often employed in frameworks like LLVM and proposed here for GCC's tree manipulation.
- term: GIMPLE
  definition: GCC's middle-end intermediate representation, a simplified form of the
    tree AST.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used in GCC's
    backend.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/amAAuEOmSKNh-_kZ@tucnak
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

Jakub Jelinek expresses strong reservations about a proposal for gradual typing in GCC's internal tree representation. He argues that the proposed syntax is ugly, more verbose than necessary, and restricts the flexibility developers currently have when working with TREE_CODEs and similar macros.
