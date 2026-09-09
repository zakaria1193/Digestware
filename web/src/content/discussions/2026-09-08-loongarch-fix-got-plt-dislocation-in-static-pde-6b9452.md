---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- ELF
discussion_id: 20260908101630.85575-1-xry111@aosc.io
source_type: public_inbox
title: '[PATCH v3] LoongArch: fix .got.plt dislocation in static PDE'
headline: 'LoongArch: Fix .got.plt dislocation in static PDE'
tldr: Patch corrects .got.plt addressing in LoongArch static position-dependent executables.
proposer: Xi Ruoyao <xry111@aosc.io>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Unifying code paths for different relocation types to improve correctness and maintainability,
  potentially at the cost of slightly increased complexity in the shared subroutine.
exchanges:
- author: Xi Ruoyao
  role: proposer
  position: Submitted a patch to fix .got.plt dislocation in LoongArch static PDEs,
    addressing issues with relocation address calculation and ifunc handling.
  quote: 'The code path handling R_LARCH_GOT{64*,{,_PC}_LO12} miscalculated the

    address of the .got.plt entry: it always counted the two .got.plt

    entries reserved for ld.so, but in static PDE those two entries do not

    exist (as in static PDE the PLT is solely for ifunc).  Thus all

    .got.plt entries dislocated for two slots.'
primer_expert: This patch addresses a bug in the LoongArch ELF backend of binutils'
  BFD library. The issue lies in the calculation of addresses for `.got.plt` entries
  when generating position-dependent executables (PDEs) in static builds. Specifically,
  the relocation handling for `R_LARCH_GOT{64*,{,_PC}_LO12}` incorrectly assumes the
  presence of two GOT entries reserved for the dynamic linker (`ld.so`), which are
  absent in static builds where the PLT is only used for ifunc resolution. This leads
  to all `.got.plt` entries being offset by two slots. The fix involves consolidating
  the handling of related reloc…
primer_glossary:
- term: LoongArch
  definition: A CPU architecture developed in China, based on MIPS.
- term: .got.plt
  definition: A section in an ELF executable that stores addresses for dynamically
    linked functions, used by the Procedure Linkage Table (PLT).
- term: Static PDE
  definition: A static Position-Dependent Executable. 'Static' means it's linked without
    dynamic libraries, and 'PDE' means its addresses are fixed relative to the program's
    base address.
- term: Relocation
  definition: A process by which the linker or dynamic loader modifies code or data
    to refer to the correct addresses at runtime.
- term: Addend
  definition: A constant value added to a symbol's address during relocation.
- term: ifunc
  definition: An indirect function, allowing runtime resolution of function pointers,
    often used for selecting architecture-specific implementations.
- term: PLT
  definition: Procedure Linkage Table. A table used in ELF executables to provide
    an indirection layer for calls to shared library functions.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260908101630.85575-1-xry111@aosc.io
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Xi Ruoyao proposes a patch to fix incorrect addressing of .got.plt entries in LoongArch static Position-Dependent Executables (PDEs). The previous implementation miscalculated the .got.plt entry address by always accounting for two reserved entries for ld.so, which do not exist in static PDEs. This resulted in a two-slot dislocation for all .got.plt entries. The patch unifies code paths for several relocation types to call a corrected subroutine that properly references .igot.plt for static builds.
