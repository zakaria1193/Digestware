---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- tls
- linker
- relocation
discussion_id: 20261005102157.2614702-3-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH v5 2/4] RISC-V: Unify TLS handling in check_relocs.'
headline: 'RISC-V: Unify TLS handling in check_relocs.'
tldr: Consolidate TLS relocation checks in RISC-V ELF object files.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Slight increase in indirection due to the new helper function, but overall simplification
  outweighs this.
- Consolidates logic, potentially making future additions or modifications to TLS
  handling easier.
exchanges: []
primer_expert: This patch refactors `bfd/elfnn-riscv.c` by consolidating multiple
  `case` statements within `riscv_elf_check_relocs` that previously handled different
  TLS relocation types (R_RISCV_TLS_GD_HI20, R_RISCV_TLS_GOT_HI20, etc.). A new helper
  function, `riscv_elf_tls_type_from_hi_reloc`, is introduced to map these relocation
  types to internal TLS type constants (e.g., `GOT_TLS_GD`). The unified code path
  simplifies the logic and allows for common checks and actions related to TLS relocations,
  improving code clarity and maintainability. It also ensures that the `DF_STATIC_TLS`
  flag is correctly set w…
primer_glossary:
- term: TLS
  definition: Thread-Local Storage. A memory model where each thread in a process
    gets its own instance of a variable.
- term: GOT
  definition: Global Offset Table. A table used by dynamically linked executables
    to store addresses of global symbols, allowing indirect access.
- term: Relocation
  definition: Information in an object file that specifies how to update addresses
    or other values when the code or data is loaded into memory or linked.
- term: R_RISCV_TLS_GD_HI20
  definition: A RISC-V relocation type for the high 20 bits of a Global Dynamic TLS
    access.
- term: R_RISCV_TLS_GOT_HI20
  definition: A RISC-V relocation type for the high 20 bits of a GOT-relative TLS
    access.
- term: R_RISCV_TLSDESC_HI20
  definition: A RISC-V relocation type for the high 20 bits of a TLSDESC access.
- term: R_RISCV_TPREL_HI20
  definition: A RISC-V relocation type for the high 20 bits of a Thread Pointer Relative
    TLS access.
- term: GOT_TLS_GD
  definition: 'Global Dynamic TLS: A TLS access mode where the GOT is used to access
    TLS variables that are globally visible.'
- term: GOT_TLS_IE
  definition: 'Global Initial Exec TLS: A TLS access mode where the GOT is used for
    TLS variables accessed from the initial executable.'
- term: GOT_TLSDESC
  definition: 'TLSDESC TLS: A TLS access mode using a descriptor table for accessing
    TLS variables.'
series_id: 'binutils:risc-v: unify tls handling in check_relocs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005102157.2614702-3-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch unifies the handling of various Thread-Local Storage (TLS) relocation types within the `check_relocs` function for RISC-V ELF files. By merging switch cases for different TLS relocations (GD, GOT, TLSDESC, TPREL), the code becomes more maintainable and reduces redundancy. This change simplifies the logic for validating TLS references and ensures consistent behavior across different TLS access models.
