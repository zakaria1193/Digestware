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
discussion_id: 20261120111841.3400822-3-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 2/3] RISC-V: Use the 2-byte worst case for alignment in norvc code'
headline: 'RISC-V: Use the 2-byte worst case for alignment in norvc code'
tldr: Adjust RISC-V assembler alignment to account for potential 2-byte shifts from
  RVC relaxation.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases the worst-case alignment padding in some scenarios, potentially slightly
  increasing code size.
- Ensures correct alignment and prevents linker errors or misaligned labels.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Proposes to use the 2-byte worst-case alignment for RISC-V norvc code
    when RVC code is present, to correct for potential shifts caused by RVC relaxation.
  quote: null
primer_expert: This patch series addresses alignment issues in the RISC-V assembler
  (`gas`) related to instruction relaxation. Specifically, it tackles problems arising
  when RVC (RISC-V Compressed) instructions are relaxed to their non-compressed equivalents,
  which can shift code by up to two bytes. This shift affects subsequent alignment
  directives (`.balign`) in `norvc` (non-compressed) regions, potentially causing
  the assembler to reserve too few no-operation (nop) instructions for `R_RISCV_ALIGN`
  relocations, or to miss them entirely when a 4-byte alignment is requested. The
  fix adjusts the alignment ca…
primer_glossary:
- term: RVC
  definition: RISC-V Compressed. A standard extension to the RISC-V ISA that provides
    16-bit compressed instruction encodings for common operations, improving code
    density.
- term: norvc
  definition: Indicates that the assembler should not emit RVC (compressed) instructions
    for the following code, even if the architecture supports it.
- term: R_RISCV_ALIGN
  definition: A relocation type in RISC-V used by the assembler and linker to enforce
    alignment. It typically pads with no-operation (nop) instructions to meet a specified
    alignment boundary.
- term: Relaxation
  definition: A process during assembly and linking where the assembler or linker
    can adjust instruction encodings or code addresses to optimize for space or performance.
    This can change the exact byte offsets of code.
series_id: 'binutils:risc-v: use the 2-byte worst case for alignment in norvc code'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120111841.3400822-3-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch addresses an alignment issue in RISC-V code where the relaxed RVC (RISC-V Compressed) instructions can shift code by up to 2 bytes. This shift can cause incorrect alignment padding, potentially leading to alignment of 4 bytes with no R_RISCV_ALIGN relocation. The change ensures that the assembler considers the 2-byte worst-case scenario when RVC code is present, thereby correcting the alignment padding.
