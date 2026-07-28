---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- amd
- gpu
- gfx1103
discussion_id: 20260727135117.23444-1-shahab.vahedi@amd.com
source_type: public_inbox
title: '[PATCH] bfd,binutils: add support for gfx1103'
headline: 'bfd,binutils: add support for gfx1103'
tldr: Adds support for the AMD GFX1103 GPU architecture to binutils.
proposer: Shahab Vahedi <shahab.vahedi@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Enables proper processing of GFX1103 object files.
- Minimal code changes, mainly additions to tables and definitions.
exchanges:
- author: Shahab Vahedi <shahab.vahedi@amd.com>
  role: proposer
  position: Submits a patch to add ELF header definitions for the AMD GFX1103 GPU
    architecture to binutils.
  quote: Add ELF header definition for gfx1103.
primer_expert: This patch extends the binutils BFD library and related tools (like
  `readelf`) to recognize and correctly handle the AMD GFX1103 GPU architecture. It
  involves adding a new machine-specific definition (`bfd_mach_amdgcn_gfx1103`) and
  its corresponding machine code (0x044) to the internal data structures that map
  architecture names to BFD definitions. The changes span multiple files, including
  header files and architecture-specific implementation files, ensuring that binutils
  can correctly interpret and display information related to this new hardware target.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a part of GNU Binutils that provides
    a common interface for reading and writing various object file formats.
- term: GFX1103
  definition: A specific GPU architecture designation from AMD, likely part of their
    RDNA 3 or a successor lineup, requiring specific toolchain support for compilation
    and debugging.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on Unix-like systems. Used here for GPU-specific
    metadata.
- term: AMDGPU
  definition: A target architecture for AMD Graphics Processing Units, used in the
    context of LLVM/Clang and related toolchain components.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260727135117.23444-1-shahab.vahedi@amd.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch adds support for the AMD GFX1103 GPU architecture to the binutils project. It includes necessary definitions in BFD (Binary File Descriptor) and related components, such as updating `archures.c`, `bfd-in2.h`, `cpu-amdgcn.c`, `readelf.c`, and `include/elf/amdgpu.h`. This enables binutils tools like `readelf` to correctly process object files targeting the GFX1103 architecture.
