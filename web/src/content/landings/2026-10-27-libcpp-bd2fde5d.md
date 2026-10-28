---
project: gcc
subsystem: libcpp
patch_id: null
tags:
- libcpp
- lexer
- c++
commit_hash: bd2fde5d72893f4c1310b08a035b30ff0d8a4500
source_type: github
author: Wilco Dijkstra
headline: 'libcpp: Use ULL for 64-bit immediates'
tldr: Uses ULL suffix for 64-bit integer literals in libcpp for clarity.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `libcpp/lex.cc`, the constants used in `search_line_neon` and `search_line_fast`
  have been updated from `UL` to `ULL` suffixes for 64-bit immediate values. This
  change improves clarity and ensures correct type promotion for 64-bit unsigned integers,
  regardless of whether `unsigned long` is 32 or 64 bits on the target platform. This
  is a minor correctness and maintainability improvement within the preprocessor's
  lexical analysis.
primer_glossary:
- term: libcpp
  definition: The C++ standard library implementation used by Clang, also known as
    libc++. This commit, however, refers to the C preprocessor (cpplib) component
    within GCC.
- term: ULL
  definition: A C/C++ integer literal suffix indicating an unsigned long long integer.
    This type is guaranteed to be at least 64 bits wide.
- term: UL
  definition: A C/C++ integer literal suffix indicating an unsigned long integer.
    The size of `unsigned long` is platform-dependent, typically 32 or 64 bits.
- term: lexer
  definition: A component of a compiler or preprocessor that performs lexical analysis,
    breaking source code into a stream of tokens.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bd2fde5d72893f4c1310b08a035b30ff0d8a4500
date: '2026-10-27'
is_stub: true
stub_reason: low_score
---

This change updates `libcpp`'s lexer to use the `ULL` suffix for 64-bit unsigned integer literals. While existing promotion rules handle these correctly even with `UL` on 32-bit systems, using `ULL` explicitly improves code clarity and robustness. The update affects `search_line_neon` and `search_line_fast` within `lex.cc`.
