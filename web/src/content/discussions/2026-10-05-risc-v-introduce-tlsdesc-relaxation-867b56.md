---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- tls
- linker
- relaxation
discussion_id: 20261005102157.2614702-5-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH v5 4/4] RISC-V: Introduce TLSDESC relaxation.'
headline: 'RISC-V: Introduce TLSDESC relaxation.'
tldr: Enable TLSDESC for static executables by relaxing sequences or rewriting them
  in place.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the relaxation pass to handle TLSDESC, potentially increasing
  compile/link times slightly.
- The in-place rewrite for non-relaxed sequences might introduce slightly larger code
  sizes than a fully relaxed sequence.
exchanges: []
primer_expert: 'This patch enables the use of TLSDESC (Thread-Local Storage Descriptor)
  relocations in RISC-V static executables. Previously, TLSDESC required runtime resolution,
  making it unusable in static binaries. This change modifies the linker''s relaxation
  pass: for R_RISCV_RELAX relocations, it shortens the TLSDESC sequence; otherwise,
  it rewrites the sequence in place using NOPs and potentially other instructions
  (like `auipc` and `l[dw]`) to emulate the descriptor access without runtime resolution.
  This ensures TLSDESC can be used for local symbols (LE) or immediately accessible
  (IE) in static execu…'
primer_glossary:
- term: TLSDESC
  definition: A mechanism for accessing thread-local storage that uses a descriptor
    to locate the data, offering more flexibility than older methods but typically
    requiring runtime support.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer (RISC) principles.
- term: Relaxation
  definition: A linker optimization that adjusts code or data addresses after initial
    layout to accommodate changes, often to shorten instruction sequences or optimize
    address calculations.
- term: R_RISCV_RELAX
  definition: A RISC-V specific relocation type that signals to the linker that the
    associated instruction sequence can be modified or shortened during relaxation.
- term: IE
  definition: 'Initial Exec (or Internal Exec): A type of TLS access mode. IE is typically
    used for TLS variables that are globally visible within the executable.'
- term: LE
  definition: 'Local Exec: A type of TLS access mode. LE is typically used for TLS
    variables that are local to the current module.'
- term: auipc
  definition: 'Add Upper Immediate to PC: A RISC-V instruction that adds a 20-bit
    immediate, shifted left by 12 bits, to the current PC value, storing the result
    in a destination register. Used for PC-relative addressing.'
- term: lui
  definition: 'Load Upper Immediate: A RISC-V instruction that loads a 20-bit immediate,
    shifted left by 12 bits, into the upper bits of a destination register. Used to
    construct 32-bit constants.'
- term: l[dw]
  definition: 'Load Doubleword/Word: RISC-V instructions to load data from memory
    into a register. The ''d'' or ''w'' indicates 64-bit or 32-bit respectively.'
- term: nop
  definition: 'No Operation: An instruction that does nothing but consume a clock
    cycle. Often used as a placeholder or for padding.'
series_id: 'binutils:risc-v: introduce tlsdesc relaxation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005102157.2614702-5-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces TLSDESC relaxation for RISC-V executables, allowing Thread-Local Storage (TLS) descriptors to function in static environments. It modifies the relax pass to either delete instructions in relaxed sequences or rewrite them in place for non-relaxed cases, ensuring TLSDESC works correctly in static executables where runtime resolution is not possible. This fixes a limitation in how TLSDESC was handled previously.
