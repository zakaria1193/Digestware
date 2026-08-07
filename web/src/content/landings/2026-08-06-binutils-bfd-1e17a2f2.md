---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- amd
- gpu
- elf
- architecture
commit_hash: 1e17a2f208f10e4bdc4e7f6001addb24cea396ee
source_type: public_inbox
author: Shahab Vahedi <shahab@sourceware.org>
headline: Add support for AMD GFX1103.
tldr: Binutils now supports the AMD GFX1103 GPU architecture.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces support for the `gfx1103` microarchitecture
  in the AMD GPU toolchain support within Binutils. It adds the corresponding `bfd_mach_amdgcn_gfx1103`
  definition and updates BFD's internal machine definitions and CPU-specific information.
  The change also updates `readelf.c` to recognize this new architecture, drawing
  definitions from an external LLVM documentation URL.
primer_glossary:
- term: GFX1103
  definition: A specific microarchitecture generation for AMD's Graphics Core Next
    (GCN) GPU architecture.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: BFD
  definition: The Binary File Descriptor library, a low-level interface for reading
    and writing various object file formats.
- term: microarchitecture
  definition: The specific design and implementation of a processor's instruction
    set architecture, often referring to a particular generation or series of chips.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260806110552.D72AE4BA2E3B@sourceware.org
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

Support for the AMD GFX1103 GPU has been added to the Binutils build. This includes defining the necessary ELF header information and machine definitions within the BFD library and related tools.
