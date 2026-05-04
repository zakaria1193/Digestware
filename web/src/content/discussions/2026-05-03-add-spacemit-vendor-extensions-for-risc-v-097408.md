---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- extensions
- vectorization
- spacemit
discussion_id: 20260503143354.142807-1-zhuangqiubin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v5 0/2] RISC-V: Add SpacemiT IME vendor extensions (xsmtvdot, xsmtvdotii)'
headline: Add SpacemiT vendor extensions for RISC-V
tldr: Adds support for SpacemiT's xsmtvdot and xsmtvdotii vector dot product extensions
  to the RISC-V assembler.
proposer: Mark Zhuang <zhuangqiubin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in the assembler to support new instructions.
- Potential performance improvements for code using the new vector dot product instructions
  on SpacemiT hardware.
- Increased code size in the assembler due to added instruction decoding logic.
exchanges:
- author: Mark Zhuang <zhuangqiubin@linux.spacemit.com>
  role: proposer
  position: Proposes adding support for the xsmtvdot and xsmtvdotii extensions, which
    are subsets of SpacemiT's IME specification.
  quote: "This series adds support for two SpacemiT vendor extensions implementing\
    \ subsets of the SpacemiT Intrinsic Matrix Extension (IME) specification:\n\n\
    \  - XsmtVdot v1.0: Vector Dot Product Extension, implemented by SpacemiT X60\n\
    \  - XsmtVdotII v1.0: Vector Dot Product II Extension, implemented by\n    SpacemiT\
    \ A100"
primer_expert: This series adds support for SpacemiT vendor extensions to the RISC-V
  assembler, specifically xsmtvdot and xsmtvdotii. These extensions define new vector
  dot product instructions. The patch modifies gas/config/tc-riscv.c, include/opcode/riscv-opc.h,
  and the test suite, and adds documentation to gas/doc/c-riscv.texi.
primer_general: The RISC-V architecture allows for custom extensions to the base instruction
  set. These extensions can add new instructions or modify existing ones to improve
  performance for specific workloads. This patch series adds support in the GNU assembler
  (gas) for two extensions defined by SpacemiT, a vendor that produces RISC-V processors.  These
  extensions implement vector dot product operations, which are commonly used in machine
  learning and signal processing.
series_id: 'binutils:risc-v: add spacemit ime vendor extensions (xsmtvdot, xsmtvdotii)'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260503143354.142807-1-zhuangqiubin@linux.spacemit.com
bugzilla_url: null
date: '2026-05-03'
---

This patch series adds support for the xsmtvdot and xsmtvdotii extensions to the RISC-V assembler. These extensions implement subsets of the SpacemiT Intrinsic Matrix Extension (IME) specification, specifically the Vector Dot Product and Vector Dot Product II extensions. The series includes updates to the assembler, documentation, and test suite to incorporate the new instructions.
