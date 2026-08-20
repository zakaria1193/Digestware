---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- language feature
commit_hash: 50a2eb56b9a350ecced4db4942e92d463dab8d8f
source_type: github
author: Marek Polacek
headline: 'c++/reflection: reject bare [: bases_of(...)[0] :]'
tldr: Correctly rejects ill-formed reflection expressions involving base class relationships
  without an object.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The C++ reflection implementation rejects attempts to use `[: bases_of(T,
  ctx)[0] :]` in splice expressions when no object is specified. This adheres to the
  interpretation of C++ standards like [expr.prim.splice]/2.4 and P3293, which imply
  that designating a direct base class relationship via splice requires an explicit
  object, preventing ill-formed expressions from causing gimplification failures.'
primer_glossary:
- term: C++ reflection
  definition: A feature in C++ that allows code to inspect and manipulate its own
    structure at compile time or runtime, often used for metaprogramming and introspection.
- term: splice
  definition: A C++ expression construct used in reflection to designate a relationship
    or entity within the reflected code.
- term: bases_of
  definition: A C++ reflection utility likely used to query the base classes of a
    given type.
- term: gimplify
  definition: The process in GCC where C++ abstract syntax tree (AST) is converted
    into GIMPLE, GCC's intermediate representation, before further optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/50a2eb56b9a350ecced4db4942e92d463dab8d8f
date: '2026-08-17'
is_stub: false
stub_reason: ''
---

This change rejects C++ reflection expressions that attempt to splice a base class relationship without specifying an object. The standard implies such expressions, which reference a direct base class relationship, require an object context, and this commit enforces that rule to prevent crashes in the compiler's gimplify phase.
