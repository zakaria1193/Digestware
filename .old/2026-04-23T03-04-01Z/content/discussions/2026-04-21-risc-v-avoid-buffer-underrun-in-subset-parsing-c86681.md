---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- disassembler
- security
discussion_id: e631583c-2890-4bb3-917f-2af5cccd2aa3@suse.com
source_type: public_inbox
title: '[PATCH 15/19] RISC-V: avoid buffer underrun in subset parsing'
headline: 'Risc-V: Avoid buffer underrun in subset parsing'
tldr: Fixes a buffer underrun vulnerability in RISC-V ISA extension parsing.
stakes: 'Security: Prevents potential crashes or exploitable behavior due to out-of-bounds
  memory access.'
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds additional checks, potentially increasing code size and execution time slightly.
- Prevents a buffer underrun, improving stability and security.
exchanges: []
primer_expert: The RISC-V backend parses ISA subset strings to configure the assembler
  and disassembler. During parsing it validates extension names. The patch modifies
  the `riscv_parse_extensions` and `riscv_update_subset1` functions to prevent a buffer
  underrun when checking for the `<number>p` suffix. The problematic code inspected
  `*(q - 1)` and `*(q - 2)` without ensuring `q` was far enough into the buffer.
primer_general: When assembling or disassembling RISC-V code, the toolchain needs
  to understand which extensions to the base RISC-V ISA are in use. This patch fixes
  a bug that could cause the assembler to read from invalid memory locations when
  parsing the list of extensions. This resolves a potential security vulnerability.
series_id: 'binutils:risc-v: avoid buffer underrun in subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/e631583c-2890-4bb3-917f-2af5cccd2aa3@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch addresses a potential buffer underrun in the RISC-V ISA extension parsing logic. The code could attempt to read before the beginning of the buffer when checking for a specific pattern ('<number>p') at the end of an extension name. The patch adds a check to ensure that the code only reads within the bounds of the buffer.
