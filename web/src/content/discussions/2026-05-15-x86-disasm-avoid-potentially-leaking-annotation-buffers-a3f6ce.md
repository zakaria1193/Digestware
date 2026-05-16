---
project: binutils
subsystem: x86/disasm
patch_id: null
tags:
- x86
- disassembler
- memory leak
- bugfix
discussion_id: 0568e50d-eaa0-4875-8fff-e44ed2e54341@suse.com
source_type: public_inbox
title: '[PATCH 2/3] x86/disasm: avoid potentially leaking annotation buffers'
headline: 'x86/disasm: Avoid potentially leaking annotation buffers'
tldr: Fixes a potential memory leak in the x86 disassembler by ensuring annotation
  buffers are always freed.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The fix has no significant performance impact.
- It slightly increases code size due to the unconditional `free` call, but the effect
  is negligible.
exchanges: []
primer_expert: This patch fixes a memory leak in `opcodes/i386-dis.c` within the `oappend_immediate`
  function.  The original code had a conditional `free(annotation)` call, which would
  not be executed if `asprintf` failed but still allocated memory.  The fix moves
  the `free` call to unconditionally release the allocated memory.
primer_general: The disassembler converts machine code into assembly language. This
  patch addresses a potential memory leak in the x86 disassembler, which could occur
  when annotating immediates (constant values) in the assembly output. The fix ensures
  that memory allocated for these annotations is always released, preventing memory
  exhaustion over time.
series_id: 'binutils:x86/disasm: avoid potentially leaking annotation buffers'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0568e50d-eaa0-4875-8fff-e44ed2e54341@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch addresses a potential memory leak in the x86 disassembler. The `asprintf` function can return 0 while still allocating memory, leading to a leak if the `free` function is only called when `asprintf` succeeds. The patch moves the `free` call outside the `if` statement to ensure the buffer is always freed.
