---
project: glibc
subsystem: posix
patch_id: null
tags:
- glibc
- wordexp
- WRDE_APPEND
- memory leak
- POSIX conformance
discussion_id: 20260422122514.603156-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: '[PATCH] posix: Fix wordexp WRDE_APPEND to preserve state on non-NOSPACE errors
  (BZ 34090, CVE-2026-6368)'
headline: 'posix: Fix wordexp WRDE_APPEND to preserve state on non-NOSPACE errors
  (BZ 34090, CVE-2026-6368)'
tldr: A patch fixes memory leaks and POSIX conformance issues in glibc's wordexp function
  when using WRDE_APPEND.
proposer: Adhemerval Zanella
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses a memory management issue in glibc's `wordexp`
  function, specifically when the `WRDE_APPEND` flag is used. The `WRDE_APPEND` flag
  is used to append the results of word expansion to an existing `wordexp_t` structure.
  The patch ensures correct error handling when reallocations occur within the `w_addword`
  function, preventing memory leaks and use-after-free scenarios. The fix involves
  duplicating the `we_wordv` array to avoid modifying the original array in case of
  errors.
primer_general: The `wordexp` function in glibc performs word expansion, which involves
  parsing a string and splitting it into words, performing expansions such as variable
  substitution and command substitution. The `WRDE_APPEND` flag allows appending the
  results of word expansion to an existing structure. This patch fixes a bug that
  could lead to memory corruption or leaks when using `WRDE_APPEND` and encountering
  errors during the expansion process. Memory leaks occur when a program fails to
  release memory that it has allocated, while use-after-free bugs occur when a program
  tries to access memory that has already been freed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260422122514.603156-1-adhemerval.zanella@linaro.org
bugzilla_url: null
date: '2026-04-22'
---

This patch addresses memory leaks and a POSIX conformance issue in glibc's `wordexp` function when the `WRDE_APPEND` flag is used. The previous implementation incorrectly restored the `wordexp_t` struct on errors, potentially leading to use-after-free and memory leaks. The fix duplicates the `we_wordv` pointer array at entry when `WRDE_APPEND` is set, ensuring that reallocations operate on the copy and preserving the original state. It also fixes error return paths and adds a new test (`tst-wordexp-append.c`) to verify the changes.
