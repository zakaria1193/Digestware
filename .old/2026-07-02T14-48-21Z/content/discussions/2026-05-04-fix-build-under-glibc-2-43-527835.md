---
project: binutils
subsystem: binutils
patch_id: null
tags:
- build
- glibc
- const
- backport
discussion_id: CAMe9rOqx910Ha3=3rcULpL7iGPqp7CEWi5N6Q+NTCkJDZvt2AA@mail.gmail.com
source_type: public_inbox
title: '[2.46 PATCHES] Fix build under glibc 2.43'
headline: Fix build under glibc 2.43
tldr: H.J. Lu proposes backporting patches to binutils 2.46 to fix build issues with
  glibc 2.43 due to stricter const checking.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Backporting the patches adds complexity to maintaining the 2.46 branch.
- Not backporting the patches means that binutils 2.46 cannot be built with glibc
  2.43.
exchanges: []
primer_expert: This patch series addresses build failures in binutils 2.46 when compiled
  against glibc 2.43. The root cause is stricter enforcement of `const` correctness
  in glibc's headers, specifically the `strrchr` declaration. The patches backport
  fixes for `-Wdiscarded-qualifiers` errors.
primer_general: Binutils, the binary utilities, are a collection of tools used for
  working with binary files, such as executables and object code. Glibc, the GNU C
  Library, provides the standard C library functions used by programs. This series
  of patches fixes a build problem where older versions of binutils fail to compile
  against newer versions of glibc. The problem stems from stricter rules about the
  use of the `const` keyword in the C language, which indicates that a value should
  not be modified.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqx910Ha3=3rcULpL7iGPqp7CEWi5N6Q+NTCkJDZvt2AA@mail.gmail.com
bugzilla_url: null
date: '2026-05-04'
---

H.J. Lu proposes backporting several patches from the master branch to binutils 2.46 to address build failures encountered with glibc 2.43. The failures are due to stricter `const` qualifier checks in glibc's `string.h` when compiling code against the C23 standard. The patches fix `-Wdiscarded-qualifiers` errors in `ldlang.c`, `ld.c`, `binutils`, and `gprof`.
