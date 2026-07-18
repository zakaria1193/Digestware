---
project: gcc
subsystem: diagnostics
patch_id: null
tags:
- diagnostics
- lto
- compiler internals
commit_hash: 613ade639ab886f853f3713b1ef4587fdcebe6d8
source_type: github
author: Lewis Hyatt
headline: Diagnostics interface prepared for LTO pragmas
tldr: Minor changes to diagnostics API support upcoming LTO diagnostic pragmas.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch modifies the diagnostics subsystem to better support LTO's
  integration of diagnostic pragmas. It exposes `option_classifier::classification_change_t`
  publicly, adds a sentinel value to `enum kind` for range reporting, and crucially
  removes the faulty return value from `option_classifier::classify_diagnostic`. The
  latter function's return value was intended to be the previous diagnostic kind,
  but computations were incorrect and unused by callers; its removal simplifies the
  interface and removes unnecessary work, which benefits LTO's processing of potentially
  large numbers of pragmas.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compilation technique where optimization occurs
    at link time rather than during individual compilation units, allowing for inter-procedural
    optimizations across the entire program.
- term: diagnostics
  definition: The component of the compiler responsible for detecting and reporting
    errors, warnings, and other informational messages to the user.
- term: pragma
  definition: A preprocessor directive that provides a way for programmers to supply
    additional information to the compiler, often for version-specific features or
    implementation details. `#pragma GCC diagnostic` controls warning/error behavior.
- term: enum
  definition: Enumeration. A data type consisting of a set of named integer constants.
    Used here to categorize different diagnostic message types.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/613ade639ab886f853f3713b1ef4587fdcebe6d8
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

This commit makes preparatory changes to the GCC diagnostics interface to enable support for `#pragma GCC diagnostic` within the LTO streaming code. It involves making a type name public, adding a range indicator to an enum for LTO's convenience, and removing unused, potentially incorrect logic from a diagnostic classification function. These adjustments facilitate LTO's ability to manage diagnostic settings across compilation units.
