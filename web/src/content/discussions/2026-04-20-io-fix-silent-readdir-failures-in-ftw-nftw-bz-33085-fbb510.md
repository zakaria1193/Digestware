---
project: glibc
subsystem: io
patch_id: null
tags:
- glibc
- io
- ftw
- nftw
- readdir
discussion_id: 20260420174349.3804322-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: '[PATCH v2] io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
headline: 'io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
tldr: Fixes silent failures in ftw/nftw functions when readdir encounters errors,
  ensuring errors are reported instead of being ignored.
stakes: Fixes a bug where file system or I/O errors during directory traversal are
  silently ignored, potentially leading to incomplete or incorrect results.
proposer: Adhemerval Zanella <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding error checking increases code complexity slightly.
- The new test case adds to the overall test suite size.
- Fixing the bug ensures more reliable file tree traversal at the cost of potentially
  surfacing errors that were previously hidden.
exchanges: []
primer_expert: The `ftw` and `nftw` functions in `io/ftw.c` provide file tree traversal
  functionality. The bug arises from the functions treating `readdir` returning NULL
  as end-of-stream, even when `errno` is set. The fix checks `errno` to distinguish
  between end-of-stream and errors. The test case uses FUSE to simulate `getdents`
  failures.
primer_general: The `ftw` (file tree walk) and `nftw` (new file tree walk) functions
  in glibc are used to traverse directory structures. They call `readdir` to read
  directory entries. When an error occurs during directory reading (e.g., due to permission
  issues or I/O errors), `readdir` can return NULL.  This patch fixes a bug where
  these errors were being silently ignored, leading to potentially incomplete or incorrect
  file tree traversals.  FUSE (Filesystem in Userspace) allows userspace programs
  to implement file systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420174349.3804322-1-adhemerval.zanella@linaro.org
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a bug in the `ftw` and `nftw` functions where `readdir` failures were not properly detected, leading to silent errors. The patch modifies `io/ftw.c` to distinguish between the end of a directory stream and actual read errors.  A new test case using FUSE is added to verify the fix.
