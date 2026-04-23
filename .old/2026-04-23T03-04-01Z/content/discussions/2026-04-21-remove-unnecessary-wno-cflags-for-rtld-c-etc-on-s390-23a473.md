---
project: glibc
subsystem: s390
patch_id: null
tags:
- glibc
- s390
- CFLAGS
- compiler warnings
- dynamic linking
discussion_id: 20260421125015.3313313-1-stli@linux.ibm.com
source_type: public_inbox
title: '[PATCH] s390: Remove Wno-CFLAGS for rtld.c/dl-load.c/dl-reloc.c'
headline: Remove Unnecessary -Wno-CFLAGS for rtld.c etc. on s390
tldr: This patch removes `-Wno-uninitialized` and `-Wno-unused` CFLAGS from `rtld.c`,
  `dl-load.c`, and `dl-reloc.c` in glibc's s390 build.
stakes: Removing unnecessary compiler flags simplifies the build process and can expose
  potential issues that were previously suppressed.
proposer: Stefan Liebler <stli@linux.ibm.com>
consensus: Ready to Land
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removing the flags can expose previously suppressed warnings, potentially requiring
  code changes.
- Simplifies the build process by removing unnecessary flags.
exchanges:
- author: Stefan Liebler
  role: proposer
  position: Proposes removing the `-Wno-uninitialized` and `-Wno-unused` CFLAGS, arguing
    that they are no longer required.
  quote: 'This patch removes those CFLAGS. If needed, we have to circumvent the issues

    again.  At least I''ve used current GCCs 12.5, 13.4, 14.3, 15.2 and gcc-head

    to successfully build current glibc on s390-64 with -O2, -O3 and -Os without

    such warnings.'
- author: Florian Weimer
  role: reviewer
  position: Acknowledges and asks about the implications of removing the flags.
  quote: null
- author: Stefan Liebler
  role: contributor
  position: Confirms that the flags suppress warnings that maintainers usually want
    to see.
  quote: null
primer_expert: This patch removes `-Wno-uninitialized` and `-Wno-unused` from the
  s390 Makefile for glibc. These flags suppress compiler warnings. Removing them can
  expose previously hidden issues in `rtld.c`, `dl-load.c` and `dl-reloc.c`, which
  are crucial for dynamic linking.  The assumption is that modern GCC versions no
  longer trigger these warnings, or the underlying code has been fixed.
primer_general: This change affects how the GNU C Library (glibc) is compiled for
  IBM System z (s390) systems.  The patch removes specific instructions that tell
  the compiler to ignore certain warnings related to uninitialized variables and unused
  code. By removing these instructions, the compiler will now report these warnings,
  potentially revealing hidden bugs or areas for improvement in the code. These areas
  relate to runtime linking, which is the process of connecting a program to the libraries
  it needs when it is run.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421125015.3313313-1-stli@linux.ibm.com
bugzilla_url: null
date: '2026-04-21'
---

Stefan Liebler proposes removing the `-Wno-uninitialized` and `-Wno-unused` compiler flags from `rtld.c`, `dl-load.c`, and `dl-reloc.c` in the glibc s390 Makefile. These flags were added long ago, potentially for older GCC versions, and may no longer be necessary.  Liebler confirms that current GCC versions build glibc successfully on s390-64 without these flags. Florian Weimer acknowledges the patch. Liebler notes that the flags suppress warnings, which maintainers usually want to see.
