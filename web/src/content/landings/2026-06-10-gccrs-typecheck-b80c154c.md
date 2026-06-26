---
project: gcc
subsystem: gccrs/typecheck
patch_id: null
tags:
- rust
- gccrs
- type-checking
- core-crate
- resolution
commit_hash: b80c154cf0fda31a6fa9ce85c60bfcb82966cd67
source_type: github
author: Arthur Cohen
headline: Special case builtin types when typechecking types
tldr: The GCC Rust front-end now correctly resolves builtin types even when name conflicts
  with modules exist, supporting `core` crate extensions.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `typecheck/rust-hir-type-check-type.cc`, specifically
  within `TypeCheckType::resolve_root_path`, to introduce special-casing for builtin
  type resolution. The issue arises when a name could resolve to both a module and
  a builtin type, a pattern frequently seen in the Rust `core` crate for extending
  core types. This change prioritizes the builtin type definition in such ambiguous
  cases, ensuring proper type inference and preventing incorrect module resolution
  when typechecking.
primer_general: In the Rust programming language, some fundamental data types (like
  integers and booleans) are considered 'builtin' types. Sometimes, the core library
  of Rust (called the `core` crate) wants to add more features to these builtin types,
  which can occasionally lead to a tricky situation where a name might refer to both
  a builtin type and a different organizational unit called a 'module.' This update
  to the GCC Rust compiler (gccrs) adds a special rule to handle these situations.
  It ensures that when there's a conflict, the compiler correctly understands that
  the developer is referring to the builtin type, allowing the `core` crate to extend
  these types without causing confusion in the compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b80c154cf0fda31a6fa9ce85c60bfcb82966cd67
date: '2026-06-10'
is_stub: false
stub_reason: ''
---

The GCC Rust front-end (gccrs) now includes special handling during type resolution for builtin types. This change allows type definition conflicts when a type name could refer to either a module or a builtin type, a common scenario in the `core` crate where builtin types are extended with additional functionality. By special-casing this resolution, the compiler ensures that builtin types are correctly identified and used, enabling more flexible and powerful type extensions.
