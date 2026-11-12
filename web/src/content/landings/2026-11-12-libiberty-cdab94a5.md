---
project: gcc
subsystem: libiberty
patch_id: null
tags:
- libiberty
- documentation
- typo
commit_hash: cdab94a53bbe481af689bcc0cd89ea690c4202f3
source_type: github
author: Pietro Monteiro
headline: 'libiberty: Fix documentation typo in strtoll documentation'
tldr: Corrects a documentation typo in libiberty's strtoll function, changing strtoul
  to strtoull.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a documentation error within `libiberty`. Specifically,
  in the documentation comment for `strtoll.c`, the function `strtoul` was erroneously
  mentioned instead of `strtoull`. The fix involves correcting this in `strtoll.c`
  and then regenerating `functions.texi` to reflect the accurate documentation. This
  follows a previous attempt to fix the typo that was reverted during a file regeneration.
primer_glossary:
- term: strtoll
  definition: A C standard library function that converts a string to a `long long`
    integer. It handles different bases and allows for error checking.
- term: strtoul
  definition: A C standard library function that converts a string to an `unsigned
    long` integer.
- term: strtoull
  definition: A C standard library function that converts a string to an `unsigned
    long long` integer.
- term: libiberty
  definition: A collection of utility functions used by GCC and GNU Binutils, providing
    common services like string manipulation and memory allocation.
- term: functions.texi
  definition: A TeXinfo file containing documentation for functions provided by the
    libiberty library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cdab94a53bbe481af689bcc0cd89ea690c4202f3
date: '2026-11-12'
is_stub: true
stub_reason: low_score
---

A documentation typo in `libiberty`'s `strtoll.c` has been corrected. The documentation comment previously referenced `strtoul` where `strtoull` was intended. This commit fixes the typo in the source file and regenerates the corresponding documentation file (`functions.texi`).
