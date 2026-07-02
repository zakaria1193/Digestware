---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- linker
- dynamic symbols
- undefined symbols
- bfd
discussion_id: 9253a1f8-4f1a-4482-801b-a1e05d91c5ea@iscas.ac.cn
source_type: public_inbox
title: '[PATCH] RISC-V: Also output undefined symbols as dynamic symbols'
headline: 'RISC-V: Output undefined symbols as dynamic symbols'
tldr: This patch fixes an issue in the RISC-V linker that prevented undefined symbols
  from being resolved by the dynamic linker when using --unresolved-symbols=ignor…
proposer: Vivian Wang <wangruikang@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reintroduces the output of undefined symbols as dynamic symbols, which may have
  been intentionally removed in a previous commit (9e10fcf71c11).
- Fixes a regression that caused crashes or errors when linking with ``--unresolved-symbols=ignore-in-object-file``.
exchanges:
- author: Vivian Wang <wangruikang@iscas.ac.cn>
  role: proposer
  position: Proposes a patch to output undefined symbols as dynamic symbols in the
    RISC-V linker, fixing an issue where these symbols were not being correctly resolved
    when using the ``--unresolved-symbols=ignore-in-object-file`` option.
  quote: Therefore, in order to fix the issue, also output undefined symbols as dynamic
    symbols.
primer_expert: When linking RISC-V code, undefined symbols (e.g., external functions
  not defined in the current object file) need to be handled so the dynamic linker
  can resolve them at runtime.  The patch modifies ``bfd/elfnn-riscv.c`` to ensure
  that these undefined symbols are output as dynamic symbols, which was unintentionally
  disabled by a prior commit. This ensures that the dynamic linker can resolve these
  symbols, preventing crashes or errors during program execution.
primer_general: When a program calls a function or uses a variable defined in a separate
  piece of code (a library, say), the linker must resolve that reference.  The dynamic
  linker handles this resolution at *runtime*, when the program is already running.
  This patch for the RISC-V architecture ensures that the linker emits the right metadata
  for undefined symbols, so the dynamic linker can do its job and the program doesn't
  crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/9253a1f8-4f1a-4482-801b-a1e05d91c5ea@iscas.ac.cn
bugzilla_url: null
date: '2026-05-11'
is_stub: false
---

The patch addresses an issue in the RISC-V linker where undefined symbols were not being correctly output as dynamic symbols when the ``--unresolved-symbols=ignore-in-object-file`` option was used. This would lead to either a crash when linking with ``-no-pie`` or an error message when linking with ``-pie``. The fix involves re-introducing the output of undefined symbols as dynamic symbols, which was removed by commit 9e10fcf71c11.  This ensures that these symbols can be resolved by the dynamic linker at runtime.
