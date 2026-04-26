---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- glibc
- GCC
discussion_id: 3197a710e4b6bd87166a0dde13812259d09b452f.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 4/4] ld: Fix discarded-qualifiers problems in ldelf.c'
headline: 'ld: Fix discarded-qualifiers problems in ldelf.c'
tldr: This patch fixes `-Werror=discarded-qualifiers` warnings in ldelf.c due to the
  new qualifier-preserving `strrchr()` in glibc 2.43 and GCC 15.2.
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
  position: Proposes fixing the discarded-qualifiers errors in `ldelf.c` by adjusting
    pointer types and usage with `strrchr()`.
  quote: 'Fix this by passing the obviously equal non-const pointer to strrchr(),

    instead of the const one.


    Fix this by declaring the local pointer varaible as const, since it is

    not modified.'
primer_expert: This patch modifies `ldelf.c` in the binutils linker. The changes are
  necessary to accommodate the new qualifier-preserving behavior of `strrchr()` introduced
  in glibc 2.43 and GCC 15.2. The linker uses `ldelf.c` to handle ELF (Executable
  and Linkable Format) specific operations, including searching for needed libraries
  and parsing configuration files.
primer_general: The binutils project provides essential tools for software development,
  including the linker (`ld`). The linker combines compiled code and libraries to
  create executable programs. This patch addresses compile errors arising from changes
  in how the `strrchr()` function (finds the last occurrence of a character in a string)
  is defined in recent versions of the GNU C Library (glibc) and GCC. Specifically,
  the patch adapts the linker's code to correctly handle `const` qualifiers, which
  indicate whether a string can be modified.
series_id: 'binutils:ld: fix discarded-qualifiers problems in ldelf.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/3197a710e4b6bd87166a0dde13812259d09b452f.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

This patch addresses compilation errors in `ldelf.c` within the binutils linker (`ld`) caused by the updated `strrchr()` function in glibc 2.43 and GCC 15.2.  The updated `strrchr()` preserves the `const` qualifier, leading to `-Werror=discarded-qualifiers` warnings when assigning the result to a non-const pointer. The patch adapts the code to handle the constness correctly, resolving the build errors.
