---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- refactor
- compiler internals
commit_hash: dfbdaf2f709a98748a1db719a31ea3f5ab3729a1
source_type: github
author: Pierre-Emmanuel Patry
headline: 'gccrs: Add ASTMapping to regroup all AST items mappings'
tldr: Introduces ASTMapping to consolidate AST item mappings, improving organization
  in gccrs.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The gccrs compiler's Rust HIR map has grown large. This commit refactors
  it by introducing `ASTMapping` to group AST-related mappings, specifically visibility
  mappings, and `ASTMappings` as a specialized collection. This improves organization
  within `rust-hir-map.cc/.h`, separating AST-specific concerns from other HIR data
  structures, which aids maintainability for developers working on the Rust frontend.
primer_glossary:
- term: AST
  definition: Abstract Syntax Tree. A tree representation of the abstract syntactic
    structure of source code, used internally by compilers to process and analyze
    code.
- term: HIR
  definition: High-Level Intermediate Representation. A representation of the code
    between the AST and the lower-level intermediate representations used by the compiler
    backend. In gccrs, it captures semantic information.
- term: gccrs
  definition: The Rust frontend for the GCC compiler, aiming to provide a robust and
    compliant Rust compilation experience within the GCC ecosystem.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dfbdaf2f709a98748a1db719a31ea3f5ab3729a1
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

The gccrs compiler has introduced a new class, ASTMapping, to better organize mappings related to Abstract Syntax Tree (AST) items. This change aims to streamline the codebase by regrouping certain AST item mappings that were previously spread across the Rust HIR map. This consolidation is expected to make the HIR map more manageable and improve the overall structure of the compiler's internal data handling.
