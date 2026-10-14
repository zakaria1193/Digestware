---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- validation
- compiler errors
commit_hash: dcf3cbc0f78de4834914895122d70530c3ffd775
source_type: github
author: Owen Avery
headline: 'gccrs: Improve bodyless function pattern check'
tldr: Enhances gccrs's AST validation to catch complex patterns in bodyless functions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Enhances `ASTValidation::visit(Function)` in gccrs's `rust-ast-validation.cc`.
  Previously, complex patterns in function parameters were only checked for extern
  functions. This change extends the check to non-extern bodyless functions as well,
  preventing potentially invalid constructs from passing through the AST validation
  stage. A new test case `rust/compile/function-param-bodyless.rs` is added to cover
  this scenario.
primer_glossary:
- term: AST
  definition: Abstract Syntax Tree. A tree representation of the abstract syntactic
    structure of source code, used internally by compilers to process and analyze
    code.
- term: bodyless function
  definition: In Rust, this typically refers to functions declared without a body,
    such as function signatures in traits or extern declarations. This commit addresses
    non-extern declarations that lack a body.
- term: gccrs
  definition: The Rust frontend for the GCC compiler, aiming to provide a robust and
    compliant Rust compilation experience within the GCC ecosystem.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dcf3cbc0f78de4834914895122d70530c3ffd775
date: '2026-09-20'
is_stub: false
stub_reason: ''
---

The gccrs compiler has improved its Abstract Syntax Tree (AST) validation to better handle bodyless functions. This commit modifies the AST validation logic to emit an error when complex patterns are used in non-extern bodyless functions. A new test case, `function-param-bodyless.rs`, has been added to verify this improved checking.
