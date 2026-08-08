---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- semantics
- scope management
commit_hash: dafe3b7de68c2b15a9b245a731f0599448c5c2ab
source_type: github
author: Lishin
headline: 'gccrs: Separate scopes for function arguments and bodies'
tldr: gccrs enhances scope management for function arguments and bodies, improving
  drop order.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'In `gccrs`, the compiler creates distinct scopes for function argument
  declarations and the function body to manage the lifetime of variables and their
  associated `drop` calls correctly. This change ensures that argument scope is established
  prior to processing function parameters, so that any `drop` actions related to arguments
  are localized to that scope. Subsequently, the function''s body is compiled within
  a nested scope. The cleanup order is reversed: the inner body scope is dropped before
  the outer argument scope, ensuring that local variables within the body are deallocated
  before argum…'
primer_glossary:
- term: scope
  definition: A region of the code where a declared variable or name is valid and
    can be accessed. In `gccrs`, scopes are used to manage the lifetime of variables
    and their associated cleanup actions (like `drop`).
- term: drop
  definition: In Rust, a `drop` is an action that runs when a value goes out of scope,
    typically to deallocate memory or release resources. `gccrs` needs to manage these
    `drop` calls correctly.
- term: HIR lowering
  definition: The process in `gccrs` of transforming the Abstract Syntax Tree (AST)
    into a High-Level Intermediate Representation (HIR). This stage typically simplifies
    code structure and prepares it for further optimization and code generation.
- term: argument scope
  definition: A scope specifically created in `gccrs` to manage variables and their
    lifetimes related to function parameters.
- term: function body scope
  definition: A scope created within `gccrs` for the variables declared inside a function's
    implementation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dafe3b7de68c2b15a9b245a731f0599448c5c2ab
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

GCC's Rust front-end, `gccrs`, now separates scope management for function arguments and their bodies. The argument scope is created before parameter compilation, ensuring argument drops are registered correctly. The function body is compiled in a nested scope, and its scope is cleaned up before the argument scope, guaranteeing that body locals are dropped before parameters.
