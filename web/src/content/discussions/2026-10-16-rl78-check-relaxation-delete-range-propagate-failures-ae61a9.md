---
project: binutils
subsystem: rl78
patch_id: null
tags:
- rl78
- linker
- relaxation
- error-handling
- testing
discussion_id: 20261016123644.1429854-8-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 7/8] rl78: check relaxation delete range, propagate failures'
headline: 'rl78: check relaxation delete range, propagate failures'
tldr: Strengthens RL78 relaxation by validating deletion ranges and propagating errors.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases the safety and correctness of the RL78 linker's relaxation process by
  adding essential boundary checks.
- Improves error management by propagating failure status, enabling robust handling
  of relaxation anomalies.
- Introduces regression tests to safeguard against future relaxation-related bugs.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Submits a patch to improve RL78 relaxation by validating deletion ranges,
    propagating failures, and adding a regression test.
  quote: 'Validate deletion range in elf32_rl78_relax_delete_bytes using

    _bfd_elf_relax_delete_range_ok.  Wrap SNIPNR and SNIP macros in

    do-while(0) blocks.  Propagate deletion return status in

    rl78_elf_relax_section and branch to error_return on failure.

    Add DejaGnu regression test ld-rl78/rl78-relax-underflow.exp.


    Note that crafted inputs with out-of-range relocation offsets can

    still fault during pre-d…'
primer_expert: This patch is part of a series addressing relaxation robustness for
  embedded architectures in binutils, focusing on RL78. It enhances the `elf32_rl78_relax_delete_bytes`
  function by incorporating a call to `_bfd_elf_relax_delete_range_ok`. This check
  ensures that the `addr`, `count`, and `toaddr` parameters for byte deletion are
  within the valid bounds of the section, preventing potential underflow or out-of-bounds
  writes during relaxation. Additionally, it wraps certain macros (`SNIPNR`, `SNIP`)
  in `do-while(0)` for safer use in conditional contexts. Crucially, the patch ensures
  that the suc…
primer_glossary:
- term: relaxation
  definition: A process in linkers where the linker adjusts machine code after initial
    assembly to resolve symbolic addresses and optimize code, often involving changing
    instruction lengths or operand values.
- term: RL78
  definition: A family of microcontrollers developed by Renesas Electronics. Binutils
    provides support for assembling and linking code for RL78 targets.
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
    by RL78.
series_id: 'binutils:rl78: check relaxation delete range, propagate failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-8-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch (v2 7/8) enhances the relaxation process for the RL78 architecture in binutils. It introduces validation for deletion ranges within `elf32_rl78_relax_delete_bytes` using `_bfd_elf_relax_delete_range_ok`, ensuring that byte deletions do not go out of bounds. The patch also wraps macros like SNIPNR and SNIP in `do-while(0)` blocks for safety and ensures that any failures during the deletion process are propagated to `rl78_elf_relax_section`. A new DejaGnu regression test (`rl78-relax-underflow.exp`) is added to cover these scenarios. The author notes that pre-deletion opcode rewriting issues may still exist and will be addressed separately.
