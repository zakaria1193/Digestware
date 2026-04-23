---
project: glibc
subsystem: s390
patch_id: null
tags:
- glibc
- s390
- compiler flags
- Makefile
- warnings
discussion_id: 20260421125015.3313313-1-stli@linux.ibm.com
source_type: public_inbox
title: '[PATCH] s390: Remove Wno-CFLAGS for rtld.c/dl-load.c/dl-reloc.c'
headline: 's390: Remove Wno-CFLAGS for rtld.c/dl-load.c/dl-reloc.c'
tldr: This patch removes specific `-Wno` compiler flags for the s390 architecture
  in glibc, which were likely added for older GCC versions.
stakes: Simplifies the build process and removes potentially unnecessary compiler
  flags, while relying on modern compilers to handle the code correctly.
proposer: Stefan Liebler <stli@linux.ibm.com>
consensus: Proposed
outcome: ready
sentiment_score: 7
sentiment_rationale: The discussion indicates agreement on the removal of the flags,
  suggesting a positive sentiment.
technical_tradeoffs:
- Reduces the complexity of the build system by removing unnecessary flags.
- Relies on modern compilers to correctly handle the code without needing the warning
  suppressions.
- May reintroduce warnings if older compilers are used, or if the underlying code
  has issues that were previously hidden by the flags.
exchanges:
- author: Stefan Liebler <stli@linux.ibm.com>
  role: proposer
  position: Proposes removing the CFLAGS, assuming they are no longer necessary with
    modern GCC versions.
  quote: 'This patch removes those CFLAGS. If needed, we have to circumvent the issues

    again.  At least I''ve used current GCCs 12.5, 13.4, 14.3, 15.2 and gcc-head

    to successfully build current glibc on s390-64 with -O2, -O3 and -Os without

    such warnings.'
- author: Florian Weimer <fweimer@redhat.com>
  role: reviewer
  position: Acknowledges the removal and implies agreement without explicitly stating
    it.
  quote: null
- author: Stefan Liebler <stli@linux.ibm.com>
  role: contributor
  position: Confirms the removal in response to Florian Weimer.
  quote: null
primer_expert: This patch modifies the s390 Makefile in glibc to remove specific `-Wno`
  flags for a few files in the dynamic linker. These flags suppress warnings about
  uninitialized variables and unused code.  They were likely added to deal with issues
  in older GCC versions, potentially related to the inclusion of architecture-specific
  headers like `dl-machine.h`. Modern compilers may no longer require these suppressions,
  and removing them simplifies the build.
primer_general: When compiling software, compilers can generate warnings about potential
  problems in the code, such as using a variable before it has been assigned a value,
  or having parts of the code that never get used. Sometimes, these warnings are spurious
  or unavoidable, and developers use flags to suppress them. This patch removes some
  of these warning-suppression flags for the s390 architecture in glibc. The assumption
  is that modern compilers are better at avoiding these warnings in the first place,
  or that the underlying code has been fixed to avoid the issues that triggered the
  warnings.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421125015.3313313-1-stli@linux.ibm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes `-Wno-uninitialized` and `-Wno-unused` CFLAGS from the s390 Makefile for `rtld.c`, `dl-load.c`, and `dl-reloc.c`. These flags were introduced in 2000, possibly to address warnings from older GCC versions related to `dl-machine.h`. Recent GCC versions (12.5 to gcc-head) build glibc on s390-64 without these warnings, suggesting the flags are no longer needed.
