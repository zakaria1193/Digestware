---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- symbols
- x86
discussion_id: a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
source_type: public_inbox
title: 'Re: [PATCH 4/8] gas: don''t fail due to local register symbols'
headline: 'gas: don''t fail due to local register symbols'
tldr: The assembler (gas) will no longer fail when encountering local register symbols,
  addressing a parsing issue in x86 Intel syntax.
stakes: Prevents assembler failures due to local register symbols, ensuring correct
  code generation. Fixes a parsing issue that could break existing assembly code.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch addresses a clear bug and includes necessary testcase
  adjustments, showing a good understanding of the issue.
technical_tradeoffs:
- The fix might expose other issues related to equate handling in the assembler.
- The check for local symbols may need to be moved depending on the desired error
  handling behavior.
- Correcting the Intel syntax parsing issue could break existing testcases.
primer: The GNU Assembler (`gas`) is the default assembler for the GNU project, which
  translates assembly source code into machine code. Symbols are named entities in
  the assembly code that represent memory locations, constants, or functions. Equates
  (equ) define symbolic constants. This patch addresses an issue where the assembler
  incorrectly handles local register symbols, which can lead to assembly failures.
series_id: 'binutils:gas: don''t fail due to local register symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch modifies the assembler (gas) to avoid errors when handling local register symbols. The change involves adding a check for local symbols in `reg_section` and adjusting a testcase. The patch also removes a redundant `sname` assignment. This resolves a deeper issue in x86 Intel syntax parsing.
