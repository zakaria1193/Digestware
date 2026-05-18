---
project: binutils
subsystem: x86/intel
patch_id: null
tags:
- assembler
- recursion
- x86
- intel
- symbol
discussion_id: agfvorYEpD-ZzK-V@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH v2] x86/Intel: avoid infinite recursion in i386_intel_simplify_symbol()
  (again)'
headline: 'x86/Intel: Avoid infinite recursion in i386_intel_simplify_symbol()'
tldr: Fixes potential infinite recursion in symbol simplification for x86/Intel assembly,
  but the proposed fix is suspected to be incorrect.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The proposed fix might not be correct and could introduce new issues.
- Fixing the recursion issue is important for assembler stability.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Expresses concern that the proposed fix may be incorrect and provides
    a test case to illustrate the issue related to symbol simplification.
  quote: I suspect that trying to cut the loop like this is wrong.
primer_expert: The `i386_intel_simplify_symbol()` function in `as` attempts to simplify
  symbol expressions in Intel syntax. This patch attempts to prevent infinite recursion
  when the symbol definitions form a cycle. The reviewer suspects the fix is wrong.
primer_general: The GNU assembler (`as`) translates assembly language into machine
  code. This patch addresses a potential infinite loop within the assembler's x86/Intel
  syntax processing logic. When the assembler encounters complex or circular symbol
  definitions, a bug can cause it to get stuck in an infinite loop while trying to
  simplify the expression.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/agfvorYEpD-ZzK-V@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-16'
is_stub: false
---

This patch attempts to fix a potential infinite recursion issue in the `i386_intel_simplify_symbol()` function within the binutils assembler, specifically for x86/Intel syntax. Alan Modra suspects that the proposed fix is not correct. The original bug can cause the assembler to enter an infinite loop when simplifying complex symbol expressions.
