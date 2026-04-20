---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- register symbols
- Intel syntax
discussion_id: a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
source_type: public_inbox
title: 'Re: [PATCH 4/8] gas: don''t fail due to local register symbols'
headline: 'gas: don''t fail due to local register symbols'
tldr: The patch prevents the assembler from failing due to local register symbols,
  addressing a deeper issue in x86 Intel syntax parsing.
stakes: Incorrect handling of register symbols can lead to assembly errors and prevent
  code from compiling. Developers working with assembly language, especially on x86
  architectures, may be affected.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a check for local register symbols prevents incorrect error messages.
- Fixing the underlying Intel syntax parsing issue is a more comprehensive solution
  but may have wider implications.
- The interaction between register equates and symbol resolution needs careful handling.
primer: The GNU Assembler (gas) translates assembly language into object code. A symbol
  is a name that represents a memory address or a value. Local symbols are only visible
  within a specific scope (e.g., a function). Register symbols represent CPU registers.
  Equates (using the `.equ` directive) define symbolic constants.
series_id: 'binutils:gas: don''t fail due to local register symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes an issue in the GNU Assembler (gas) where it incorrectly failed when encountering local register symbols. The patch adds a check for local symbols in the reg_section. The author notes that this is a special case of a wider problem related to how the assembler parses Intel syntax.
