---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- rust
- generic programming
- compiler
commit_hash: f4fede6edba2bbb51f7ec00f60565db9156796c8
source_type: github
author: Utkarsh Bahuguna
headline: 'gccrs: Reject type param defaults using later params'
tldr: Compiler now rejects Rust type parameter defaults that reference parameters
  declared later in the sequence.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ForeverStack::forward_declared` check in `rust-forever-stack.h`
  has been enhanced to detect type parameter defaults that reference parameters appearing
  later in the declaration sequence, in addition to self-referential defaults. The
  `resolve_type_path_like` function in `rust-late-name-resolver-2.0.cc` is updated
  to skip this check for `Self`, as it's a special case. This addresses a gap in compile-time
  validation for generic Rust types.
primer_glossary:
- term: gccrs
  definition: The GCC frontend for the Rust programming language.
- term: Type Parameter
  definition: In generic programming, a placeholder for a type that is specified when
    a generic type or function is used. In Rust, these are often denoted by angle
    brackets like `<T>`.
- term: Default
  definition: A pre-defined value or type that is used for a type parameter if no
    specific type is provided when the generic is instantiated. For example, `struct
    Foo<T = i32>`.
- term: Self
  definition: A special type keyword in Rust that refers to the type the current impl
    block is for. It is distinct from other generic type parameters.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f4fede6edba2bbb51f7ec00f60565db9156796c8
date: '2026-10-03'
is_stub: false
stub_reason: ''
---

The gccrs compiler has been updated to reject invalid Rust type parameter defaults. Previously, it only caught cases where a default referred to its own parameter; now, it also flags defaults that reference parameters declared later in the generic parameter list. This prevents potentially erroneous type definitions and improves compile-time error checking for generic types.
