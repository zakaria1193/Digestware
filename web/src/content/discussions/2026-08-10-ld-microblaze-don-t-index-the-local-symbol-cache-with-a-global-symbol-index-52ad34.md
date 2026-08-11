---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- microblaze
- ELF
- relaxation
discussion_id: 20260810060011.4186926-1-neal.frager@amd.com
source_type: public_inbox
title: '[PATCH v1 1/1] ld: microblaze: don''t index the local symbol cache with a
  global symbol index'
headline: 'ld: microblaze: don''t index the local symbol cache with a global symbol
  index'
tldr: Fix an out-of-bounds read in microblaze ELF relaxation that silently corrupts
  relocation addends.
proposer: Neal Frager <neal.frager@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds a small performance overhead to the `microblaze_elf_relax_section` function
  due to the added bounds check.
- Fixes a silent miscompilation bug, improving code correctness and reliability for
  the microblaze target.
exchanges:
- author: Neal Frager <neal.frager@amd.com>
  role: proposer
  position: Proposes to add a missing bounds check to the microblaze ELF relaxation
    code to prevent out-of-bounds reads that corrupt relocation addends.
  quote: microblaze_elf_relax_section() was copied from sh_elf_relax_delete_bytes()
    in 2009 (7ba29e2a41) but the copy dropped a bounds check that was already present
    in the sh original.  This adds the missing two-line guard from bfd/elf32-sh.c:1227-1228,
    preventing an out-of-bounds read that silently corrupts relocation addends.
primer_expert: The microblaze ELF relaxation code in binutils' ld is missing a bounds
  check, analogous to the one present in the sh ELF relaxation code. This allows an
  out-of-bounds read when indexing the local symbol buffer `isymbuf` with a global
  symbol index. If the out-of-bounds data resembles a local symbol for the current
  section, relocation addends can be miscalculated, causing silent code corruption,
  particularly with structure member accesses at optimization levels like -O2.
primer_glossary:
- term: ELF relaxation
  definition: A linker optimization pass that adjusts relocation addends to account
    for code/data size changes during linking. This is crucial for certain instruction
    sets and addressing modes to maintain correctness.
- term: relocation addend
  definition: A value embedded in an object file that is added to a symbol's address
    to form the final address of a reference. During relaxation, this addend might
    be modified.
- term: microblaze
  definition: A 32-bit RISC soft processor core from Xilinx, often used in FPGAs.
    Binutils supports targeting this architecture.
- term: isymbuf
  definition: In binutils' BFD library, this likely refers to a buffer holding local
    symbols for a specific section, as opposed to global symbols in the main symbol
    table.
series_id: 'binutils:ld: microblaze: don''t index the local symbol cache with a global
  symbol index'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260810060011.4186926-1-neal.frager@amd.com
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the microblaze ELF relaxation code where an out-of-bounds read can corrupt relocation addends, leading to silent miscompilations. The issue arises from indexing a local symbol cache with a global symbol index without proper bounds checking. The fix restores a missing bounds check, preventing incorrect adjustment of relocation addends and ensuring data structure accesses are compiled correctly.
