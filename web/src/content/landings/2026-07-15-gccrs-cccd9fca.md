---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- rust
- compiler
- c++
- compatibility
commit_hash: cccd9fca61c7a73a1d6017c38d8567581cf30370
source_type: github
author: Yap Zhi Heng
headline: Define constructor for LoadedCrate struct in gccrs
tldr: gccrs adds a constructor for `LoadedCrate` to fix C++20 aggregate initialization
  issues.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: An explicit constructor is added to the `Session::LoadedCrate` struct
  within `rust-session-manager.h` to address problems encountered with aggregate initialization
  under C++20 standards. This change ensures that the `LoadedCrate` structure can
  be correctly instantiated in the C++ compilation environment used by gccrs.
primer_glossary:
- term: gccrs
  definition: The GCC backend for the Rust programming language, enabling Rust code
    to be compiled by GCC.
- term: LoadedCrate
  definition: An internal gccrs data structure representing a Rust crate that has
    been loaded and processed by the compiler session.
- term: aggregate initialization
  definition: A C++ feature for initializing objects of aggregate types (like structs
    and arrays) using braces `{}`. C++20 introduced changes that affected how this
    works for certain types.
- term: C++20
  definition: The 2020 edition of the C++ programming language standard, introducing
    new features and modifying existing ones.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cccd9fca61c7a73a1d6017c38d8567581cf30370
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

A C++20 compatibility issue with aggregate initialization for the `LoadedCrate` struct in gccrs has been resolved by adding an explicit constructor. This ensures that `LoadedCrate` can be properly initialized in C++20 environments, maintaining the compiler's stability.
