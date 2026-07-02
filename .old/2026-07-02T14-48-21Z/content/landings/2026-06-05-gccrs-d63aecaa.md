---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- testing
- literals
- parser
commit_hash: d63aecaae6cb9c5e96339238b045ba6eb431222d
source_type: github
author: Pierre-Emmanuel Patry
headline: Add a new test for unsuffixed float literals
tldr: GCC Rust gains a new test case explicitly designed to cover unsuffixed float
  literals.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds `float_literals.rs` to the `gcc/testsuite/rust/compile`
  directory. This new test specifically covers the parsing of unsuffixed floating-point
  literals. This is important because a previous change to `utf8_identifiers` narrowed
  its scope, inadvertently removing coverage for these specific float literal forms.
  The new test restores and explicitly ensures correct parsing behavior for such literals
  in the GCC Rust frontend.
primer_general: When you write a number with a decimal point, like `3.14`, in a programming
  language, it's called a 'float literal.' Sometimes, these floats don't have a special
  letter at the end (a 'suffix') to say what kind of float they are (like 'f' for
  single-precision). This change to the GCC Rust compiler adds a new test to make
  sure the compiler correctly understands and processes these 'unsuffixed' float literals.
  This helps ensure that Rust code involving decimal numbers is always correctly interpreted
  by the compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d63aecaae6cb9c5e96339238b045ba6eb431222d
date: '2026-06-05'
is_stub: true
stub_reason: low_score
---

This commit introduces a new test case, `float_literals.rs`, to the GCC Rust test suite. This test specifically targets the parsing and handling of unsuffixed floating-point literals, which were previously no longer covered by an existing, modified test. The addition ensures comprehensive testing for various forms of float notation.
