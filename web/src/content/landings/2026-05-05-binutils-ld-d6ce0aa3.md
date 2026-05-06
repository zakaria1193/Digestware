---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- ld
- hppa64
- hp-ux
- gc-sections
commit_hash: d6ce0aa3f877dd4475f77033496383c66383d69b
source_type: public_inbox
author: John David Anglin
headline: 'hppa64: Disable -gc-section support on hppa*64*-*-hpux*'
tldr: Disables `-gc-section` support for HP-UX on hppa64 due to dynamic linker issues
  with R_PARISC_NONE relocations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The HP-UX dynamic linker's inability to handle `R_PARISC_NONE` relocations
  in garbage-collected sections necessitates disabling `-gc-section`. The patch modifies
  `elf64-hppa.c` to disable garbage collection and updates the linker testsuite to
  xfail affected tests. This issue is specific to HP-UX on hppa64.
primer_general: Linker garbage collection (`-gc-sections`) removes unused sections
  from the final executable, reducing its size.  Relocations are adjustments the linker
  makes to code and data addresses when combining object files. This commit disables
  linker garbage collection for HP-UX on hppa64 because the HP-UX dynamic linker has
  issues processing a specific type of relocation (`R_PARISC_NONE`) in sections that
  have been garbage collected. This prevents errors during program execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260505185244.341244BA7998@sourceware.org
date: '2026-05-05'
---

The HP-UX dynamic linker on hppa64 platforms generates an error when encountering dynamic relocations with the type `R_PARISC_NONE`. This commit disables `-gc-section` support on `hppa*64*-*-hpux*` to avoid these errors, as there is no reliable way to handle relocations in garbage-collected sections. Testsuite entries are also updated to reflect this change.
