---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- elf
- bfd
- dynobj
discussion_id: cover.1778457849.git.amodra@gmail.com
source_type: public_inbox
title: various tidies to use a linker created dynobj
headline: Tidies for using a linker-created dynobj in binutils.
tldr: Alan Modra proposes a series of tidy-up patches to prepare for using a linker-created
  bfd for dynamic sections in ELF linkers.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The main tradeoff is the potential for regressions when modifying core components
  of the linker.
- The benefits are improved code clarity, reduced redundancy, and better handling
  of dynamic linking
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a series of patches to clean up binutils code in preparation
    for using a linker-created BFD for dynamic sections in ELF linkers.
  quote: This series of patches came about as I was playing with the idea of making
    all the ELF linker targets use a linker created bfd for attaching dynamic sections.
- author: Alan Modra <amodra@gmail.com>
  role: other
  position: Explains a change related to delaying the setting of PLT header and entry
    size for ARM targets.
  quote: elf32_arm_create_dynamic_sections was used to set plt_header_size and plt_entry_size.  This
    necessitated a hack for using_thumb_only() as the output file attributes used
    by that function are not set until lang_check calls bfd_merge_private_bfd_data.
- author: Alan Modra <amodra@gmail.com>
  role: other
  position: Details the removal of a restriction in cris check_relocs due to access
    to the output bfd now being available.
  quote: A comment in cris check_relocs bemoans not being able to access the output
    bfd in adjust_dynamic_symbol.  A little over three years after the comment was
    written, commit f13a99db51c0 gave that access.  So let's make use of it and remove
    a restriction.
- author: Alan Modra <amodra@gmail.com>
  role: other
  position: Describes a change to test frvfdpic_relocs_info directly instead of dynobj
    in elf32_frvfdpic_late_size_sections.
  quote: This function runs passes over frvfdpic_relocs_info if dynobj is set, which
    is OK since the two variables are both non-NULL or both NULL in the current linker.  That
    may change in the future, so test frvfdpic_relocs_info directly rather than dynobj.
- author: Alan Modra <amodra@gmail.com>
  role: other
  position: Explains the removal of a duplicate call to _bfd_elf_create_got_section
    in lm32_elf_create_dynamic_sections.
  quote: lm32_elf_create_dynamic_sections has two calls to _bfd_elf_create_got_section.  That
    doesn't cause a problem, but one such call suffices.
- author: Alan Modra <amodra@gmail.com>
  role: other
  position: Describes a fix for testsuite failures related to discarding GOT sections
    in elf64-alpha.c.
  quote: This fixes testsuite failures I noticed when changing dynobj to be linker
    created, but I think the bug could be triggered by suitably crafted linker scripts
    without any dynobj changes.
primer_expert: BFD (Binary File Descriptor) is a library for working with different
  object file formats.  dynobj refers to the dynamic object, a BFD structure used
  for handling dynamic linking. The patches aim to use a linker-created BFD for dynamic
  sections to avoid type mismatches and simplify the code.
primer_general: When creating executable programs, a linker combines different parts
  of the code together. A dynamic object (dynobj) is used to manage how the program
  interacts with shared libraries at runtime. This series of patches aims to improve
  how the linker handles these dynamic objects, making the process more robust and
  less prone to errors.
series_id: 1778457849.git.amodra@gmail.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/cover.1778457849.git.amodra@gmail.com
bugzilla_url: null
date: '2026-05-11'
is_stub: false
---

Alan Modra proposes a series of patches to tidy up the binutils code in preparation for a larger change to use a linker-created BFD (Back-End File Descriptor) for attaching dynamic sections in ELF linkers. These cleanups address issues in ARM, CRIS, FRV, LM32, Alpha and HPPA64 targets.
