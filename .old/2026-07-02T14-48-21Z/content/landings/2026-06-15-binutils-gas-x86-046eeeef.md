---
project: binutils
subsystem: binutils/gas/x86
patch_id: null
tags:
- x86
- assembler
- optimization
- AVX
commit_hash: 046eeeef47216439ea7c7411b9d55ca86dbacac2
source_type: public_inbox
author: H.J. Lu <hjl@sourceware.org>
headline: X86 assembler correctly optimizes VPBROADCASTQ to VPUNPCKLQDQ
tldr: The x86 assembler now correctly optimizes 128-bit VPBROADCASTQ instructions
  by verifying the destination operand is an XMM register before converting to VPUNPC…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in `gas/config/tc-i386.c` addresses an oversight in the
  `optimize_encoding` function during AVX instruction optimization. Specifically,
  for 128-bit `VPBROADCASTQ` operations, the instruction was optimistically converted
  to `VPUNPCKLQDQ`. The issue arose because the optimization did not strictly check
  that the destination operand (`i.op[1].regs->reg_type.bitfield.xmmword`) was an
  XMM register, allowing incorrect transformations when YMM registers were targeted.
  This fix ensures the optimization only triggers when both source and destination
  are XMM, preventing invalid encoding for…
primer_general: Modern CPUs have special instructions that can process multiple pieces
  of data at once, which is called Single Instruction Multiple Data (SIMD). On x86
  processors, this uses registers like XMM (128-bit) and YMM (256-bit). An instruction
  called `VPBROADCASTQ` copies a 64-bit value to all parts of a larger register, effectively
  'broadcasting' it. Another instruction, `VPUNPCKLQDQ`, rearranges data within registers.
  Compilers and assemblers try to optimize your code by replacing slower instructions
  with faster, equivalent ones. In some cases, `VPBROADCASTQ` can be optimized into
  `VPUNPCKLQDQ` for 128-bit operations. However, a bug allowed this optimization to
  happen even when the target was a larger 256-bit YMM register. This commit fixes
  that bug, ensuring the assembler only performs this specific optimization when it's
  safe and correct for 128-bit XMM registers, preventing your program from behaving
  unexpectedly or crashing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260615150709.16A814C900D9@sourceware.org
date: '2026-06-15'
is_stub: false
---

A fix ensures the x86 assembler (GAS) properly optimizes 128-bit `VPBROADCASTQ` instructions. Previously, the optimization, which converts `VPBROADCASTQ %xmmN, %xmmM` to `VPUNPCKLQDQ %xmmN, %xmmN, %xmmM`, would incorrectly apply even if the destination was a YMM register. This change adds a check to confirm the destination is indeed an XMM register, preventing miscompilations and ensuring valid code generation for AVX instructions.
