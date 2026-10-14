---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- rust
- name resolution
commit_hash: bfc7edfb8d2e7144db57c04811762c13a3025d1e
source_type: github
author: Owen Avery
headline: 'gccrs: Ignore bindings on bodyless functions'
tldr: Compiler now correctly handles parameter names in bodyless functions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `Late::Late` name resolver in `gccrs` now correctly handles functions
  without bodies. It initializes `in_bodyless_params` and, within `visit(FunctionParam)`,
  skips processing parameter patterns if the function lacks a body. This prevents
  incorrect resolution when multiple parameters in a bodyless function share the same
  name, addressing a subtlety in Rust's name binding rules for such cases.
primer_glossary:
- term: Bodyless function
  definition: A function declaration in Rust that does not include an implementation
    body, often used in trait definitions or forward declarations.
- term: Late Name Resolver
  definition: A phase in the gccrs compiler's name resolution process that occurs
    after initial parsing and resolves names and bindings, particularly in the later
    stages of semantic analysis.
- term: Pattern
  definition: In Rust, a pattern is used in various contexts like function parameters,
    `match` expressions, and `let` bindings to deconstruct values and bind names to
    parts of those values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bfc7edfb8d2e7144db57c04811762c13a3025d1e
date: '2026-09-20'
is_stub: false
stub_reason: ''
---

gccrs has been updated to ignore bindings on parameters of bodyless functions, resolving an issue where different parameters could have the same name. The Late Name Resolver now initializes an `in_bodyless_params` flag and skips visiting patterns of function parameters in bodyless functions. This ensures correct name resolution for functions without bodies, as demonstrated in the new test case `multiple_bindings3.rs`.
