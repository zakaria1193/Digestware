---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- risc-v
- assembler
- supervisor
commit_hash: edf055957924fe69920126c2c1b18fddfce31c45
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: RISC-V assembler now implies Zicsr extension for supervisor ISA
tldr: 'RISC-V assembler: "Ss" now implies "Zicsr" for supervisor ISA support.'
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change modifies the `riscv_implicit_subsets` table in `bfd/elfxx-riscv.c`.
  The `Ss` subset, representing supervisor functionality, now has an explicit dependency
  on `Zicsr` (CSR instructions). This aligns the assembler's understanding of RISC-V
  profiles with the supervisor architecture requirements, ensuring correct instruction
  encoding and ELF attribute generation for supervisor-mode code.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: Zicsr
  definition: A RISC-V standard extension that adds instructions for accessing Control
    and Status Registers (CSRs). CSRs control various aspects of the processor's operation
    and state.
- term: Ss
  definition: A RISC-V ISA subset that indicates supervisor-level functionality. This
    implies the need for instructions and features used in operating system kernels
    and other privileged software.
- term: RV64I
  definition: The base integer instruction set for 64-bit RISC-V processors.
- term: CSR
  definition: Control and Status Register. Special-purpose registers used to control
    processor behavior and report status.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261123065547.3400A4FC39DA@sourceware.org
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

The RISC-V assembler now correctly implies the Zicsr extension when the supervisor ISA subset "Ss" is selected. This ensures that selecting a supervisor ISA version on RV64I is sufficient to assemble Control and Status Register (CSR) access instructions, which are required for supervisor operations.
