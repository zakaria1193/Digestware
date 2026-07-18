---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- lto
- testsuite
- testing
commit_hash: 8d1f9ea822060a4e77238a33d2eb6ef99991c3d1
source_type: github
author: Lewis Hyatt
headline: Testsuite adds option to augment LTO test configurations
tldr: New `dg-lto-additional-options` directive simplifies adding options to LTO test
  configurations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The LTO test framework's `lib/lto.exp` now handles the `dg-lto-additional-options`
  directive. This allows test writers to append arbitrary flags to the standard set
  of LTO test options, rather than completely replacing them as `dg-lto-options` does.
  This is particularly useful for testing specific diagnostic behaviors with LTO,
  as it preserves the comprehensive default LTO test options while adding targeted
  flags.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compilation technique where optimization occurs
    at link time rather than during individual compilation units, allowing for inter-procedural
    optimizations across the entire program.
- term: testsuite
  definition: A collection of automated tests designed to verify the correctness of
    the compiler's behavior across various features, targets, and optimization levels.
- term: directive
  definition: A special command or instruction within a test case file that controls
    how the test runner executes or interprets the test.
- term: -Wall
  definition: A common compiler flag that enables a wide range of useful, but not
    necessarily critical, warning messages.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8d1f9ea822060a4e77238a33d2eb6ef99991c3d1
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

A new testsuite directive, `dg-lto-additional-options`, has been introduced to simplify the process of adding specific compiler flags to existing LTO test configurations. Previously, overriding options with `dg-lto-options` removed default configurations, making it cumbersome to add flags like `-Wall`. This new directive allows augmenting the default set of options, proving useful for testing features like LTO diagnostic pragmas.
