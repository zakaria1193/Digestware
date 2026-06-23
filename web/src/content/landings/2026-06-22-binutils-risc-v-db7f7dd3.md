---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- atomic operations
- memory model
- multi-threading
- concurrency
commit_hash: db7f7dd31576bc2e5c004aa4484fe75265cc1ea2
source_type: public_inbox
author: Jeff Law <law@sourceware.org>
headline: Binutils gains support for the RISC-V Zalasr atomic extension
tldr: Binutils now supports the RISC-V Zalasr extension, enabling the use of load-acquire
  and store-release instructions for robust multi-threaded programming.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit integrates the RISC-V Zalasr extension into GNU Binutils.
  The Zalasr extension introduces new atomic load-acquire and store-release instructions,
  essential for memory ordering in multi-core systems. The changes involve defining
  new match and mask opcodes in `include/opcode/riscv-opc.h`, updating `opcodes/riscv-opc.c`
  for instruction definitions, and modifying `bfd/elfxx-riscv.c` to recognize the
  Zalasr extension within ELF object files. The `riscv_multi_subset_supports` and
  `riscv_multi_subset_supports_ext` functions in `bfd/elfxx-riscv.c` are updated to
  account for this new exten…
primer_general: This update adds support for a new set of instructions, called the
  Zalasr extension, to RISC-V processors within Binutils. Imagine you have several
  parts of a program (threads) running at the same time, all trying to access and
  modify the same data. Without proper coordination, these threads can interfere with
  each other, leading to incorrect results (this is called a data race). The Zalasr
  extension provides special "atomic" instructions, specifically "load-acquire" and
  "store-release." These instructions ensure that memory operations happen in a specific
  order, creating a fence in the program's execution. A "load-acquire" instruction
  makes sure that all memory operations after it happen after the load itself and
  are visible to other threads. A "store-release" instruction ensures that all memory
  operations before it are completed and visible to other threads before the store
  itself happens. This guarantees that your multi-threaded programs will behave predictably
  and correctly, which…
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260622142239.491864B9DB72@sourceware.org
date: '2026-06-22'
is_stub: false
---

This update to Binutils introduces support for the RISC-V Zalasr extension, which provides atomic load-acquire and store-release instructions. These instructions are crucial for writing correct and performant code in multi-threaded environments, ensuring proper memory synchronization and preventing data races. The change impacts the assembler, disassembler, and ELF object file handling for RISC-V architectures.
