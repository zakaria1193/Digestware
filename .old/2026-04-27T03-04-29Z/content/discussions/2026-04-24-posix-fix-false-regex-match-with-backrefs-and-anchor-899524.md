---
project: glibc
subsystem: posix
patch_id: null
tags:
- glibc
- regex
- posix
- bugfix
- backreferences
discussion_id: 15e6f619-09b1-4bbe-8daa-98d509066e22@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v2] posix: fix false regex match with backrefs and $ anchor'
headline: 'posix: fix false regex match with backrefs and $ anchor'
tldr: Fixes a bug in glibc's regex matching where the $ anchor was ignored with backreferences,
  causing false matches.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Ready to Land
outcome: ready
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Collin Funk
  role: proposer
  position: Proposes a fix for a bug where the $ anchor is ignored in regex matching
    with backreferences.
  quote: "This fixes the $ anchor being ignored in the following grep command:\n\n\
    \    $ grep -E '^(.?)(.?).?\\2\\1$' <<< ab\n    ab\n\nHowever, the regular expression\
    \ should only match palindromes."
- author: Adhemerval Zanella Netto
  role: reviewer
  position: Reviewed the patch and gave it a LGTM.
  quote: LGTM, thanks.
primer_expert: This patch addresses a bug in `regexec.c`, the glibc implementation
  of regular expression matching (part of the POSIX regex API). The bug involves incorrect
  handling of the `$` anchor in conjunction with backreferences, leading to false
  positives.  This affects any application using glibc's regex functions and relying
  on the correct behavior of anchors and backreferences.
primer_general: Regular expressions are patterns used to match text.  In glibc, the
  standard C library, the `regexec` function implements this matching. The `$` anchor
  in a regular expression means "end of line". A backreference lets you reuse a previously
  matched part of the text. This patch fixes a bug where the `$` anchor was being
  ignored when combined with backreferences, leading to incorrect results when programs
  use regular expressions to search for patterns in text.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/15e6f619-09b1-4bbe-8daa-98d509066e22@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch fixes a bug in glibc's regular expression matching implementation where the `$` anchor was ignored when used with backreferences, leading to incorrect matches.  The fix is largely based on code from Gnulib and addresses a bug reported in GNU sed. This issue could cause programs using regular expressions with backreferences and the `$` anchor to behave unexpectedly.
