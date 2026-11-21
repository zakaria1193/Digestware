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
discussion_id: 20261120111841.3400822-2-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 1/3] RISC-V: Emit R_RISCV_ALIGN in norelax code after relaxable code'
headline: 'RISC-V: Emit R_RISCV_ALIGN in norelax code after relaxable code'
tldr: Ensure RISC-V assembler emits R_RISCV_ALIGN relocations even in 'norelax' sections
  if relaxable code preceded them.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Correctly handles alignment in complex scenarios involving both relaxable and non-relaxable
  code within the same section.
- Ensures that the linker's potential adjustments to alignment points are respected,
  preventing errors.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Proposes to emit R_RISCV_ALIGN in norelax code after relaxable code, to
    handle linker-shifted alignment points.
  quote: null
primer_expert: This patch modifies `gas/config/tc-riscv.c` to ensure that if `riscv_opts.relax`
  is true (meaning relaxation is enabled for the section) and the current fragment
  is `last_relax`, then an `R_RISCV_ALIGN` relocation is appended. This is done even
  if the `.option norelax` directive is active for the subsequent code. This addresses
  a scenario where relaxable code earlier in a section causes the linker to shift
  the alignment point, leading to incorrect padding or errors if the assembler doesn't
  account for this potential shift by emitting an `R_RISCV_ALIGN` relocation.
primer_glossary:
- term: R_RISCV_ALIGN
  definition: A relocation type in RISC-V used by the assembler and linker to enforce
    alignment. It typically pads with no-operation (nop) instructions to meet a specified
    alignment boundary.
- term: norelax code
  definition: Code segments where the assembler and linker are instructed not to perform
    relaxation, meaning their layout and addresses are fixed.
- term: Relaxable code
  definition: Code segments or instructions that the linker can modify or adjust (e.g.,
    change addresses, padding) to optimize for space or performance, or to satisfy
    alignment requirements.
- term: Alignment padding
  definition: Extra bytes (often no-operation instructions) inserted by the assembler
    or linker to ensure that subsequent code or data starts at a memory address aligned
    to a specific boundary (e.g., 4-byte, 8-byte).
series_id: 'binutils:risc-v: emit r_riscv_align in norelax code after relaxable code'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120111841.3400822-2-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch modifies the RISC-V assembler to emit R_RISCV_ALIGN relocations even when the current section is marked as `norelax` (non-relaxable). This is crucial because if relaxable code appeared earlier in the same section, the linker might still shift the alignment point. Without this change, alignment directives like `.balign 8` in `norelax` code following relaxable code could lead to misaligned labels or linker errors due to the unexpected movement of the alignment boundary.
