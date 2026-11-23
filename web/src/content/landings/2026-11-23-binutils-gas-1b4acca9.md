---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- risc-v
- extensions
- memory management
commit_hash: 1b4acca9ab1bd00f73e81252510cab503fae0cac
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: RISC-V Svukte extension support added
tldr: Binutils now supports the RISC-V Svukte extension for address-independent fault
  latency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds the `Svukte` extension to `bfd/elfxx-riscv.c`, registering
  version 1.0, its implicit dependency on `Zicsr`, and a conflict with `RV32`. The
  `riscv_parse_check_conflicts` function is updated to reject `Svukte` on `RV32`.
  New tests in `gas/testsuite/gas/riscv/` cover its RV64 attribute, RV32 rejection,
  and the `-march` help output. The `NEWS` file is also updated.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: Svukte
  definition: A RISC-V standard extension related to address-independent fault latency.
    It implies the use of certain memory management features.
- term: Zicsr
  definition: A RISC-V standard extension that adds instructions for accessing Control
    and Status Registers (CSRs). CSRs control various aspects of the processor's operation
    and state.
- term: RV32
  definition: The base integer instruction set for 32-bit RISC-V processors.
- term: Sv39
  definition: A RISC-V memory management feature that defines a 39-bit virtual address
    translation scheme.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils to handle
    various object file formats.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261123065531.D8E2648EFB5B@sourceware.org
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

Support for the RISC-V `Svukte` extension, which deals with address-independent fault latency, has been added. Version 1.0 of this extension implies `Zicsr` and is incompatible with the 32-bit architecture (`RV32`) as it requires `Sv39`. The changes include updates to assembler and BFD library logic and new test cases for validation.
