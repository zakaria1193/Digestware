---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- architecture
- assembler
- elf
commit_hash: b16f10037c4814ab03416a4ab143337591881e2b
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: Add Sspmp extension support to RISC-V
tldr: Binutils now supports the RISC-V Sspmp, Sspmpen, and Smpmpdeleg extensions and
  their associated CSRs.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Support for the RISC-V Sspmp (Scalar Symmetric Memory Protection),
  Sspmpen (Scalar Symmetric Memory Protection Enable), and Smpmpdeleg (Symmetric Memory
  Protection Delegation) extensions and their CSRs is added. This involves updates
  to BFD's `riscv_implicit_subsets` and `riscv_supported_std_s_ext` in `elfxx-riscv.c`,
  and to GAS's CSR handling in `tc-riscv.c` and `riscv-opc.h`. New test cases are
  included in the GAS test suite.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computing principles. It is designed to be simple, modular, and
    extensible.
- term: Sspmp extension
  definition: A proposed extension for the RISC-V architecture related to memory protection,
    likely involving scalar operations for managing protection attributes.
- term: CSR
  definition: Control and Status Register. Special registers in a processor architecture
    used for controlling system functions, managing interrupts, and monitoring status.
    In RISC-V, CSRs are accessed via specific instructions.
- term: BFD
  definition: The 'Binary File Descriptor' library. It's a core component of GNU Binutils,
    providing a common interface for reading and writing various object file formats,
    such as ELF, COFF, and a.out.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps, primarily used on Unix-like operating
    systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260914100959.5ACAF4BA79A8@sourceware.org
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This commit introduces support for the RISC-V Sspmp, Sspmpen, and Smpmpdeleg extensions, including their control and status registers (CSRs). The changes affect BFD for ELF parsing and GAS for assembler syntax and CSR handling, along with corresponding test suite updates.
