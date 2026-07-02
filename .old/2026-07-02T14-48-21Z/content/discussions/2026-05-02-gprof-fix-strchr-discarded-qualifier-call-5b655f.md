---
project: binutils
subsystem: gprof
patch_id: null
tags:
- gprof
- strrchr
- const correctness
- profiling
discussion_id: CAMe9rOptBq08_9TMcZE4zdys-LnoQjuhrV0HXvQ_LrnRbCibeA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] gprof: Fix strchr discarded qualifier call'
headline: 'Gprof: Fix strchr discarded qualifier call'
tldr: This patch fixes a discarded qualifier call in gprof by ensuring the result
  of strrchr is stored in a const char *.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures const correctness in gprof, preventing potential issues with string manipulation.
- No significant performance impact.
- Improved code maintainability.
exchanges:
- author: '"H.J. Lu" <hjl.tools@gmail.com>'
  role: proposer
  position: Agrees with the patch and suggests combining it with another patch set
    from Calvin Owens.
  quote: 'We should  combine this strrchr patch set with the patch set from Calvin
    Owens <calvin@wbinvd.org>:


    https://patchwork.sourceware.org/project/binutils/list/?series=60290'
primer_expert: This patch modifies `gprof/source.c` to correct the assignment of the
  return value of `strrchr`. The `strrchr` function, when called on a `const char
  *`, returns a `const char *`. The original code was assigning this value to a non-const
  `char *`, which discards the const qualifier. The patch fixes this by declaring
  `name_only` as `const char *`.  The related patch series mentioned may address similar
  issues or other improvements to gprof.
primer_general: The `strrchr` function finds the last occurrence of a character in
  a string.  `gprof` is a program profiling tool that helps developers understand
  where their program spends its time. This patch ensures that `gprof` correctly handles
  constant strings when using `strrchr`, avoiding potential issues if the program
  attempts to modify a string that should not be changed. The suggestion to combine
  this patch with another indicates possible related work or dependencies between
  the two.
series_id: 'binutils:gprof: fix strchr discarded qualifier call'
series_role: reply
series_parts:
- title: 'gprof: Fix strchr discarded qualifier call'
  url: https://inbox.sourceware.org/binutils/20260502170132.3303884-2-mark@klomp.org
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/CAMe9rOptBq08_9TMcZE4zdys-LnoQjuhrV0HXvQ_LrnRbCibeA@mail.gmail.com
bugzilla_url: null
date: '2026-05-02'
---

This patch addresses an issue in `gprof` where the return value of `strrchr` (which is a `const char *`) was being assigned to a non-const `char *`. The patch modifies `gprof/source.c` to ensure const correctness in the `annotate_source` function. H.J. Lu suggests combining this patch with another related patch set from Calvin Owens.
