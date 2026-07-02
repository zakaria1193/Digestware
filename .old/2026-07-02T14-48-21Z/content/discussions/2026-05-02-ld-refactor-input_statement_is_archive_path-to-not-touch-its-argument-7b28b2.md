---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- refactoring
- const correctness
- linker
- code safety
discussion_id: afXK1aC_OSpZlefr@mozart.vkv.me
source_type: public_inbox
title: 'Re: [PATCH 2/4] ld: Refactor input_statement_is_archive_path() to not touch
  its argument'
headline: 'Ld: Refactor input_statement_is_archive_path() to not touch its argument'
tldr: The linker's input_statement_is_archive_path function is refactored to avoid
  modifying its input argument, improving code safety.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Eliminates unnecessary memory allocation.
- Improves code safety by preventing modification of input arguments.
- Increases code clarity and maintainability.
exchanges:
- author: Calvin Owens <calvin@wbinvd.org>
  role: proposer
  position: Acknowledges Alan Modra's modifications and expresses gratitude for applying
    the patch.
  quote: It's very generous of you to credit me, but not necessary :)
primer_expert: The patch refactors `input_statement_is_archive_path` in `ld/ldlang.c`
  to avoid modifying its input. Originally, a copy of `file_spec` was created using
  `stat_strdup` to allow for in-place modification by temporarily null-terminating
  the string. The refactored version avoids this copy by using `const char*` for the
  `sep` argument (the result of `strchr`) and ensuring that `archive_path` also returns
  `const char*`. This change eliminates a potential memory allocation and improves
  const correctness.
primer_general: The `input_statement_is_archive_path` function in the linker checks
  if a given input statement refers to an archive file path. This patch improves the
  function by avoiding modifications to its input, making it safer and more predictable.
  Instead of copying the input string, the function now uses constant pointers (`const
  char*`) to work with the string without altering it. This reduces the risk of unintended
  side effects and memory allocation overhead.
series_id: 'binutils:ld: refactor input_statement_is_archive_path() to not touch its
  argument'
series_role: reply
series_parts:
- title: 'ld: Refactor input_statement_is_archive_path() to not touch its argument'
  url: https://inbox.sourceware.org/binutils/afWwkUQyfAvTUGTw@squeak.grove.modra.org
  n: 2
  total: 4
url: https://inbox.sourceware.org/binutils/afXK1aC_OSpZlefr@mozart.vkv.me
bugzilla_url: null
date: '2026-05-02'
---

This patch refactors the `input_statement_is_archive_path` function in the linker to avoid modifying its input argument `file_spec`. Alan Modra applied a modified version of Calvin Owens' original patch, eliminating an unnecessary copy of the input string. The refactoring involves assigning the result of `strchr` to a `const char*` and ensuring `archive_path` returns a `const char*`.  This prevents unintended side effects and improves the overall safety and maintainability of the code.
