---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- elf
- linker
- gotplt
discussion_id: 20260802040719.1136959-1-xry111@xry111.site
source_type: public_inbox
title: '[PATCH] LoongArch: fix .got.plt dislocation in static PDE'
headline: 'LoongArch: fix .got.plt dislocation in static PDE'
tldr: Fixes an issue in LoongArch's ELF linker where .got.plt entries are misaligned
  in static Position-Dependent Executables (PDE).
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Correcting miscalculation of .got.plt addresses ensures proper dynamic linking behavior.
- Refactoring code improves maintainability and reduces the risk of similar bugs.
- Ensuring static linking scenarios are handled correctly alongside dynamic ones.
exchanges:
- author: Xi Ruoyao <xry111@xry111.site>
  role: proposer
  position: Submits a patch to correct the calculation of .got.plt entry addresses
    for static Position-Dependent Executables (PDE) in LoongArch, resolving a dislocation
    issue.
  quote: 'The code path handling R_LARCH_GOT{64*,{,_PC}_LO12} miscalculated the

    address of the .got.plt entry: it always counted the two .got.plt

    entries reserved for ld.so, but in static PDE those two entries do not

    exist (as in static PDE the PLT is solely for ifunc).  Thus all

    .got.plt entries dislocated for two slots.


    Fix the issue by factoring out the correct .got.plt entry addressing

    logic handling…'
primer_expert: The LoongArch ELF linker has a bug in calculating addresses for .got.plt
  entries when generating static Position-Dependent Executables (PDE). Specifically,
  the code incorrectly accounts for reserved ld.so entries in .got.plt, causing a
  shift. This patch corrects the addressing logic by factoring out common code for
  R_LARCH_GOT and R_LARCH_GOT_HI20 relocations.
primer_glossary:
- term: .got.plt
  definition: A section in ELF executables that holds addresses for Procedure Linkage
    Table (PLT) entries, used for dynamic linking.
- term: PDE
  definition: Position-Dependent Executable, a type of executable that is linked at
    a fixed base address and may not be safely relocated.
- term: static PDE
  definition: A statically linked executable that is position-dependent. In this context,
    it implies the absence of runtime dynamic linking components like ld.so's .got.plt
    entries.
- term: ifunc
  definition: Indirect function, a mechanism in ELF for resolving function symbols
    at runtime, often used for optimized or hardware-specific implementations.
- term: R_LARCH_GOT_PC_HI20
  definition: A LoongArch relocation type used to address global offset table (GOT)
    entries relative to the program counter.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260802040719.1136959-1-xry111@xry111.site
bugzilla_url: null
date: '2026-08-02'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the LoongArch ELF linker where the calculation of .got.plt entry addresses was incorrect for static Position-Dependent Executables (PDE). The code incorrectly assumed the presence of two .got.plt entries reserved for ld.so, which do not exist in static PDE, leading to a two-slot dislocation of all .got.plt entries. This error, latent in earlier releases, became exploitable in 2.47.
