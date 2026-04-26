---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- glibc
- GCC
- const
- qualifiers
discussion_id: cover.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 0/4] Fix build errors due to qualifier preserving strchr()'
headline: Fix build errors due to qualifier preserving strchr()
tldr: This patch series fixes build errors in binutils caused by the qualifier-preserving
  behavior of `strchr()` and `strrchr()` in glibc 2.43 and GCC 15.2.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adapts binutils to the new `strchr()` and `strrchr()` behavior, ensuring compatibility
  with recent glibc and GCC versions.
- Maintains code correctness by appropriately handling `const` qualifiers.
exchanges:
- author: Calvin Owens <calvin@wbinvd.org>
  role: proposer
  position: Proposes a series of patches to fix build errors in binutils caused by
    the qualifier-preserving behavior of `strchr()` and `strrchr()`.
  quote: 'Building binutils with glibc 2.43 and GCC 15.2 fails due to the new

    qualifier preserving strchr() and strrchr(), which now return a const

    pointer when passed one as their first argument.'
primer_expert: This patch series addresses issues in binutils arising from the new
  qualifier-preserving behavior of `strchr()` and `strrchr()` in glibc 2.43 and GCC
  15.2. The series touches `gprof` and `ld`, requiring adjustments to pointer types
  and usage.
primer_general: This patch series resolves build errors in binutils, a collection
  of essential tools for software development. These errors stem from changes in how
  the `strchr()` and `strrchr()` functions operate in recent versions of the GNU C
  Library (glibc) and GCC. The patches adapt binutils to correctly handle string constness,
  preventing compilation errors.
series_id: binutils:fix build errors due to qualifier preserving strchr()
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/cover.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

This patch series addresses build errors encountered when compiling binutils with glibc 2.43 and GCC 15.2. The errors are due to changes in the `strchr()` and `strrchr()` functions, which now preserve the `const` qualifier, leading to `-Werror=discarded-qualifiers` warnings. The series includes fixes for `gprof` and `ld`, adapting the code to handle the updated function behavior.
