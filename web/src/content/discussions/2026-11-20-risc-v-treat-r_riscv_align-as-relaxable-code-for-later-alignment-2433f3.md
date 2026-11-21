---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- alignment
- relaxation
- relocation
discussion_id: 20261120111841.3400822-4-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 3/3] RISC-V: Treat R_RISCV_ALIGN as relaxable code for later alignment'
headline: 'RISC-V: Treat R_RISCV_ALIGN as relaxable code for later alignment'
tldr: Make R_RISCV_ALIGN relocations in RISC-V act as relaxable code to allow subsequent
  alignments.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures that alignment is correctly handled even when `R_RISCV_ALIGN` relocations
  are involved.
- May add complexity to the alignment logic by treating `R_RISCV_ALIGN` as a relaxable
  point.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Proposes to mark R_RISCV_ALIGN as relaxable code, so that subsequent alignment
    in norelax code is handled correctly.
  quote: null
primer_expert: This patch modifies `gas/config/tc-riscv.c` to set the `last_relax`
  flag on the segment information when an `R_RISCV_ALIGN` relocation is generated.
  This ensures that the assembler treats the `R_RISCV_ALIGN` as a relaxable point,
  allowing subsequent alignment directives in `norelax` code to be correctly handled
  by the linker, preventing misalignments that could occur if the linker adjusts the
  section size due to the `R_RISCV_ALIGN` itself.
primer_glossary:
- term: R_RISCV_ALIGN
  definition: A relocation type in RISC-V used by the assembler and linker to enforce
    alignment. It typically pads with no-operation (nop) instructions to meet a specified
    alignment boundary.
- term: Relaxable code
  definition: Code segments or instructions that the linker can modify or adjust (e.g.,
    change addresses, padding) to optimize for space or performance, or to satisfy
    alignment requirements.
- term: norelax code
  definition: Code segments where the assembler and linker are instructed not to perform
    relaxation, meaning their layout and addresses are fixed.
- term: Section size
  definition: The total number of bytes occupied by a section within an object file
    or executable. Alignment directives and relocations can affect this size.
series_id: 'binutils:risc-v: treat r_riscv_align as relaxable code for later alignment'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120111841.3400822-4-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch ensures that R_RISCV_ALIGN relocations are treated as relaxable code by the assembler. This is necessary because an R_RISCV_ALIGN relocation itself can alter the section size. Consequently, subsequent alignment directives in non-relaxable code may require their own R_RISCV_ALIGN relocation to maintain correct alignment, even if no instructions immediately preceding them are relaxable.
