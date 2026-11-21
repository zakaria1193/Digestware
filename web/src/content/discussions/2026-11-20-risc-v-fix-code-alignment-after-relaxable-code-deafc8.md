---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- alignment
- relaxation
- rvc
discussion_id: 20261120111841.3400822-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 0/3] RISC-V: Fix code alignment after relaxable code'
headline: 'RISC-V: Fix code alignment after relaxable code'
tldr: Series of patches to fix RISC-V code alignment issues caused by instruction
  relaxation and compressed instruction encoding.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves code alignment correctness for RISC-V, preventing linker errors and misaligned
  labels.
- Adds complexity to the assembler's alignment logic to handle interactions between
  relaxation, RVC, and `norelax` modes.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Submits a 3-patch series to fix RISC-V code alignment issues arising from
    relaxation and RVC code.
  quote: null
primer_expert: 'This patch series addresses a subtle bug in the RISC-V assembler (`gas`)
  concerning code alignment. The core problem is that `gas` determines alignment padding
  based solely on the relaxation and RVC state at the alignment point itself. However,
  if relaxable code (like RVC instructions or `R_RISCV_ALIGN` relocations) precedes
  an alignment directive in `norelax` mode, the linker can still adjust the exact
  code addresses, effectively moving the alignment point. This series introduces three
  patches: 1) ensures `R_RISCV_ALIGN` is emitted in `norelax` sections following relaxable
  code; 2) accounts…'
primer_glossary:
- term: RVC
  definition: RISC-V Compressed. A standard extension to the RISC-V ISA that provides
    16-bit compressed instruction encodings for common operations, improving code
    density.
- term: Relaxation
  definition: A process during assembly and linking where the assembler or linker
    can adjust instruction encodings or code addresses to optimize for space or performance.
    This can change the exact byte offsets of code.
- term: R_RISCV_ALIGN
  definition: A relocation type in RISC-V used by the assembler and linker to enforce
    alignment. It typically pads with no-operation (nop) instructions to meet a specified
    alignment boundary.
- term: norelax code
  definition: Code segments where the assembler and linker are instructed not to perform
    relaxation, meaning their layout and addresses are fixed.
- term: Alignment directive
  definition: An assembler command (e.g., `.balign`) that specifies the required memory
    alignment for the subsequent code or data.
series_id: 'binutils:risc-v: fix code alignment after relaxable code'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120111841.3400822-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This series of three patches aims to resolve issues with code alignment in the RISC-V assembler, particularly when instruction relaxation or RVC (RISC-V Compressed) instructions are involved. The assembler's current logic only considers the immediate relaxation and RVC state, failing to account for how the linker might shift alignment points due to preceding relaxable code. This can lead to misaligned labels or linker errors. The patches introduce changes to ensure proper alignment by emitting specific relocations and accounting for worst-case scenarios.
