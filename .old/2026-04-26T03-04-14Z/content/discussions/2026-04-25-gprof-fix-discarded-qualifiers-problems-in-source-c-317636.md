---
project: binutils
subsystem: gprof
patch_id: null
tags:
- binutils
- gprof
- profiling
- glibc
- GCC
discussion_id: 003fed7e07f6f9ed6a8c365e31325162a840fa03.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 1/4] gprof: Fix discarded-qualifiers problems in source.c'
headline: 'gprof: Fix discarded-qualifiers problems in source.c'
tldr: This patch fixes `-Werror=discarded-qualifiers` warnings in gprof's source.c
  due to the new qualifier-preserving `strrchr()` in glibc 2.43 and GCC 15.2.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adapts the code to the new `strrchr()` behavior, ensuring compatibility with recent
  glibc and GCC versions.
- Maintains code correctness by appropriately handling `const` qualifiers.
exchanges:
- author: Calvin Owens <calvin@wbinvd.org>
  role: proposer
  position: Proposes fixing the discarded-qualifiers errors in `source.c` by declaring
    local pointer variables as const.
  quote: 'Fix this and the similar problem immediately below it by declaring the

    local pointer varaibles as const, since they are not modified.'
primer_expert: This patch modifies `gprof/source.c` in the binutils project.  The
  change addresses build errors related to the new qualifier-preserving `strrchr()`
  in glibc 2.43 and GCC 15.2. The file `gprof/source.c` is responsible for source
  code annotation functionality in gprof, a performance analysis tool.
primer_general: This patch resolves a compilation error in the `gprof` tool, which
  is part of the binutils collection. `gprof` helps developers analyze the performance
  of their programs. The error arises from recent updates in the GNU C Library (glibc)
  and GCC that change how the `strrchr()` function (finds the last occurrence of a
  character in a string) handles string constness. The patch updates the `gprof` code
  to correctly handle these changes, allowing it to compile without errors.
series_id: 'binutils:gprof: fix discarded-qualifiers problems in source.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/003fed7e07f6f9ed6a8c365e31325162a840fa03.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

This patch addresses a build error in `gprof/source.c` within the binutils project. The error is a `-Werror=discarded-qualifiers` warning that arises due to the new qualifier-preserving behavior of the `strrchr()` function in glibc 2.43 and GCC 15.2. The patch fixes this by declaring local pointer variables as `const char *` where appropriate, ensuring that the code correctly handles the constness of the returned pointers.
