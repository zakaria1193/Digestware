---
project: glibc
subsystem: io
patch_id: null
tags:
- glibc
- ftw
- nftw
- readdir
- bug fix
discussion_id: ae04fe83-569f-4eb8-9ff2-a25c481d32a9@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
headline: 'io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
tldr: The patch to fix silent readdir failures in ftw/nftw has some minor typo and
  memory leak issues, which are being addressed.
stakes: This patch fixes a bug that can cause programs using ftw/nftw to silently
  fail, which can lead to unexpected behavior and data loss.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The patch adds additional error checking to the readdir operation.
- The patch includes a new test case to verify the fix.
- The patch ensures that memory is properly freed in the error path.
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: proposer
  position: Submitted a patch to fix silent readdir failures in ftw/nftw.
  quote: null
- author: DJ Delorie
  role: reviewer
  position: Identified a potential memory leak in the error handling path of the patch,
    as well as some typos in the test case.
  quote: Need to free(buf) here.
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: proposer
  position: Acknowledged the memory leak and typos, clarifying one point about the
    cleanup state.
  quote: Good catch.
primer_expert: The ftw and nftw functions provide a way to traverse a directory tree.
  This patch addresses a failure to properly handle errors during the readdir operation.
  Specifically, the patch ensures that errno is checked after readdir and that memory
  is properly freed in the error path. The patch also includes a test case to verify
  the fix.
primer_general: The ftw() and nftw() functions in glibc provide a way to walk a directory
  tree, applying a function to each file and directory found. This is similar to the
  `find` command in a shell. This patch fixes a bug where errors during directory
  reading (readdir) were not being properly handled, which could lead to the program
  silently failing to process some files or directories. The fix ensures that errors
  are checked and resources are cleaned up correctly, preventing unexpected behavior.
  The patch includes a test case to confirm that the fix works as expected.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/ae04fe83-569f-4eb8-9ff2-a25c481d32a9@linaro.org
bugzilla_url: null
date: '2026-04-20'
---

DJ Delorie found a memory leak in the error handling path and some typos in the test case. Adhemerval Zanella Netto confirmed the memory leak and typos and indicated they would be addressed.
