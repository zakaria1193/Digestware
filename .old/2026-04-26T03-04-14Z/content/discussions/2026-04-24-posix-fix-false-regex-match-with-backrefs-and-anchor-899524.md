---
project: glibc
subsystem: posix
patch_id: null
tags:
- regex
- glibc
- bugfix
- posix
- backreferences
discussion_id: 15e6f619-09b1-4bbe-8daa-98d509066e22@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v2] posix: fix false regex match with backrefs and $ anchor'
headline: 'Posix: Fix false regex match with backrefs and $ anchor'
tldr: Fixes a bug in glibc's regex implementation where the $ anchor is ignored when
  using backreferences.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: ready
sentiment_score: null
technical_tradeoffs:
- Increased complexity in regex engine vs. correctness of regex matching.
- Potential performance impact due to additional checks in regex matching.
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: reviewer
  position: Reviewed and approved the patch.
  quote: 'LGTM, thanks.


    Reviewed-by: Adhemerval Zanella  <adhemerval.zanella@linaro.org>'
primer_expert: This patch addresses a bug in `regexec.c` that caused the `$` anchor
  to be ignored when used with backreferences in regular expressions. The fix involves
  changes to the regex engine to correctly handle the end-of-string anchor in these
  cases.
primer_general: Regular expressions are a powerful tool for pattern matching in text.  The
  `$` anchor is used to match the end of a string.  This patch fixes a bug in glibc's
  regular expression implementation that caused the `$` anchor to be ignored when
  used with backreferences, leading to incorrect matches.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/15e6f619-09b1-4bbe-8daa-98d509066e22@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch fixes an issue in glibc's regular expression matching where the `$` anchor (end-of-string) was being ignored when using backreferences. This could lead to incorrect matches, particularly in tools like `grep`. The fix is based on code from Gnulib. Adhemerval Zanella Netto reviewed and approved the patch.
