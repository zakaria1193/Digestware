---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- risc-v
- profiles
- supervisor
- extensions
commit_hash: c876d9f45414d5ba01a615e306c41abdbb64b483
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: RISC-V profiles RVA20S64 and RVA22S64 now supported
tldr: Binutils now supports the RISC-V RVA20S64 and RVA22S64 profiles.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces support for `rva20s64` and `rva22s64` in `bfd/elfxx-riscv.c`,
  adding them to `riscv_profiles_table`. These profiles require specific supervisor
  extensions (`ss1p11`, `ss1p12`) and standard extensions like `zifencei`, `zihpm`,
  `sscounterenw`, `svpbmt`, and `svinval`. New test cases in `gas/testsuite/gas/riscv/`
  check the ELF architecture attributes for these profiles. The `NEWS` file is also
  updated.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: RVA20S64
  definition: A RISC-V application profile for 64-bit systems, including supervisor-mode
    features, based on the RVA20 specification.
- term: RVA22S64
  definition: A RISC-V application profile for 64-bit systems, including supervisor-mode
    features, based on the RVA22 specification.
- term: Ss1p11
  definition: RISC-V supervisor extension version 1.11.
- term: Ss1p12
  definition: RISC-V supervisor extension version 1.12.
- term: Zifencei
  definition: A RISC-V standard extension that provides an instruction-fetch fence.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils to handle
    various object file formats.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261123065536.F21BB48EEBC3@sourceware.org
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

The RISC-V assembler and BFD library now support the RVA20S64 and RVA22S64 profiles. This includes adding the required supervisor ISA versions (Ss 1.11 and 1.12 respectively), the Zifencei extension, and other specific extensions like Zihpm, Sscounterenw, Svpbmt, and Svinval for RVA22S64. New `readelf` tests verify the complete ISA attributes.
