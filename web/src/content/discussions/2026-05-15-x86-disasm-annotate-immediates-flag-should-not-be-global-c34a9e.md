---
project: binutils
subsystem: x86/disasm
patch_id: null
tags:
- x86
- disassembler
- thread safety
- global state
discussion_id: a660ef39-7af1-4897-94a9-8501ad89c075@suse.com
source_type: public_inbox
title: '[PATCH 1/3] x86/disasm: "annotate immediates" flag should not be global'
headline: 'x86/disasm: "Annotate immediates" flag should not be global'
tldr: Makes the "annotate immediates" flag thread-local in the x86 disassembler to
  avoid introducing new global state.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The change might introduce a slight performance overhead due to accessing the flag
  through the `instr_info` struct instead of directly.
- It increases the size of the `instr_info` struct, but the impact is minimal.
exchanges: []
primer_expert: This patch refactors the x86 disassembler in `opcodes/i386-dis.c` to
  remove the global `annotate_immediates` variable.  It moves this flag into the `instr_info`
  structure, which is local to each disassembly operation.  This change is important
  for thread safety, as global variables can cause race conditions and unpredictable
  behavior in multi-threaded environments.
primer_general: The disassembler converts machine code into assembly language. This
  patch addresses a thread-safety issue in the x86 disassembler. By making the "annotate
  immediates" flag thread-local, the patch ensures that multiple threads can disassemble
  code concurrently without interfering with each other's settings, preventing potential
  corruption or incorrect disassembly output.
series_id: 'binutils:x86/disasm: "annotate immediates" flag should not be global'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a660ef39-7af1-4897-94a9-8501ad89c075@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch modifies the x86 disassembler to make the "annotate immediates" flag thread-local. This change avoids introducing new global state variables, as disassembly functions have been made thread-safe. The flag is moved into the `instr_info` struct, ensuring each thread has its own copy.
