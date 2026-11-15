---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- Rust
- pattern matching
- exhaustiveness
commit_hash: fceddda853fa2543b6d3ddbbe75f7e2468521a91
source_type: github
author: Utkarsh Bahuguna
headline: Check exhaustiveness of unit variant patterns in gccrs
tldr: GCC's Rust front-end now correctly checks pattern matching exhaustiveness for
  enum variants.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Commit `fceddda853fa2543b6d3ddbbe75f7e2468521a91` modifies the pattern
  analysis in `gccrs` (`rust/checks/errors/rust-hir-pattern-analysis.cc`) to correctly
  handle the exhaustiveness checking of enum variants. Previously, patterns that only
  named a subset of an enum's variants were incorrectly considered exhaustive because
  the unit variants were treated as wildcards. The patch implements `lower_pattern`
  to correctly reduce a pattern naming a variant to that specific variant, ensuring
  that only patterns covering all possibilities are deemed exhaustive. This fixes
  issues like Rust-GCC/gccrs#2311…
primer_glossary:
- term: pattern matching
  definition: A mechanism in programming languages that allows checking a value against
    a sequence of patterns to see if it matches. It's often used in control flow structures
    like `match` or `switch` statements.
- term: exhaustiveness checking
  definition: A compile-time check that ensures a pattern matching construct covers
    all possible cases for the input value. If a pattern match is not exhaustive,
    the compiler issues an error, preventing potential runtime bugs.
- term: enum variant
  definition: One of the possible values that an enumeration type can hold. For example,
    in `enum Color { Red, Green, Blue }`, `Red`, `Green`, and `Blue` are variants.
- term: unit variant
  definition: An enum variant that does not carry any associated data. It's essentially
    a named constant within the enum.
- term: gccrs
  definition: The Rust front-end for GCC, enabling the compilation of Rust code using
    the GCC toolchain.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fceddda853fa2543b6d3ddbbe75f7e2468521a91
date: '2026-10-07'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in GCC's Rust front-end (gccrs) where unit variants in patterns were incorrectly treated as wildcards, leading to false positives for exhaustiveness checks. The change lowers path patterns that name a specific enum variant to that variant, ensuring that patterns explicitly listing variants are correctly recognized. This fixes a bug where only some variants of an enum were matched, but the pattern was still considered exhaustive.
