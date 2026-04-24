---
project: glibc
subsystem: posix
patch_id: null
tags:
- security
- use-after-free
- wordexp
- posix
- memory management
discussion_id: 20260422122514.603156-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: '[PATCH] posix: Fix wordexp WRDE_APPEND to preserve state on non-NOSPACE errors
  (BZ 34090, CVE-2026-6368)'
headline: 'Posix: Fix wordexp WRDE_APPEND to preserve state on non-NOSPACE errors
  (BZ 34090, CVE-2026-6368)'
tldr: A use-after-free vulnerability and POSIX conformance issue in `wordexp` with
  `WRDE_APPEND` flag are fixed by duplicating the `we_wordv` array at entry.
proposer: Adhemerval Zanella <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Duplicating the `we_wordv` array increases memory usage.
- The new test increases the size of the test suite.
- The fix adds complexity to the error handling logic.
exchanges: []
primer_expert: This patch addresses a bug in `wordexp` related to the `WRDE_APPEND`
  flag and memory management of the `we_wordv` array.  Incorrect error handling could
  lead to use-after-free. The fix involves duplicating the array, affecting memory
  usage and requiring careful management of allocated resources.
primer_general: '`wordexp` is a function used for word expansion, similar to what
  a shell does. When you use the `WRDE_APPEND` flag, you''re asking `wordexp` to add
  the newly expanded words to an existing list. This patch fixes a bug where, if an
  error occurred, the function could try to use memory that had already been freed,
  leading to unpredictable behavior. The patch also ensures compliance with the POSIX
  standard, a set of standards for operating systems.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260422122514.603156-1-adhemerval.zanella@linaro.org
bugzilla_url: null
date: '2026-04-22'
---

A use-after-free vulnerability (CVE-2026-6368) and a POSIX conformance issue exist in the `wordexp` function when using the `WRDE_APPEND` flag.  The previous implementation incorrectly restored the `wordexp_t` struct on error, potentially leading to a use-after-free in the caller. The patch fixes this by duplicating the `we_wordv` pointer array at entry when `WRDE_APPEND` is set.  A new test, `tst-wordexp-append.c`, is added to verify the fix and ensure POSIX compliance.
