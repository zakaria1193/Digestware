---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- undefined symbols
- dynamic linking
- symbol table
discussion_id: 0965fef2-6c0f-4e0a-9d41-e757b9fea708@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Also output undefined symbols as dynamic symbols'
headline: 'RISC-V: Also output undefined symbols as dynamic symbols'
tldr: Reverts a change that caused incorrect handling of undefined symbols in RISC-V
  binaries when linking with `--unresolved-symbols=ignore-in-object-file`.
proposer: Vivian Wang <wangruikang@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Restores a previous behavior that may not be the ideal long-term solution.
- Potential for different behavior compared to other architectures.
exchanges:
- author: Nelson Chu
  role: other
  position: Questions whether dynamic symbols should still be generated for undefined
    symbols.
  quote: 'So do you think we should also stop output dynamic symbols for

    undefined symbols?  umm maybe you are right, I am not sure.'
- author: Vivian Wang <wangruikang@iscas.ac.cn>
  role: proposer
  position: Clarifies that the patch restores a previous behavior to avoid a bogus
    error message, and explains observed behavior on other architectures.
  quote: 'FWIW, I can''t really claim that this handling of undefined symbols is

    what *should* be done, just that this restores some slightly earlier

    version''s behavior for riscv, and gets rid of the bogus error message

    from ld.'
primer_expert: The RISC-V linker needs to handle undefined symbols correctly, especially
  when the `--unresolved-symbols=ignore-in-object-file` option is used.  Dynamic symbols
  are used to resolve symbols at runtime.  This patch modifies the linker's symbol
  table output logic to ensure undefined symbols are treated as dynamic symbols in
  certain cases.
primer_general: When linking programs, undefined symbols are references to functions
  or variables that are not defined in the current object file.  The linker is responsible
  for resolving these references, either by finding the definitions in other object
  files or by marking them as external dependencies to be resolved at runtime by the
  dynamic linker. The `--unresolved-symbols=ignore-in-object-file` option instructs
  the linker to leave these symbols unresolved.  This patch corrects how the RISC-V
  linker handles these undefined symbols, ensuring proper dynamic linking behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/0965fef2-6c0f-4e0a-9d41-e757b9fea708@iscas.ac.cn
bugzilla_url: null
date: '2026-05-14'
is_stub: false
---

This patch addresses an issue in the RISC-V linker where undefined symbols were not being handled correctly when linking with the `--unresolved-symbols=ignore-in-object-file` option.  The patch restores previous behavior by ensuring that undefined symbols are output as dynamic symbols. This fixes problems where the linker would generate incorrect code or error messages. The proposer clarifies that the patch restores previous behavior and avoids a specific bogus error message.
