---
project: glibc
subsystem: io
patch_id: null
tags:
- glibc
- io
- ftw
- nftw
- error handling
discussion_id: ae04fe83-569f-4eb8-9ff2-a25c481d32a9@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
headline: 'io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
tldr: A patch fixing silent readdir failures in ftw/nftw is undergoing review with
  minor feedback.
stakes: Fixing silent failures improves program reliability and debugging experience.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding error checks increases code complexity slightly.
- Correcting the error handling improves reliability at the cost of potentially surfacing
  errors that were previously hidden.
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: proposer
  position: Submitted a patch to fix silent readdir failures in ftw/nftw.
  quote: null
- author: DJ Delorie
  role: reviewer
  position: Identified missing `free()` calls and typos in the patch.
  quote: Need to free(buf) here.
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: proposer
  position: Acknowledged the missing `free()` call and typos, clarifying that another
    identified issue is not a real problem.
  quote: null
primer_expert: The `ftw` and `nftw` functions in `io/ftw.c` recursively traverse directory
  trees, calling a user-supplied function for each entry.  These functions use `readdir64`
  internally, and this patch ensures that errors from `readdir64` are correctly propagated,
  preventing silent failures. A general toolchain dev should know that `ftw` is POSIX,
  but might not know about its error handling nuances.
primer_general: '`ftw` and `nftw` are POSIX functions that traverse a directory tree,
  applying a user-defined function to each file and directory. They are used to perform
  operations on entire directory structures.  This patch fixes a bug where errors
  during directory reading (`readdir`) were not being correctly reported by `ftw`
  and `nftw`. This could lead to programs silently failing to process files, making
  debugging difficult. The fix involves adding checks for errors returned by `readdir`
  and ensuring these errors are propagated to the caller.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/ae04fe83-569f-4eb8-9ff2-a25c481d32a9@linaro.org
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a bug in the ftw and nftw functions where readdir failures were not properly handled, leading to silent errors. The patch adds error checking to the readdir calls within these functions. Reviewers have identified minor issues such as missing `free()` calls and typos.
