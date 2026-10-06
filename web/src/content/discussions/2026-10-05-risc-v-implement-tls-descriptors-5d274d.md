---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- tls
- linker
- relaxation
- elf
discussion_id: 20261005102157.2614702-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH v5 0/4] RISC-V: Implement TLS Descriptors.'
headline: 'RISC-V: Implement TLS Descriptors.'
tldr: Adds support for Thread-Local Storage (TLS) descriptors to the RISC-V toolchain.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increases complexity in the linker's relaxation and ELF handling code for RISC-V.
- Introduces new internal relocation types and sequences to manage TLSDESC in static
  contexts.
exchanges: []
primer_expert: This is the cover letter for a series implementing TLS Descriptor support
  for RISC-V in binutils. The core of the work involves enabling TLSDESC relocations
  (like `R_RISCV_TLSDESC_HI20`) to function correctly in static executables. This
  is achieved through relaxation mechanisms and by rewriting non-relaxed sequences
  to avoid runtime descriptor resolution. The series also refactors related TLS handling
  code (e.g., `riscv_elf_record_tls_type`, `riscv_elf_check_relocs`) and ensures that
  symbol information (`elf_link_hash_entry`) is properly passed during relaxation.
  The goal is to provide comple…
primer_glossary:
- term: TLS Descriptors
  definition: A mechanism for accessing thread-local storage that uses an indirection
    through a descriptor, offering flexibility but typically requiring runtime support
    for resolution.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer (RISC) principles.
- term: Relaxation
  definition: A linker optimization that adjusts code or data addresses and instruction
    sequences after initial layout to improve code density or fix addressability issues.
- term: Static Executable
  definition: An executable file that contains all necessary code and data, without
    relying on dynamic linking to external shared libraries at runtime.
- term: TLSDESC
  definition: A specific type of TLS access method that uses a descriptor, often for
    dynamic TLS access.
- term: R_RISCV_TLSDESC_HI20
  definition: A RISC-V relocation type used for the high 20 bits of a TLSDESC access.
- term: GOT
  definition: Global Offset Table. A table used by dynamically linked executables
    to store addresses of global symbols.
- term: IE
  definition: 'Initial Exec (or Internal Exec): A type of TLS access mode often used
    for TLS variables accessed from the main executable.'
- term: LE
  definition: 'Local Exec: A type of TLS access mode for TLS variables local to the
    current module.'
series_id: 'binutils:risc-v: implement tls descriptors'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005102157.2614702-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This series of patches, the fifth version from Tatsuyuki Ishi, introduces and refines support for Thread-Local Storage (TLS) descriptors in the RISC-V binutils. Key changes include enabling TLSDESC for static executables by implementing relaxation and in-place rewriting strategies, unifying TLS handling logic, and improving the integration of symbol information during relaxation. These updates aim to provide robust and correct TLS support for RISC-V binaries, particularly in scenarios previously unsupported by the toolchain.
