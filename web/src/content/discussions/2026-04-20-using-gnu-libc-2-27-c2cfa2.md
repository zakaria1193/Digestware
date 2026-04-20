---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- compatibility
- core-math
- testing
- linking
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: Using GNU libc 2.27
tldr: User seeks advice on using GNU libc 2.27 with the CORE-MATH test suite and modern
  compilers, encountering linking issues with `__isoc23_strtol`.
stakes: This discussion addresses the challenges of testing older glibc versions with
  modern toolchains, which is crucial for maintaining compatibility and verifying
  the correctness of math functions.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using older glibc versions may require manual configuration and workarounds to ensure
  compatibility with modern compilers.
- May need to adjust compiler flags and include paths to resolve symbol versioning
  issues.
- Testing with older glibc versions can help identify and prevent regressions introduced
  by newer toolchains.
primer: The GNU C Library (glibc) provides standard functions used by programs on
  Linux systems. The CORE-MATH test suite validates the correctness of mathematical
  functions within glibc. Testing older glibc versions with newer compilers can expose
  compatibility issues due to changes in standards, symbol versions, and system headers.
  The `__isoc23_strtol` symbol relates to the ISO C23 standard's string conversion
  functions, which may not be present or compatible in older glibc releases.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

Paul Zimmermann is trying to use GNU libc 2.27 with the CORE-MATH test suite but is encountering issues related to the `__isoc23_strtol` symbol when linking with modern compilers (gcc 15.2.0). He seeks advice on how to resolve these linking errors and successfully test the math functions. The thread includes suggestions about compiler flags, sysroot configuration, and manual fixes for include paths to ensure compatibility between the older glibc and the newer toolchain.
