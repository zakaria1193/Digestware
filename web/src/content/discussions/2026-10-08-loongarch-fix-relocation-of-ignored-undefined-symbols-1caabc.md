---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- linker
- LoongArch
- relocation
- BFD
discussion_id: 20261008111834.54179-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Fix relocation of ignored undefined symbols'
headline: 'LoongArch: Fix relocation of ignored undefined symbols'
tldr: Fixes a BFD assertion in LoongArch linking by correctly classifying ignored
  undefined symbols.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Corrects a specific bug, improving linker stability.
- Adds test cases to verify the fix.
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits a patch to correct how ignored undefined symbols are handled in
    LoongArch linking, preventing BFD assertions.
  quote: 'For LoongArch, an ignored undefined symbol that fails to resolve locally

    is treated as dynamically resolved.


    Enable --unresolved-symbols=ignore-all Branch and call relocations of

    ignored undefined symbol could request a non-exist PLT entry thus

    trigger a BFD assertion.'
primer_expert: This patch modifies `bfd/elfnn-loongarch.c` and adds test cases to
  `ld/testsuite/ld-loongarch-elf/`. It addresses a specific issue where the LoongArch
  ELF linker, when encountering undefined symbols marked with `RM_IGNORE` and not
  having a dynamic symbol entry, would incorrectly attempt to resolve them dynamically.
  This leads to a BFD assertion when processing call-related relocations that expect
  a PLT entry. The change reclassifies these symbols to avoid the assertion.
primer_glossary:
- term: LoongArch
  definition: A family of instruction set architectures developed in China.
- term: relocation
  definition: A process performed by the linker to adjust symbolic addresses in machine
    code after it has been assembled, typically to account for the final memory locations
    of code and data.
- term: undefined symbol
  definition: A symbol that is referenced in object code but not defined within any
    of the object files being linked. The linker typically resolves these by finding
    their definition in other object files or libraries.
- term: BFD
  definition: Binary File Descriptor library, a library used by GNU Binutils to support
    various object file formats.
- term: PLT
  definition: Procedure Linkage Table, a table used in dynamically linked executables
    to resolve addresses of functions at runtime.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261008111834.54179-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the LoongArch linker where ignored undefined symbols could lead to a BFD assertion. Previously, ignored undefined symbols were treated as dynamically resolved, causing issues with branch and call relocations. The fix classifies these symbols as constants if they lack dynamic entries, while maintaining dynamic resolution for those with dynamic entries to ensure shared link compatibility.
