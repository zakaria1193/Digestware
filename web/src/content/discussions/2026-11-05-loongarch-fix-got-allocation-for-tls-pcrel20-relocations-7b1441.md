---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- linker
- TLS
- GOT
discussion_id: 20261105113149.38514-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Fix GOT allocation for TLS PCREL20 relocations'
headline: 'LoongArch: Fix GOT allocation for TLS PCREL20 relocations'
tldr: A patch for LoongArch in Binutils ensures that GOT entries for TLS PCREL20 relocations
  are recorded, preventing link-time crashes.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Correctly handling GOT entries for TLS PCREL20 relocations vs. potential complexity
  in relocation processing.
- Preventing link-time crashes vs. ensuring efficient resource (GOT entry) allocation.
exchanges:
- author: zhaozhou
  role: proposer
  position: Submitted a patch to record GOT references for LoongArch TLS PCREL20 relocations,
    preventing link crashes.
  quote: 'Record GOT references for R_LARCH_TLS_{LD,GD,DESC}_PCREL20_S2 in

    loongarch_elf_check_relocs, otherwise unallocated GOT entries will cause

    the link crash when reaching final relocation.


    PR ld/34809'
primer_expert: This patch modifies the `bfd/elfnn-loongarch.c` file in Binutils to
  correctly handle Global Offset Table (GOT) allocation for Thread-Local Storage (TLS)
  PCREL20 relocations on the LoongArch architecture. The `loongarch_elf_check_relocs`
  function is updated to register references for specific TLS relocation types (`R_LARCH_TLS_{LD,GD,DESC}_PCREL20_S2`).
  Without this, the linker would fail to allocate GOT entries for these relocations,
  leading to a crash when attempting to resolve them later in the linking process.
  New test cases are added to cover this scenario, addressing PR ld/34809.
primer_glossary:
- term: LoongArch
  definition: A RISC instruction set architecture developed in China, supported by
    Binutils and GCC.
- term: GOT
  definition: Global Offset Table. A table used in position-independent code to store
    addresses of global variables and functions, allowing them to be accessed indirectly.
- term: TLS
  definition: Thread-Local Storage. A mechanism that allows each thread in a program
    to have its own copy of a variable. Accessing TLS variables often involves special
    relocation types.
- term: PCREL20
  definition: A type of PC-relative relocation that uses a 20-bit signed displacement.
    This indicates a reference relative to the program counter.
- term: relocation
  definition: Information stored in an object file that tells the linker how to modify
    certain memory addresses or data when creating the final executable or shared
    library. This is necessary for position-independent code and references to external
    symbols.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a common interface for reading and writing various executable file formats (like
    ELF, COFF, a.out).
- term: PR ld/34809
  definition: Patch Request or Problem Report number 34809 within the ld (linker)
    component of GNU Binutils. This identifier refers to a specific bug or feature
    request.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261105113149.38514-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the LoongArch target for Binutils where Global Offset Table (GOT) entries for TLS (Thread-Local Storage) PCREL20 relocations were not being properly recorded. The `loongarch_elf_check_relocs` function now accounts for `R_LARCH_TLS_{LD,GD,DESC}_PCREL20_S2` relocations. Failure to do so would result in unallocated GOT entries, leading to link-time crashes during the final relocation phase. The change includes updates to the `bfd/elfnn-loongarch.c` file and adds new test cases to verify the fix.
