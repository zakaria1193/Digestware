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
tldr: The patch prevents errors when using local register symbols in GAS, which could
  arise due to Intel syntax parsing issues.
stakes: This fix ensures that GAS (the GNU Assembler) correctly handles local register
  symbols, preventing unexpected errors and improving assembler usability, especially
  when using Intel syntax on x86.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Prevents errors when using local register symbols in GAS.
- Addresses a symptom of a deeper issue in x86 Intel syntax parsing.
- May require further changes to fully resolve the underlying parsing problem.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Describes the issue and the fix, noting its connection to a deeper problem
    in x86 Intel syntax parsing, and explains the implications of the fix.
  quote: 'This is about global symbols. This is further supported by S_IS_LOCAL()
    returning true

    for symbols in reg_section. Add the missing check, adjusting the testcase

    that was introduced back at the time (where the sole diagnostic originally

    issued was therefore wrong, while other diagnostics were missing, but got

    added thanks to work done elsewhere).'
primer_expert: This patch addresses a symbol handling issue in GAS, specifically related
  to local register symbols and their interaction with Intel syntax parsing on x86.
  The core problem lies in how GAS handles equates involving registers, and how this
  can lead to spurious errors during symbol resolution. The fix ensures that local
  register symbols are not incorrectly treated as global symbols, preventing the errors.
primer_general: GAS (GNU Assembler) translates assembly code into machine code. Assembly
  code uses symbols to represent memory locations, registers, and other program elements.
  This patch fixes an error in GAS related to how it handles symbols that represent
  registers when those symbols are used only within a specific part of the assembly
  code (local symbols). The error could occur due to inconsistencies in how GAS parses
  assembly code written in Intel syntax, a common way of writing x86 assembly.
series_id: 'binutils:gas: don''t fail due to local register symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses an issue in GAS where local register symbols could cause errors, particularly when using Intel syntax. The patch adds a check to ensure that local register symbols are properly handled and prevents them from causing incorrect diagnostics or errors during symbol resolution.
