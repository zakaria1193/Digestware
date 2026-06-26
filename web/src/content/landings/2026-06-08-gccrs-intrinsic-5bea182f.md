---
project: gcc
subsystem: gccrs/intrinsic
patch_id: null
tags:
- rust
- gccrs
- intrinsics
- alignment
- memory
commit_hash: 5bea182f3db92485bd6f00125043a9192d425ac9
source_type: github
author: Enes Cevik
headline: Add min_align_of intrinsic
tldr: The GCC Rust front-end now supports the `min_align_of` intrinsic, allowing retrieval
  of minimum alignment for sized types.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces the `min_align_of` intrinsic to the `gccrs`
  project. This intrinsic, implemented via `min_align_of_handler` in `backend/rust-intrinsic-handlers.cc`
  and registered in `backend/rust-compile-intrinsic.cc`, provides the minimum alignment
  of a compile-time sized type. It returns a `size_type_node` integer constant expression,
  allowing for static alignment queries which can be crucial for data structure packing,
  FFI boundaries, and various memory optimization strategies within the Rust toolchain.
primer_general: When a computer stores data in memory, it often needs to place that
  data at specific memory addresses, a concept known as 'alignment.' Different types
  of data have different alignment requirements to perform efficiently. This update
  adds a new special function, or 'intrinsic,' to the GCC Rust compiler called `min_align_of`.
  This intrinsic lets Rust programmers ask the compiler, at the time the program is
  being built, what is the smallest required alignment for a particular data type.
  This information is useful for advanced programming tasks, such as making sure data
  structures are laid out efficiently in memory, which can lead to faster programs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5bea182f3db92485bd6f00125043a9192d425ac9
date: '2026-06-08'
is_stub: false
stub_reason: ''
---

The GCC Rust front-end (gccrs) has gained support for a new compiler intrinsic called `min_align_of`. This intrinsic allows developers to query the minimum alignment requirements for a given compile-time sized type. It resolves this information and returns it as an integer constant expression, which can be useful for low-level memory management and optimization in Rust code.
