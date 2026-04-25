---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- refactoring
- glibc
discussion_id: 91ef07eb095ae29ba9bc320ca057769231202eae.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 2/4] ld: Refactor input_statement_is_archive_path() to not touch its
  argument'
headline: 'ld: Refactor input_statement_is_archive_path() to not touch its argument'
tldr: This patch refactors `input_statement_is_archive_path()` in ldlang.c to avoid
  modifying its input argument, as preparation for later patches.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Avoids modifying the input argument, improving code safety.
- Introduces a temporary copy, potentially increasing memory usage slightly.
- Prepares the code for upcoming changes related to `const` qualifiers.
exchanges:
- author: Calvin Owens <calvin@wbinvd.org>
  role: proposer
  position: Proposes refactoring `input_statement_is_archive_path()` to avoid modifying
    its input argument as a preparatory step for subsequent patches.
  quote: This is prep work for the next patch, no functional change intended.
primer_expert: This patch modifies `ldlang.c` in the binutils linker, specifically
  the `input_statement_is_archive_path()` function. The refactoring prepares the ground
  for later patches that address issues arising from the new qualifier-preserving
  behavior of `strchr()` in glibc 2.43 and GCC 15.2. `ldlang.c` handles the language-specific
  aspects of the linker command language.
primer_general: This patch prepares the binutils linker (`ld`) for upcoming changes
  related to how strings are handled.  The patch modifies the `input_statement_is_archive_path()`
  function in `ldlang.c`.  It changes the function to avoid directly modifying its
  input string. Instead, it creates a temporary copy, works on the copy, and then
  discards it. This change makes the code more robust and prepares it for future updates
  to string handling in the GNU C Library (glibc) and GCC.
series_id: 'binutils:ld: refactor input_statement_is_archive_path() to not touch its
  argument'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/91ef07eb095ae29ba9bc320ca057769231202eae.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

This patch refactors the `input_statement_is_archive_path()` function in `ldlang.c` within the binutils linker. The goal is to prevent the function from modifying its input argument.  It achieves this by creating a temporary copy of the input string, performing operations on the copy, and then freeing the copy. This change is a preparation step for subsequent patches that address `-Werror=discarded-qualifiers` warnings.
