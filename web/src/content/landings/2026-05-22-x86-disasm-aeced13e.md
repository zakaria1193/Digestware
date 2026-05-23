---
project: binutils
subsystem: x86/disasm
patch_id: null
tags:
- disassembler
- x86
- comments
commit_hash: aeced13ee0cd570d78cb37ab1f9bba840958515a
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: 'X86/disasm: Rework comment handling in the disassembler'
tldr: The x86 disassembler now handles comments like operands, allowing them to be
  emitted in the same order.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The x86 disassembler is responsible for converting machine code back
  into assembly language.  Disassembly annotations provide additional context, such
  as symbol names for immediate values.  This commit refactors the comment emission
  logic within `opcodes/i386-dis.c` to ensure comments are displayed consistently
  with operands.  The change avoids treating symbol names as "comment starts".
primer_general: A disassembler translates machine code back into human-readable assembly
  language. This is useful for understanding how a compiled program works or debugging
  issues. The x86 disassembler is the part of the GNU binutils toolchain that performs
  this translation for x86-based architectures. This change improves how the disassembler
  adds explanatory comments to the disassembled code, making it easier to read and
  understand.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260522065040.D23CE48F6641@sourceware.org
date: '2026-05-22'
is_stub: false
---

The x86 disassembler's comment handling was reworked to align with operand handling. This change enables comments to be emitted in the same order as operands, improving the clarity of disassembled code. Tests were added to verify the new comment handling in both Intel and AT&T syntax.
