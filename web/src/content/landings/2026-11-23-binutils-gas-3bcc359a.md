---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- risc-v
- profiles
- extensions
commit_hash: 3bcc359a28e67919b5ee598ce44a6a0d5cfce7ca
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: RISC-V profiles RVA23S64 and RVB23S64 now require Zifencei and SS1P13 extensions
tldr: RISC-V profiles RVA23S64 and RVB23S64 now include Zifencei and SS1P13 extensions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates `bfd/elfxx-riscv.c` by adding `_ss1p13` and `_zifencei`
  to the `riscv_profiles_table` entries for `RVA23S64` and `RVB23S64`. It also updates
  gas test suite cases (`gas/testsuite/gas/riscv/attribute-rva23s.d` and `attribute-rvb23s.d`)
  to verify the ELF architecture attributes reflect these additions. This change ensures
  compliance with the RVA23 and RVB23 profile specifications.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: Zifencei
  definition: A RISC-V standard extension that provides an instruction-fetch fence,
    ensuring that previously issued instruction fetches are completed before subsequent
    ones are initiated.
- term: Ss1p13
  definition: A RISC-V ISA extension indicating supervisor-level functionality with
    version 1.13. This refers to a specific revision of the supervisor-mode architecture.
- term: RVA23S64
  definition: A RISC-V application profile for 64-bit systems, targeting embedded
    applications, including supervisor-mode features.
- term: RVB23S64
  definition: A RISC-V profile for 64-bit systems, potentially related to embedded
    or real-time applications, including supervisor-mode features.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261123065542.1940E46F7C11@sourceware.org
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

The RISC-V assembler now supports the RVA23S64 and RVB23S64 profiles by including the `Zifencei` (instruction-fetch fence) and `Ss1p13` (supervisor ISA version 1.13) extensions. This ensures that the assembler accepts `fence.i` instructions and correctly records these extensions in the ELF architecture attribute for these profiles.
