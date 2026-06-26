---
project: gcc
subsystem: gccrs/testsuite
patch_id: null
tags:
- rust
- gccrs
- testsuite
- refactoring
commit_hash: fdb375f5f3d798d83fd6186dd660cbbbd2e2efae
source_type: github
author: Owen Avery
headline: Move a test into compile/macros/mbe
tldr: A Rust compiler test for macro attributes has been relocated to the correct
  'macros by example' test directory.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit is a minor reorganization of the `gccrs` testsuite. The
  test `rust/compile/attr-macro.rs`, which focuses on Rust macro attributes, has been
  logically relocated to `rust/compile/macros/mbe/macro_attr_expr.rs`. This places
  it among other tests related to 'macros by example' (MBE), which is the underlying
  mechanism for Rust's declarative macros. This improves the internal consistency
  and navigability of the testsuite structure.
primer_general: Software projects, especially compilers, have many tests to ensure
  they work correctly. These tests are usually organized into folders based on what
  part of the compiler they are testing. This update simply moves one specific Rust
  compiler test, which checks how attributes on macros work, from a general 'compile'
  folder into a more specific folder dedicated to 'macros by example.' This tidies
  up the test suite, making it easier for developers to find and manage related tests.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fdb375f5f3d798d83fd6186dd660cbbbd2e2efae
date: '2026-06-23'
is_stub: true
stub_reason: low_score
---

A specific GCC Rust compiler test, `attr-macro.rs`, which focuses on macro attributes, has been moved to a more appropriate location within the testsuite. The test is now situated in `rust/compile/macros/mbe/macro_attr_expr.rs`, aligning it with other tests related to 'macros by example.' This change is purely organizational and improves the structure of the Rust testsuite.
