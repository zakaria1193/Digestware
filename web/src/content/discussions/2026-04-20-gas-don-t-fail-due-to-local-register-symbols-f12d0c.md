---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- register symbols
- equates
discussion_id: a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
source_type: public_inbox
title: 'Re: [PATCH 4/8] gas: don''t fail due to local register symbols'
headline: 'gas: don''t fail due to local register symbols'
tldr: A patch to prevent the assembler from failing due to local register symbols,
  with considerations for Intel syntax parsing.
stakes: Fixes a bug where the assembler incorrectly errors on local register symbols,
  and considers impacts from deeper x86 Intel syntax parsing issues.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The patch needs to consider the interaction with x86 Intel syntax parsing.
- The check for local register symbols needs to be in the correct location to avoid
  false positives.
primer_expert: This patch addresses an issue in the GNU assembler (gas) related to
  local register symbols and their interaction with equates, specifically in the x86
  Intel syntax parsing. The core problem is that the assembler was incorrectly erroring
  on local register symbols. The fix involves adjusting the logic within `resolve_symbol_value()`
  to properly handle these symbols. The author mentions a deeper issue with Intel
  syntax parsing that exacerbates the problem.
primer_general: The GNU assembler (gas) translates assembly language into machine
  code. Assembly language uses symbolic names to represent registers and memory locations.  An
  'equate' is a way to assign a name to a value or expression.  'Local' symbols have
  a limited scope within a program.  This patch fixes a bug in the assembler that
  caused it to incorrectly report errors when dealing with local symbols that represent
  registers, and which come from equates. This ensures that the assembler correctly
  handles these symbols during the assembly process.
series_id: 'binutils:gas: don''t fail due to local register symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a4ce5bf4-c44b-4e28-9411-c625e19d9010@suse.com
bugzilla_url: null
date: '2026-04-20'
---

Jan Beulich discusses a patch that prevents the GNU assembler (gas) from failing when encountering local register symbols. The patch adds a check for local symbols in the register section. The author notes a deeper issue in x86 Intel syntax parsing that relates to how equates are handled, and how fixing that would expose the need for this patch.
