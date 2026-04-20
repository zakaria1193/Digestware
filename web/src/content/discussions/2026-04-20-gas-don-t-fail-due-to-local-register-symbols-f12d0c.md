---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- symbols
- bug fix
discussion_id: a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
source_type: public_inbox
title: 'Re: [PATCH 4/8] gas: don''t fail due to local register symbols'
headline: 'gas: don''t fail due to local register symbols'
tldr: The patch fixes an issue in the assembler (`gas`) where local register symbols
  were incorrectly flagged as errors.
stakes: Fixes a bug in the assembler that could prevent correct assembly of certain
  code.  All developers using the affected assembler should care.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Fixes a bug, preventing incorrect error messages.
- Improves the accuracy of the assembler.
- No known drawbacks.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes a fix to prevent the assembler from incorrectly flagging local
    register symbols as global errors.
  quote: Add the missing check, adjusting the testcase that was introduced back at
    the time (where the sole diagnostic originally issued was therefore wrong, while
    other diagnostics were missing, but got added thanks to work done elsewhere).
primer_expert: This patch modifies the gas assembler, specifically addressing an issue
  where `resolve_symbol_value` incorrectly flagged local register symbols as errors
  due to a missing `S_IS_LOCAL` check. The issue is further complicated by interactions
  with the x86 Intel syntax parser. The `reg_section` and `expr_section` are involved.
primer_general: The GNU assembler (`gas`) translates assembly code into machine code.
  This patch fixes a bug where the assembler was incorrectly identifying local register
  symbols (symbols specific to a small section of code) as global symbols (symbols
  that can be accessed from anywhere in the code). This could lead to assembly errors
  and prevent programs from compiling correctly. The patch corrects this behavior
  by properly checking if a symbol is local before processing it.
series_id: 'binutils:gas: don''t fail due to local register symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a bug in the GNU assembler (`gas`) that caused it to incorrectly flag local register symbols as errors. The fix involves adding a check for local symbols to prevent the erroneous diagnostic. The patch also removes redundant code in a testcase.
