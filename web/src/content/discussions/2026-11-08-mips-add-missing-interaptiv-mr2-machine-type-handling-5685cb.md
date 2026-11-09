---
project: binutils
subsystem: mips
patch_id: null
tags:
- MIPS
- interAptiv MR2
- binutils
- assembler
- linker
discussion_id: alpine.DEB.2.21.2611081823050.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS: Add missing interAptiv MR2 machine type handling'
headline: 'MIPS: Add missing interAptiv MR2 machine type handling'
tldr: Commit adds missing interAptiv MR2 machine type handling to BFD, a.out, and
  gold.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This commit extends MIPS architecture support within binutils by integrating
  the Imagination interAptiv MR2 processor. It ensures that this specific MIPS core
  is correctly identified and processed by the assembler, linker (via gold), and related
  utilities. The changes involve updating internal mappings for machine types and
  processor extensions across BFD, elfcpp, and gold to include `bfd_mach_mips_interaptiv_mr2`
  and `AFL_EXT_INTERAPTIV_MR2`.
primer_glossary:
- term: MIPS
  definition: A family of Reduced Instruction Set Computer (RISC) architectures originally
    developed by MIPS Computer Systems (now MIPS Technologies).
- term: interAptiv MR2
  definition: A specific MIPS processor core developed by Imagination Technologies,
    likely part of their PowerVR or similar embedded processor lines.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface for reading and writing various object file formats.
- term: a.out
  definition: A legacy executable file format used on Unix-like systems, typically
    preceding the ELF format.
- term: gold
  definition: The GNU linker, a high-performance replacement for the traditional GNU
    linker (ld).
- term: MIPS32r3
  definition: A revision of the MIPS32 instruction set architecture.
- term: AFL_EXT_INTERAPTIV_MR2
  definition: An extension identifier likely used within binutils to represent the
    interAptiv MR2 MIPS processor core.
series_id: alpine.DEB.2.21.2611081823050.17804@angie.orcam.me.uk
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611081823050.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This commit enhances MIPS support in binutils by adding handling for the Imagination interAptiv MR2 processor. It complements a prior commit that introduced support for this processor by adding the `AFL_EXT_INTERAPTIV_MR2` extension to the machine type conversion logic in BFD and gold. The interAptiv MR2 machine type is also added to a.out support.
