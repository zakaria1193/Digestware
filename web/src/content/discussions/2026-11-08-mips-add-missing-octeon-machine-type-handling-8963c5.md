---
project: binutils
subsystem: mips
patch_id: null
tags:
- MIPS
- Octeon
- binutils
- assembler
- linker
discussion_id: alpine.DEB.2.21.2611081816290.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS: Add missing Octeon machine type handling'
headline: 'MIPS: Add missing Octeon machine type handling'
tldr: Commit adds missing Octeon machine type handling to BFD, a.out, and gold.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This commit enhances MIPS architecture support in binutils by integrating
  handling for the Octeon family of processors (Octeon, OcteonP, Octeon2, Octeon3).
  It ensures these specific MIPS cores are correctly identified and processed by the
  assembler, linker (via gold), and related utilities. The changes update internal
  mappings for machine types and processor extensions across BFD, elfcpp, and gold
  to include relevant `AFL_EXT_` identifiers and corresponding `bfd_mach_` values.
primer_glossary:
- term: MIPS
  definition: A family of Reduced Instruction Set Computer (RISC) architectures originally
    developed by MIPS Computer Systems (now MIPS Technologies).
- term: Octeon
  definition: A family of multi-core MIPS-based microprocessors designed by Cavium
    Networks (now Marvell) for networking and telecommunications equipment.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface for reading and writing various object file formats.
- term: a.out
  definition: A legacy executable file format used on Unix-like systems, typically
    preceding the ELF format.
- term: gold
  definition: The GNU linker, a high-performance replacement for the traditional GNU
    linker (ld).
- term: AFL_EXT_OCTEON3
  definition: An extension identifier likely used within binutils to represent the
    Octeon 3 MIPS processor core.
series_id: alpine.DEB.2.21.2611081816290.17804@angie.orcam.me.uk
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611081816290.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This commit addresses missing support for the Octeon family of processors within binutils. It complements a previous commit that added Octeon 3 support by including the `AFL_EXT_OCTEON3` extension in the machine type conversion logic for BFD and gold. Additionally, it adds missing Octeon types to the a.out support.
