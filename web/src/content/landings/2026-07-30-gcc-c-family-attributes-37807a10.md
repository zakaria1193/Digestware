---
project: gcc
subsystem: gcc/c-family/attributes
patch_id: null
tags:
- attributes
- diagnostics
- c-family
- gcc
commit_hash: 37807a10d8816f650d38d6f59a4e230ddc9f785a
source_type: github
author: Josef Melcr
headline: Use positional_argument in callback_only attribute handler
tldr: Unified attribute diagnostics by using positional_argument and downgrading errors
  to warnings.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `handle_callback_only_attribute` function previously performed
  manual error reporting. By integrating calls to `positional_argument`, it now leverages
  that utility's bounds-checking and warning/error reporting mechanisms. The explicit
  choice to downgrade errors to warnings aligns the attribute's diagnostics with a
  common standard within the compiler, improving user experience.
primer_glossary:
- term: callback_only attribute
  definition: A function attribute that, when applied, can enforce specific constraints
    on how a function is called, often related to its arguments or execution context.
- term: positional_argument
  definition: A GCC utility function used for parsing and validating function arguments
    based on their position, often issuing warnings or errors for incorrect usage.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/37807a10d8816f650d38d6f59a4e230ddc9f785a
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

The handler for the `callback_only` attribute in GCC's C-family frontends has been updated to use the `positional_argument` utility for bounds checking. This change harmonizes diagnostic reporting by downgrading attribute errors to warnings, aligning them with the behavior of `positional_argument` and improving diagnostic consistency for attribute usage.
