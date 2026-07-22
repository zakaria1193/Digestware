---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler internals
- c++
- type system
- ergonomics
discussion_id: 8b074ff81c6cd18c313d7f46626922c9e1aa9b62.camel@gwdg.de
source_type: public_inbox
title: 'Re: Gradual ''tree'' typing and C++'
headline: Gradual 'tree' typing and C++
tldr: Reviewers critique a gradual typing proposal for GCC's tree representation,
  calling it an 'abomination' that makes developers' lives harder.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 2
technical_tradeoffs:
- Increased code verbosity and complexity for developers.
- Potential for compile-time type safety vs. runtime checks.
- Impact on developer productivity and code maintainability.
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: reviewer
  position: Initially rejected the idea outright, stating it's 'the exact opposite'
    of an improvement.
  quote: I'm sorry, but this is not an improvement, it is an exact opposite of that.
- author: Eric Botcazou <ebotcazou@libertysurf.fr>
  role: reviewer
  position: Agrees with Jakub Jelinek, criticizing the proposal as making developers'
    lives harder and contrary to expectations from C++ adoption.
  quote: "Yes, a very promising attempt at making the life of compiler hackers harder.\n\
    \nAnd we were told that the transition to C++ would not lead to this kind of \n\
    abominations..."
- author: Arsen Arsenović <aarsenovic@baylibre.com>
  role: contributor
  position: Proposed the change to use explicit fallible conversion functions.
  quote: "Checks-and-uses of TREE_CODEs would also need to become (explicit)\nfallible\
    \ conversion functions, i.e.\n\n  if (TREE_CODE (t) == A) use t;\n\n... becomes:\n\
    \n  if (auto tA = try_as_tree_or_whatever<A> (t)) use tA;"
primer_expert: This is a discussion about proposed changes to GCC's internal representation
  handling, specifically regarding how developers check and cast types within the
  'tree' data structure. The proposal, motivated by gradual typing, suggests replacing
  simple macros like `TREE_CODE` with C++ dynamic casts (`dyn_cast` or similar fallible
  conversions). Reviewers like Jelinek and Botcazou argue this significantly increases
  verbosity and complexity without clear benefits for the majority of use cases, which
  involve inspecting diverse tree nodes rather than expecting specific types.
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
url: https://inbox.sourceware.org/gcc/al--r68ddzGweLld@tucnak
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

This discussion follows an exchange about gradual typing in GCC's internal tree representation. Arsen Arsenović suggested converting checks into fallible conversion functions (e.g., `try_as_tree_or_whatever`). Jakub Jelinek strongly disagreed, calling it an improvement. Eric Botcazou concurs with Jelinek, expressing dismay that the transition to C++ has led to such 'abominations' and arguing it makes compiler development harder.
