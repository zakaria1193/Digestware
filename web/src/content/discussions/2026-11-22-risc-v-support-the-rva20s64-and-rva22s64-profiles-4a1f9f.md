---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- isa
- assembler
- linker
discussion_id: 19b70c022b11119f0f21fe92ae5a5d2d08eb175f.1795334376.git.jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v2 1/3] RISC-V: Support the RVA20S64 and RVA22S64 profiles'
headline: 'RISC-V: Support the RVA20S64 and RVA22S64 profiles'
tldr: Adds support for RVA20S64 and RVA22S64 RISC-V profiles to binutils.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds new profiles to the RISC-V support, increasing complexity.
- Ensures compatibility with evolving RISC-V standards.
exchanges: []
primer_expert: This patch, the first in a series, updates binutils' RISC-V support
  by adding definitions for the RVA20S64 and RVA22S64 profiles. These profiles, detailed
  in RISC-V specifications, require specific supervisor ISA versions (Ss 1.11 and
  1.12) and extensions (e.g., Zifencei). The changes are made in `bfd/elfxx-riscv.c`
  to the `riscv_profiles_table` and in `gas/` to the `NEWS` file and test suite. This
  ensures that `gas` and `bfd` can correctly interpret and represent these profiles
  in ELF objects.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA).
- term: RVA20S64
  definition: A specific RISC-V profile for 64-bit systems, including supervisor ISA
    features.
- term: RVA22S64
  definition: A more recent RISC-V profile for 64-bit systems, potentially with updated
    supervisor ISA features.
- term: Zifencei
  definition: A RISC-V extension for instruction-fetch fence instructions.
- term: BFD
  definition: Binary File Descriptor library, used by GNU Binutils for handling object
    files.
- term: GAS
  definition: The GNU Assembler.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables
    and libraries.
series_id: 'binutils:risc-v: support the rva20s64 and rva22s64 profiles'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/19b70c022b11119f0f21fe92ae5a5d2d08eb175f.1795334376.git.jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This is the first patch in a series that adds support for the RVA20S64 and RVA22S64 RISC-V profiles. It includes the necessary supervisor ISA versions and extensions like Zifencei. The changes update the BFD ELF backend and GAS, and add new readelf tests to verify the complete ISA attributes. This patch is part of a larger effort to integrate these profiles into binutils.
