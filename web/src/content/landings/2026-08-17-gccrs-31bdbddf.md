---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- rust
- compiler
- standard library
commit_hash: 31bdbddf39bebc3381db10addb60c709abf81f5d
source_type: github
author: Yap Zhi Heng
headline: Add missing lang item declarations for Rust core 1.49
tldr: GCC Rust compiler adds support for language items required by Rust standard
  library version 1.49.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gccrs` compiler's `LangItem::Kind` enum and `LangItem::lang_items`
  map have been extended with declarations for missing language items. These are specifically
  required to support compilation against Rust's standard library version 1.49. This
  commit ensures that `gccrs` can correctly resolve and instantiate fundamental language
  features defined within the Rust ecosystem.
primer_glossary:
- term: gccrs
  definition: The GCC implementation of the Rust programming language compiler. It
    aims to compile Rust code using the GCC backend infrastructure.
- term: lang item
  definition: In the context of Rust compilers like `rustc` and `gccrs`, language
    items are intrinsic functions, types, or traits that are fundamental to the language's
    operation and are often implemented directly by the compiler. They are essential
    for the standard library to function.
- term: Rust standard library
  definition: The collection of modules and functions that come with the Rust programming
    language, providing essential functionalities like collections, I/O, and string
    manipulation. Commonly referred to as 'std' or 'core'.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/31bdbddf39bebc3381db10addb60c709abf81f5d
date: '2026-08-17'
is_stub: false
stub_reason: ''
---

GCC Rust (gccrs) has been updated with new language item declarations necessary for compiling Rust code that depends on the standard library version 1.49. These additions in `rust-lang-item.h` and `rust-lang-item.cc` ensure compatibility and allow the compiler to correctly resolve and utilize essential features provided by the Rust core library.
