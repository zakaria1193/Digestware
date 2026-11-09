---
project: binutils
subsystem: sframe
patch_id: null
tags:
- sframe
- stack unwinding
- CFI
- RA
- FP
discussion_id: 20261109064949.1370408-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v2] sframe: Fix RA and FP stack recovery rules'
headline: 'sframe: Fix RA and FP stack recovery rules'
tldr: v2 patch corrects typos and dereferences pointers for RA and FP stack recovery
  rules in sframe.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the sframe library, which is part of binutils and
  used for stack unwinding information. It corrects how the Return Address (RA) and
  Frame Pointer (FP) are recovered from the stack based on Call Frame Information
  (CFI) directives. The changes involve fixing typos in documentation and ensuring
  that stack offsets are dereferenced correctly when calculating the addresses of
  RA and FP.
primer_glossary:
- term: sframe
  definition: A library or mechanism for managing and interpreting stack frame information,
    crucial for stack unwinding and debugging.
- term: RA
  definition: Return Address, the memory address of the instruction to which the program
    control should return after a subroutine call.
- term: FP
  definition: Frame Pointer, a register that points to the base of the current stack
    frame, used to access local variables and parameters.
- term: CFA
  definition: Call Frame Address, a value that represents the address of the current
    stack frame, often used as a reference point for locating other stack variables
    like RA and FP.
- term: stack recovery rules
  definition: Rules used during stack unwinding to determine the values and locations
    of registers (like RA and FP) from saved information on the stack.
series_id: 20261109064949.1370408-1-mengqinggang@loongson.cn
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109064949.1370408-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch series updates the Stack Frame (sframe) library to fix interpreted typos and correctly implement stack recovery rules for Return Address (RA) and Frame Pointer (FP). Version 2 includes changes to the documentation (sframe-spec.texi) and corrects the interpretation of stack recovery rules by dereferencing pointers (e.g., `*(CFA + offset)`) instead of direct addition.
