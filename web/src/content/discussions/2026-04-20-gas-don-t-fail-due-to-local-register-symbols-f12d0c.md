---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- symbols
- registers
discussion_id: a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
source_type: public_inbox
title: 'Re: [PATCH 4/8] gas: don''t fail due to local register symbols'
headline: 'gas: don''t fail due to local register symbols'
tldr: The assembler (gas) is incorrectly treating local register symbols as global
  symbols, causing errors. This patch fixes that.
stakes: Fixes a bug in the assembler that could prevent successful assembly of code
  using local register symbols.  This ensures that valid assembly code is assembled
  correctly.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The fix avoids false errors but may mask other underlying issues.
- The solution may need to be revisited when the Intel syntax parsing issue is resolved.
- There may be broader implications for how equates are handled.
primer_expert: The GNU assembler (`gas`) incorrectly diagnosed local register symbols
  as global, causing errors in `resolve_symbol_value`. This patch adds a check using
  `S_IS_LOCAL()` to avoid this. The issue is related to how the assembler handles
  equates and register symbols in the presence of Intel syntax parsing.
primer_general: The GNU assembler (`gas`) translates assembly language code into machine
  code. Assembly language uses symbols to represent memory locations, registers, and
  other program elements. This patch fixes a bug where the assembler was misinterpreting
  the scope of register symbols (symbols that refer to CPU registers), causing assembly
  to fail when it shouldn't.
series_id: 'binutils:gas: don''t fail due to local register symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses an issue in the GNU assembler (`gas`) where local register symbols were being incorrectly treated as global symbols, leading to errors during assembly. The patch adds a check to ensure that local symbols in the register section are not flagged as errors. The submitter also improved test cases by removing redundant code.
