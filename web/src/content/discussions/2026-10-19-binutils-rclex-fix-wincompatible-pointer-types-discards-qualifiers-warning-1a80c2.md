---
project: binutils
subsystem: binutils/rclex
patch_id: null
tags:
- warnings
- glibc
- lexer
- const correctness
discussion_id: 20261019193231.1708375-13-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 12/18] binutils/rclex: fix -Wincompatible-pointer-types-discards-qualifiers
  warning'
headline: 'binutils/rclex: fix -Wincompatible-pointer-types-discards-qualifiers warning'
tldr: Fix pointer type warning in binutils/rclex.c by using a const char pointer.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Ensures correct handling of `const` qualifiers, preventing potential runtime issues
  and satisfying compiler warnings.
- Introduces a minor code change to correctly manage pointer types.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Proposes fixing a pointer type warning in `binutils/rclex.c` by correctly
    handling `const` qualifiers.
  quote: "Building binutils with glibc 2.43 or later gives:\n\n    /home/smarchi/src/binutils-gdb/binutils/rclex.c:218:8:\
    \ warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]\n\
    \nSince glibc 2.43, strchr returns a pointer to const when passed a\npointer to\
    \ const.  The result is assigned to `send`, which needs to stay\nnon-const because\
    \ it is als…"
primer_expert: This patch addresses a compiler warning in `binutils/rclex.c` related
  to pointer type compatibility, specifically `-Wincompatible-pointer-types-discards-qualifiers`.
  The warning occurs because `strchr` in recent glibc versions returns `const char
  *` when operating on `const char *` input. The code assigns this to `char *send`,
  discarding the `const` qualifier. The fix introduces a new `const char *quote` variable
  to hold the result of `strchr`, preserving the `const` qualifier and avoiding the
  warning. The original `send` variable is still used for the non-const operation
  with `strtol`.
primer_glossary:
- term: rclex.c
  definition: A C source file containing a lexer for parsing resource compiler directives.
- term: glibc 2.43
  definition: Version 2.43 of the GNU C Library, a widely used C standard library
    for Linux and other Unix-like systems.
- term: strchr
  definition: A C standard library function that searches for the first occurrence
    of a character within a string.
- term: const char *
  definition: A pointer to a character that cannot be modified through the pointer.
- term: char *
  definition: A pointer to a character that can be modified through the pointer.
- term: -Wincompatible-pointer-types-discards-qualifiers
  definition: A compiler warning flag that flags assignments between pointer types
    where a 'const' qualifier is discarded.
series_id: 'binutils:binutils/rclex: fix -wincompatible-pointer-types-discards-qualifiers
  warning'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-13-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Simon Marchi is addressing a compiler warning in `binutils/rclex.c` related to assigning `const char *` to `char *`. This warning arises because glibc 2.43 onwards makes `strchr` return a `const char *` when given a `const char *`. The patch introduces a new `const char *quote` variable to store the result of `strchr`, preventing the qualifier discard and resolving the warning.
