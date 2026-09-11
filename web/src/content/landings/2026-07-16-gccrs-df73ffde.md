---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- rust
- pin
- unpin
- language items
commit_hash: df73ffdeb7e0152ae5efe7554adc9e2834a34798
source_type: github
author: Enes Cevik
headline: 'gccrs: lang: Add pin and unpin lang items'
tldr: gccrs compiler now registers 'pin' and 'unpin' language items.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `Rust::LangItem::lang_items` BiMap in `rust-lang-item.cc` is updated
  to include new entries for `PIN` and `UNPIN`. Concurrently, the `Kind` enum in `rust-lang-item.h`
  is expanded with these variants. This change lays the groundwork for gccrs to recognize
  and handle `Pin` and `Unpin` types and their associated traits, crucial for safe
  handling of self-referential data structures and in-place mutation scenarios.
primer_glossary:
- term: language items
  definition: Special intrinsic items recognized by the Rust compiler that represent
    fundamental language concepts, such as primitive types, traits (`Send`, `Sync`),
    and built-in functions. They are essential for the compiler's internal operations
    and type system.
- term: Pin
  definition: A Rust type that guarantees a value will not be moved in memory after
    its initial allocation. It's crucial for scenarios involving self-referential
    data structures and certain concurrency patterns.
- term: Unpin
  definition: A Rust trait indicating that a type is allowed to be moved in memory.
    Types that are `Unpin` do not require special handling regarding memory stability,
    unlike types that are only `Pin`.
- term: BiMap
  definition: A data structure that stores bidirectional mappings between keys and
    values. In this context, it likely maps string names or identifiers to internal
    representations of language items.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/df73ffdeb7e0152ae5efe7554adc9e2834a34798
date: '2026-07-16'
is_stub: false
stub_reason: ''
---

This commit introduces the `pin` and `unpin` language items into the gccrs compiler. These items are fundamental for supporting Rust's `Pin` type, which guarantees that a value will not be moved in memory after it has been initially placed. While the language items are registered, full testing is pending due to related issues.
