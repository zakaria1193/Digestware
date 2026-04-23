---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- memory management
- error handling
discussion_id: ab2b7941-e67a-41ea-8cac-5e5cb72fb197@suse.com
source_type: public_inbox
title: '[PATCH 11/19] RISC-V: avoid strdup()'
headline: 'Risc-V: Avoid strdup()'
tldr: Replaces `strdup()` with `xstrdup()` in RISC-V code for consistent memory allocation
  and error handling.
stakes: Ensures consistent memory allocation practices and leverages existing error
  handling mechanisms.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Consistent memory allocation and error handling.
- No performance impact.
exchanges: []
primer_expert: The RISC-V backend in binutils uses `strdup()` in `bfd/elfxx-riscv.c`
  and `gas/config/tc-riscv.c` for string duplication.  This patch replaces these calls
  with `xstrdup()`, which is expected to handle allocation failures consistently with
  the rest of the codebase.  This ensures that out-of-memory conditions are handled
  gracefully.
primer_general: This patch replaces a standard C library function with a custom version
  that provides better error checks in the binutils RISC-V code. This ensures that
  memory allocation failures are handled consistently across the toolchain, improving
  reliability.
series_id: 'binutils:risc-v: avoid strdup()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ab2b7941-e67a-41ea-8cac-5e5cb72fb197@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch replaces instances of `strdup()` with `xstrdup()` in the RISC-V code within binutils.  `xstrdup()` is assumed to be a wrapper around `strdup()` that also checks for allocation failures. Using `xstrdup()` promotes consistency and better error handling within the codebase.
