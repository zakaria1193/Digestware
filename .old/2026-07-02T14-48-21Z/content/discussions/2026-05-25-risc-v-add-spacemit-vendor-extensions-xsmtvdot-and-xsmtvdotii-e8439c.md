---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- spacemit
- xsmtvdot
- xsmtvdotii
discussion_id: 20260525082008.1219171-1-zhuangqiubin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v6 0/2] RISC-V: Add SpacemiT vendor extensions xsmtvdot and xsmtvdotii'
headline: 'RISC-V: Add SpacemiT vendor extensions xsmtvdot and xsmtvdotii'
tldr: This series adds support for SpacemiT's xsmtvdot and xsmtvdotii vendor extensions,
  implementing subsets of the Intrinsic Matrix Extension.
proposer: Mark Zhuang <zhuangqiubin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding vendor-specific extensions can increase the complexity of the toolchain and
  potentially lead to fragmentation.
- The extensions may not be compatible with other RISC-V implementations.
exchanges:
- author: Mark Zhuang
  role: proposer
  position: Proposes adding support for SpacemiT vendor extensions xsmtvdot and xsmtvdotii,
    which implement subsets of the SpacemiT Intrinsic Matrix Extension.
  quote: "This series adds support for two SpacemiT vendor extensions implementing\n\
    subsets of the SpacemiT Intrinsic Matrix Extension (IME) specification:\n\n  -\
    \ XsmtVdot v1.0: Vector Dot Product Extension, implemented by SpacemiT X60\n \
    \ - XsmtVdotII v1.0: Vector Dot Product II Extension, implemented by\n    SpacemiT\
    \ A100"
primer_expert: This patch series introduces SpacemiT vendor extensions (XsmtVdot and
  XsmtVdotII) into the RISC-V toolchain. These extensions implement subsets of the
  Intrinsic Matrix Extension (IME) specification and require updates to the assembler,
  disassembler, and related opcodes tables. The patches add new instructions and modify
  existing tools to support these new extensions.
primer_general: The RISC-V architecture allows for custom extensions to the base instruction
  set. This patch series adds support for two extensions from SpacemiT, a company
  specializing in RISC-V processors. These extensions, XsmtVdot and XsmtVdotII, provide
  specialized instructions for performing vector dot product operations, which are
  commonly used in machine learning and signal processing.
series_id: 'binutils:risc-v: add spacemit vendor extensions xsmtvdot and xsmtvdotii'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260525082008.1219171-1-zhuangqiubin@linux.spacemit.com
bugzilla_url: null
date: '2026-05-25'
is_stub: false
---

This patch series adds support for two SpacemiT vendor extensions to the RISC-V toolchain: XsmtVdot v1.0 (Vector Dot Product Extension) and XsmtVdotII v1.0. These extensions implement subsets of the SpacemiT Intrinsic Matrix Extension (IME) specification and are implemented by SpacemiT X60 and A100, respectively. The patches include updates to the assembler, disassembler, and testsuite.
