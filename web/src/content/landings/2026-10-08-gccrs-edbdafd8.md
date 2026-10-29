---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- compiler-error
- pattern-matching
commit_hash: edbdafd8688939ddeeca395d7a997a2ce7308d2b
source_type: github
author: Utkarsh Bahuguna
headline: 'gccrs: Fix ICE on enum tuple variants with rest patterns'
tldr: Fixes an internal compiler error in gccrs when processing rest patterns in enum
  tuple variants.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In gccrs, pattern matching on enum variants that use rest patterns
  (`..`) was causing an ICE. The `CompilePatternCheckExpr` and `CompilePatternBindings`
  visitors in `rust-compile-pattern.cc` were not equipped to handle the structure
  of enum variants with rest patterns, as they only understood struct field layouts.
  This patch modifies these visitors to correctly access enum variant fields via the
  payload union, similar to how non-rest patterns are processed, thus fixing the ICE
  and addressing Rust-GCC/gccrs#4978.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A condition where the compiler encounters an
    unrecoverable error during its execution, leading to a crash.
- term: rest pattern
  definition: A pattern matching syntax (often `..`) that allows a variable number
    of fields or elements to be ignored or captured in a single binding.
- term: enum tuple variant
  definition: A variant of an enumeration that holds its data as a tuple of unnamed
    fields.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/edbdafd8688939ddeeca395d7a997a2ce7308d2b
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

This commit resolves an ICE (Internal Compiler Error) in gccrs that occurred when encountering rest patterns (using `..`) in enum tuple variants. Previously, the pattern checking and binding visitors incorrectly assumed the field layout of structs, not enums. The fix involves reading enum variant fields through the payload union, aligning with how non-rest patterns are handled.
