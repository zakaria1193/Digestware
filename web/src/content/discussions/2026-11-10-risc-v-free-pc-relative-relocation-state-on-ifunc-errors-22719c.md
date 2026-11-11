---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- memory leak
- relocation
- ifunc
discussion_id: 20261110201522.2149977-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/5] RISC-V: free PC-relative relocation state on IFUNC errors'
headline: 'RISC-V: free PC-relative relocation state on IFUNC errors'
tldr: Fixes a memory leak in RISC-V relocation handling by ensuring PC-relative state
  is freed on IFUNC error paths.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixes a memory leak, improving resource management and stability, with no negative
  tradeoffs.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Corrects a memory leak in `riscv_elf_relocate_section` by adding a `goto
    out;` to free PC-relative relocation state on IFUNC error paths.
  quote: 'The RISC-V relocation function allocates PC-relative relocation state at

    entry.  On error paths for STT_GNU_IFUNC symbols, the function previously

    returned false directly without freeing this state.


    Branch to the existing out label to free the PC-relative relocation state

    before exiting.'
primer_expert: This patch addresses a resource management issue in the RISC-V relocation
  code within `bfd/elfnn-riscv.c`. When handling `STT_GNU_IFUNC` symbols, certain
  error conditions caused the function `riscv_elf_relocate_section` to return prematurely
  without releasing dynamically allocated PC-relative relocation state. The fix ensures
  that control flow now correctly jumps to the `out` label, which contains the deallocation
  logic, thus preventing memory leaks.
primer_glossary:
- term: STT_GNU_IFUNC
  definition: A symbol type used in ELF files to represent indirect functions, allowing
    for runtime selection of function implementations. Binutils needs to handle these
    specially during linking.
- term: PC-relative relocation
  definition: A type of relocation where the target address is calculated relative
    to the current Program Counter (PC). This is common for function calls and global
    data access in position-independent code.
- term: memory leak
  definition: A situation where a program allocates memory but fails to release it
    when it's no longer needed, leading to a gradual depletion of available memory
    over time.
series_id: 'binutils:risc-v: free pc-relative relocation state on ifunc errors'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110201522.2149977-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch corrects a memory leak in the RISC-V relocation function `riscv_elf_relocate_section`. Previously, on error paths related to `STT_GNU_IFUNC` symbols, the function would exit without freeing allocated PC-relative relocation state. The fix introduces a `goto out;` statement to ensure this state is properly deallocated before returning, preventing memory leaks.
