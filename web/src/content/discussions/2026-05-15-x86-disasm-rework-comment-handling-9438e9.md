---
project: binutils
subsystem: x86/disasm
patch_id: null
tags:
- x86
- disassembler
- comments
- annotation
- refactoring
discussion_id: 916dde10-59ed-4180-86e6-a42677b90c20@suse.com
source_type: public_inbox
title: '[PATCH 3/3] x86/disasm: rework comment handling'
headline: 'x86/disasm: Rework comment handling'
tldr: Refactors x86 disassembler to handle comments in the same order as operands,
  improving annotation consistency.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Unifying %rip-relative comments with other comments is currently not possible due
  to the `print_address_func()` hook.
- Moving the test suite might require adjustments to the testing infrastructure.
- The new approach might introduce subtle changes in the generated disassembly output.
exchanges: []
primer_expert: This patch modifies the x86 disassembly code in `opcodes/i386-dis.c`
  to improve comment annotation.  It moves away from ad-hoc comment insertion towards
  a model where comments are handled similarly to operands. The patch also touches
  the testsuite, specifically the `binutils-all/x86-64` directory, to add new tests
  for the improved comment handling.
primer_general: The disassembler is a tool that translates machine code back into
  human-readable assembly code. This patch focuses on improving how the x86 disassembler
  annotates the generated assembly with comments, aiming for better readability and
  consistency. The changes involve refactoring the internal logic of the disassembler
  to handle comments in a more structured way, similar to how operands are processed.
series_id: 'binutils:x86/disasm: rework comment handling'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/916dde10-59ed-4180-86e6-a42677b90c20@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch refactors the x86 disassembler's comment handling to align it with operand handling, allowing comments to be emitted in the same order as operands. It aims to provide a more consistent approach to annotation. The author discusses the limitations of unifying %rip-relative comments due to the `print_address_func()` hook and proposes moving the test suite to a more generic location.
