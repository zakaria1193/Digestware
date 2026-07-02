---
project: gcc
subsystem: gcc
patch_id: null
tags:
- warnings
- gcc
- middle-end
- stringop
- array
discussion_id: CAMfHzOvU2soBeBYpUmh1N-su6dcv1xoPA7A55=om0HczhJQHHQ@mail.gmail.com
source_type: public_inbox
title: 'Re: Is it time to take the middle-end stringop/array warnings out of -Wall?'
headline: Take middle-end stringop/array warnings out of -Wall?
tldr: Move middle-end stringop/array warnings out of `-Wall` and into `-Wextra`, adding
  a new `-Wmiddle-end` diagnostic group for finer control.
proposer: Eric Gallager <egall@gwmail.gwu.edu>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Moving warnings to `-Wextra` reduces the number of warnings seen by default, potentially
  hiding real issues from developers who only use `-Wall`.
- Creating a new `-Wmiddle-end` group gives developers more control over which warnings
  are enabled, but requires them to learn about and manage another warning group.
exchanges:
- author: Eric Gallager <egall@gwmail.gwu.edu>
  role: other
  position: Agrees with moving the warnings to `-Wextra` and creating a `-Wmiddle-end`
    group, suggesting a delay before removing them from `-Wextra`.
  quote: I agree with doing steps 1 through 3 listed here; I think that if 4 is to
    be done, it should wait a release until people have had time to adjust to the
    new -Wmiddle-end existing, though.
primer_expert: This concerns the grouping of warnings emitted by GCC's middle-end,
  specifically those related to string and array operations.  These warnings can be
  noisy and may not always indicate genuine errors, leading to debate about their
  inclusion in `-Wall`.
primer_general: Compilers like GCC can emit warnings about potential problems in your
  code.  These warnings can be enabled in groups; `-Wall` is a common group that enables
  many useful warnings. This discussion is about whether certain warnings related
  to string and array operations, which might be overly sensitive, should be moved
  out of the `-Wall` group and into a less frequently used group (`-Wextra`) to reduce
  noise for developers.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/CAMfHzOvU2soBeBYpUmh1N-su6dcv1xoPA7A55=om0HczhJQHHQ@mail.gmail.com
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

Eric Gallager agrees with a proposal to move middle-end stringop/array warnings from `-Wall` to `-Wextra`.  The proposal includes creating a new diagnostic group, `-Wmiddle-end`, for these warnings. Gallager suggests waiting a release cycle before removing them from `-Wextra` to allow users to adjust.
