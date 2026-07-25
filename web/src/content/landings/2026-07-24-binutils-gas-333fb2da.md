---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- x86
- assembly
- optimization
- AVX
- bugfix
commit_hash: 333fb2dac903a18fe87eefa932aa87fc6878b630
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: 'x86: Simplify VPBROADCASTQ to VUNPCKLQDQ optimization'
tldr: Refines the x86 assembler's optimization for VPBROADCASTQ to VUNPCKLQDQ, fixing
  a condition check.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit revisits the optimization logic for transforming `VPBROADCASTQ`
  to `VUNPCKLQDQ` in the x86 gas backend. It appears that a fix in eb4031cb20aa incorrectly
  added a check for `i.op[0].regs->reg_type.bitfield.xmmword` (the destination operand).
  This check is not necessary for the optimization itself, which primarily depends
  on the source operand's properties and the instruction encoding. Removing this extraneous
  check rectifies the logic.
primer_glossary:
- term: VPBROADCASTQ
  definition: An x86 AVX instruction that broadcasts a 64-bit quadword to all elements
    within a 128-bit YMM register.
- term: VUNPCKLQDQ
  definition: An x86 AVX instruction that unpacks and interleaves lower and upper
    quadwords from two 128-bit source registers into a destination register.
- term: Optimization
  definition: The process of modifying an algorithm or code structure to improve its
    efficiency, typically in terms of speed or memory usage.
- term: xmmword
  definition: Refers to a 128-bit register size, commonly used by SSE and AVX instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260724062542.57BF64BA2E3B@sourceware.org
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

The x86 assembler's optimization converting `VPBROADCASTQ` to `VUNPCKLQDQ` has been slightly simplified by removing an redundant check on the destination operand's `xmmword` property. This change corrects a logic flaw introduced in a previous commit, ensuring the optimization applies correctly.
