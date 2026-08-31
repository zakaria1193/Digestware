---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- elf
- relocation
- static-linking
discussion_id: 20260830105225.796966-1-xry111@xry111.site
source_type: public_inbox
title: '[PATCH v2] LoongArch: fix .got.plt dislocation in static PDE'
headline: 'LoongArch: fix .got.plt dislocation in static PDE'
tldr: Fixes an issue where static Position-Dependent Executables (PDEs) on LoongArch
  incorrectly offset .got.plt entries due to miscalculation of reserved slots.
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The previous behavior relied on a coincidence where `.got.plt` and `.got.iplt` addresses
  were the same in static builds with default linker scripts, which could break with
  custom scripts.
- The fix unifies multiple code paths, which could increase complexity but improves
  correctness and maintainability.
- Avoiding C23 attributes in the test suite ensures compatibility with older GCC versions.
exchanges:
- author: Xi Ruoyao <xry111@xry111.site>
  role: proposer
  position: Submits a patch to correct .got.plt dislocation in LoongArch static PDEs.
  quote: 'The code path handling R_LARCH_GOT{64*,{,_PC}_LO12} miscalculated the

    address of the .got.plt entry: it always counted the two .got.plt

    entries reserved for ld.so, but in static PDE those two entries do not

    exist (as in static PDE the PLT is solely for ifunc).  Thus all

    .got.plt entries dislocated for two slots.'
primer_expert: This patch targets the LoongArch ELF backend in binutils. Specifically,
  it fixes an issue in static Position-Dependent Executables (PDEs) where relocations
  like R_LARCH_GOT{64*,{,_PC}_LO12} and R_LARCH_GOT_{PC_,}HI20, as well as R_LARCH_SOP_PUSH_GPREL
  used for ifuncs, miscalculate the address of `.got.plt` entries. In static PDEs,
  the two entries typically reserved for `ld.so` are absent, leading to a two-slot
  offset. The fix introduces a unified subroutine that correctly handles these cases,
  using `.got.iplt` for static builds and addressing latent issues that became apparent
  in binutils 2.4…
primer_glossary:
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China, with specific
    ELF object file format conventions.
- term: .got.plt
  definition: The 'Global Offset Table for the Procedure Linkage Table'. It stores
    addresses of dynamically resolved external functions and variables used in Position-Independent
    Code (PIC).
- term: static PDE
  definition: A statically linked Position-Dependent Executable. In this context,
    it means the executable is linked without shared libraries, and its code relies
    on fixed memory addresses.
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to provide an indirect jump to shared library functions, allowing lazy binding.
- term: ifunc
  definition: An indirect function. It's a mechanism used for function selection at
    runtime, often based on CPU features detected via hardware probing.
- term: relocation
  definition: Information in an object file that specifies how addresses and references
    need to be adjusted by the linker to create the final executable or shared library.
- term: ld.so
  definition: The dynamic linker/loader, responsible for loading shared libraries
    and resolving symbols at runtime.
- term: .got.iplt
  definition: Likely refers to a GOT entry specifically used for indirect function
    (ifunc) resolution, distinct from the standard .got.plt.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260830105225.796966-1-xry111@xry111.site
bugzilla_url: null
date: '2026-08-30'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in LoongArch's handling of relocations for static Position-Dependent Executables (PDEs). The code incorrectly accounted for two reserved `.got.plt` entries, which do not exist in static PDEs (as the PLT is only for ifuncs). This resulted in a two-slot dislocation for all `.got.plt` entries. The fix unifies several relocation handling paths, including those for ifuncs, into a common subroutine that correctly references `.got.iplt` instead of `.got.plt` for static builds, resolving latent issues that became exploitable in recent releases.
