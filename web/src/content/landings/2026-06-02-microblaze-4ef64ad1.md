---
project: gcc
subsystem: microblaze
patch_id: null
tags:
- microblaze
- linux
- libgcc
- debugging
- nptl
commit_hash: 4ef64ad1aa9bbbe9471610e2de6ef0c8afed8b1f
source_type: github
author: Ramin Moussavi
headline: MicroBlaze adds Linux signal frame unwinding support
tldr: GCC's libgcc for MicroBlaze Linux now supports DWARF unwinding through signal
  frames, enabling correct stack traces andpthread cancellation.
impact_score: 8
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit adds `MD_FALLBACK_FRAME_STATE_FOR` support for MicroBlaze
  Linux within `libgcc`, specifically by introducing `config/microblaze/linux-unwind.h`.
  The core issue was the DWARF unwinder''s inability to traverse signal frames, particularly
  impacting NPTL asynchronous cancellation, as the on-stack signal trampoline was
  not recognized. The solution implemented mirrors patterns in MIPS/AArch64 `linux-unwind.h`:
  it identifies the two-instruction kernel trampoline (`addik r12, r0, __NR_rt_sigreturn;
  brki r14, 0x8`) and rebuilds the frame state from the `pt_regs` in the `sigcontext_t`.
  `DWAR…'
primer_general: When a program runs, it often needs to keep track of where it is in
  a sequence of function calls, which is called the 'call stack.' If something unexpected
  happens, like an error or a message from the operating system (a 'signal'), the
  program might jump to a special 'signal handler' function. After the handler finishes,
  the program needs to 'unwind' the stack to figure out where it was before the signal.
  This update fixes an issue in the GCC compiler's support for MicroBlaze Linux systems,
  where this unwinding process would break when encountering signal handlers. This
  meant that certain advanced features, like canceling a background task (`pthread
  cancellation`), would either fail silently or crash the program. Now, the compiler
  knows how to correctly navigate these signal handler jumps, allowing debugging tools
  to get correct stack traces and ensuring features like task cancellation work reliably.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4ef64ad1aa9bbbe9471610e2de6ef0c8afed8b1f
date: '2026-06-02'
is_stub: false
---

GCC's `libgcc` for MicroBlaze Linux now properly supports DWARF unwinding through signal handler frames. Previously, applications using asynchronous pthread cancellation (like NPTL) or similar signal mechanisms would fail to unwind correctly past a signal, resulting in incomplete stack traces, incorrect cleanup handlers, or crashes. This fix introduces code to recognize the kernel's signal trampoline and reconstructs the stack state from the `pt_regs` within the `sigcontext`, ensuring that unwinding operations can correctly traverse signal frames.
