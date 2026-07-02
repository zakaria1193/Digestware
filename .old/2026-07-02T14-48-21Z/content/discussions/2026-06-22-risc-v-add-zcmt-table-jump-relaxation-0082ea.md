---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- linker
- ZCMT
- symbols
- linker scripts
discussion_id: tencent_170D8B04403D2E57660C49C0@qq.com
source_type: public_inbox
title: 'Re: [PATCH 1/3] RISC-V: Add ZCMT table jump relaxation'
headline: 'RISC-V: Add ZCMT table jump relaxation'
tldr: A patch for Binutils' RISC-V linker fixes an issue where the `__riscv_table_jump_base`
  symbol was unconditionally created, overriding linker script definitions.
proposer: Bigmagic <zhaofujin@nucleisys.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Bigmagic
  role: contributor
  position: Proposes a patch to prevent the RISC-V linker from unconditionally creating
    the `__riscv_table_jump_base` symbol, allowing linker script definitions to take
    precedence.
  quote: This patch fixes an issue where the RISC-V linker would unconditionally create
    the __riscv_table_jump_base symbol during ZCMT relaxation, even if it was already
    defined in a linker script via PROVIDE.
primer_expert: This patch targets the Binutils BFD library (`bfd/elfnn-riscv.c`) for
  the RISC-V architecture, specifically concerning Zero-Cost Jump Tables (ZCMT) relaxation.
  The `riscv_elf_late_size_sections` function is responsible for creating the `__riscv_table_jump_base`
  symbol. The original logic unconditionally called `_bfd_generic_link_add_one_symbol`.
  The fix adds a preliminary `bfd_link_hash_lookup` call to check if `RISCV_TABLE_JUMP_BASE_SYMBOL`
  already exists in the link hash table (`info->hash`). This ensures that `PROVIDE`
  directives in linker scripts, which allow users to define symbols and t…
primer_general: This is about a change to the Binutils linker for RISC-V computer
  chips. The linker is a program that combines different pieces of code into a single
  executable program. When performing a specific optimization called ZCMT (Zero-Cost
  Jump Tables) relaxation, the linker would always create a special symbol called
  `__riscv_table_jump_base`. This caused a problem for developers who wanted to define
  this symbol themselves using a 'linker script' (a file that tells the linker how
  to arrange the different parts of a program). The proposed change makes the linker
  check if this symbol already exists before creating it, allowing developers full
  control over its definition. This improves the flexibility and prevents conflicts
  when working with RISC-V programs that use these advanced optimizations.
series_id: 'binutils:risc-v: add zcmt table jump relaxation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/tencent_170D8B04403D2E57660C49C0@qq.com
bugzilla_url: null
date: '2026-06-22'
is_stub: false
---

This patch for the Binutils RISC-V linker addresses an issue where the `__riscv_table_jump_base` symbol was being created unconditionally during ZCMT relaxation, regardless of whether it was already defined in a linker script. The fix modifies `riscv_elf_late_size_sections` to first check for an existing definition of `__riscv_table_jump_base` before creating it. This change ensures that linker script-provided definitions are respected, offering greater flexibility and preventing symbol redefinition errors for RISC-V projects utilizing table jump relaxation.
