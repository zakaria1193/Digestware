---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- relaxation
- error-handling
- testing
discussion_id: 20261016123644.1429854-9-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 8/8] riscv: check relaxation delete range, propagate failures'
headline: 'riscv: check relaxation delete range, propagate failures'
tldr: Enhances RISC-V relaxation handling by validating deletion ranges and propagating
  errors.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves the robustness and correctness of the RISC-V linker's relaxation process
  by adding crucial boundary checks.
- Enhances error reporting by propagating failure status, allowing for cleaner termination
  of the linking process when relaxation issues occur.
- Adds regression tests to prevent future regressions in relaxation handling.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Submits the final patch in a series to improve RISC-V relaxation by validating
    deletion ranges, propagating failures, and adding a regression test.
  quote: 'In _riscv_relax_delete_bytes, validate deletion range using

    _bfd_elf_relax_delete_range_ok before computing bytes_to_move.

    Propagate deletion return values to callers in _bfd_riscv_relax_tlsdesc

    and _bfd_riscv_relax_pc.

    Add DejaGnu regression test ld-riscv-elf/riscv-relax-underflow.exp.'
primer_expert: 'This patch is part of a series addressing relaxation issues in the
  RISC-V linker backend of binutils. Specifically, it targets the `_riscv_relax_delete_bytes`
  function, which is responsible for removing code bytes during relaxation. The key
  changes are: 1) Introducing a call to `_bfd_elf_relax_delete_range_ok` to validate
  the `addr`, `count`, and `toaddr` parameters before performing the deletion, preventing
  potential underflows or out-of-bounds operations. 2) Ensuring that the boolean return
  value of `_riscv_relax_delete_bytes` is checked and propagated by its callers, `_bfd_riscv_relax_tlsd…'
primer_glossary:
- term: relaxation
  definition: A process in linkers where the linker adjusts machine code after initial
    assembly to resolve symbolic addresses and optimize code, often involving changing
    instruction lengths or operand values.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles. Binutils provides linker support for RISC-V.
- term: linker
  definition: A program that combines one or more object files (produced by an assembler
    or compiler) into a single executable file, library file, or another object file.
    It resolves symbolic references between files.
- term: underflow
  definition: In this context, an underflow during relaxation likely refers to an
    operation that results in an invalid or nonsensical memory address or size calculation,
    potentially due to incorrect calculations or boundary violations.
- term: DejaGnu
  definition: A testing framework developed by the Free Software Foundation for testing
    C compilers and other programming tools. It provides a common infrastructure for
    writing test harnesses.
- term: BFD
  definition: Binutils 'Binary File Descriptor' library. It provides a common interface
    for reading and writing various object file formats, including ELF files used
    by RISC-V.
series_id: 'binutils:riscv: check relaxation delete range, propagate failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-9-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch, the final in a series (v2 8/8), strengthens the relaxation process for RISC-V binaries by adding range validation to byte deletion operations within `_riscv_relax_delete_bytes`. It utilizes `_bfd_elf_relax_delete_range_ok` to ensure deletions occur within valid bounds before calculating how many bytes to move. Furthermore, the patch ensures that any failures during this deletion process are propagated to the calling functions (`_bfd_riscv_relax_tlsdesc` and `_bfd_riscv_relax_pc`). A new DejaGnu regression test (`riscv-relax-underflow.exp`) is included to specifically check for and prevent relaxation underflow issues.
