---
project: binutils
subsystem: binutils/loongarch
patch_id: null
tags:
- loongarch
- linker
- relocation
- static-linking
commit_hash: 8ec22f3191b1917a06dcbe84f6bbef042462bf5b
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch static executables: fix .got.plt dislocation'
tldr: Correctly calculates .got.plt entry addresses for static LoongArch executables,
  fixing a latent bug exposed in version 2.47.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `R_LARCH_GOT*` relocation handling in `bfd/elfnn-loongarch.c` incorrectly
  assumed the presence of `ld.so` entries in the `.got.plt` section for static PDEs.
  This caused a two-slot offset error. Prior to binutils 2.47, `R_LARCH_GOT*` relocations
  used `pointer_equality_needed`, directing them to the PLT stub instead of `.got.plt`,
  masking the error. This change corrects the address calculation and unifies handling
  for `R_LARCH_GOT{64*,{,_PC}_LO12}`, `R_LARCH_GOT{PC_,}HI20`, and `R_LARCH_SOP_PUSH_GPREL`
  to use a robust subroutine, fixing latent issues with ifuncs and custom linker scripts.
primer_glossary:
- term: .got.plt
  definition: A section in ELF executables that holds addresses of functions and data
    used in dynamic linking, specifically for Procedure Linkage Table (PLT) entries
    that require global offset table (GOT) lookups.
- term: Static PDE
  definition: Static Position-Dependent Executable. A statically linked executable
    that may still rely on position-dependent addressing, which is less common than
    dynamically linked PDEs or Position-Independent Executables (PIEs).
- term: Ifunc
  definition: Indirect Function. A mechanism in ELF that allows the dynamic linker
    to resolve a function call to different implementations at runtime, often based
    on hardware capabilities.
- term: Relocation
  definition: Information in an object file that describes how to modify parts of
    the code or data when linking, typically to resolve addresses of external symbols
    or relative offsets.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260910061805.6F5054BB58D2@sourceware.org
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in LoongArch ELF object file generation where the address calculation for `.got.plt` entries in static Position-Dependent Executables (PDEs) was incorrect. The code mistakenly always accounted for two `.got.plt` entries reserved for `ld.so`, which are absent in static PDEs. This resulted in a dislocation of all `.got.plt` entries by two slots. The fix unifies code paths for related relocations to use a correct subroutine, resolving latent issues in ifunc handling and ensuring correct .got.plt addressing for static builds.
