---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- memory allocation
- strdup
- xstrdup
discussion_id: ab2b7941-e67a-41ea-8cac-5e5cb72fb197@suse.com
source_type: public_inbox
title: '[PATCH 11/19] RISC-V: avoid strdup()'
headline: 'Risc-V: Avoid strdup()'
tldr: Replaces `strdup()` with `xstrdup()` for more consistent memory allocation error
  handling in RISC-V code.
stakes: Improved code robustness by using a consistent memory allocation scheme, potentially
  preventing crashes due to memory allocation failures.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- No functional change, assuming xstrdup behaves as expected.
- Improved robustness in the face of OOM conditions.
exchanges: []
primer_expert: '`strdup` is a standard C library function for duplicating strings.
  `xstrdup` is a custom function (likely provided by binutils) that behaves similarly
  but provides consistent error handling, such as exiting the program if memory allocation
  fails. This patch replaces `strdup` with `xstrdup` in the RISC-V assembler and linker
  code to ensure consistent memory allocation error handling.'
primer_general: '`strdup` is a C function that duplicates a string by allocating memory
  and copying the string into the allocated memory. This patch replaces `strdup` with
  a safer alternative (`xstrdup`) that handles memory allocation errors more consistently,
  leading to a more stable toolchain.'
series_id: 'binutils:risc-v: avoid strdup()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ab2b7941-e67a-41ea-8cac-5e5cb72fb197@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch replaces instances of `strdup()` with `xstrdup()` in the RISC-V related code. `xstrdup()` is a variant that ensures consistent error handling when memory allocation fails, which can improve the robustness of the code.
