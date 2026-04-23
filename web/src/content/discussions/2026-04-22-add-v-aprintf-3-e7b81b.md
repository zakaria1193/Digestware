---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- printf
- aprintf
- vaprintf
- dynamic allocation
discussion_id: aekinurc3ld1IA9g@devuan
source_type: public_inbox
title: 'Re: [PATCH 0/3] Add [v]aprintf(3)'
headline: Add [v]aprintf(3)
tldr: A patch series adds `aprintf(3)` and `vaprintf(3)` to glibc, along with tests
  and documentation, and fixes a typo.
stakes: Adding `aprintf` provides a safer and more convenient alternative to `asprintf`,
  reducing the risk of buffer overflows. These new functions improve developer ergonomics.
proposer: Alejandro Colomar <alx@kernel.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding new functions increases the size of the glibc codebase.
- '`aprintf` provides dynamic allocation, which can be more convenient but requires
  careful memory management.'
- The `_chk` variants add additional security checks at the cost of potential performance
  overhead.
exchanges: []
primer_expert: This patch introduces `aprintf` (and its `va_list` variant `vaprintf`)
  to glibc. These functions dynamically allocate a buffer to hold the formatted string,
  similar to `asprintf`, but potentially with additional features or security checks.
  The patch also updates ABI lists and versioning files to reflect the new symbols.
  The `_chk` variants are security-enhanced versions of the functions.
primer_general: Glibc is the standard C library, providing functions that programs
  use for basic operations. `printf` is a function that formats data into a string.  `asprintf`
  is a non-standard glibc extension that creates a string on the heap. This thread
  is about adding `aprintf` to glibc, which is similar to `asprintf` function but
  potentially safer or more featureful.  The patch also includes updates to track
  compatibility (ABI) and versioning.
series_id: glibc:add [v]aprintf(3)
series_role: cover
series_parts:
- title: Add [v]aprintf(3)
  url: https://inbox.sourceware.org/libc-alpha/cover.1776882798.git.alx@kernel.org
  n: 0
  total: 3
- title: Add [v]aprintf(3)
  url: https://inbox.sourceware.org/libc-alpha/4c17f2c584e30390d8a4418f7628e3fed29445f0.1776882798.git.alx@kernel.org
  n: 1
  total: 3
url: https://inbox.sourceware.org/libc-alpha/aekinurc3ld1IA9g@devuan
bugzilla_url: null
date: '2026-04-22'
---

This patch series adds the `aprintf(3)` and `vaprintf(3)` functions to glibc, providing dynamically allocated string formatting. The series includes updated `.abilist` and `Versions` files, new tests for `_chk` implementations, a manual page update, and a fix for a typo in an existing test file. The author indicates that the changes have been tested and are ready for review.
