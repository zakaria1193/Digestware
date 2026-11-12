---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- relocations
- VMA
- relaxation
discussion_id: 20261111133209.1242949-1-xeonacid@archlinuxcn.org
source_type: public_inbox
title: '[PATCH v2] RISC-V: Add no-op relax pass 0 to update section VMAs before shortening
  [PR34979]'
headline: 'RISC-V: Add no-op relax pass 0 to update section VMAs before shortening
  [PR34979]'
tldr: Introduces a no-op relaxation pass at the beginning of the RISC-V linker's relaxation
  process to ensure section VMAs are consistently updated before code short…
proposer: Zhuo Zhi <xeonacid@archlinuxcn.org>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Introduces a new relaxation pass for RISC-V, adding a small overhead.
- Fixes a critical relocation overflow bug that could prevent linking.
- Ensures consistent VMA handling during relaxation.
exchanges: []
primer_expert: 'This patch resolves a specific issue in the RISC-V linker''s relaxation
  mechanism. Relaxation is a multi-pass process where the linker adjusts instruction
  offsets and lengths to fit within available space, particularly for PC-relative
  branches and loads. The problem arises in the context of program header manipulation:
  when `elf_program_header_size` increases, the linker re-evaluates section VMAs.
  If this VMA update happens *after* an earlier section has already been processed
  by the relaxation ''shorten'' pass but *before* a later section is processed, the
  earlier section''s VMA might be ahead o…'
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles.
- term: Relaxation
  definition: A linker optimization process where instructions are adjusted (e.g.,
    shortened or lengthened) to fit within specific encoding constraints, often related
    to PC-relative addressing. This typically involves multiple passes.
- term: VMA
  definition: Virtual Memory Address. The address of a location in memory as seen
    by a program.
- term: Section
  definition: A part of an object file or executable that contains code, data, or
    other information. Examples include .text (code), .data (initialized data), and
    .bss (uninitialized data).
- term: PC-relative offset
  definition: An offset calculated relative to the current value of the Program Counter
    (PC). This is common for position-independent code.
- term: auipc+jalr
  definition: A common instruction pair in RISC-V used to load an immediate value
    into a register and then perform an indirect jump. This pair can sometimes be
    shortened to a single `jal` instruction if the target is within range.
- term: R_RISCV_JAL
  definition: A RISC-V relocation type used for jump and link (JAL) instructions,
    typically for PC-relative jumps.
- term: Program Header
  definition: A structure in an ELF file that describes segments, which are mappings
    of sections into memory during execution.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111133209.1242949-1-xeonacid@archlinuxcn.org
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch addresses a relocation overflow issue on RISC-V (PR ld/34979) caused by inconsistent Virtual Memory Address (VMA) updates during the linker's relaxation process. When segment headers grow, output section VMAs are updated. If a later section's VMA is still stale when an earlier section needs to calculate relative offsets, it can lead to incorrect shortening of instructions (e.g., auipc+jalr to jal), causing relocation overflows. The fix adds a no-op 'layout' pass as the first relaxation pass (pass 0) to ensure all section VMAs are recalculated consistently before the 'shorten' pass, resolving the problem without affecting other targets.
