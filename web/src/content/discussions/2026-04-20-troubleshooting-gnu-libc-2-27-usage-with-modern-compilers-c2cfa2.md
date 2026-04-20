---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- compatibility
- linking
- gcc
- sysroot
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: Troubleshooting GNU libc 2.27 usage with modern compilers
tldr: User experiences linking errors when trying to use glibc 2.27 with a modern
  compiler due to missing `__isoc23_strtol` symbol.
stakes: Demonstrates challenges in using older glibc versions with newer compilers,
  potentially affecting reproducibility and testing.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using `--sysroot` might require significant changes to the build environment.
- Older glibc versions may lack security fixes and performance improvements.
- Mixing glibc versions can lead to unexpected behavior.
primer_expert: This thread discusses compatibility issues when using an older glibc
  (2.27) with a newer compiler. The core issue is the presence of `__isoc23_strtol`,
  a symbol introduced in a later glibc version.  The discussion suggests using `--sysroot`
  to ensure consistent header and library versions during compilation of dependent
  libraries (GMP, MPFR).
primer_general: The GNU C Library (glibc) is the standard C library for Linux systems.
  Different glibc versions introduce new features and symbols. When using an older
  glibc version with a newer compiler, compatibility issues can arise due to missing
  symbols or ABI differences. This thread highlights such an issue and explores potential
  solutions, as the standard library might be used by multiple components of the toolchain.
  The suggested solution involves using `--sysroot` option which specifies the location
  of the system root directory to be used during compilation, which is a way of ensuring
  correct header and library lookup paths.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

A user is encountering linking errors when trying to use GNU libc 2.27 with a modern compiler (gcc 15.2.0). The issue arises from missing `__isoc23_strtol` symbol, which is part of the newer C standard. The user tried recompiling GMP and MPFR with `-std=c99` but still faces issues. The thread discusses potential solutions involving sysroot configuration.
