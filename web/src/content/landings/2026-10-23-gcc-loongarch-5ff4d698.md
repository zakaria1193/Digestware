---
project: gcc
subsystem: gcc/loongarch
patch_id: null
tags:
- gcc
- loongarch
- optimization
commit_hash: 5ff4d69897539786097091ed637f6e943ade9fc8
source_type: github
author: Xi Ruoyao
headline: LoongArch optimization patterns improved for bit manipulation and byte picking.
tldr: Optimizations for LoongArch improve code generation for bitwise operations and
  byte manipulation.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: LoongArch's RTX cost model and instruction patterns are updated to
  better handle transformations involving bitwise OR and shifts, and for byte manipulation
  instructions like `bytepick.w`. Specifically, the `bstrins_d_for_ior_ashift_and`
  pattern now accounts for cases where `(a << 1) | (b & 1)` is transformed to `(a
  << 1) + (b & 1)`, which can be implemented more efficiently. The `bytepick.w` pattern
  was rewritten to adapt to the upstream change of preferring `+` over `ior` when
  bitwise AND is zero. These changes enable more effective instruction selection,
  especially after target-independent…
primer_glossary:
- term: RTX
  definition: Represents the intermediate language (IL) within GCC. It's a tree-based
    representation used for performing optimizations and transformations before generating
    machine code.
- term: LoongArch
  definition: A 64-bit RISC instruction set architecture developed in China, featuring
    a modular design and support for various extensions.
- term: bytepick.w
  definition: A LoongArch instruction that extracts a byte from a word and extends
    it, often used for bit manipulation tasks.
- term: LA32S
  definition: A specific variant of the LoongArch architecture, notable for its 32-bit
    address space.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5ff4d69897539786097091ed637f6e943ade9fc8
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

GCC's LoongArch backend gains improved optimization for bit string instructions and byte picking. The changes address issues where target-independent code transformations caused previously optimal instruction sequences to be overlooked. Cost models were updated to accurately reflect instruction costs, enabling the compiler to select more efficient code, and patterns were refined for better code generation, including support for LA32S.
