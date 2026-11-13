---
project: gcc
subsystem: pretty-print.cc
patch_id: null
tags:
- gcc
- compiler
- warning
commit_hash: ad442499bbe27caafb81323681dfee3ac449b70d
source_type: github
author: Oleg Tolmatcev
headline: Fix -Wcast-qual warning in pretty-print.cc by making delim const
tldr: Resolves a compiler warning in `pretty-print.cc` by correctly marking a character
  pointer as constant, as it's only read.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses a `-Wcast-qual` warning in `gcc/pretty-print.cc`
  within the `eat_esc_sequence` function. The function uses `memchr` on a buffer that
  is correctly treated as `const`. However, the result of `memchr` was cast to a `char
  *` and assigned to the `delim` parameter, which was not declared `const`. This commit
  rectifies this by declaring `delim` as `const char *`, aligning the type with its
  usage and silencing the warning, as `delim` is only ever read from, never written
  to.
primer_glossary:
- term: -Wcast-qual
  definition: A GCC compiler warning flag that detects incorrect casts involving qualifiers
    like `const` and `volatile`. It helps ensure type safety by flagging potentially
    dangerous or erroneous type conversions.
- term: memchr
  definition: A C standard library function that searches for the first occurrence
    of a specified character within a block of memory. It returns a pointer to the
    first occurrence of the character, or NULL if the character is not found.
- term: const
  definition: A type qualifier in C and C++ that indicates a variable or object cannot
    be modified after initialization. Using `const` helps prevent accidental modifications
    and can enable compiler optimizations.
- term: pretty-print.cc
  definition: A source file within the GCC compiler that contains code responsible
    for formatting and displaying code or compiler internal structures in a human-readable
    way.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ad442499bbe27caafb81323681dfee3ac449b70d
date: '2026-11-12'
is_stub: true
stub_reason: low_score
---

This commit fixes a `-Wcast-qual` compiler warning in GCC's `pretty-print.cc` file. The function `eat_esc_sequence` was casting the result of `memchr` on a constant buffer to a non-const `char *`. By changing the `delim` parameter to `const char *`, the code now correctly reflects that the buffer is only being read, eliminating the warning.
