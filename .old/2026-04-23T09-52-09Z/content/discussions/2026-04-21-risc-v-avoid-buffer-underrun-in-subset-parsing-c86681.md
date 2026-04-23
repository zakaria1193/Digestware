---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- buffer underrun
- code quality
- isa extension
discussion_id: e631583c-2890-4bb3-917f-2af5cccd2aa3@suse.com
source_type: public_inbox
title: '[PATCH 15/19] RISC-V: avoid buffer underrun in subset parsing'
headline: 'Risc-V: Avoid buffer underrun in subset parsing'
tldr: Fixes a potential buffer underrun when parsing RISC-V ISA extensions, and adjusts
  indentation to improve code clarity.
stakes: Prevents crashes due to out-of-bounds reads and improves code maintainability,
  which are important for overall toolchain stability.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The fix involves adding a bounds check, which may introduce a small performance
  overhead.
- The indentation changes improve readability but don't affect functionality.
exchanges: []
primer_expert: In `bfd/elfxx-riscv.c`, the `riscv_parse_extensions` and `riscv_update_subset1`
  functions parse RISC-V ISA extensions from strings like "rv64gc". This patch fixes
  a potential out-of-bounds read when checking for the `<number>p` suffix. It also
  corrects misleading indentation around these checks.
primer_general: The RISC-V architecture uses extensions to add functionality to the
  base instruction set. Binutils needs to parse these extensions correctly to assemble
  and disassemble code for different RISC-V variants. This patch fixes a bug where
  the parser could read before the beginning of the string, causing a crash or misinterpretation
  of the ISA. It also improves code readability, making the code easier to maintain.
series_id: 'binutils:risc-v: avoid buffer underrun in subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/e631583c-2890-4bb3-917f-2af5cccd2aa3@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch prevents a buffer underrun in the RISC-V ISA extension parsing logic. It addresses a situation where inspecting a character immediately ahead of 'p' can lead to undefined behavior if 'p' is the first character. The patch also adjusts indentation for better code readability.
