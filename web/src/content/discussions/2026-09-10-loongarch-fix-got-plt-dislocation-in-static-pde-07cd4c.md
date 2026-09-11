---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocation
- static linking
- GOT
discussion_id: 69f1006e-9a25-40dc-9569-02790c975056@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH v3] LoongArch: fix .got.plt dislocation in static PDE'
headline: 'LoongArch: Fix .got.plt dislocation in static PDE'
tldr: Corrected .got.plt addressing for static executables on LoongArch.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Simplifies and unifies relocation handling code.
- Corrects a latent bug that became apparent after changes in a previous release.
exchanges:
- author: mengqinggang
  role: proposer
  position: Applied the patch, thanking the author.
  quote: Applied, thanks!
- author: Xi Ruoyao
  role: contributor
  position: Submitted a patch series to fix .got.plt dislocation and related issues
    in static PDE for LoongArch.
  quote: 'The code path handling R_LARCH_GOT{64*,{,_PC}_LO12} miscalculated the

    address of the .got.plt entry: it always counted the two .got.plt

    entries reserved for ld.so, but in static PDE those two entries do not

    exist (as in static PDE the PLT is solely for ifunc).  Thus all

    .got.plt entries dislocated for two slots.


    Those affected relocations are practically always used together with

    the R_LARCH_GOT…'
primer_expert: This discussion concerns the LoongArch toolchain's handling of Position-Dependent
  Executables (PDE) in static builds. Specifically, it addresses incorrect address
  calculations for .got.plt entries when the dynamic linker stubs are not present
  in static linking scenarios. The patch unifies several relocation handling paths
  (R_LARCH_GOT*, R_LARCH_GOT_HI20, R_LARCH_SOP_PUSH_GPREL) to use a common, correct
  subroutine, thereby fixing latent issues related to ifunc resolution and custom
  linker scripts.
primer_glossary:
- term: .got.plt
  definition: The Global Offset Table section used for Procedure Linkage Table (PLT)
    entries. It stores addresses of dynamically resolved functions and is essential
    for dynamic linking.
- term: static PDE
  definition: Static Position-Dependent Executable. A program that is linked statically
    (no dynamic shared libraries) but has its code and data addresses fixed at link
    time, allowing for runtime relocation.
- term: ifunc
  definition: An Indirect Function, a mechanism in ELF that allows lazy resolution
    of function pointers. The actual function address is resolved at runtime, typically
    via a resolver function.
- term: R_LARCH_GOT_HI20
  definition: A LoongArch relocation type that targets the high 20 bits of a Global
    Offset Table entry.
- term: relocation
  definition: A process performed by the linker or dynamic loader to resolve symbolic
    references between different object files or libraries. It involves adjusting
    addresses based on the final memory layout.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/69f1006e-9a25-40dc-9569-02790c975056@loongson.cn
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch addresses an issue on LoongArch where the .got.plt entry addresses were miscalculated for static Position-Dependent Executables (PDE). The miscalculation stemmed from always accounting for .got.plt entries reserved for ld.so, which are absent in static PDE. This resulted in a two-slot dislocation for all .got.plt entries. The fix unifies code paths to use a correct subroutine, addressing latent issues in ifunc handling as well.
