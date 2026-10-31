---
project: binutils
subsystem: binutils/rclex
patch_id: null
tags:
- warning
- glibc
- rclex
commit_hash: c6f22007f684c55b205ce28b0f842443b66b0262
source_type: public_inbox
author: Simon Marchi <simark@sourceware.org>
headline: 'Binutils rclex: Fix pointer type mismatch warning with newer glibc'
tldr: Fixes a pointer type mismatch warning in rclex.c when using glibc 2.43+.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `binutils/rclex.c` lexer uses `strchr` to find the closing quote
  for string literals. Recent glibc versions (2.43+) change the return type of `strchr`
  to `const char *` when the input is `const char *`. The original code assigned this
  directly to `char *send`, triggering a `-Wincompatible-pointer-types-discards-qualifiers`
  warning. The fix introduces a `const char *quote` to store the result of `strchr`,
  and then uses this `quote` pointer to correctly calculate the length and copy the
  string into the `char *fn` buffer, which is then passed to `strtol`.
primer_glossary:
- term: strchr
  definition: A C standard library function that searches for the first occurrence
    of a character within a string. It returns a pointer to the found character or
    NULL if the character is not present.
- term: const char *
  definition: A pointer to a character that should not be modified through this pointer.
    It signifies that the data being pointed to is read-only via this reference.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261030140329.9D51C4BA9006@sourceware.org
date: '2026-10-30'
is_stub: true
stub_reason: low_score
---

A warning about assigning a `const char*` to a `char*` was introduced in `binutils/rclex.c` with glibc 2.43. This commit resolves the issue by using a separate `const char*` variable to hold the result of `strchr`, preventing the loss of qualifiers when that result is later used for string manipulation and passed to `strtol`. This ensures compatibility with newer glibc versions.
