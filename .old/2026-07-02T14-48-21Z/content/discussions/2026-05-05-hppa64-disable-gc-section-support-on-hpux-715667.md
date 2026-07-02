---
project: binutils
subsystem: hppa64
patch_id: null
tags:
- binutils
- hppa64
- hpux
- gc-sections
- relocation
discussion_id: afo9vUauRLAvdR9o@mx3210.local
source_type: public_inbox
title: '[committed] hppa64: Disable -gc-section support on hppa*64*-*-hpux*'
headline: 'Hppa64: Disable -gc-section support on HPUX'
tldr: Garbage collection of sections is now disabled for hppa64 HP-UX due to dynamic
  linker errors with R_PARISC_NONE relocations.
proposer: John David Anglin <dave.anglin@bell.net>
consensus: Proposed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Disabling `-gc-sections` increases the size of the final executable.
- Avoids runtime errors due to incompatible relocations on HP-UX.
- No longer able to remove unused sections, which might include dead code or data.
exchanges:
- author: John David Anglin <dave.anglin@bell.net>
  role: proposer
  position: Disables -gc-section support for hppa64 HP-UX due to dynamic linker issues
    with R_PARISC_NONE relocations.
  quote: The HP-UX dynamic linker on hppa generates an error if it detects a dynamic
    relocation with the R_PARISC_NONE type.  As a result, there is no way to handle
    relocations in sections that are garbage collected.  Although these can mostly
    be avoided, I think it best to disable -gc-section support.
primer_expert: The HP-UX dynamic linker's inability to handle `R_PARISC_NONE` relocations
  within garbage-collected sections necessitates disabling `-gc-section` support for
  hppa64. This involves modifying `elf64-hppa.c` to disable section garbage collection
  and updating testsuite files to exclude HP-UX targets. The `BFD_ASSERT` is reworked
  to only trigger on HP-UX, and `elf_backend_can_gc_sections` is set to zero.
primer_general: '`-gc-sections` is a linker flag that instructs the linker to remove
  unused sections from the final executable, reducing its size. This is achieved by
  marking sections as eligible for garbage collection. Relocations are adjustments
  the linker makes to addresses within the code to ensure they point to the correct
  locations after linking.  HP-UX''s dynamic linker has problems with a specific type
  of relocation (`R_PARISC_NONE`) when combined with garbage collection, leading to
  errors. To avoid these errors, support for `-gc-sections` is disabled specifically
  for HP-UX on hppa64 architecture.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afo9vUauRLAvdR9o@mx3210.local
bugzilla_url: null
date: '2026-05-05'
---

The HP-UX dynamic linker on hppa64 generates an error when encountering dynamic relocations of type `R_PARISC_NONE`, which can occur in garbage collected sections.  This change disables `-gc-section` support for hppa64 HP-UX to avoid these errors. The patch modifies `bfd/elf64-hppa.c` and updates several testsuite files to xfail on hppa*64*-*-hpux*.
