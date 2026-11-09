---
project: binutils
subsystem: mips
patch_id: null
tags:
- MIPS
- Allegrex
- binutils
- assembler
- linker
discussion_id: alpine.DEB.2.21.2611081828290.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS: Add missing Allegrex machine type handling'
headline: 'MIPS: Add missing Allegrex machine type handling'
tldr: Commit adds missing Allegrex machine type handling to BFD, a.out, and gold.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This commit enhances MIPS architecture support in binutils by adding
  handling for the Allegrex machine type. It ensures that the Allegrex CPU, identified
  by `bfd_mach_mips_allegrex` and `AFL_EXT_ALLEGREX`, is correctly recognized and
  processed by the assembler (gas), linker (ld, via gold), and object file utilities
  (like readelf). This involves updating internal data structures and machine type
  mappings across BFD, elfcpp, and gold.
primer_glossary:
- term: MIPS
  definition: A family of Reduced Instruction Set Computer (RISC) architectures originally
    developed by MIPS Computer Systems (now MIPS Technologies).
- term: Allegrex
  definition: A specific MIPS processor core, often found in embedded systems like
    the PSP (PlayStation Portable).
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface for reading and writing various object file formats.
- term: a.out
  definition: A legacy executable file format used on Unix-like systems, typically
    preceding the ELF format.
- term: gold
  definition: The GNU linker, a high-performance replacement for the traditional GNU
    linker (ld).
- term: MIPS II
  definition: A revision of the MIPS instruction set architecture, introducing new
    instructions and capabilities.
- term: .MIPS.abiflags
  definition: A section in MIPS object files that specifies the ABI (Application Binary
    Interface) flags and features supported by the object code.
series_id: alpine.DEB.2.21.2611081828290.17804@angie.orcam.me.uk
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611081828290.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This commit adds missing handling for the Allegrex machine type in various components of binutils. It complements a previous commit that introduced Allegrex CPU support by defining the `.MIPS.abiflags` tag and including the Allegrex machine type in a.out and gold. The Allegrex type is also reordered within the list of MIPS II extensions to maintain chronological order.
