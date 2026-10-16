---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocations
- undefined symbols
discussion_id: 20261015104636.11161-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH v3] LoongArch: Fix relocation of ignored undefined symbols'
headline: 'LoongArch: Fix relocation of ignored undefined symbols'
tldr: LoongArch linker now correctly handles ignored undefined symbols during relocation
  for call instructions, preventing BFD assertions.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Correctly handling ignored undefined symbols improves linker robustness but adds
  complexity to the relocation logic.
- Ensures that the linker does not crash on valid, albeit unusual, symbol resolution
  scenarios.
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits a patch to fix how LoongArch relocations handle ignored undefined
    symbols, preventing BFD assertion failures.
  quote: 'For LoongArch, an ignored undefined symbol that fails to resolve locally

    is treated as dynamically resolved.


    Enable --unresolved-symbols=ignore-all Branch and call relocations of

    ignored undefined symbol could request a non-exist PLT entry thus

    trigger a BFD assertion.'
primer_expert: This patch series for the LoongArch backend of binutils addresses a
  bug in relocation handling for ignored undefined symbols. When the linker is configured
  with `--unresolved-symbols=ignore-all`, previously undefined symbols that couldn't
  be resolved locally were incorrectly treated as dynamically resolved. This led to
  a BFD assertion when a call relocation was attempted for such a symbol without a
  corresponding PLT entry. The fix modifies `bfd/elfnn-loongarch.c` to specifically
  handle call relocations for ignored undefined symbols, treating them as weak symbols
  when no PLT entry exists.
primer_glossary:
- term: LoongArch
  definition: A 64-bit instruction set architecture developed by the Loongson Technology
    Corporation, primarily used in China.
- term: relocation
  definition: The process of updating symbolic references in object code to absolute
    addresses or other information needed to create an executable or shared library.
    This is typically done by the linker.
- term: ignored undefined symbols
  definition: Symbols that are referenced but not defined within the current compilation
    unit, and are explicitly marked to be ignored by the linker (e.g., using `--unresolved-symbols=ignore-all`).
- term: PLT
  definition: Procedure Linkage Table, a table used in dynamically linked executables
    to hold addresses of functions that are not part of the executable itself but
    are called by it.
- term: BFD assertion
  definition: An assertion failure within the BFD (Binary Description Format) library,
    which is part of GNU Binutils and handles various object file formats. Such failures
    indicate a programming error or an unexpected state.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261015104636.11161-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the LoongArch linker where ignored undefined symbols were treated as dynamically resolved. When such symbols were involved in call relocations and lacked a PLT entry, it could lead to a BFD assertion failure. The fix ensures that for call relocations, ignored undefined symbols are handled appropriately by treating them as undefined weak symbols when no PLT entry is available, thus preventing the assertion.
