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
discussion_id: ae04fe83-569f-4eb8-9ff2-a25c481d32a9@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
headline: 'io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
tldr: The patch fixing silent readdir failures in ftw/nftw (BZ 33085) needs a memory
  leak fix, other nits.
stakes: Memory leaks could cause the application to crash or use more memory leading
  to performance degradation.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The fix prevents a memory leak, but it adds complexity to the error handling path.
- The memory leak could mask underlying I/O errors in some cases but is now fixed.
exchanges:
- author: Adhemerval Zanella Netto
  role: proposer
  position: Presents a patch to fix silent readdir failures in ftw/nftw.
  quote: null
- author: DJ Delorie
  role: reviewer
  position: Points out a missing free(buf) call in open_dir_stream, which is a memory
    leak.
  quote: Need to free(buf) here.
- author: Adhemerval Zanella Netto
  role: proposer
  position: Acknowledges the missing free(buf) and the typos.
  quote: 'Good catch.


    Ack.'
primer_expert: This concerns the fix for BZ 33085, which addresses silent errors during
  directory traversal in `ftw` and `nftw`. The patch involves changes to `io/ftw.c`
  and adds a test case `io/tst-ftw-bz33085.c`. The review identifies a missing `free(buf)`
  call in `open_dir_stream`, leading to a memory leak when `readdir` fails.
primer_general: '`ftw` and `nftw` are functions in glibc used to walk through file
  system directory trees. This patch addresses a bug where errors during the directory
  reading process (`readdir`) were being silently ignored. The reviewer found a memory
  leak, where allocated memory was not being freed when an error occurred.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/ae04fe83-569f-4eb8-9ff2-a25c481d32a9@linaro.org
bugzilla_url: null
date: '2026-04-20'
---

DJ Delorie reviewed the patch and found a missing `free(buf)` call in `open_dir_stream` which is a memory leak. Adhemerval agrees with the missing free and also acknowledges the typo fixes.
