---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- core-math
- linking
- compatibility
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: Troubleshooting GNU libc 2.27 usage with CORE-MATH test suite
tldr: Paul Zimmermann seeks help using GNU libc 2.27 with the CORE-MATH test suite,
  encountering linking errors related to missing symbols.
stakes: This discussion addresses challenges in using older glibc versions with newer
  compilers, impacting reproducibility and testing of math libraries.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Proposed
outcome: proposed
sentiment_score: 5
sentiment_rationale: User is facing technical difficulties and seeking help.
technical_tradeoffs:
- Compatibility issues between older glibc versions and modern compilers.
- Challenges in setting up the correct environment for testing specific glibc versions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

Paul Zimmermann is trying to use GNU libc 2.27 with the CORE-MATH test suite but faces linking errors due to missing `__isoc23_strtol` and `__isoc23_sscanf` symbols. He has attempted recompiling GMP and MPFR with `-std=c99` but the issue persists.  He seeks assistance in resolving these errors to validate correctly rounded math functions integrated from MathLibm.
