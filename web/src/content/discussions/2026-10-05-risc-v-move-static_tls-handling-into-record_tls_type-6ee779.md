---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- tls
- linker
- refactoring
discussion_id: 20261005102157.2614702-2-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH v5 1/4] RISC-V: Move STATIC_TLS handling into record_tls_type.'
headline: 'RISC-V: Move STATIC_TLS handling into record_tls_type.'
tldr: Integrate STATIC_TLS flag setting into the TLS type recording function.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Slightly increases the complexity of `riscv_elf_record_tls_type` by adding another
  responsibility.
- Improves code organization and reduces potential for redundant flag setting.
exchanges: []
primer_expert: This patch refactors `bfd/elfnn-riscv.c` by moving the setting of the
  `DF_STATIC_TLS` linker flag from `riscv_elf_check_relocs` into `riscv_elf_record_tls_type`.
  The `DF_STATIC_TLS` flag indicates that the executable uses static TLS, which has
  implications for how TLS variables are managed. By integrating this logic into the
  function responsible for recording TLS types, the code becomes more cohesive. It
  also correctly handles the interaction between `GOT_TLS_IE` and dynamically linked
  executables (`bfd_link_dll`). The patch also adds a missing early return in the
  `R_RISCV_TPREL_HI20` case wi…
primer_glossary:
- term: DF_STATIC_TLS
  definition: A flag within the ELF header that indicates the executable uses static
    Thread-Local Storage, meaning TLS variables are resolved at link time rather than
    runtime.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer (RISC) principles.
- term: TLS
  definition: Thread-Local Storage. A memory model where each thread in a process
    gets its own instance of a variable.
- term: GOT_TLS_IE
  definition: 'Global Initial Exec TLS: A TLS access mode where the Global Offset
    Table (GOT) is used for TLS variables accessed from the initial executable.'
- term: bfd_link_dll
  definition: A function within the BFD library that checks if the current link operation
    is for a dynamically linked object (DLL or shared library).
series_id: 'binutils:risc-v: move static_tls handling into record_tls_type'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005102157.2614702-2-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch moves the logic for setting the `DF_STATIC_TLS` flag into the `riscv_elf_record_tls_type` function in binutils. Previously, this flag was handled separately in `riscv_elf_check_relocs`. Consolidating this logic improves code organization and ensures that the flag is set consistently whenever a TLS type is recorded, enhancing the accuracy of TLS handling for RISC-V executables.
