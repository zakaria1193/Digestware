---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- bootstrap
- build failure
- Werror
- uninitialized variable
discussion_id: CAOPLpQepw3jVJ3S2jYY=yOje4BXp3xOa9mKsWKVQe9NZRCnkWg@mail.gmail.com
source_type: public_inbox
title: stage2 build failure
headline: Stage2 build failure due to uninitialized variable
tldr: GCC trunk fails to bootstrap due to a maybe-uninitialized variable warning being
  treated as an error in stage2.
proposer: Ulrich Drepper <drepper@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Sam James <sam@gentoo.org>
  role: other
  position: Implied agreement/acknowledgment that the issue exists.
  quote: null
primer_expert: This indicates a regression in the GCC trunk.  The `-Werror` flag promotes
  warnings to errors, which is commonly used in build systems to ensure code quality.
  The specific error involves `tree-vect-stmts.cc`, which is part of the tree-vectorization
  pass in GCC's middle-end.
primer_general: When building a compiler like GCC, it's common to use a multi-stage
  process (bootstrap) where the compiler compiles itself. This report indicates a
  failure during the second stage of this process. The failure is caused by a warning
  (about a potentially uninitialized variable) being treated as a fatal error.  This
  usually indicates a recent change in the code introduced the problem.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAOPLpQepw3jVJ3S2jYY=yOje4BXp3xOa9mKsWKVQe9NZRCnkWg@mail.gmail.com
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

Ulrich Drepper reports that the GCC trunk fails to bootstrap in stage2 due to a `-Werror=maybe-uninitialized` error. The error occurs in `tree-vect-stmts.cc` where the variable `stride_step` may be used uninitialized. He asks if he should file a bug report.
