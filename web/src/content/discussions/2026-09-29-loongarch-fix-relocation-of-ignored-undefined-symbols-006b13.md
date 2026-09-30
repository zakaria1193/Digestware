---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- relocations
- symbols
- bfd
discussion_id: 20260929120125.65108-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Fix relocation of ignored undefined symbols'
headline: 'LoongArch: Fix relocation of ignored undefined symbols'
tldr: Corrects how ignored undefined symbols are handled in LoongArch to prevent BFD
  assertions.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Classifying ignored symbols without dynamic entries as constants simplifies resolution
  logic and prevents PLT issues, but relies on correct symbol table information.
- Maintaining dynamic resolution for ignored symbols with dynamic entries ensures
  compatibility with existing shared linking mechanisms.
exchanges: []
primer_expert: 'This patch modifies `elfnn-loongarch.c` to correctly handle ignored
  undefined symbols in LoongArch. Previously, symbols marked `RM_IGNORE` that didn''t
  resolve locally were treated as dynamic, leading to PLT lookups and assertion failures.
  The change differentiates between ignored symbols with and without dynamic entries:
  those without dynamic entries are now treated as constants, preventing unnecessary
  PLT resolution. This is crucial for branch and call instructions targeting such
  symbols.'
primer_glossary:
- term: relocation
  definition: Information in an object file that describes how to modify (relocate)
    certain memory addresses when the code or data is loaded into memory at a different
    address than the one it was compiled for. This is crucial for position-independent
    code and dynamic linking.
- term: undefined symbol
  definition: A symbol (like a function or variable name) that is referenced in one
    object file but not defined within it. The linker's job is to resolve these references
    to definitions in other object files or libraries.
- term: PLT
  definition: Procedure Linkage Table. A table in an executable or shared library
    used to resolve calls to functions in dynamically linked libraries at runtime.
- term: BFD assertion
  definition: An assertion failure within the Binary File Descriptor (BFD) library,
    which is part of binutils. Assertions are checks that must be true for the program
    to function correctly; failure indicates a bug.
- term: dynamic symbol entry
  definition: An entry in the symbol table of an object file that provides information
    for dynamic linking, such as the symbol's value and whether it needs to be resolved
    at runtime.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260929120125.65108-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch resolves an issue in LoongArch where ignored undefined symbols, when not resolved locally, were treated as dynamically resolved. This led to a BFD assertion failure when branch and call relocations requested non-existent PLT entries. The fix classifies ignored symbols without dynamic entries as constants, while those with dynamic entries remain dynamically resolved to maintain compatibility with shared links.
