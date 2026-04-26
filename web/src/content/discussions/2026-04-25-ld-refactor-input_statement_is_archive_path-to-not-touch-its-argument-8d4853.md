---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- refactoring
- const correctness
discussion_id: 91ef07eb095ae29ba9bc320ca057769231202eae.1777074100.git.calvin@wbinvd.org
source_type: public_inbox
title: '[PATCH 2/4] ld: Refactor input_statement_is_archive_path() to not touch its
  argument'
headline: 'ld: Refactor input_statement_is_archive_path() to not touch its argument'
tldr: Refactors input_statement_is_archive_path() in ldlang.c to avoid modifying its
  input argument, preparing for const-correctness fixes.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Slightly increased memory usage due to string duplication.
- Improved code clarity and const-correctness.
exchanges: []
primer_expert: This patch refactors `input_statement_is_archive_path` in `ldlang.c`
  to take a `const char*` instead of `char*` as input, and duplicates the string locally
  before modification. This is in preparation for dealing with `strchr`'s new const-correctness.
  `ldlang.c` contains the ld linker's input language parsing.
primer_general: This patch modifies the binutils linker (`ld`) to prepare for changes
  in how the C standard library handles constant strings. Specifically, the `input_statement_is_archive_path`
  function is refactored to avoid modifying its input. This change is a necessary
  step to ensure the linker remains compatible with newer versions of the C standard
  library and avoids potential build errors.
series_id: 'binutils:ld: refactor input_statement_is_archive_path() to not touch its
  argument'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/91ef07eb095ae29ba9bc320ca057769231202eae.1777074100.git.calvin@wbinvd.org
bugzilla_url: null
date: '2026-04-25'
---

This patch refactors the `input_statement_is_archive_path()` function in `ld/ldlang.c` to avoid modifying its input argument.  This is a preparatory step for subsequent patches that address `const` qualifier issues related to glibc 2.43's `strchr()` changes. The refactoring ensures that the function does not alter the input string, which is important for maintaining const-correctness.
