---
project: binutils
subsystem: binutils/hppa
patch_id: null
tags:
- binutils
- linker
- hppa
- relocation
- PIC
commit_hash: 98a43c9d844d480968b41fbe9ae6e15382ee383d
source_type: public_inbox
author: John David Anglin <danglin@sourceware.org>
headline: Binutils linker handles HPPA ldil/addl sequences for PIC relocations.
tldr: HPPA linker now supports dynamic relocations for ldil/addl sequences in PIC
  objects, improving linking of shared executables.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch enhances `bfd/elf32-hppa.c`'s `final_link_relocate` function
  to support `R_PARISC_DLTIND21L` and `R_PARISC_DPREL21L` relocations for `ldil/addl`
  instruction sequences. Previously, only `addil` was supported, which limited the
  linker's ability to handle PIC code generation on HPPA without register spills.
  This update allows the linker to inspect the `addl` instruction following `ldil`
  to correctly rewrite the general register to `%dp` or `%r0`, resolving PR rtl-optimization/127142.
primer_glossary:
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. This is crucial for shared libraries.
- term: Relocation
  definition: A process performed by the linker to adjust symbolic addresses in machine
    code after it has been compiled, so that it can be loaded at a specific memory
    address. Dynamic relocations are those that are resolved at runtime.
- term: ldil/addl
  definition: Specific HPPA machine instructions. `ldil` likely loads a 21-bit immediate
    value into a register, and `addl` adds to it. This sequence is used for addressing
    data relative to a base register.
- term: DP register
  definition: Data Pointer register. On some architectures like HPPA, a dedicated
    register used as a base pointer for accessing global or static data.
- term: HPPA
  definition: Hewlett-Packard Precision Architecture, a RISC instruction set architecture.
- term: LRA
  definition: Link-Time Register Allocation. A GCC optimization pass that attempts
    to allocate registers during the linking phase.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261027195743.D66D34BA2E23@sourceware.org
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

The binutils linker has been updated to correctly handle dynamic relocations for `ldil`/`addl` instruction sequences on the HPPA architecture. This change allows the linker to properly convert PIC register usage (%r19) to the DP register (%r27) in non-shared executables, even when `addl` immediately follows `ldil`. This resolves issues caused by the previous limitation that only supported `addil` instructions, which had stricter register constraints.
