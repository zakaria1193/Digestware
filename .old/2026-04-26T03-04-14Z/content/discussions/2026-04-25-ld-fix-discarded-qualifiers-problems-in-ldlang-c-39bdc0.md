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
discussion_id: 33f90399c05753a483d91cc801953714bb7b83d9.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 3/4] ld: Fix discarded-qualifiers problems in ldlang.c'
headline: 'ld: Fix discarded-qualifiers problems in ldlang.c'
tldr: This patch fixes `-Werror=discarded-qualifiers` warnings in ldlang.c due to
  the new qualifier-preserving `strchr()` in glibc 2.43 and GCC 15.2.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adapts the code to the new `strchr()` behavior, ensuring compatibility with recent
  glibc and GCC versions.
- Maintains code correctness by appropriately handling `const` qualifiers.
exchanges:
- author: Calvin Owens <calvin@wbinvd.org>
  role: proposer
  position: Proposes fixing the discarded-qualifiers errors in `ldlang.c` by adjusting
    the return type of `archive_path()` to const and updating the calling functions.
  quote: 'Because the prior patch refactored input_statement_is_archive_path() to

    take a constant pointer as its second argument, fix this by making the

    return type of archive_path() const, and fixing up its two callers.'
primer_expert: This patch modifies `ldlang.c` within the binutils linker. It's another
  fix related to the new `strchr()` behavior and `const` qualifiers. `ldlang.c` handles
  the language-specific parts of the linker command language, including archive paths
  and wildcard matching.
primer_general: This patch addresses compile errors in the binutils linker (`ld`).  It
  fixes issues caused by the updated `strchr()` function in recent versions of the
  GNU C Library (glibc) and GCC. The patch modifies `ldlang.c`, a file that handles
  the linker's command language, specifically archive paths. The changes ensure that
  the linker code correctly handles string constness, preventing errors during compilation.
series_id: 'binutils:ld: fix discarded-qualifiers problems in ldlang.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/33f90399c05753a483d91cc801953714bb7b83d9.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

Another patch in the series to address `-Werror=discarded-qualifiers` warnings, this one modifies `ldlang.c` in the binutils linker due to changes in the `strchr()` function. The patch modifies the return type of `archive_path()` to `const char *` and updates callers accordingly. This ensures compatibility with the new qualifier-preserving behavior, preventing build errors.
