---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- compatibility
- CORE-MATH
- MPFR
- GMP
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: Problems using GNU libc 2.27 with CORE-MATH test suite
tldr: Paul Zimmermann reports issues using glibc 2.27 with the CORE-MATH test suite
  due to missing `__isoc23_strtol` reference, even after recompiling GMP and MPFR.
stakes: Building software against older glibc versions can be challenging due to compatibility
  issues; understanding these issues is crucial for maintaining legacy systems or
  ensuring reproducible builds.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Proposed
outcome: proposed
sentiment_score: 5
sentiment_rationale: A question about a technical problem.
technical_tradeoffs: []
primer: The GNU C Library (glibc) is the standard C library for GNU systems.  The
  CORE-MATH test suite likely checks the correctness of math functions in glibc.  Linking
  against older glibc versions while using newer compilers can lead to compatibility
  problems due to changes in symbol versions and dependencies.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

Paul Zimmermann is trying to use GNU libc 2.27 with the CORE-MATH test suite. He encounters an "undefined reference to `__isoc23_strtol`" error, which persists even after recompiling GMP and MPFR with `-std=c99`. He seeks advice on resolving this issue to check math functions integrated from MathLibm.
