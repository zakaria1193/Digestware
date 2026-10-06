---
project: gcc
subsystem: diagnostics
patch_id: null
tags:
- diagnostics
- optimization
commit_hash: b3b1b80477c25b6ed74c2c5d3a54a6d7a15c9a09
source_type: github
author: linden
headline: 'diagnostics: take HTML tag names as const char * in source-printing'
tldr: Optimizes HTML generation in GCC diagnostics by using const char* for tag names,
  avoiding unnecessary string copies.
impact_score: 3
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `diagnostics::to_text` and `diagnostics::to_html` utility functions
  previously took tag and class names by value as `std::string`. Since these were
  always passed as string literals, this resulted in unnecessary string constructions.
  The change modifies the parameters to `const char*`, eliminating the temporary string
  allocations for `to_text` and removing redundant `std::move` calls in `to_html`.
primer_glossary:
- term: const char*
  definition: A pointer to a constant character, commonly used to represent C-style
    strings (null-terminated arrays of characters).
- term: std::string
  definition: A C++ standard library class that manages sequences of characters, providing
    dynamic resizing and various string manipulation functions.
- term: diagnostics
  definition: The component of a compiler responsible for reporting errors, warnings,
    and other informational messages to the user. This includes formatting the output,
    often with source code context.
- term: string literal
  definition: A fixed sequence of characters enclosed in quotes, such as "hello",
    representing a constant string value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3b1b80477c25b6ed74c2c5d3a54a6d7a15c9a09
date: '2026-09-06'
is_stub: true
stub_reason: low_score
---

GCC's diagnostics module now accepts HTML tag and class names as `const char*` instead of `std::string` by value in its source-printing functions. This change avoids creating temporary `std::string` objects when passing string literals, improving performance for the `to_text` path and removing no-op `std::move` calls.
